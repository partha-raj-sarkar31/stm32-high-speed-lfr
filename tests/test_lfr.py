import unittest
from lfr_model import estimate_position, normalize, PID, motor_mix, N

class LfrTests(unittest.TestCase):
    def test_centered_line(self):
        values = [0.0]*N
        values[6] = values[7] = 1.0
        self.assertAlmostEqual(estimate_position(values), 0.0, places=6)

    def test_left_and_right_sign(self):
        left, right = [0.0]*N, [0.0]*N
        left[0] = 1.0
        right[-1] = 1.0
        self.assertLess(estimate_position(left), 0)
        self.assertGreater(estimate_position(right), 0)

    def test_line_loss_is_none(self):
        self.assertIsNone(estimate_position([0.0]*N))

    def test_wrong_sensor_count_rejected(self):
        with self.assertRaises(ValueError):
            estimate_position([0.0]*13)

    def test_normalization_clamps(self):
        self.assertEqual(normalize(-20, 0, 100), 0.0)
        self.assertEqual(normalize(150, 0, 100), 1.0)
        self.assertEqual(normalize(0, 0, 0), 0.0)
        self.assertEqual(normalize(0, 0, 100, False), 1.0)

    def test_pid_proportional_and_invalid_dt(self):
        p = PID(kp=2, ki=0, kd=0)
        self.assertAlmostEqual(p.step(0.25, 0.01), 0.5)
        self.assertEqual(p.step(1, 0), 0.0)

    def test_pid_integral_is_bounded(self):
        p = PID(kp=0, ki=1, kd=0, integral_limit=0.2)
        for _ in range(100):
            p.step(1, 0.1)
        self.assertAlmostEqual(p.integral, 0.2)

    def test_pid_derivative_damps_change(self):
        p = PID(kp=0, ki=0, kd=1)
        p.step(0, 0.1)
        self.assertAlmostEqual(p.step(0.5, 0.1), 5.0)

    def test_motor_commands_bounded(self):
        left, right = motor_mix(0.9, 0.8, 0.6)
        self.assertEqual(left, 0.6)
        self.assertAlmostEqual(right, 0.1)
        self.assertTrue(-1 <= left <= 1 and -1 <= right <= 1)

if __name__ == "__main__":
    unittest.main()

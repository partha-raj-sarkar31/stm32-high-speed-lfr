from lfr_model import estimate_position, PID, motor_mix, N

sensors = [0.0] * N
sensors[6] = sensors[7] = 1.0
position = estimate_position(sensors)
pid = PID()
correction = pid.step(position, 0.01)
left, right = motor_mix(0.4, correction)
print("Synthetic sensor input: centered line (channels 6 and 7 active)")
print(f"position_error={position:.3f}")
print(f"line_detected={position is not None}")
print(f"normalized_motor_commands: left={left:.3f}, right={right:.3f}")
print("NOTE: software demonstration only; no hardware or track measurement.")

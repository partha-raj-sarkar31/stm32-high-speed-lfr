"""Hardware-independent reference algorithms used by tests and demo."""
from dataclasses import dataclass

N = 14

def clamp(value, low, high):
    return max(low, min(value, high))

def normalize(raw, low, high, line_is_high=True):
    if high <= low:
        return 0.0
    value = clamp((raw - low) / (high - low), 0.0, 1.0)
    return value if line_is_high else 1.0 - value

def estimate_position(values, threshold=0.15):
    if len(values) != N:
        raise ValueError(f"expected {N} sensor values")
    active = [(i, clamp(float(v), 0.0, 1.0)) for i, v in enumerate(values)
              if clamp(float(v), 0.0, 1.0) >= threshold]
    total = sum(v for _, v in active)
    if total <= 1e-9:
        return None
    return sum(((-1.0 + 2.0*i/(N-1))*v) for i, v in active) / total

@dataclass
class PID:
    kp: float = 0.7
    ki: float = 0.0
    kd: float = 0.02
    integral_limit: float = 0.5
    integral: float = 0.0
    previous: float = 0.0
    initialized: bool = False

    def step(self, error, dt):
        if dt <= 0:
            return 0.0
        self.integral = clamp(self.integral + error*dt, -self.integral_limit, self.integral_limit)
        derivative = (error-self.previous)/dt if self.initialized else 0.0
        self.previous, self.initialized = error, True
        return self.kp*error + self.ki*self.integral + self.kd*derivative

def motor_mix(base, correction, limit=1.0):
    limit = clamp(limit, 0.0, 1.0)
    return clamp(base+correction, -limit, limit), clamp(base-correction, -limit, limit)

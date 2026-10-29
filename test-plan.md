# Test plan

## Software-only
Run `python -m unittest discover -s tests -v` and `python tests/demo.py`. Tests cover center/left/right position, line loss, sensor-count validation, normalization bounds/polarity, PID response, integral clamp, invalid dt and motor saturation.

## Hardware protocol (pending)
1. Record board ID, firmware commit, track dimensions/surface, battery voltage, wheel/motor details and sensor height.
2. With motors unplugged, record each channel over light and dark surfaces; choose polarity and per-channel min/max.
3. Raise wheels and verify motor direction at low duty cycle; test stop command and driver standby.
4. Start at conservative speed; complete 10 runs or document why fewer were possible.
5. Record each trial's lap time, completed/not completed, line-loss count, battery start/end voltage, and notes in CSV.
6. Report completion rate = completed laps / total attempts; line-loss frequency = total line-loss events / completed laps (also report denominator and failed laps).
7. Never substitute synthetic demo values for measured data. Results remain Pending hardware validation until trials are recorded.

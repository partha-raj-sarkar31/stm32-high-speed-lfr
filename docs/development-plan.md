# Development plan (5–10 days after components arrive)

## Day 0–1: verify and document
- Photograph module labels; record board revision, sensor part number, motor datasheet and battery rating.
- Measure supply rails with a multimeter before connecting logic.
- Confirm stall current is within driver limits; do not test by prolonged stall.

## Day 1–2: sensor bench
- Keep motors disconnected.
- Read all 14 channels over serial; verify channel order, min/max, line polarity and saturation.
- Save calibration values and test over intended track material.

## Day 2–3: motor stage
- Wheels raised; test standby/enable behavior, direction and low PWM independently.
- Confirm motor supply and regulated logic rails remain stable during starts/stops.

## Day 3–5: closed-loop
- Integrate ADC and PWM adapters, fixed control period, line-loss state, and watchdog/failsafe stop.
- Start with low base command and P-only control, then add D and only necessary I.

## Day 5–7: track baseline
- Use fixed track, start point, battery condition and robot configuration.
- Record 10+ attempts where feasible, including failures; publish CSV and firmware revision.

## Day 7–10: tuning and review
- Change one parameter at a time; compare median lap time, completion rate, line-loss count and battery voltage.
- Record limitations and attach real hardware photos/video only after captured.

## Exit criteria
No claim of "high speed" performance until repeatable track data supports it. Hardware integration and physical safety checks take precedence over schedule.

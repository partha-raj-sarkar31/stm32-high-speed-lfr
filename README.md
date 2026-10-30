# STM32 High-Speed Line Follower Robot

**Robotics Society of Varendra University (RSVU), Bangladesh**  
**Status:** software prototype / hardware integration pending

A modular control-software foundation for a line-following robot targeting an STM32F103C8T6 (Blue Pill), a 14-channel analog/digital IR sensor array, TB6612FNG dual motor driver, two nominal 800-1500 RPM geared motors, and a compact LiPo/Li-ion pack (6.6 V nominal). Exact sensor model, motor electrical ratings, regulator, and measured performance remain unverified.

## Objectives
- Sample and calibrate 14 analog channels.
- Estimate line position using a weighted centroid.
- Apply bounded PID steering and a defined line-loss response.
- Keep control logic testable independently of STM32 hardware.
- Measure lap time, completion rate, and line-loss frequency only after track tests.

## Features
- Hardware-independent C++ control primitives in `firmware/src/`.
- Python reference model and deterministic tests in `tests/`.
- Synthetic terminal demonstration.
- Provisional BOM, pin map, wiring plan, safety checklist, and test protocol.


## Repository Structure

``` text
stm32-high-speed-lfr/
├── README.md
├── .gitignore
├── CONTRIBUTING.md
├── firmware/
│   ├── include/
│   │   └── lfr_control.hpp
│   └── src/
│       └── smoke.cpp
├── hardware/
│   ├── BOM.md
│   ├── pin-map.md
│   └── wiring.md
├── docs/
│   ├── architecture.md
│   └── development-plan.md
└── tests/
    ├── lfr_model.py
    ├── test_lfr.py
    ├── demo.py
    ├── test-plan.md
    └── example-results.csv
```

## Architecture
`ADC acquisition -> per-channel calibration/normalization -> weighted position -> PID -> bounded left/right command -> motor driver`

The C++ code is a portable logic layer, not a complete STM32CubeIDE project: clock setup, ADC/DMA, timer PWM, GPIO, startup code, and board-specific HAL integration remain to be added after confirming the exact board and pin allocation.

See [docs/architecture.md](docs/architecture.md), [docs/development-plan.md](docs/development-plan.md), [tests/test-plan.md](tests/test-plan.md), and `hardware/`.

## Components
| Component | Current target | Verification |
|---|---|---|
| MCU board | STM32F103C8T6 Blue Pill | Board revision/clone and pinout pending |
| Sensor array | 14-channel analog IR array | Exact model, output range, spacing and polarity pending |
| Motor driver | TB6612FNG | Verify board breakout and current/thermal limits |
| Motors | Geared motors advertised as 800 RPM | Voltage, stall current, gearbox/output RPM and encoder status pending |
| Battery | 3S 900 mAh, 11.1 V nominal | Chemistry, discharge rating, connector and protection pending |
| Logic regulator | Required, exact part TBD | Must suit input range and current demand |
| Chassis, wheels, switch, wiring | Required | Select and document actual parts |

## Setup
Requirements: Python 3.9+ for tests/demo; a C++11 compiler for the portable control header; STM32CubeIDE only for later MCU integration. No Python third-party dependencies are required.

```bash
python -m unittest discover -s tests -v
python tests/demo.py
```

Portable C++ smoke compile (if `g++` is installed):
```bash
g++ -std=c++11 -Wall -Wextra -Werror -Ifirmware/include firmware/src/smoke.cpp -o /tmp/lfr_smoke
/tmp/lfr_smoke
```

## Usage
The Python demo uses synthetic sensor values; it is not a sensor capture or robot simulation. Example:
```text
Synthetic input: centered line
position: 0.000
line_detected: True
bounded steering correction: 0.000
```
Exact output is available by running the command above.

## Testing
Python tests cover weighted position, calibration bounds, line loss, PID proportional/integral/derivative behavior, and output saturation. The C++ smoke program checks portable primitives compile and execute. Neither test set validates ADC timing, motor electronics, speed, or track performance.

## Results
| Evidence | Status |
|---|---|
| Python unit tests | Run locally before presenting; record actual result |
| C++ portable smoke test | Run locally if compiler available |
| STM32CubeIDE target build | Pending hardware/toolchain integration |
| Sensor calibration on track | Pending hardware validation |
| Lap time / completion rate / line-loss rate | Pending hardware validation |

## Limitations
- No hardware measurements are claimed.
- Sensor polarity, channel order, ADC range, and line color are configurable assumptions.
- PID gains are starting values only and require controlled tuning.
- Line-loss recovery is a bounded search request, not a guarantee of reacquiring the track.
- A 3S battery requires a suitable regulator and careful verification of driver voltage margin.

## Roadmap
1. Confirm exact sensor/motor/battery/regulator specifications.
2. Verify all voltage domains and stall-current limits.
3. Implement CubeIDE ADC/PWM/GPIO adapters.
4. Bench-test sensor readings with motors disconnected.
5. Lift wheels and verify motor direction at low PWM.
6. Calibrate on a marked track and tune controller.
7. Run repeatable laps and publish raw CSV data.

## Safety
Disconnect the battery before wiring. Use a correctly rated charger and battery protection. Never power the MCU from the raw 3S pack. Verify motor stall current against the driver rating, provide a common logic ground where required, and perform first motor tests with wheels raised. Do not leave a LiPo charging unattended.

## License
See `LICENSE`.


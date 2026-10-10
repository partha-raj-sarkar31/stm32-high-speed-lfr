# STM32 High-Speed Line Follower Robot

An STM32-based line follower robot focused on reliable line tracking,
real-time motor control, and measured speed optimization.

> **Project status:** In development\
> **Performance status:** Baseline testing pending. No speed or
> reliability claims are made until results are measured and documented.

## Demo

**Prototype video:** *Placeholder --- add a link after recording a real
hardware demonstration.*

`[Add demo video URL here]`

## Objectives

-   Read and calibrate an infrared line-sensor array.
-   Control two DC motors using an H-bridge motor driver and PWM.
-   Implement line-position estimation and a PID-based steering
    controller.
-   Add line-loss detection and recovery behavior.
-   Measure lap time, completion rate, and line-loss frequency under
    repeatable conditions.

## Hardware

Update this list to match the components actually used.

-   STM32 development board: **\[exact board/model to be added\]**
-   IR line-sensor array: **\[model/channel count to be added\]**
-   DC gear motors and wheels: **\[specifications to be added\]**
-   Dual motor driver: **\[model to be added\]**
-   Battery and power regulation: **\[specifications to be added\]**
-   Chassis, wiring, and switch: **\[details to be added\]**

See [`hardware/`](hardware/) for the bill of materials, wiring, pin
mapping, and chassis files.

## Repository Structure

``` text
stm32-high-speed-lfr/
├── firmware/       # STM32 application, sensor/motor drivers, PID controller
├── hardware/       # BOM, wiring diagrams, pin map, chassis files
├── tests/          # Calibration data, lap logs, line-loss tests
├── docs/           # Design notes, tuning report, test methodology
├── README.md
├── LICENSE
└── .gitignore
```

## Software and Setup

1.  Install the toolchain appropriate for the selected STM32 board (for
    example, STM32CubeIDE).
2.  Record the exact MCU/board revision and firmware toolchain version
    in `docs/`.
3.  Configure GPIO, PWM timer channels, and sensor inputs according to
    the board pinout.
4.  Build and flash the firmware.
5.  Raise the robot on a stand for initial motor-direction and PWM tests
    before placing it on the track.
6.  Calibrate the sensor array on the actual track surface and save the
    calibration procedure/results in `tests/`.

**Pin assignments are not final until the exact board and wiring are
verified.** Check sensor output voltage compatibility with the STM32
input pins before connecting them.

## Control Approach

1.  Sample and calibrate the line sensors.
2.  Estimate the line position from the sensor readings.
3.  Compute steering correction using a documented controller (initially
    P, then PID if needed).
4.  Apply bounded left/right motor PWM commands.
5.  Detect line loss and enter a defined recovery state.

Document controller parameters, sampling rate, PWM frequency, and any
filtering choices in `docs/`.

## Testing and Metrics

Use the same track, start procedure, battery condition, and robot
configuration when comparing changes.

  -----------------------------------------------------------------------
  Metric                  Definition              Status
  ----------------------- ----------------------- -----------------------
  Lap time                Elapsed time for one    Pending testing
                          completed lap           

  Completion rate         Completed laps / total  Pending testing
                          attempts                

  Line-loss count         Number of line-loss     Pending testing
                          events per lap          

  Battery voltage         Voltage recorded for    Pending testing
                          each test session       

  Controller              Firmware revision and   To be recorded
  configuration           controller parameters   
  -----------------------------------------------------------------------

Record individual trials in `tests/` as CSV or another documented
format. Do not publish estimated values as measured results.

## Baseline Results

**Status: Pending testing.** No baseline performance numbers are
available yet.

After testing, report the number of trials, track description, battery
condition, firmware commit, summary statistics, and relevant
limitations. Prefer median and range (or mean and standard deviation
where appropriate) rather than reporting only the best lap.

## Safety

-   Keep wheels off the ground during initial motor-direction tests.
-   Verify driver current limits and motor stall current before extended
    operation.
-   Check battery polarity and voltage before powering the system.
-   Disconnect power before changing wiring.

## Roadmap

-   [ ] Confirm board, sensor, motor-driver, and battery specifications
-   [ ] Document BOM and wiring
-   [ ] Validate sensor readings
-   [ ] Validate independent motor control
-   [ ] Implement line-position estimation
-   [ ] Establish baseline lap tests
-   [ ] Tune PID and compare against baseline
-   [ ] Add real prototype demo video

## License

The project license has not yet been selected. Add the chosen license
text to `LICENSE` before describing this repository as open source.

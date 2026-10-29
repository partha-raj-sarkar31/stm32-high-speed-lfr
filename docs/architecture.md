# Architecture and component requirements

## Data flow
ADC/DMA adapter (future) -> 14 raw samples -> per-channel calibration -> normalized activation -> weighted centroid -> PID -> bounded differential motor command -> TB6612FNG adapter (future).

## Algorithm contract
- Exactly 14 channels, ordered left-to-right.
- Position coordinate is normalized to [-1, +1]; left is negative and right is positive.
- The caller must configure whether line reflectance maps to high or low ADC readings.
- No active sensor above threshold means line lost; return no position rather than inventing a center reading.
- PID time step is seconds and must be positive. Gains are provisional.
- Motor commands are normalized to [-1, +1]; the board adapter must translate magnitude to PWM and sign to direction pins.

## Target integration
Target MCU: STM32F103C8T6. Add a CubeIDE project with HAL ADC/DMA, timer PWM, GPIO, watchdog, and a fixed-rate control loop only after pin mapping is confirmed. Do not put blocking delays in the control loop. Log sampled data over UART only at a rate that does not disrupt control timing.

## Required component specifications
Obtain sensor part number/output voltage/spacing; motor rated voltage, no-load speed and stall current; TB6612FNG breakout schematic; battery chemistry/discharge rating; regulator input/output/current ratings; and chassis/wheel dimensions. Current and voltage compatibility are not verified by this document.

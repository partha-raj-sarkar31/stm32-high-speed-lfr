# Bill of materials (provisional)

| Item | Target | Required verification |
|---|---|---|
| MCU | STM32F103C8T6 Blue Pill | Board clone/revision, USB/programmer |
| Sensor array | 14-channel analog IR | Model, supply voltage, each output range, channel pitch |
| Motor driver | TB6612FNG | Breakout ratings, VM range, continuous/stall current, thermal path |
| Motors | 2 × advertised 800 RPM geared motors | Rated voltage, gearbox output RPM, stall current, shaft |
| Battery | 3S 900 mAh, 11.1 V nominal | Chemistry, max charge voltage, C rating, protection |
| Regulator | Buck converter TBD | 3S input compatibility, regulated output, current rating |
| Mechanical | Chassis, wheels, mounts | Wheel diameter, track width, alignment |
| Safety/wiring | Main switch, fuse, connectors, wire | Current rating, polarity, insulation |

Do not order/energize based on RPM alone. Verify motor stall current and driver thermal/current limits. Use a regulated logic supply; raw 3S voltage is not a 3.3 V rail.

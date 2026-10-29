# Wiring and power checklist

- Battery positive -> appropriately rated fuse/switch -> motor-driver VM, only after confirming pack and driver voltage limits.
- Battery -> appropriately rated buck converter -> MCU/sensor logic rail, with output verified by meter before connection.
- Common ground between MCU, sensor and motor driver as required by module design.
- TB6612 VCC is logic supply; VM is motor supply. Do not confuse the rails.
- STBY must default low until firmware deliberately enables the driver.
- Check sensor output voltage against MCU ADC limits; add level conditioning if required.
- Confirm motor stall current, battery current capability, wire/connector ratings and thermal behavior.
- Disconnect battery before changing wiring. No final wiring until module pin labels and datasheets are checked.

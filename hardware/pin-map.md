# Provisional pin map — not yet electrically verified

| Function | Proposed MCU pin | Notes |
|---|---|---|
| 14 analog sensor outputs | PA0–PA7, PB0–PB1, PC0–PC3 | **Not a valid assumption for every Blue Pill board:** STM32F103C8T6 has limited exposed ADC-capable pins and package pin constraints. Verify exact package/board and remap before use. 14 simultaneous analog inputs may require an external ADC/multiplexer or a different MCU. |
| TB6612 AIN1/AIN2/PWMA | PB12/PB13/PB6 (example only) | Check timer channel mapping and conflicts |
| TB6612 BIN1/BIN2/PWMB | PB14/PB15/PB7 (example only) | Check timer channel mapping and conflicts |
| STBY | PA8 (example only) | Add defined pull-down so driver remains disabled during reset |
| UART debug | PA9/PA10 (USART1) | Commonly used mapping; verify board routing |

This is a planning table, not a final wiring authorization. **Critical architecture gap:** 14 independent analog outputs do not straightforwardly fit the Blue Pill's exposed ADC inputs. Confirm the sensor's interface; if all 14 outputs are analog, choose a verified external ADC/multiplexer or revised MCU before finalizing pins. Never connect a sensor output above the MCU's permitted ADC voltage.

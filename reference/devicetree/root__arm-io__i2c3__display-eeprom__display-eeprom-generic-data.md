# `/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`

- Name: `display-eeprom-generic-data`
- Parent: [`/arm-io/i2c3/display-eeprom`](root__arm-io__i2c3__display-eeprom.md)
- phandle: `185`
- compatible: `display-generic-data,rw`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleEmbeddedTouchEEPROMDriver` | `AppleARMNORFlashDevice` | [`com.apple.driver.AppleEmbeddedTouchEEPROM`](../kexts/com.apple.driver.AppleEmbeddedTouchEEPROM.md) | `display-generic-data,rw` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x440` | `0x126` (294 B) | not memory-mapped (bus address) |

## All properties (6) [DT]

- **`AAPL,phandle`**: `185` (`0xb9`) → phandle of [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md)
- **`compatible`**: `display-generic-data,rw`
- **`display-index`**: `0` (`0x0`)
- **`name`**: `display-eeprom-generic-data`
- **`reg`**: `0x12600000440` (u64; as two u32: `0x440`, `0x126`)
- **`size`**: 16 bytes
  - u32: `0x32 0x32 0x2 0xc0`
  ```
  000000  32 00 00 00 32 00 00 00 02 00 00 00 c0 00 00 00  2...2...........
  ```

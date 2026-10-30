# `/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`

- Name: `display-eeprom-generic-data-2`
- Parent: [`/arm-io/i2c3/display-eeprom-2`](root__arm-io__i2c3__display-eeprom-2.md)
- phandle: `190`
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

- **`AAPL,phandle`**: `190` (`0xbe`) → phandle of [`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md)
- **`compatible`**: `display-generic-data,rw`
- **`display-index`**: `1` (`0x1`)
- **`name`**: `display-eeprom-generic-data-2`
- **`reg`**: `0x12600000440` (u64; as two u32: `0x440`, `0x126`)
- **`size`**: 16 bytes
  - u32: `0x32 0x32 0x2 0xc0`
  ```
  000000  32 00 00 00 32 00 00 00 02 00 00 00 c0 00 00 00  2...2...........
  ```

# `/arm-io/i2c3/display-eeprom`

- Name: `display-eeprom`
- Parent: [`/arm-io/i2c3`](root__arm-io__i2c3.md)
- phandle: `183`
- compatible: `eeprom,i2c`
- Children (2): [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](root__arm-io__i2c3__display-eeprom__display-eeprom-data.md), [`/arm-io/i2c3/display-eeprom/display-eeprom-generic-data`](root__arm-io__i2c3__display-eeprom__display-eeprom-generic-data.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMI2CEEPROM` | `AppleARMIICDevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `eeprom,i2c` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x52 0x9c4 0x0 0x0` | | |

## All properties (7) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `183` (`0xb7`) → phandle of [`/arm-io/i2c3/display-eeprom`](root__arm-io__i2c3__display-eeprom.md)
- **`compatible`**: `eeprom,i2c`
- **`name`**: `display-eeprom`
- **`page-size`**: `32` (`0x20`)
- **`reg`**: 16 bytes
  - u32: `0x52 0x9c4 0x0 0x0`
  ```
  000000  52 00 00 00 c4 09 00 00 00 00 00 00 00 00 00 00  R...............
  ```

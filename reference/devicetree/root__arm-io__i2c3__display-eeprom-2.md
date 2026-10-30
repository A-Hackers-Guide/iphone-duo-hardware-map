# `/arm-io/i2c3/display-eeprom-2`

- Name: `display-eeprom-2`
- Parent: [`/arm-io/i2c3`](root__arm-io__i2c3.md)
- phandle: `188`
- compatible: `eeprom,i2c`
- Children (2): [`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md), [`/arm-io/i2c3/display-eeprom-2/display-eeprom-generic-data-2`](root__arm-io__i2c3__display-eeprom-2__display-eeprom-generic-data-2.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMI2CEEPROM` | `AppleARMIICDevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `eeprom,i2c` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x54 0x9c4 0x0 0x0` | | |

## All properties (7) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `188` (`0xbc`) → phandle of [`/arm-io/i2c3/display-eeprom-2`](root__arm-io__i2c3__display-eeprom-2.md)
- **`compatible`**: `eeprom,i2c`
- **`name`**: `display-eeprom-2`
- **`page-size`**: `32` (`0x20`)
- **`reg`**: 16 bytes
  - u32: `0x54 0x9c4 0x0 0x0`
  ```
  000000  54 00 00 00 c4 09 00 00 00 00 00 00 00 00 00 00  T...............
  ```

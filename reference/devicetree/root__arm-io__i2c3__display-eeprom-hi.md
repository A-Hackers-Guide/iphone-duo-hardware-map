# `/arm-io/i2c3/display-eeprom-hi`

- Name: `display-eeprom-hi`
- Parent: [`/arm-io/i2c3`](root__arm-io__i2c3.md)
- phandle: `186`
- compatible: `eeprom,i2c`
- Children (1): [`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMI2CEEPROM` | `AppleARMIICDevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `eeprom,i2c` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x53 0x9c4 0x0 0x0` | | |

## All properties (7) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `186` (`0xba`) → phandle of [`/arm-io/i2c3/display-eeprom-hi`](root__arm-io__i2c3__display-eeprom-hi.md)
- **`compatible`**: `eeprom,i2c`
- **`name`**: `display-eeprom-hi`
- **`page-size`**: `32` (`0x20`)
- **`reg`**: 16 bytes
  - u32: `0x53 0x9c4 0x0 0x0`
  ```
  000000  53 00 00 00 c4 09 00 00 00 00 00 00 00 00 00 00  S...............
  ```

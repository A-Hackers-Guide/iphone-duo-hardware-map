# `/arm-io/i2c3`

- Name: `i2c3`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `182`
- compatible: `i2c,t8101`, `i2c,s5l8940x`, `iic,soft`
- device_type: `i2c`
- Children (6): [`/arm-io/i2c3/display-eeprom`](root__arm-io__i2c3__display-eeprom.md), [`/arm-io/i2c3/display-eeprom-hi`](root__arm-io__i2c3__display-eeprom-hi.md), [`/arm-io/i2c3/display-eeprom-2`](root__arm-io__i2c3__display-eeprom-2.md), [`/arm-io/i2c3/display-eeprom-2-hi`](root__arm-io__i2c3__display-eeprom-2-hi.md), [`/arm-io/i2c3/mogul-display`](root__arm-io__i2c3__mogul-display.md), [`/arm-io/i2c3/mogul-display2`](root__arm-io__i2c3__mogul-display2.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleS5L8940XI2CController` | `AppleARMIODevice` | [`com.apple.driver.AppleS5L8940XI2C`](../kexts/com.apple.driver.AppleS5L8940XI2C.md) | `i2c,s5l8940x` |
| `AppleARMSoftIICController` | `AppleARMIODevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `iic,soft` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa501c000` | `0x4000` (16,384 B) | `0x2a501c000`–`0x2a501ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1347`

## All properties (15) [DT]

- **`#address-cels`**: `1` (`0x1`)
- **`#size-cells`**: `3` (`0x3`)
- **`AAPL,phandle`**: `182` (`0xb6`) → phandle of [`/arm-io/i2c3`](root__arm-io__i2c3.md)
- **`clock-ids`**: `4` (`0x4`)
- **`compatible`**: `i2c,t8101`, `i2c,s5l8940x`, `iic,soft`
- **`device_type`**: `i2c`
- **`gpio-iic_scl`**: 12 bytes
  - u32: `0xc8 0x10102 0x5041`
  ```
  000000  c8 00 00 00 02 01 01 00 41 50 00 00              ........AP..
  ```
- **`gpio-iic_sda`**: 12 bytes
  - u32: `0xc9 0x10102 0x5041`
  ```
  000000  c9 00 00 00 02 01 01 00 41 50 00 00              ........AP..
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1347` (`0x543`)
- **`name`**: `i2c3`
- **`reg`**: 16 bytes
  - u32: `0xa501c000 0x0 0x4000 0x0`
  ```
  000000  00 c0 01 a5 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`service-gates`**: `14` (`0xe`)
- **`service-reset`**: `35` (`0x23`)
- **`wakeup-device`**: `mogul-display`, `mogul-display2`

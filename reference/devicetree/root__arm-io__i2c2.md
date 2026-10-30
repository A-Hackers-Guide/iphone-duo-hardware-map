# `/arm-io/i2c2`

- Name: `i2c2`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `180`
- compatible: `i2c,t8101`, `i2c,s5l8940x`, `iic,soft`
- device_type: `i2c`
- Children (1): [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleS5L8940XI2CController` | `AppleARMIODevice` | [`com.apple.driver.AppleS5L8940XI2C`](../kexts/com.apple.driver.AppleS5L8940XI2C.md) | `i2c,s5l8940x` |
| `AppleARMSoftIICController` | `AppleARMIODevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `iic,soft` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa5018000` | `0x4000` (16,384 B) | `0x2a5018000`–`0x2a501bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1346`

## All properties (14) [DT]

- **`#address-cels`**: `1` (`0x1`)
- **`#size-cells`**: `3` (`0x3`)
- **`AAPL,phandle`**: `180` (`0xb4`) → phandle of [`/arm-io/i2c2`](root__arm-io__i2c2.md)
- **`clock-ids`**: `4` (`0x4`)
- **`compatible`**: `i2c,t8101`, `i2c,s5l8940x`, `iic,soft`
- **`device_type`**: `i2c`
- **`gpio-iic_scl`**: 12 bytes
  - u32: `0xca 0x10102 0x5041`
  ```
  000000  ca 00 00 00 02 01 01 00 41 50 00 00              ........AP..
  ```
- **`gpio-iic_sda`**: 12 bytes
  - u32: `0xcb 0x10102 0x5041`
  ```
  000000  cb 00 00 00 02 01 01 00 41 50 00 00              ........AP..
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1346` (`0x542`)
- **`name`**: `i2c2`
- **`reg`**: 16 bytes
  - u32: `0xa5018000 0x0 0x4000 0x0`
  ```
  000000  00 80 01 a5 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`service-gates`**: `13` (`0xd`)
- **`service-reset`**: `34` (`0x22`)

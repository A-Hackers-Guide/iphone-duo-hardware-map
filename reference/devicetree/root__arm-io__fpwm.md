# `/arm-io/fpwm`

- Name: `fpwm`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `74`
- compatible: `fpwm,s5l8920x`
- device_type: `fpwm`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleS5L8920XFPWM` | `AppleARMIODevice` | [`com.apple.driver.AppleS5L8920XPWM`](../kexts/com.apple.driver.AppleS5L8920XPWM.md) | `fpwm,s5l8920x` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa5040000` | `0x4000` (16,384 B) | `0x2a5040000`–`0x2a5043fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1353`

## All properties (7) [DT]

- **`AAPL,phandle`**: `74` (`0x4a`) → phandle of [`/arm-io/fpwm`](root__arm-io__fpwm.md)
- **`compatible`**: `fpwm,s5l8920x`
- **`device_type`**: `fpwm`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1353` (`0x549`)
- **`name`**: `fpwm`
- **`reg`**: 16 bytes
  - u32: `0xa5040000 0x0 0x4000 0x0`
  ```
  000000  00 00 04 a5 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

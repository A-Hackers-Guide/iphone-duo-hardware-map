# `/arm-io/mtp-gpio`

- Name: `mtp-gpio`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `117`
- compatible: `gpio,t8101`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8101GPIOIC` | `AppleARMIODevice` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) | `gpio,t8101` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x9481c000` | `0x4000` (16,384 B) | `0x29481c000`–`0x29481ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1392, 1393, 1394, 1395, 1396, 1397, 1398`

## Firmware with a matching name [FW]

- [`Firmware/V68_MtpFirmware.im4p`](../firmware/Firmware__V68_MtpFirmware.im4p.md) (2,308,247 B) Tag: IM4P  Type: mtpf  Version: 1

## All properties (19) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#gpio-int-groups`**: `7` (`0x7`)
- **`#gpio-pins`**: `18` (`0x12`)
- **`#interrupt-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `117` (`0x75`) → phandle of [`/arm-io/mtp-gpio`](root__arm-io__mtp-gpio.md)
- **`compatible`**: `gpio,t8101`
- **`device_type`**: `interrupt-controller`
- **`glitchless`**: `1` (`0x1`)
- **`ie-fix`**: `1` (`0x1`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 28 bytes
  - u32: `0x570 0x571 0x572 0x573 0x574 0x575 0x576`
  ```
  000000  70 05 00 00 71 05 00 00 72 05 00 00 73 05 00 00  p...q...r...s...
  000010  74 05 00 00 75 05 00 00 76 05 00 00              t...u...v...
  ```
- **`name`**: `mtp-gpio`
- **`no-resume-restore`**: `1` (`0x1`)
- **`reg`**: 16 bytes
  - u32: `0x9481c000 0x0 0x4000 0x0`
  ```
  000000  00 c0 81 94 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`role`**: `MTP`
- **`supported-int-groups`**: 12 bytes
  - u32: `0x4 0x5 0x6`
  ```
  000000  04 00 00 00 05 00 00 00 06 00 00 00              ............
  ```
- **`wake-events`**: (present, empty)
- **`wake-no-interrupt-group`**: `4` (`0x4`)

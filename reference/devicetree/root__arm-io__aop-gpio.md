# `/arm-io/aop-gpio`

- Name: `aop-gpio`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `114`
- compatible: `gpio,t8101`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8101GPIOIC` | `AppleARMIODevice` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) | `gpio,t8101` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x90824000` | `0x4000` (16,384 B) | `0x290824000`–`0x290827fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`456, 457, 458, 459, 460, 461, 462`

## Referenced by (8) [DT]

- [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md): function-rose_coredump `GPIO`
- [`/arm-io/aop/iop-aop-nub/gnss`](root__arm-io__aop__iop-aop-nub__gnss.md): function-gnss-time-mark `GPIO`
- [`/arm-io/mt-bt-timestamp-sync`](root__arm-io__mt-bt-timestamp-sync.md): function-timestamp_sync `GPIO`
- [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md): function-reset `GPIO`
- [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md): function-enable `GPIO`
- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-perst `GPIO`
- [`/arm-io/apcie/pci-bridge1`](root__arm-io__apcie__pci-bridge1.md): function-perst `GPIO`
- [`/baseband`](root__baseband.md): function-reset_det `GPIO`

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (20) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#gpio-int-groups`**: `7` (`0x7`)
- **`#gpio-pins`**: `95` (`0x5f`)
- **`#interrupt-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `114` (`0x72`) → phandle of [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md)
- **`compatible`**: `gpio,t8101`
- **`device_type`**: `interrupt-controller`
- **`event_name-mask16`**: `baseband`
- **`glitchless`**: `1` (`0x1`)
- **`ie-fix`**: `1` (`0x1`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 28 bytes
  - u32: `0x1c8 0x1c9 0x1ca 0x1cb 0x1cc 0x1cd 0x1ce`
  ```
  000000  c8 01 00 00 c9 01 00 00 ca 01 00 00 cb 01 00 00  ................
  000010  cc 01 00 00 cd 01 00 00 ce 01 00 00              ............
  ```
- **`name`**: `aop-gpio`
- **`no-resume-restore`**: `1` (`0x1`)
- **`reg`**: 16 bytes
  - u32: `0x90824000 0x0 0x4000 0x0`
  ```
  000000  00 40 82 90 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  ```
- **`role`**: `AOP`
- **`supported-int-groups`**: 16 bytes
  - u32: `0x3 0x4 0x5 0x6`
  ```
  000000  03 00 00 00 04 00 00 00 05 00 00 00 06 00 00 00  ................
  ```
- **`wake-events`**: `4102` (`0x1006`)
- **`wake-no-interrupt-group`**: `4` (`0x4`)

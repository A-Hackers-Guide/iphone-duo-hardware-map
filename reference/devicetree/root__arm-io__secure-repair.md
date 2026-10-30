# `/arm-io/secure-repair`

- Name: `secure-repair`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `448`
- compatible: `secure-repair,1`
- device_type: `secure-repair`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSecureRepair` | `AppleARMIODevice` | [`com.apple.driver.AppleSecureRepair`](../kexts/com.apple.driver.AppleSecureRepair.md) | `secure-repair,1` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x90824000` | `0x4000` (16,384 B) | `0x290824000`–`0x290827fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`456, 457, 458, 459, 460, 461, 462`

## Firmware with a matching name [FW]

- [`Firmware/M3/bin/securem3fw-v68.im4p`](../firmware/Firmware__M3__bin__securem3fw-v68.im4p.md) (99,533 B) Tag: IM4P  Type: sm3f  Version: 1

## All properties (19) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#gpio-int-groups`**: `7` (`0x7`)
- **`#gpio-pins`**: `95` (`0x5f`)
- **`#interrupt-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `448` (`0x1c0`) → phandle of [`/arm-io/secure-repair`](root__arm-io__secure-repair.md)
- **`compatible`**: `secure-repair,1`
- **`device_type`**: `secure-repair`
- **`glitchless`**: `1` (`0x1`)
- **`gpio-repair_en`**: 12 bytes
  - u32: `0x5a 0x101 0x504f41`
  ```
  000000  5a 00 00 00 01 01 00 00 41 4f 50 00              Z.......AOP.
  ```
- **`ie-fix`**: `1` (`0x1`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 28 bytes
  - u32: `0x1c8 0x1c9 0x1ca 0x1cb 0x1cc 0x1cd 0x1ce`
  ```
  000000  c8 01 00 00 c9 01 00 00 ca 01 00 00 cb 01 00 00  ................
  000010  cc 01 00 00 cd 01 00 00 ce 01 00 00              ............
  ```
- **`name`**: `secure-repair`
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
- **`wake-no-interrupt-group`**: `4` (`0x4`)

# `/arm-io/aop-spmi1`

- Name: `aop-spmi1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `215`
- compatible: `aapl,spmi`
- device_type: `interrupt-controller`
- Children (3): [`/arm-io/aop-spmi1/uwb`](root__arm-io__aop-spmi1__uwb.md), [`/arm-io/aop-spmi1/wlan-idc`](root__arm-io__aop-spmi1__wlan-idc.md), [`/arm-io/aop-spmi1/baseband-idc`](root__arm-io__aop-spmi1__baseband-idc.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPMIController` | `AppleARMIODevice` | [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md) | `aapl,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x90b14000` | `0x4000` (16,384 B) | `0x290b14000`–`0x290b17fff` |
| 1 | `0x90b04000` | `0x4000` (16,384 B) | `0x290b04000`–`0x290b07fff` |
| 2 | `0x90b00000` | `0x4000` (16,384 B) | `0x290b00000`–`0x290b03fff` |

## Interrupts [DT]

Controller: unresolved

`256, 501, 281, 260, 261, 264, 265, 266, 268, 269, 279, 280, 282, 283, 284, 285, 272, 273, 262, 263, 267`

## Referenced by (2) [DT]

- [`/arm-io/aop-spmi1/wlan-idc`](root__arm-io__aop-spmi1__wlan-idc.md): interrupts 28, 26, 29, 32
- [`/arm-io/aop-spmi1/baseband-idc`](root__arm-io__aop-spmi1__baseband-idc.md): interrupts 0, 71, 65, 75, 29, 2

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (15) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `215` (`0xd7`) → phandle of [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)
- **`compatible`**: `aapl,spmi`
- **`device_type`**: `interrupt-controller`
- **`error-interrupts`**: 60 bytes
  - u32: `0x104 0x105 0x108 0x109 0x10a 0x10c 0x10d 0x117 0x118 0x11a 0x11b 0x11c 0x11d 0x110 0x111`
  ```
  000000  04 01 00 00 05 01 00 00 08 01 00 00 09 01 00 00  ................
  000010  0a 01 00 00 0c 01 00 00 0d 01 00 00 17 01 00 00  ................
  000020  18 01 00 00 1a 01 00 00 1b 01 00 00 1c 01 00 00  ................
  000030  1d 01 00 00 10 01 00 00 11 01 00 00              ............
  ```
- **`fatal-interrupts`**: `281` (`0x119`)
- **`gen`**: `4` (`0x4`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: 12 bytes
  - u32: `0xd7 0x2d 0xd7`
  ```
  000000  d7 00 00 00 2d 00 00 00 d7 00 00 00              ....-.......
  ```
- **`interrupts`**: 84 bytes
  - u32: `0x100 0x1f5 0x119 0x104 0x105 0x108 0x109 0x10a 0x10c 0x10d 0x117 0x118 0x11a 0x11b 0x11c 0x11d 0x110 0x111 0x106 0x107 0x10b`
  ```
  000000  00 01 00 00 f5 01 00 00 19 01 00 00 04 01 00 00  ................
  000010  05 01 00 00 08 01 00 00 09 01 00 00 0a 01 00 00  ................
  000020  0c 01 00 00 0d 01 00 00 17 01 00 00 18 01 00 00  ................
  000030  1a 01 00 00 1b 01 00 00 1c 01 00 00 1d 01 00 00  ................
  000040  10 01 00 00 11 01 00 00 06 01 00 00 07 01 00 00  ................
  000050  0b 01 00 00                                      ....
  ```
- **`name`**: `aop-spmi1`
- **`other-interrupts`**: 12 bytes
  - u32: `0x106 0x107 0x10b`
  ```
  000000  06 01 00 00 07 01 00 00 0b 01 00 00              ............
  ```
- **`queue-depth`**: `0x10000000100` (u64; as two u32: `0x100`, `0x100`)
- **`reg`**: 48 bytes
  - u32: `0x90b14000 0x0 0x4000 0x0 0x90b04000 0x0 0x4000 0x0 0x90b00000 0x0 0x4000 0x0`
  ```
  000000  00 40 b1 90 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  000010  00 40 b0 90 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  000020  00 00 b0 90 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

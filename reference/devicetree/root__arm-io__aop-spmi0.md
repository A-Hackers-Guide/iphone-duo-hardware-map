# `/arm-io/aop-spmi0`

- Name: `aop-spmi0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `207`
- compatible: `aapl,spmi`
- device_type: `interrupt-controller`
- Children (5): [`/arm-io/aop-spmi0/wlan-heb`](root__arm-io__aop-spmi0__wlan-heb.md), [`/arm-io/aop-spmi0/baseband-heb`](root__arm-io__aop-spmi0__baseband-heb.md), [`/arm-io/aop-spmi0/stockholm-spmi`](root__arm-io__aop-spmi0__stockholm-spmi.md), [`/arm-io/aop-spmi0/hammerfest-spmi`](root__arm-io__aop-spmi0__hammerfest-spmi.md), [`/arm-io/aop-spmi0/uwb0`](root__arm-io__aop-spmi0__uwb0.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPMIController` | `AppleARMIODevice` | [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md) | `aapl,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x90914000` | `0x4000` (16,384 B) | `0x290914000`–`0x290917fff` |
| 1 | `0x90904000` | `0x4000` (16,384 B) | `0x290904000`–`0x290907fff` |
| 2 | `0x90900000` | `0x4000` (16,384 B) | `0x290900000`–`0x290903fff` |

## Interrupts [DT]

Controller: unresolved

`256, 497, 281, 260, 261, 264, 265, 266, 268, 269, 279, 280, 282, 283, 284, 285, 272, 273, 262, 263, 267`

## Referenced by (3) [DT]

- [`/arm-io/aop-spmi0/baseband-heb`](root__arm-io__aop-spmi0__baseband-heb.md): interrupts 0, 71, 65, 75, 29, 76
- [`/arm-io/aop-spmi0/stockholm-spmi`](root__arm-io__aop-spmi0__stockholm-spmi.md): interrupts 176, 177, 178, 179, 180, 181
- [`/arm-io/aop-spmi0/hammerfest-spmi`](root__arm-io__aop-spmi0__hammerfest-spmi.md): interrupts 160, 161, 162, 163, 164, 165

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (15) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `207` (`0xcf`) → phandle of [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
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
  - u32: `0xcf 0x2d 0xcf`
  ```
  000000  cf 00 00 00 2d 00 00 00 cf 00 00 00              ....-.......
  ```
- **`interrupts`**: 84 bytes
  - u32: `0x100 0x1f1 0x119 0x104 0x105 0x108 0x109 0x10a 0x10c 0x10d 0x117 0x118 0x11a 0x11b 0x11c 0x11d 0x110 0x111 0x106 0x107 0x10b`
  ```
  000000  00 01 00 00 f1 01 00 00 19 01 00 00 04 01 00 00  ................
  000010  05 01 00 00 08 01 00 00 09 01 00 00 0a 01 00 00  ................
  000020  0c 01 00 00 0d 01 00 00 17 01 00 00 18 01 00 00  ................
  000030  1a 01 00 00 1b 01 00 00 1c 01 00 00 1d 01 00 00  ................
  000040  10 01 00 00 11 01 00 00 06 01 00 00 07 01 00 00  ................
  000050  0b 01 00 00                                      ....
  ```
- **`name`**: `aop-spmi0`
- **`other-interrupts`**: 12 bytes
  - u32: `0x106 0x107 0x10b`
  ```
  000000  06 01 00 00 07 01 00 00 0b 01 00 00              ............
  ```
- **`queue-depth`**: `0x10000000100` (u64; as two u32: `0x100`, `0x100`)
- **`reg`**: 48 bytes
  - u32: `0x90914000 0x0 0x4000 0x0 0x90904000 0x0 0x4000 0x0 0x90900000 0x0 0x4000 0x0`
  ```
  000000  00 40 91 90 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  000010  00 40 90 90 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  000020  00 00 90 90 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

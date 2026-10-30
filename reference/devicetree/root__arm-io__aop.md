# `/arm-io/aop`

- Name: `aop`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `79`
- compatible: `iop,ascwrap-v8`
- device_type: `aop`
- Children (1): [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x90600000` | `0x74000` (475,136 B) | `0x290600000`–`0x290673fff` |
| 1 | `0x90050000` | `0x4000` (16,384 B) | `0x290050000`–`0x290053fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x90c00000` | `0x1e0000` (1,966,080 B) | `0x290c00000`–`0x290ddffff` |
| 4 | `0x9060c000` | `0x3c008` (245,768 B) | `0x29060c000`–`0x290648007` |
| 5 | `0x882a8000` | `0x8` (8 B) | `0x2882a8000`–`0x2882a8007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`194, 154, 114`

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (18) [DT]

- **`AAPL,phandle`**: `79` (`0x4f`) → phandle of [`/arm-io/aop`](root__arm-io__aop.md)
- **`aop-timesync-reg-index`**: `5` (`0x5`)
- **`clock-gates`**: (present, empty)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `aop`
- **`ext-irq-reg-index`**: `4` (`0x4`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xc2 0x9a 0x72`
  ```
  000000  c2 00 00 00 9a 00 00 00 72 00 00 00              ........r...
  ```
- **`iommu-parent`**: `142` (`0x8e`) → phandle of [`/arm-io/dart-sbr/mapper-aop`](root__arm-io__dart-sbr__mapper-aop.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `0` (`0x0`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `aop`
- **`power-gates`**: (present, empty)
- **`reg`**: 96 bytes
  - u32: `0x90600000 0x0 0x74000 0x0 0x90050000 0x0 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x90c00000 0x0 0x1e0000 0x0 0x9060c000 0x0 0x3c008 0x0 0x882a8000 0x0 0x8 0x0`
  ```
  000000  00 00 60 90 00 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 90 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 00 c0 90 00 00 00 00 00 00 1e 00 00 00 00 00  ................
  000040  00 c0 60 90 00 00 00 00 08 c0 03 00 00 00 00 00  ..`.............
  000050  00 80 2a 88 00 00 00 00 08 00 00 00 00 00 00 00  ..*.............
  ```
- **`role`**: `AOP`

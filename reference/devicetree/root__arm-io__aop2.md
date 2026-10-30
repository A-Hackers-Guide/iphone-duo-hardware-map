# `/arm-io/aop2`

- Name: `aop2`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `110`
- compatible: `iop,ascwrap-v8`
- device_type: `aop2`
- Children (1): [`/arm-io/aop2/iop-aop2-nub`](root__arm-io__aop2__iop-aop2-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x91600000` | `0x74000` (475,136 B) | `0x291600000`–`0x291673fff` |
| 1 | `0x91050000` | `0x4000` (16,384 B) | `0x291050000`–`0x291053fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x9160c000` | `0x3c008` (245,768 B) | `0x29160c000`–`0x291648007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`195, 155, 115`

## Firmware with a matching name [FW]

- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (18) [DT]

- **`AAPL,phandle`**: `110` (`0x6e`) → phandle of [`/arm-io/aop2`](root__arm-io__aop2.md)
- **`clock-gates`**: (present, empty)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `aop2`
- **`ext-irq-reg-index`**: `3` (`0x3`)
- **`idle-ctrl-check`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xc3 0x9b 0x73`
  ```
  000000  c3 00 00 00 9b 00 00 00 73 00 00 00              ........s...
  ```
- **`iommu-parent`**: `143` (`0x8f`) → phandle of [`/arm-io/dart-sbr/mapper-aop2`](root__arm-io__dart-sbr__mapper-aop2.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `1` (`0x1`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `aop2`
- **`power-gates`**: (present, empty)
- **`reg`**: 64 bytes
  - u32: `0x91600000 0x0 0x74000 0x0 0x91050000 0x0 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x9160c000 0x0 0x3c008 0x0`
  ```
  000000  00 00 60 91 00 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 91 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 c0 60 91 00 00 00 00 08 c0 03 00 00 00 00 00  ..`.............
  ```
- **`role`**: `AOP2`

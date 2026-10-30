# `/arm-io/dcpsec`

- Name: `dcpsec`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `255`
- compatible: `iop,ascwrap-v8`
- device_type: `dcp`
- Children (1): [`/arm-io/dcpsec/iop-dcpsec-nub`](root__arm-io__dcpsec__iop-dcpsec-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18ae00000` | `0x74000` (475,136 B) | `0x38ae00000`–`0x38ae73fff` |
| 1 | `0x18a850000` | `0x4000` (16,384 B) | `0x38a850000`–`0x38a853fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x18ae0c000` | `0x3c008` (245,768 B) | `0x38ae0c000`–`0x38ae48007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`205, 165, 125`

## All properties (21) [DT]

- **`AAPL,phandle`**: `255` (`0xff`) → phandle of [`/arm-io/dcpsec`](root__arm-io__dcpsec.md)
- **`clock-gates`**: `38` (`0x26`)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `dcp`
- **`hdcp-channels`**: `6` (`0x6`)
- **`hdcp-parent`**: `126` (`0x7e`) → phandle of [`/arm-io/sep`](root__arm-io__sep.md)
- **`idle-ctrl-check`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xcd 0xa5 0x7d`
  ```
  000000  cd 00 00 00 a5 00 00 00 7d 00 00 00              ........}...
  ```
- **`iommu-parent`**: `261` (`0x105`) → phandle of [`/arm-io/dart-dcpsec/mapper-dcpsec`](root__arm-io__dart-dcpsec__mapper-dcpsec.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `11` (`0xb`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `dcpsec`
- **`power-gates`**: `38` (`0x26`)
- **`reg`**: 64 bytes
  - u32: `0x8ae00000 0x1 0x74000 0x0 0x8a850000 0x1 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x8ae0c000 0x1 0x3c008 0x0`
  ```
  000000  00 00 e0 8a 01 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 8a 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 c0 e0 8a 01 00 00 00 08 c0 03 00 00 00 00 00  ................
  ```
- **`role`**: `DCPSEC`
- **`service-gates`**: `38` (`0x26`)
- **`service-reset`**: `14` (`0xe`)

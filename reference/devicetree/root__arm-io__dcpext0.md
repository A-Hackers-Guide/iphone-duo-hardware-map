# `/arm-io/dcpext0`

- Name: `dcpext0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `277`
- compatible: `iop,ascwrap-v8`
- device_type: `dcp`
- Children (1): [`/arm-io/dcpext0/iop-dcpext0-nub`](root__arm-io__dcpext0__iop-dcpext0-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18ee00000` | `0x74000` (475,136 B) | `0x38ee00000`–`0x38ee73fff` |
| 1 | `0x18e850000` | `0x4000` (16,384 B) | `0x38e850000`–`0x38e853fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x18ee0c000` | `0x3c008` (245,768 B) | `0x38ee0c000`–`0x38ee48007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`204, 164, 124`

## All properties (25) [DT]

- **`AAPL,phandle`**: `277` (`0x115`) → phandle of [`/arm-io/dcpext0`](root__arm-io__dcpext0.md)
- **`audio`**: `289` (`0x121`)
- **`clock-gates`**: `42` (`0x2a`)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `dcp`
- **`dp-switch-parent`**: `219` (`0xdb`) → phandle of [`/arm-io/display-crossbar0`](root__arm-io__display-crossbar0.md)
- **`dp-switch-ufp-endpoint`**: `1` (`0x1`)
- **`dp-switch-ufp-port`**: `0` (`0x0`)
- **`hdcp-channels`**: `7` (`0x7`)
- **`hdcp-parent`**: `126` (`0x7e`) → phandle of [`/arm-io/sep`](root__arm-io__sep.md)
- **`idle-ctrl-check`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xcc 0xa4 0x7c`
  ```
  000000  cc 00 00 00 a4 00 00 00 7c 00 00 00              ........|...
  ```
- **`iommu-parent`**: `280` (`0x118`) → phandle of [`/arm-io/dart-dcpext0/mapper-dcpext0`](root__arm-io__dart-dcpext0__mapper-dcpext0.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `10` (`0xa`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `dcpext0`
- **`power-gates`**: `42` (`0x2a`)
- **`reg`**: 64 bytes
  - u32: `0x8ee00000 0x1 0x74000 0x0 0x8e850000 0x1 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x8ee0c000 0x1 0x3c008 0x0`
  ```
  000000  00 00 e0 8e 01 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 8e 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 c0 e0 8e 01 00 00 00 08 c0 03 00 00 00 00 00  ................
  ```
- **`role`**: `DCPEXT`
- **`service-gates`**: `42` (`0x2a`)
- **`service-reset`**: `12` (`0xc`)

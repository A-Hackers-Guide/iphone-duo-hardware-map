# `/arm-io/dcp`

- Name: `dcp`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `230`
- compatible: `iop,ascwrap-v8`
- device_type: `dcp`
- Children (1): [`/arm-io/dcp/iop-dcp-nub`](root__arm-io__dcp__iop-dcp-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x186e00000` | `0x74000` (475,136 B) | `0x386e00000`–`0x386e73fff` |
| 1 | `0x186850000` | `0x4000` (16,384 B) | `0x386850000`–`0x386853fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x186e0c000` | `0x3c008` (245,768 B) | `0x386e0c000`–`0x386e48007` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`203, 163, 123`

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (21) [DT]

- **`AAPL,phandle`**: `230` (`0xe6`) → phandle of [`/arm-io/dcp`](root__arm-io__dcp.md)
- **`clock-gates`**: `34` (`0x22`)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `dcp`
- **`hdcp-channels`**: `5` (`0x5`)
- **`hdcp-parent`**: `126` (`0x7e`) → phandle of [`/arm-io/sep`](root__arm-io__sep.md)
- **`idle-ctrl-check`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xcb 0xa3 0x7b`
  ```
  000000  cb 00 00 00 a3 00 00 00 7b 00 00 00              ........{...
  ```
- **`iommu-parent`**: `236` (`0xec`) → phandle of [`/arm-io/dart-dcp/mapper-dcp`](root__arm-io__dart-dcp__mapper-dcp.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `9` (`0x9`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `dcp`
- **`power-gates`**: `34` (`0x22`)
- **`reg`**: 64 bytes
  - u32: `0x86e00000 0x1 0x74000 0x0 0x86850000 0x1 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x86e0c000 0x1 0x3c008 0x0`
  ```
  000000  00 00 e0 86 01 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 86 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 c0 e0 86 01 00 00 00 08 c0 03 00 00 00 00 00  ................
  ```
- **`role`**: `DCP`
- **`service-gates`**: `34` (`0x22`)
- **`service-reset`**: `13` (`0xd`)

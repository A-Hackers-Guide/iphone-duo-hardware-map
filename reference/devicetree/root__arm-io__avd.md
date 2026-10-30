# `/arm-io/avd`

- Name: `avd`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `313`
- compatible: `avd,t8103`
- device_type: `avd`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleAVD` | `AppleARMIODevice` | [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md) | `avd,t8103` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x204000000` | `0x163c000` (23,314,432 B) | `0x404000000`–`0x40563bfff` |
| 1 | `0x88078000` | `0x4000` (16,384 B) | `0x288078000`–`0x28807bfff` |
| 2 | `0x96000000` | `0x1c000` (114,688 B) | `0x296000000`–`0x29601bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`207, 167`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `get_valid_perf_states` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFG` | `0x2e 0x2` |
| `mcc_dataset` | [`/arm-io/mcc`](root__arm-io__mcc.md) | `M$DS` | `` |
| `set_perf_state_floor` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFS` | `0x2e 0x2` |

## Firmware with a matching name [FW]

- [`Firmware/avd/AppleAVDFW_H19P.im4p`](../firmware/Firmware__avd__AppleAVDFW_H19P.im4p.md) (107,464 B) Tag: IM4P  Type: avdf  Version: 280d6e11

## All properties (23) [DT]

- **`AAPL,phandle`**: `313` (`0x139`) → phandle of [`/arm-io/avd`](root__arm-io__avd.md)
- **`ads-present`**: `1` (`0x1`)
- **`avd-ads-keytype-version`**: `3` (`0x3`)
- **`avd-version`**: `4` (`0x4`)
- **`clock-gates`**: `46` (`0x2e`)
- **`clock-ids`**: `336` (`0x150`)
- **`compatible`**: `avd,t8103`
- **`decode-samples-per-second`**: `28096` (`0x6dc0`)
- **`device_type`**: `avd`
- **`function-get_valid_perf_states`**: 16 bytes
  - u32: `0x30 0x50524647 0x2e 0x2`
  - text inside: `GFRP.`
  ```
  000000  30 00 00 00 47 46 52 50 2e 00 00 00 02 00 00 00  0...GFRP........
  ```
- **`function-mcc_dataset`**: `0x4d24445300000036` (u64; as two u32: `0x36`, `0x4d244453`)
- **`function-set_perf_state_floor`**: 16 bytes
  - u32: `0x30 0x50524653 0x2e 0x2`
  - text inside: `SFRP.`
  ```
  000000  30 00 00 00 53 46 52 50 2e 00 00 00 02 00 00 00  0...SFRP........
  ```
- **`h264-playback-level`**: `42` (`0x2a`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0xa7000000cf` (u64; as two u32: `0xcf`, `0xa7`)
- **`iommu-parent`**: 12 bytes
  - u32: `0x13b 0x13c 0x13d`
  ```
  000000  3b 01 00 00 3c 01 00 00 3d 01 00 00              ;...<...=...
  ```
- **`msgbox-mailbox-connection`**: `13` (`0xd`)
- **`msgbox-using-postoffice`**: `1` (`0x1`)
- **`name`**: `avd`
- **`power-gates`**: `46` (`0x2e`)
- **`reg`**: 48 bytes
  - u32: `0x4000000 0x2 0x163c000 0x0 0x88078000 0x0 0x4000 0x0 0x96000000 0x0 0x1c000 0x0`
  ```
  000000  00 00 00 04 02 00 00 00 00 c0 63 01 00 00 00 00  ..........c.....
  000010  00 80 07 88 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 00 96 00 00 00 00 00 c0 01 00 00 00 00 00  ................
  ```
- **`service-gates`**: `46` (`0x2e`)
- **`service-reset`**: `9` (`0x9`)

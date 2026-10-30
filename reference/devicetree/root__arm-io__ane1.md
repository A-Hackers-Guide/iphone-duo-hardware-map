# `/arm-io/ane1`

- Name: `ane1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `330`
- compatible: `iop-ane,ascwrap-v8`
- device_type: `ane`
- Children (1): [`/arm-io/ane1/iop-ane1-nub`](root__arm-io__ane1__iop-ane1-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8ANE` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop-ane,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x213e00000` | `0x74000` (475,136 B) | `0x413e00000`–`0x413e73fff` |
| 1 | `0x213850000` | `0x4000` (16,384 B) | `0x413850000`–`0x413853fff` |
| 2 | `0x96000000` | `0x1c000` (114,688 B) | `0x296000000`–`0x29601bfff` |
| 3 | `0x212000000` | `0x1ff4000` (33,505,280 B) | `0x412000000`–`0x413ff3fff` |
| 4 | `0x80700000` | `0x1c000` (114,688 B) | `0x280700000`–`0x28071bfff` |
| 5 | `0x80724000` | `0x4000` (16,384 B) | `0x280724000`–`0x280727fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`211, 171, 726, 739`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `mcc_dataset` | [`/arm-io/mcc`](root__arm-io__mcc.md) | `M$DS` | `` |

## Referenced by (10) [DT]

- [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md): function-ane_perf_ctr1 `ANCR`
- [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md): function-ane1_power_func `ANPW`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-ane1_data_param_set `dSet`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-ane1_ep_control `eCtl`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-ane1_data_param_get `dGet`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-ane1_power_func `ANPW`
- [`/arm-io/isp`](root__arm-io__isp.md): function-ane1_data_param_set `dSet`
- [`/arm-io/isp`](root__arm-io__isp.md): function-ane1_ep_control `eCtl`
- [`/arm-io/isp`](root__arm-io__isp.md): function-ane1_data_param_get `dGet`
- [`/arm-io/isp`](root__arm-io__isp.md): function-ane1_power_func `ANPW`

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane1_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane1_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: ane1  Version: 1

## All properties (25) [DT]

- **`AAPL,phandle`**: `330` (`0x14a`) → phandle of [`/arm-io/ane1`](root__arm-io__ane1.md)
- **`ane-id`**: `1` (`0x1`)
- **`ane-subtype`**: `1` (`0x1`)
- **`ane-type`**: `1024` (`0x400`)
- **`clock-gates`**: `0x1d00000041` (u64; as two u32: `0x41`, `0x1d`)
- **`clock-ids`**: 12 bytes
  - u32: `0x14b 0x14a 0x176`
  ```
  000000  4b 01 00 00 4a 01 00 00 76 01 00 00              K...J...v...
  ```
- **`compatible`**: `iop-ane,ascwrap-v8`
- **`device_type`**: `ane`
- **`die-ane-id`**: `1` (`0x1`)
- **`die-id`**: `0` (`0x0`)
- **`exclave-proxy-parent`**: `343` (`0x157`) → phandle of [`/arm-io/ane1-exclave-proxy`](root__arm-io__ane1-exclave-proxy.md)
- **`function-mcc_dataset`**: `0x4d24445300000036` (u64; as two u32: `0x36`, `0x4d244453`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 16 bytes
  - u32: `0xd3 0xab 0x2d6 0x2e3`
  ```
  000000  d3 00 00 00 ab 00 00 00 d6 02 00 00 e3 02 00 00  ................
  ```
- **`iommu-parent`**: `0x1550000014d` (u64; as two u32: `0x14d`, `0x155`)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `17` (`0x11`)
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `ane1`
- **`power-gates`**: `0x1d00000041` (u64; as two u32: `0x41`, `0x1d`)
- **`reg`**: 96 bytes
  - u32: `0x13e00000 0x2 0x74000 0x0 0x13850000 0x2 0x4000 0x0 0x96000000 0x0 0x1c000 0x0 0x12000000 0x2 0x1ff4000 0x0 0x80700000 0x0 0x1c000 0x0 0x80724000 0x0 0x4000 0x0`
  ```
  000000  00 00 e0 13 02 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 13 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 00 96 00 00 00 00 00 c0 01 00 00 00 00 00  ................
  000030  00 00 00 12 02 00 00 00 00 40 ff 01 00 00 00 00  .........@......
  000040  00 00 70 80 00 00 00 00 00 c0 01 00 00 00 00 00  ..p.............
  000050  00 40 72 80 00 00 00 00 00 40 00 00 00 00 00 00  .@r......@......
  ```
- **`role`**: `ANE1`
- **`service-gates`**: `0x1d00000041` (u64; as two u32: `0x41`, `0x1d`)
- **`service-reset`**: `1` (`0x1`)
- **`sptm-allow-reg`**: 64 bytes
  - u32: `0x81200000 0x0 0xc000 0x0 0x803c0000 0x0 0x40000 0x0 0x11000000 0x0 0xff4000 0x0 0x882c8000 0x0 0x4000 0x0`
  ```
  000000  00 00 20 81 00 00 00 00 00 c0 00 00 00 00 00 00  .. .............
  000010  00 00 3c 80 00 00 00 00 00 00 04 00 00 00 00 00  ..<.............
  000020  00 00 00 11 00 00 00 00 00 40 ff 00 00 00 00 00  .........@......
  000030  00 80 2c 88 00 00 00 00 00 40 00 00 00 00 00 00  ..,......@......
  ```

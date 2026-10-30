# `/arm-io/ispRtb`

- Name: `ispRtb`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `297`
- compatible: `iop-isp,ascwrap-v8`
- device_type: `isp`
- Children (1): [`/arm-io/ispRtb/iop-isp-nub`](root__arm-io__ispRtb__iop-isp-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8SISP` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop-isp,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x181600000` | `0x74000` (475,136 B) | `0x381600000`–`0x381673fff` |
| 1 | `0x181050000` | `0x4000` (16,384 B) | `0x381050000`–`0x381053fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x180000000` | `0x8000` (32,768 B) | `0x380000000`–`0x380007fff` |
| 4 | `0x180000000` | `0x4000000` (67,108,864 B) | `0x380000000`–`0x383ffffff` |
| 5 | `0x80700000` | `0x1c000` (114,688 B) | `0x280700000`–`0x28071bfff` |
| 6 | `0x80724000` | `0x4000` (16,384 B) | `0x280724000`–`0x280727fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`212, 172, 132, 410, 411, 412, 413, 183`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `motion_data_param_set` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datS` | `` |
| `ane_data_param_set` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `dSet` | `` |
| `ane_power_func` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `ANPW` | `` |
| `motion_state_set` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `mstS` | `` |
| `saca0` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d30` |
| `ane1_data_param_set` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `dSet` | `` |
| `saca1` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d31` |
| `saca2` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d36` |
| `saca3` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d42` |
| `saca4` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d44` |
| `saca5` | [`/sacm-jasper`](root__sacm-jasper.md) | `SACA` | `0x63616d47` |
| `saca0b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d32` |
| `saca0c` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d34` |
| `saca0d` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d41` |
| `saca1b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d33` |
| `ane1_ep_control` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `eCtl` | `` |
| `saca1c` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d35` |
| `mcc_dataset` | [`/arm-io/mcc`](root__arm-io__mcc.md) | `M$DS` | `` |
| `saca2b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d37` |
| `ane1_data_param_get` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `dGet` | `` |
| `saca2c` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d38` |
| `motion_data_enable` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `enbl` | `` |
| `saca2d` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d39` |
| `saca3b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d43` |
| `saca4b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d45` |
| `saca4c` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d46` |
| `ane_data_param_get` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `dGet` | `` |
| `motion_data_param_get` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datG` | `` |
| `ane1_power_func` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `ANPW` | `` |
| `ane_ep_control` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `eCtl` | `` |

## All properties (59) [DT]

- **`AAPL,phandle`**: `297` (`0x129`) → phandle of [`/arm-io/ispRtb`](root__arm-io__ispRtb.md)
- **`back-camera-autofocus-recal`**: `syscfg/BCAR` *(placeholder, filled in by iBoot at boot)*
- **`camera-front`**: `1` (`0x1`)
- **`camera-rear`**: `1` (`0x1`)
- **`camera-strobe-color-cal`**: `syscfg/STRB` *(placeholder, filled in by iBoot at boot)*
- **`clock-gates`**: 16 bytes
  - u32: `0x1e 0x1f 0x20 0x21`
  ```
  000000  1e 00 00 00 1f 00 00 00 20 00 00 00 21 00 00 00  ........ ...!...
  ```
- **`clock-ids`**: `0x15a00000158` (u64; as two u32: `0x158`, `0x15a`)
- **`compatible`**: `iop-isp,ascwrap-v8`
- **`device_type`**: `isp`
- **`face-detection-support`**: `1` (`0x1`)
- **`function-ane1_data_param_get`**: `0x644765740000014a` (u64; as two u32: `0x14a`, `0x64476574`)
- **`function-ane1_data_param_set`**: `0x645365740000014a` (u64; as two u32: `0x14a`, `0x64536574`)
- **`function-ane1_ep_control`**: `0x6543746c0000014a` (u64; as two u32: `0x14a`, `0x6543746c`)
- **`function-ane1_power_func`**: `0x414e50570000014a` (u64; as two u32: `0x14a`, `0x414e5057`)
- **`function-ane_data_param_get`**: `0x644765740000013e` (u64; as two u32: `0x13e`, `0x64476574`)
- **`function-ane_data_param_set`**: `0x645365740000013e` (u64; as two u32: `0x13e`, `0x64536574`)
- **`function-ane_ep_control`**: `0x6543746c0000013e` (u64; as two u32: `0x13e`, `0x6543746c`)
- **`function-ane_power_func`**: `0x414e50570000013e` (u64; as two u32: `0x13e`, `0x414e5057`)
- **`function-mcc_dataset`**: `0x4d24445300000036` (u64; as two u32: `0x36`, `0x4d244453`)
- **`function-motion_data_enable`**: `0x656e626c0000005e` (u64; as two u32: `0x5e`, `0x656e626c`)
- **`function-motion_data_param_get`**: `0x646174470000005e` (u64; as two u32: `0x5e`, `0x64617447`)
- **`function-motion_data_param_set`**: `0x646174530000005e` (u64; as two u32: `0x5e`, `0x64617453`)
- **`function-motion_state_set`**: `0x6d7374530000005e` (u64; as two u32: `0x5e`, `0x6d737453`)
- **`function-saca0`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d30`
  - text inside: `ACAS0mac`
  ```
  000000  d2 01 00 00 41 43 41 53 30 6d 61 63              ....ACAS0mac
  ```
- **`function-saca0b`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d32`
  - text inside: `ACAS2mac`
  ```
  000000  d2 01 00 00 41 43 41 53 32 6d 61 63              ....ACAS2mac
  ```
- **`function-saca0c`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d34`
  - text inside: `ACAS4mac`
  ```
  000000  d2 01 00 00 41 43 41 53 34 6d 61 63              ....ACAS4mac
  ```
- **`function-saca0d`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d41`
  - text inside: `ACASAmac`
  ```
  000000  d2 01 00 00 41 43 41 53 41 6d 61 63              ....ACASAmac
  ```
- **`function-saca1`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d31`
  - text inside: `ACAS1mac`
  ```
  000000  d2 01 00 00 41 43 41 53 31 6d 61 63              ....ACAS1mac
  ```
- **`function-saca1b`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d33`
  - text inside: `ACAS3mac`
  ```
  000000  d2 01 00 00 41 43 41 53 33 6d 61 63              ....ACAS3mac
  ```
- **`function-saca1c`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d35`
  - text inside: `ACAS5mac`
  ```
  000000  d2 01 00 00 41 43 41 53 35 6d 61 63              ....ACAS5mac
  ```
- **`function-saca2`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d36`
  - text inside: `ACAS6mac`
  ```
  000000  d2 01 00 00 41 43 41 53 36 6d 61 63              ....ACAS6mac
  ```
- **`function-saca2b`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d37`
  - text inside: `ACAS7mac`
  ```
  000000  d2 01 00 00 41 43 41 53 37 6d 61 63              ....ACAS7mac
  ```
- **`function-saca2c`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d38`
  - text inside: `ACAS8mac`
  ```
  000000  d2 01 00 00 41 43 41 53 38 6d 61 63              ....ACAS8mac
  ```
- **`function-saca2d`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d39`
  - text inside: `ACAS9mac`
  ```
  000000  d2 01 00 00 41 43 41 53 39 6d 61 63              ....ACAS9mac
  ```
- **`function-saca3`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d42`
  - text inside: `ACASBmac`
  ```
  000000  d2 01 00 00 41 43 41 53 42 6d 61 63              ....ACASBmac
  ```
- **`function-saca3b`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d43`
  - text inside: `ACASCmac`
  ```
  000000  d2 01 00 00 41 43 41 53 43 6d 61 63              ....ACASCmac
  ```
- **`function-saca4`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d44`
  - text inside: `ACASDmac`
  ```
  000000  d2 01 00 00 41 43 41 53 44 6d 61 63              ....ACASDmac
  ```
- **`function-saca4b`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d45`
  - text inside: `ACASEmac`
  ```
  000000  d2 01 00 00 41 43 41 53 45 6d 61 63              ....ACASEmac
  ```
- **`function-saca4c`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x63616d46`
  - text inside: `ACASFmac`
  ```
  000000  d2 01 00 00 41 43 41 53 46 6d 61 63              ....ACASFmac
  ```
- **`function-saca5`**: 12 bytes
  - u32: `0x1d3 0x53414341 0x63616d47`
  - text inside: `ACASGmac`
  ```
  000000  d3 01 00 00 41 43 41 53 47 6d 61 63              ....ACASGmac
  ```
- **`has-sphere`**: `1` (`0x1`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 32 bytes
  - u32: `0xd4 0xac 0x84 0x19a 0x19b 0x19c 0x19d 0xb7`
  ```
  000000  d4 00 00 00 ac 00 00 00 84 00 00 00 9a 01 00 00  ................
  000010  9b 01 00 00 9c 01 00 00 9d 01 00 00 b7 00 00 00  ................
  ```
- **`iommu-parent`**: 24 bytes
  - u32: `0x12d 0x12e 0x12f 0x130 0x131 0x132`
  ```
  000000  2d 01 00 00 2e 01 00 00 2f 01 00 00 30 01 00 00  -......./...0...
  000010  31 01 00 00 32 01 00 00                          1...2...
  ```
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `18` (`0x12`)
- **`msgbox-using-alias`**: `1` (`0x1`)
- **`msgbox-using-postoffice`**: `1` (`0x1`)
- **`name`**: `ispRtb`
- **`pearl-calibration-data`**: `syscfg/PrCL` *(placeholder, filled in by iBoot at boot)*
- **`photon-detector-cal-data`**: `syscfg/RACa` *(placeholder, filled in by iBoot at boot)*
- **`photon-detector-cal-data-offset`**: `syscfg/RACm` *(placeholder, filled in by iBoot at boot)*
- **`power-gates`**: 16 bytes
  - u32: `0x1e 0x1f 0x20 0x21`
  ```
  000000  1e 00 00 00 1f 00 00 00 20 00 00 00 21 00 00 00  ........ ...!...
  ```
- **`reg`**: 112 bytes
  - u32: `0x81600000 0x1 0x74000 0x0 0x81050000 0x1 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x80000000 0x1 0x8000 0x0 0x80000000 0x1 0x4000000 0x0 0x80700000 0x0 0x1c000 0x0 0x80724000 0x0 0x4000 0x0`
  ```
  000000  00 00 60 81 01 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 81 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 00 00 80 01 00 00 00 00 80 00 00 00 00 00 00  ................
  000040  00 00 00 80 01 00 00 00 00 00 00 04 00 00 00 00  ................
  000050  00 00 70 80 00 00 00 00 00 c0 01 00 00 00 00 00  ..p.............
  000060  00 40 72 80 00 00 00 00 00 40 00 00 00 00 00 00  .@r......@......
  ```
- **`role`**: `ISP`
- **`rosaline-calibration-current`**: `syscfg/RxCL` *(placeholder, filled in by iBoot at boot)*
- **`sensor-type`**: `131` (`0x83`)
- **`service-gates`**: 16 bytes
  - u32: `0x1e 0x1f 0x20 0x21`
  ```
  000000  1e 00 00 00 1f 00 00 00 20 00 00 00 21 00 00 00  ........ ...!...
  ```
- **`service-reset`**: `15` (`0xf`)

# `/arm-io/isp`

- Name: `isp`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `299`
- compatible: `isp,isp-generic-ex`, `isp,s5l8960x`
- device_type: `isp`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleCamera` | `AppleARMIODevice` | [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md) | `isp,isp-generic-ex` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x180000000` | `0x4000000` (67,108,864 B) | `0x380000000`–`0x383ffffff` |
| 1 | `0x80700000` | `0x1c000` (114,688 B) | `0x280700000`–`0x28071bfff` |
| 2 | `0x80724000` | `0x4000` (16,384 B) | `0x280724000`–`0x280727fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`410, 411, 412, 413, 183`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `conf_isp_ref0_clk_freq` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `ISPC` | `0x0 0x55c11a9e 0x551b9816` |
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
| `saca2b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d37` |
| `ane1_data_param_get` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `dGet` | `` |
| `saca2c` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d38` |
| `motion_data_enable` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `enbl` | `` |
| `saca2d` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d39` |
| `saca3b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d43` |
| `saca4b` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d45` |
| `saca4c` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x63616d46` |
| `conf_isp_ref2_clk_freq` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `ISPC` | `0x2 0x55c11a9e 0x551b9816` |
| `ane_data_param_get` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `dGet` | `` |
| `motion_data_param_get` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datG` | `` |
| `conf_isp_ref1_clk_freq` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `ISPC` | `0x1 0x55c11a9e 0x551b9816` |
| `ane1_power_func` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `ANPW` | `` |
| `ane_ep_control` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `eCtl` | `` |

## Firmware with a matching name [FW]

- [`Firmware/isp_bni/adc-boreas-v68.im4p`](../firmware/Firmware__isp_bni__adc-boreas-v68.im4p.md) (29,851,675 B) Tag: IM4P  Type: ispf  Version: 1

## All properties (61) [DT]

- **`AAPL,phandle`**: `299` (`0x12b`) → phandle of [`/arm-io/isp`](root__arm-io__isp.md)
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
- **`compatible`**: `isp,isp-generic-ex`, `isp,s5l8960x`
- **`device_type`**: `isp`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.ISPEngine_EDK`
- **`exclave-service`**: `com.apple.service.ISPEngine`
- **`face-detection-support`**: `1` (`0x1`)
- **`function-ane1_data_param_get`**: `0x644765740000014a` (u64; as two u32: `0x14a`, `0x64476574`)
- **`function-ane1_data_param_set`**: `0x645365740000014a` (u64; as two u32: `0x14a`, `0x64536574`)
- **`function-ane1_ep_control`**: `0x6543746c0000014a` (u64; as two u32: `0x14a`, `0x6543746c`)
- **`function-ane1_power_func`**: `0x414e50570000014a` (u64; as two u32: `0x14a`, `0x414e5057`)
- **`function-ane_data_param_get`**: `0x644765740000013e` (u64; as two u32: `0x13e`, `0x64476574`)
- **`function-ane_data_param_set`**: `0x645365740000013e` (u64; as two u32: `0x13e`, `0x64536574`)
- **`function-ane_ep_control`**: `0x6543746c0000013e` (u64; as two u32: `0x13e`, `0x6543746c`)
- **`function-ane_power_func`**: `0x414e50570000013e` (u64; as two u32: `0x13e`, `0x414e5057`)
- **`function-conf_isp_ref0_clk_freq`**: 20 bytes
  - u32: `0x30 0x49535043 0x0 0x55c11a9e 0x551b9816`
  - text inside: `CPSI`
  ```
  000000  30 00 00 00 43 50 53 49 00 00 00 00 9e 1a c1 55  0...CPSI.......U
  000010  16 98 1b 55                                      ...U
  ```
- **`function-conf_isp_ref1_clk_freq`**: 20 bytes
  - u32: `0x30 0x49535043 0x1 0x55c11a9e 0x551b9816`
  - text inside: `CPSI`
  ```
  000000  30 00 00 00 43 50 53 49 01 00 00 00 9e 1a c1 55  0...CPSI.......U
  000010  16 98 1b 55                                      ...U
  ```
- **`function-conf_isp_ref2_clk_freq`**: 20 bytes
  - u32: `0x30 0x49535043 0x2 0x55c11a9e 0x551b9816`
  - text inside: `CPSI`
  ```
  000000  30 00 00 00 43 50 53 49 02 00 00 00 9e 1a c1 55  0...CPSI.......U
  000010  16 98 1b 55                                      ...U
  ```
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
- **`interrupts`**: 20 bytes
  - u32: `0x19a 0x19b 0x19c 0x19d 0xb7`
  ```
  000000  9a 01 00 00 9b 01 00 00 9c 01 00 00 9d 01 00 00  ................
  000010  b7 00 00 00                                      ....
  ```
- **`iommu-parent`**: 24 bytes
  - u32: `0x12d 0x12e 0x12f 0x130 0x131 0x132`
  ```
  000000  2d 01 00 00 2e 01 00 00 2f 01 00 00 30 01 00 00  -......./...0...
  000010  31 01 00 00 32 01 00 00                          1...2...
  ```
- **`name`**: `isp`
- **`no-firmware-service`**: (present, empty)
- **`pearl-calibration-data`**: `syscfg/PrCL` *(placeholder, filled in by iBoot at boot)*
- **`photon-detector-cal-data`**: `syscfg/RACa` *(placeholder, filled in by iBoot at boot)*
- **`photon-detector-cal-data-offset`**: `syscfg/RACm` *(placeholder, filled in by iBoot at boot)*
- **`power-gates`**: 16 bytes
  - u32: `0x1e 0x1f 0x20 0x21`
  ```
  000000  1e 00 00 00 1f 00 00 00 20 00 00 00 21 00 00 00  ........ ...!...
  ```
- **`reg`**: 48 bytes
  - u32: `0x80000000 0x1 0x4000000 0x0 0x80700000 0x0 0x1c000 0x0 0x80724000 0x0 0x4000 0x0`
  ```
  000000  00 00 00 80 01 00 00 00 00 00 00 04 00 00 00 00  ................
  000010  00 00 70 80 00 00 00 00 00 c0 01 00 00 00 00 00  ..p.............
  000020  00 40 72 80 00 00 00 00 00 40 00 00 00 00 00 00  .@r......@......
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

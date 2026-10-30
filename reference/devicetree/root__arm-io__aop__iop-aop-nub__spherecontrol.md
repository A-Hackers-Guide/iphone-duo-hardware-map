# `/arm-io/aop/iop-aop-nub/spherecontrol`

- Name: `spherecontrol`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `94`
- device_type: `spherecontrol`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Referenced by (8) [DT]

- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-motion_data_param_set `datS`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-motion_state_set `mstS`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-motion_data_enable `enbl`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-motion_data_param_get `datG`
- [`/arm-io/isp`](root__arm-io__isp.md): function-motion_data_param_set `datS`
- [`/arm-io/isp`](root__arm-io__isp.md): function-motion_state_set `mstS`
- [`/arm-io/isp`](root__arm-io__isp.md): function-motion_data_enable `enbl`
- [`/arm-io/isp`](root__arm-io__isp.md): function-motion_data_param_get `datG`

## All properties (7) [DT]

- **`AAPL,phandle`**: `94` (`0x5e`) → phandle of [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md)
- **`device_type`**: `spherecontrol`
- **`isp-aop-control-config`**: 16 bytes
  - u32: `0x90610000 0x2 0x20000000 0x3d`
  ```
  000000  00 00 61 90 02 00 00 00 00 00 00 20 3d 00 00 00  ..a........ =...
  ```
- **`isp-aop-motion_1-config`**: 16 bytes
  - u32: `0x90610000 0x2 0x40000000 0x3e`
  ```
  000000  00 00 61 90 02 00 00 00 00 00 00 40 3e 00 00 00  ..a........@>...
  ```
- **`isp-aop-motion_full_rate-config`**: 16 bytes
  - u32: `0x90610000 0x2 0x8000000 0x3b`
  ```
  000000  00 00 61 90 02 00 00 00 00 00 00 08 3b 00 00 00  ..a.........;...
  ```
- **`isp-aop-pearl-config`**: 16 bytes
  - u32: `0x90610000 0x2 0x10000000 0x3c`
  ```
  000000  00 00 61 90 02 00 00 00 00 00 00 10 3c 00 00 00  ..a.........<...
  ```
- **`name`**: `spherecontrol`

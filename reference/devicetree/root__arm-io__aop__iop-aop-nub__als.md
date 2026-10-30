# `/arm-io/aop/iop-aop-nub/als`

- Name: `als`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `103`
- device_type: `als`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (13) [DT]

- **`AAPL,phandle`**: `103` (`0x67`) → phandle of [`/arm-io/aop/iop-aop-nub/als`](root__arm-io__aop__iop-aop-nub__als.md)
- **`ce-model`**: `4` (`0x4`)
- **`ce-threshold`**: `26214` (`0x6666`)
- **`device_type`**: `als`
- **`digitizer-location-id`**: `544` (`0x220`)
- **`hotspot-center-x`**: `389480448` (`0x17370000`)
- **`hotspot-center-y`**: `45940736` (`0x2bd0000`)
- **`ma-channel-thr`**: 20 bytes
  - u32: `0x42240000 0x41880000 0x41c80000 0x41c80000 0x41c80000`
  ```
  000000  00 00 24 42 00 00 88 41 00 00 c8 41 00 00 c8 41  ..$B...A...A...A
  000010  00 00 c8 41                                      ...A
  ```
- **`name`**: `als`
- **`occlusion-drives-grimaldi`**: `1` (`0x1`)
- **`strobe-coex`**: `2` (`0x2`)
- **`supports-float-lux`**: `1` (`0x1`)
- **`use-prox-for-occlusion`**: `1` (`0x1`)

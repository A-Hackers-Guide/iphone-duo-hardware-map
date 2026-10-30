# `/arm-io/aop/iop-aop-nub/als2b`

- Name: `als2b`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `84`
- device_type: `als2b`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (11) [DT]

- **`AAPL,phandle`**: `84` (`0x54`) → phandle of [`/arm-io/aop/iop-aop-nub/als2b`](root__arm-io__aop__iop-aop-nub__als2b.md)
- **`angle-dependent`**: `1` (`0x1`)
- **`ce-model`**: `0` (`0x0`)
- **`device_type`**: `als2b`
- **`digitizer-location-id`**: `545` (`0x221`)
- **`hotspot-center-x`**: `670171136` (`0x27f20000`)
- **`hotspot-center-y`**: `658702336` (`0x27430000`)
- **`ma-channel-thr`**: 20 bytes
  - u32: `0x42240000 0x41880000 0x41c80000 0x41c80000 0x41c80000`
  ```
  000000  00 00 24 42 00 00 88 41 00 00 c8 41 00 00 c8 41  ..$B...A...A...A
  000010  00 00 c8 41                                      ...A
  ```
- **`name`**: `als2b`
- **`supports-float-lux`**: `1` (`0x1`)
- **`use-prox-for-occlusion`**: `0` (`0x0`)

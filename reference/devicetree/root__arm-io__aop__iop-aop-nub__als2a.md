# `/arm-io/aop/iop-aop-nub/als2a`

- Name: `als2a`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `83`
- device_type: `als2a`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (12) [DT]

- **`AAPL,phandle`**: `83` (`0x53`) → phandle of [`/arm-io/aop/iop-aop-nub/als2a`](root__arm-io__aop__iop-aop-nub__als2a.md)
- **`angle-dependent`**: `1` (`0x1`)
- **`ce-model`**: `5` (`0x5`)
- **`ce-threshold`**: `7864` (`0x1eb8`)
- **`device_type`**: `als2a`
- **`digitizer-location-id`**: `545` (`0x221`)
- **`hotspot-center-x`**: `46465024` (`0x2c50000`)
- **`hotspot-center-y`**: `348585984` (`0x14c70000`)
- **`ma-channel-thr`**: 20 bytes
  - u32: `0x42240000 0x41880000 0x41c80000 0x41c80000 0x41c80000`
  ```
  000000  00 00 24 42 00 00 88 41 00 00 c8 41 00 00 c8 41  ..$B...A...A...A
  000010  00 00 c8 41                                      ...A
  ```
- **`name`**: `als2a`
- **`supports-float-lux`**: `1` (`0x1`)
- **`use-prox-for-occlusion`**: `0` (`0x0`)

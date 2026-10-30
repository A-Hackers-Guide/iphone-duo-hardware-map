# `/arm-io/aop/iop-aop-nub/hgaccel`

- Name: `hgaccel`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `89`
- device_type: `hgaccel`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (7) [DT]

- **`AAPL,phandle`**: `89` (`0x59`) → phandle of [`/arm-io/aop/iop-aop-nub/hgaccel`](root__arm-io__aop__iop-aop-nub__hgaccel.md)
- **`accel-nominal-extr-cal`**: `syscfg/AhXN,hex/02000201464D30692800000001000000000000000000010000000000000001000000000000000000000000000000000000000100524D3069280000000100000000000100000000000000000000000000000001000000000000000000000000000000FFFF17AF70D7` *(placeholder, filled in by iBoot at boot)*
- **`accel-range-intr-cal`**: 60 bytes
  - u32: `0x1010002 0x0 0x2c 0x1 0x100 0x7d000 0x0 0x0 0x0 0x7d000 0x0 0x0 0x0 0x7d000 0x0`
  ```
  000000  02 00 01 01 00 00 00 00 2c 00 00 00 01 00 00 00  ........,.......
  000010  00 01 00 00 00 d0 07 00 00 00 00 00 00 00 00 00  ................
  000020  00 00 00 00 00 d0 07 00 00 00 00 00 00 00 00 00  ................
  000030  00 00 00 00 00 d0 07 00 00 00 00 00              ............
  ```
- **`device-usage`**: `30` (`0x1e`)
- **`device-usage-page`**: `65280` (`0xff00`)
- **`device_type`**: `hgaccel`
- **`name`**: `hgaccel`

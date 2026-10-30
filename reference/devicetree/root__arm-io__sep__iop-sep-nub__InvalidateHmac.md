# `/arm-io/sep/iop-sep-nub/InvalidateHmac`

- Name: `InvalidateHmac`
- Parent: [`/arm-io/sep/iop-sep-nub`](root__arm-io__sep__iop-sep-nub.md)
- phandle: `130`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (6) [DT]

- **`AAPL,phandle`**: `130` (`0x82`) → phandle of [`/arm-io/sep/iop-sep-nub/InvalidateHmac`](root__arm-io__sep__iop-sep-nub__InvalidateHmac.md)
- **`config`**: `1` (`0x1`)
- **`name`**: `InvalidateHmac`
- **`reg-block`**: 16 bytes
  - u32: `0x882dc000 0x2 0x18000 0x0`
  ```
  000000  00 c0 2d 88 02 00 00 00 00 80 01 00 00 00 00 00  ..-.............
  ```
- **`sio-hmac1-disable-mask`**: `0x1` (u64; as two u32: `0x1`, `0x0`)
- **`sio-hmac1-offset`**: `T`

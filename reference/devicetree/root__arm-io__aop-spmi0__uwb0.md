# `/arm-io/aop-spmi0/uwb0`

- Name: `uwb0`
- Parent: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- phandle: `214`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000f` (12,884,901,903 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## All properties (3) [DT]

- **`AAPL,phandle`**: `214` (`0xd6`) → phandle of [`/arm-io/aop-spmi0/uwb0`](root__arm-io__aop-spmi0__uwb0.md)
- **`name`**: `uwb0`
- **`reg`**: 24 bytes
  - u32: `0xf 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0f 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

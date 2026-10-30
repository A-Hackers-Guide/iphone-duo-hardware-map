# `/arm-io/aop-spmi0/wlan-heb`

- Name: `wlan-heb`
- Parent: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- phandle: `208`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000e` (12,884,901,902 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## All properties (3) [DT]

- **`AAPL,phandle`**: `208` (`0xd0`) → phandle of [`/arm-io/aop-spmi0/wlan-heb`](root__arm-io__aop-spmi0__wlan-heb.md)
- **`name`**: `wlan-heb`
- **`reg`**: 24 bytes
  - u32: `0xe 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0e 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

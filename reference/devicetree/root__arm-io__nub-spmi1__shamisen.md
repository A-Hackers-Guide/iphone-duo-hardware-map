# `/arm-io/nub-spmi1/shamisen`

- Name: `shamisen`
- Parent: [`/arm-io/nub-spmi1`](root__arm-io__nub-spmi1.md)
- phandle: `203`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000c` (12,884,901,900 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## All properties (3) [DT]

- **`AAPL,phandle`**: `203` (`0xcb`) → phandle of [`/arm-io/nub-spmi1/shamisen`](root__arm-io__nub-spmi1__shamisen.md)
- **`name`**: `shamisen`
- **`reg`**: 24 bytes
  - u32: `0xc 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0c 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

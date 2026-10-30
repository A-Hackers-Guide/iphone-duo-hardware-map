# `/arm-io/exdisplaypipe-s-proxy`

- Name: `exdisplaypipe-s-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `254`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x3c4000000` | `0xe2c000` (14,860,288 B) | not memory-mapped (bus address) |
| 1 | `0x3c5000000` | `0xe2c000` (14,860,288 B) | not memory-mapped (bus address) |
| 2 | `0x3c6430000` | `0xc000` (49,152 B) | not memory-mapped (bus address) |
| 3 | `0x3c64b0000` | `0x17c000` (1,556,480 B) | not memory-mapped (bus address) |

## All properties (4) [DT]

- **`AAPL,phandle`**: `254` (`0xfe`) → phandle of [`/arm-io/exdisplaypipe-s-proxy`](root__arm-io__exdisplaypipe-s-proxy.md)
- **`exclave-assigned`**: (present, empty)
- **`name`**: `exdisplaypipe-s-proxy`
- **`reg`**: 64 bytes
  - u32: `0xc4000000 0x3 0xe2c000 0x0 0xc5000000 0x3 0xe2c000 0x0 0xc6430000 0x3 0xc000 0x0 0xc64b0000 0x3 0x17c000 0x0`
  ```
  000000  00 00 00 c4 03 00 00 00 00 c0 e2 00 00 00 00 00  ................
  000010  00 00 00 c5 03 00 00 00 00 c0 e2 00 00 00 00 00  ................
  000020  00 00 43 c6 03 00 00 00 00 c0 00 00 00 00 00 00  ..C.............
  000030  00 00 4b c6 03 00 00 00 00 c0 17 00 00 00 00 00  ..K.............
  ```

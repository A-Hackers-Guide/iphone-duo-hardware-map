# `/arm-io/exdisplaypipe1-s-proxy`

- Name: `exdisplaypipe1-s-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `274`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x3c8000000` | `0xe2c000` (14,860,288 B) | not memory-mapped (bus address) |
| 1 | `0x3c9000000` | `0xe2c000` (14,860,288 B) | not memory-mapped (bus address) |
| 2 | `0x3ca430000` | `0xc000` (49,152 B) | not memory-mapped (bus address) |
| 3 | `0x3ca4b0000` | `0x17c000` (1,556,480 B) | not memory-mapped (bus address) |

## All properties (4) [DT]

- **`AAPL,phandle`**: `274` (`0x112`) → phandle of [`/arm-io/exdisplaypipe1-s-proxy`](root__arm-io__exdisplaypipe1-s-proxy.md)
- **`exclave-assigned`**: (present, empty)
- **`name`**: `exdisplaypipe1-s-proxy`
- **`reg`**: 64 bytes
  - u32: `0xc8000000 0x3 0xe2c000 0x0 0xc9000000 0x3 0xe2c000 0x0 0xca430000 0x3 0xc000 0x0 0xca4b0000 0x3 0x17c000 0x0`
  ```
  000000  00 00 00 c8 03 00 00 00 00 c0 e2 00 00 00 00 00  ................
  000010  00 00 00 c9 03 00 00 00 00 c0 e2 00 00 00 00 00  ................
  000020  00 00 43 ca 03 00 00 00 00 c0 00 00 00 00 00 00  ..C.............
  000030  00 00 4b ca 03 00 00 00 00 c0 17 00 00 00 00 00  ..K.............
  ```

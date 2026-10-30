# `/arm-io/isp-exclave-s-proxy`

- Name: `isp-exclave-s-proxy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `308`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x3c1800000` | `0x480000` (4,718,592 B) | not memory-mapped (bus address) |
| 1 | `0x3c2980000` | `0x1ac000` (1,753,088 B) | not memory-mapped (bus address) |
| 2 | `0x3c2b2c000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 3 | `0x2d6010000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |

## Firmware with a matching name [FW]

- [`Firmware/isp_bni/adc-boreas-v68.im4p`](../firmware/Firmware__isp_bni__adc-boreas-v68.im4p.md) (29,851,675 B) Tag: IM4P  Type: ispf  Version: 1

## All properties (4) [DT]

- **`AAPL,phandle`**: `308` (`0x134`) → phandle of [`/arm-io/isp-exclave-s-proxy`](root__arm-io__isp-exclave-s-proxy.md)
- **`exclave-assigned`**: (present, empty)
- **`name`**: `isp-exclave-s-proxy`
- **`reg`**: 64 bytes
  - u32: `0xc1800000 0x3 0x480000 0x0 0xc2980000 0x3 0x1ac000 0x0 0xc2b2c000 0x3 0x4000 0x0 0xd6010000 0x2 0x4000 0x0`
  ```
  000000  00 00 80 c1 03 00 00 00 00 00 48 00 00 00 00 00  ..........H.....
  000010  00 00 98 c2 03 00 00 00 00 c0 1a 00 00 00 00 00  ................
  000020  00 c0 b2 c2 03 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000030  00 00 01 d6 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

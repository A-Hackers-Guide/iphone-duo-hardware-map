# `/pram`

- Name: `pram`
- Parent: [`/`](root.md)
- phandle: `42`
- device_type: `pram`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x0` (0 B) | `0x0`–`0x0` |

## All properties (4) [DT]

- **`AAPL,phandle`**: `42` (`0x2a`) → phandle of [`/pram`](root__pram.md)
- **`device_type`**: `pram`
- **`name`**: `pram`
- **`reg`**: 16 bytes
  - u32: `0x0 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```

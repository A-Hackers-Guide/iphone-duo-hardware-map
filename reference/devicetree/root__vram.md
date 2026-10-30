# `/vram`

- Name: `vram`
- Parent: [`/`](root.md)
- phandle: `43`
- device_type: `vram`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x0` (0 B) | `0x0`–`0x0` |
| 1 | `0x0` | `0x0` (0 B) | `0x0`–`0x0` |

## All properties (4) [DT]

- **`AAPL,phandle`**: `43` (`0x2b`) → phandle of [`/vram`](root__vram.md)
- **`device_type`**: `vram`
- **`name`**: `vram`
- **`reg`**: 32 bytes
  - u32: `0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```

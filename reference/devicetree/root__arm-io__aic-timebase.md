# `/arm-io/aic-timebase`

- Name: `aic-timebase`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `46`
- device_type: `timer`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x281180000` | `0x1000` (4,096 B) | not memory-mapped (bus address) |

## All properties (4) [DT]

- **`AAPL,phandle`**: `46` (`0x2e`) → phandle of [`/arm-io/aic-timebase`](root__arm-io__aic-timebase.md)
- **`device_type`**: `timer`
- **`name`**: `aic-timebase`
- **`reg`**: 16 bytes
  - u32: `0x81180000 0x2 0x1000 0x0`
  ```
  000000  00 00 18 81 02 00 00 00 00 10 00 00 00 00 00 00  ................
  ```

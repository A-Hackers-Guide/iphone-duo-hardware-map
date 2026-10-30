# `/arm-io/dbgCPU`

- Name: `dbgCPU`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `437`
- compatible: `AppleDebugCPU`
- device_type: `dbgCPU`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x89b00000` | `0x20000` (131,072 B) | `0x289b00000`–`0x289b1ffff` |
| 1 | `0x899c0000` | `0x4000` (16,384 B) | `0x2899c0000`–`0x2899c3fff` |
| 2 | `0x89b78000` | `0x10000` (65,536 B) | `0x289b78000`–`0x289b87fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`374`

## All properties (7) [DT]

- **`AAPL,phandle`**: `437` (`0x1b5`) → phandle of [`/arm-io/dbgCPU`](root__arm-io__dbgCPU.md)
- **`compatible`**: `AppleDebugCPU`
- **`device_type`**: `dbgCPU`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `374` (`0x176`)
- **`name`**: `dbgCPU`
- **`reg`**: 48 bytes
  - u32: `0x89b00000 0x0 0x20000 0x0 0x899c0000 0x0 0x4000 0x0 0x89b78000 0x0 0x10000 0x0`
  ```
  000000  00 00 b0 89 00 00 00 00 00 00 02 00 00 00 00 00  ................
  000010  00 00 9c 89 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 80 b7 89 00 00 00 00 00 00 01 00 00 00 00 00  ................
  ```

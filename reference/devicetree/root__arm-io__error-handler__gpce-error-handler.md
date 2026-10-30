# `/arm-io/error-handler/gpce-error-handler`

- Name: `gpce-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `69`
- device_type: `gpce-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x80440000 0x0 0x4000 0x0 0x80444000 0x0 0x4000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1093, 1095`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `69` (`0x45`) → phandle of [`/arm-io/error-handler/gpce-error-handler`](root__arm-io__error-handler__gpce-error-handler.md)
- **`device_type`**: `gpce-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x44700000445` (u64; as two u32: `0x445`, `0x447`)
- **`name`**: `gpce-error-handler`
- **`nametag`**: `1735418656` (`0x67706320`) (four-char code `gpc `)
- **`reg`**: 32 bytes
  - u32: `0x80440000 0x0 0x4000 0x0 0x80444000 0x0 0x4000 0x0`
  ```
  000000  00 00 44 80 00 00 00 00 00 40 00 00 00 00 00 00  ..D......@......
  000010  00 40 44 80 00 00 00 00 00 40 00 00 00 00 00 00  .@D......@......
  ```

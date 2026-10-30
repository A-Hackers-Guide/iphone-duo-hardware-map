# `/arm-io/error-handler/cllt-error-handler`

- Name: `cllt-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `59`
- device_type: `cllt-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x80770000 0x0 0x4000 0x0 0x80771000 0x0 0x4000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`304`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `59` (`0x3b`) → phandle of [`/arm-io/error-handler/cllt-error-handler`](root__arm-io__error-handler__cllt-error-handler.md)
- **`device_type`**: `cllt-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `304` (`0x130`)
- **`name`**: `cllt-error-handler`
- **`nametag`**: `1668050036` (`0x636c6c74`) (four-char code `cllt`)
- **`reg`**: 32 bytes
  - u32: `0x80770000 0x0 0x4000 0x0 0x80771000 0x0 0x4000 0x0`
  ```
  000000  00 00 77 80 00 00 00 00 00 40 00 00 00 00 00 00  ..w......@......
  000010  00 10 77 80 00 00 00 00 00 40 00 00 00 00 00 00  ..w......@......
  ```

# `/arm-io/error-handler/amcc-error-handler`

- Name: `amcc-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `56`
- device_type: `amcc-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x20000000 0x0 0x100000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`356, 358, 360`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `56` (`0x38`) → phandle of [`/arm-io/error-handler/amcc-error-handler`](root__arm-io__error-handler__amcc-error-handler.md)
- **`device_type`**: `amcc-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0x164 0x166 0x168`
  ```
  000000  64 01 00 00 66 01 00 00 68 01 00 00              d...f...h...
  ```
- **`name`**: `amcc-error-handler`
- **`nametag`**: `1634558819` (`0x616d6363`) (four-char code `amcc`)
- **`reg`**: 16 bytes
  - u32: `0x20000000 0x0 0x100000 0x0`
  ```
  000000  00 00 00 20 00 00 00 00 00 00 10 00 00 00 00 00  ... ............
  ```

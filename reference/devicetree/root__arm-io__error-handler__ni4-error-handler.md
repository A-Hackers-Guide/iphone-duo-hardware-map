# `/arm-io/error-handler/ni4-error-handler`

- Name: `ni4-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `65`
- device_type: `ni4-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x55000000 0x0 0x8000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`84`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `65` (`0x41`) → phandle of [`/arm-io/error-handler/ni4-error-handler`](root__arm-io__error-handler__ni4-error-handler.md)
- **`device_type`**: `ni4-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `84` (`0x54`)
- **`name`**: `ni4-error-handler`
- **`nametag`**: `1852388384` (`0x6e693420`) (four-char code `ni4 `)
- **`reg`**: 16 bytes
  - u32: `0x55000000 0x0 0x8000 0x0`
  ```
  000000  00 00 00 55 00 00 00 00 00 80 00 00 00 00 00 00  ...U............
  ```

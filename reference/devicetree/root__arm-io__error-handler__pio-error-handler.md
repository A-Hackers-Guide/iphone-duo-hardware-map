# `/arm-io/error-handler/pio-error-handler`

- Name: `pio-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `67`
- device_type: `pio-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x5b000000 0x0 0x24000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`87`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `67` (`0x43`) → phandle of [`/arm-io/error-handler/pio-error-handler`](root__arm-io__error-handler__pio-error-handler.md)
- **`device_type`**: `pio-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `87` (`0x57`)
- **`name`**: `pio-error-handler`
- **`nametag`**: `1885957920` (`0x70696f20`) (four-char code `pio `)
- **`reg`**: 16 bytes
  - u32: `0x5b000000 0x0 0x24000 0x0`
  ```
  000000  00 00 00 5b 00 00 00 00 00 40 02 00 00 00 00 00  ...[.....@......
  ```

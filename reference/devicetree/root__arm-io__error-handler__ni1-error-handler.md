# `/arm-io/error-handler/ni1-error-handler`

- Name: `ni1-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `62`
- device_type: `ni1-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x50000000 0x0 0x8000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`81`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `62` (`0x3e`) → phandle of [`/arm-io/error-handler/ni1-error-handler`](root__arm-io__error-handler__ni1-error-handler.md)
- **`device_type`**: `ni1-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `81` (`0x51`)
- **`name`**: `ni1-error-handler`
- **`nametag`**: `1852387616` (`0x6e693120`) (four-char code `ni1 `)
- **`reg`**: 16 bytes
  - u32: `0x50000000 0x0 0x8000 0x0`
  ```
  000000  00 00 00 50 00 00 00 00 00 80 00 00 00 00 00 00  ...P............
  ```

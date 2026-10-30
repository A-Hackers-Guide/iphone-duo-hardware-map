# `/arm-io/error-handler/ni2-error-handler`

- Name: `ni2-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `63`
- device_type: `ni2-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x51000000 0x0 0x8000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`82`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `63` (`0x3f`) → phandle of [`/arm-io/error-handler/ni2-error-handler`](root__arm-io__error-handler__ni2-error-handler.md)
- **`device_type`**: `ni2-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `82` (`0x52`)
- **`name`**: `ni2-error-handler`
- **`nametag`**: `1852387872` (`0x6e693220`) (four-char code `ni2 `)
- **`reg`**: 16 bytes
  - u32: `0x51000000 0x0 0x8000 0x0`
  ```
  000000  00 00 00 51 00 00 00 00 00 80 00 00 00 00 00 00  ...Q............
  ```

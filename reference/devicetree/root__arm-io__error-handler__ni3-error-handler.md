# `/arm-io/error-handler/ni3-error-handler`

- Name: `ni3-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `64`
- device_type: `ni3-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x52000000 0x0 0x8000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`83`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `64` (`0x40`) → phandle of [`/arm-io/error-handler/ni3-error-handler`](root__arm-io__error-handler__ni3-error-handler.md)
- **`device_type`**: `ni3-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `83` (`0x53`)
- **`name`**: `ni3-error-handler`
- **`nametag`**: `1852388128` (`0x6e693320`) (four-char code `ni3 `)
- **`reg`**: 16 bytes
  - u32: `0x52000000 0x0 0x8000 0x0`
  ```
  000000  00 00 00 52 00 00 00 00 00 80 00 00 00 00 00 00  ...R............
  ```

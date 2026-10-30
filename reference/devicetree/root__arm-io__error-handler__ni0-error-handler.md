# `/arm-io/error-handler/ni0-error-handler`

- Name: `ni0-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `61`
- device_type: `ni0-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4f000000 0x0 0x8000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`80`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `61` (`0x3d`) → phandle of [`/arm-io/error-handler/ni0-error-handler`](root__arm-io__error-handler__ni0-error-handler.md)
- **`device_type`**: `ni0-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `80` (`0x50`)
- **`name`**: `ni0-error-handler`
- **`nametag`**: `1852387360` (`0x6e693020`) (four-char code `ni0 `)
- **`reg`**: 16 bytes
  - u32: `0x4f000000 0x0 0x8000 0x0`
  ```
  000000  00 00 00 4f 00 00 00 00 00 80 00 00 00 00 00 00  ...O............
  ```

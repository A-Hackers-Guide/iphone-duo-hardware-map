# `/arm-io/error-handler/nsi-error-handler`

- Name: `nsi-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `66`
- device_type: `nsi-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x57000000 0x0 0x1000000 0x0 0x58000000 0x0 0x1000000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`85, 86`

## All properties (11) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `66` (`0x42`) → phandle of [`/arm-io/error-handler/nsi-error-handler`](root__arm-io__error-handler__nsi-error-handler.md)
- **`afi-ns-names`**: `0x4e5331204e533020` (u64; as two u32: `0x4e533020`, `0x4e533120`)
- **`device_type`**: `nsi-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `U`, `V`
- **`name`**: `nsi-error-handler`
- **`nametag`**: `1853057312` (`0x6e736920`) (four-char code `nsi `)
- **`reg`**: 32 bytes
  - u32: `0x57000000 0x0 0x1000000 0x0 0x58000000 0x0 0x1000000 0x0`
  ```
  000000  00 00 00 57 00 00 00 00 00 00 00 01 00 00 00 00  ...W............
  000010  00 00 00 58 00 00 00 00 00 00 00 01 00 00 00 00  ...X............
  ```

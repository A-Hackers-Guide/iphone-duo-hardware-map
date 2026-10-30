# `/arm-io/atc0-dpphy`

- Name: `atc0-dpphy`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `221`
- compatible: `atc-dpphy,t8160`
- device_type: `AAPL,atc-dpphy`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (13) [DT]

- **`AAPL,phandle`**: `221` (`0xdd`) → phandle of [`/arm-io/atc0-dpphy`](root__arm-io__atc0-dpphy.md)
- **`atc-phy`**: `222` (`0xde`)
- **`compatible`**: `atc-dpphy,t8160`
- **`device_type`**: `AAPL,atc-dpphy`
- **`dp-switch-dfp-endpoint`**: `0` (`0x0`)
- **`dp-switch-dfp-port`**: `0` (`0x0`)
- **`dp-switch-parent`**: `219` (`0xdb`) → phandle of [`/arm-io/display-crossbar0`](root__arm-io__display-crossbar0.md)
- **`dpxbar-parent`**: `220` (`0xdc`) → phandle of [`/arm-io/atc0-dpxbar`](root__arm-io__atc0-dpxbar.md)
- **`name`**: `atc0-dpphy`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`transport-tunneled`**: `0` (`0x0`)
- **`transport-type`**: `5` (`0x5`)

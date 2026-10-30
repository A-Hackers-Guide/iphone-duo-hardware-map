# `/arm-io/display-crossbar0`

- Name: `display-crossbar0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `219`
- compatible: `display-crossbar,t8112`
- device_type: `AAPL,display-crossbar`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8112DisplayCrossbar` | `AppleARMIODevice` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) | `display-crossbar,t8112` |

## Referenced by (2) [DT]

- [`/arm-io/atc0-dpphy`](root__arm-io__atc0-dpphy.md): `dp-switch-parent`
- [`/arm-io/dcpext0`](root__arm-io__dcpext0.md): `dp-switch-parent`

## All properties (7) [DT]

- **`AAPL,phandle`**: `219` (`0xdb`) → phandle of [`/arm-io/display-crossbar0`](root__arm-io__display-crossbar0.md)
- **`compatible`**: `display-crossbar,t8112`
- **`device_type`**: `AAPL,display-crossbar`
- **`dfp-endpoints`**: `atc0`, `lpdptx`
- **`name`**: `display-crossbar0`
- **`ufp-count`**: `1` (`0x1`)
- **`ufp-endpoints`**: `dispext0`, `dispext1`

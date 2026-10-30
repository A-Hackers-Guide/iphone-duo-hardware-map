# `/arm-io/atc0-dpxbar`

- Name: `atc0-dpxbar`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `220`
- compatible: `atc-dpxbar,t602x`
- device_type: `AAPL,atc-dpxbar`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT602XATCDPXBAR` | `AppleARMIODevice` | [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md) | `atc-dpxbar,t602x` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x323074000` | `0x4000` (16,384 B) | `0x323074000`–`0x323077fff` |

## Referenced by (1) [DT]

- [`/arm-io/atc0-dpphy`](root__arm-io__atc0-dpphy.md): `dpxbar-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `220` (`0xdc`) → phandle of [`/arm-io/atc0-dpxbar`](root__arm-io__atc0-dpxbar.md)
- **`compatible`**: `atc-dpxbar,t602x`
- **`device_type`**: `AAPL,atc-dpxbar`
- **`name`**: `atc0-dpxbar`
- **`reg`**: 16 bytes
  - u32: `0x23074000 0x3 0x4000 0x0`
  ```
  000000  00 40 07 23 03 00 00 00 00 40 00 00 00 00 00 00  .@.#.....@......
  ```

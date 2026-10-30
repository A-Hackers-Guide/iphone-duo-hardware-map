# `/arm-io/bluetooth`

- Name: `bluetooth`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `443`
- device_type: `bluetooth`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0xf 0x0` | | |

## All properties (6) [DT]

- **`AAPL,phandle`**: `443` (`0x1bb`) → phandle of [`/arm-io/bluetooth`](root__arm-io__bluetooth.md)
- **`device_type`**: `bluetooth`
- **`local-mac-address`**: `macaddr/btaddr,syscfg/BMac/6,zeroes/6` *(placeholder, filled in by iBoot at boot)*
- **`name`**: `bluetooth`
- **`reg`**: `0xf` (u64; as two u32: `0xf`, `0x0`)
- **`transport-encoding`**: `9` (`0x9`)

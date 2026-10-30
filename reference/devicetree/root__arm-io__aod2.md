# `/arm-io/aod2`

- Name: `aod2`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `438`
- compatible: `aod,t8101`, `aod,s5l8960x`
- device_type: `aod`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `aod_swclk` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x68 0x101` |
| `aod_swdio` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x62 0x100` |

## All properties (8) [DT]

- **`AAPL,phandle`**: `438` (`0x1b6`) → phandle of [`/arm-io/aod2`](root__arm-io__aod2.md)
- **`compatible`**: `aod,t8101`, `aod,s5l8960x`
- **`default-tck`**: `5000` (`0x1388`)
- **`device_type`**: `aod`
- **`function-aod_swclk`**: 16 bytes
  - u32: `0x35 0x4750494f 0x68 0x101`
  - text inside: `OIPGh`
  ```
  000000  35 00 00 00 4f 49 50 47 68 00 00 00 01 01 00 00  5...OIPGh.......
  ```
- **`function-aod_swdio`**: 16 bytes
  - u32: `0x35 0x4750494f 0x62 0x100`
  - text inside: `OIPGb`
  ```
  000000  35 00 00 00 4f 49 50 47 62 00 00 00 00 01 00 00  5...OIPGb.......
  ```
- **`name`**: `aod2`
- **`probe-port`**: `7882` (`0x1eca`)

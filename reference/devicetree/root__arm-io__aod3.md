# `/arm-io/aod3`

- Name: `aod3`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `439`
- compatible: `aod,t8101`, `aod,s5l8960x`
- device_type: `aod`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `aod_swclk` | [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md) | `GPIO` | `0x5 0x100` |
| `aod_swdio` | [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md) | `GPIO` | `0x8 0x101` |

## All properties (8) [DT]

- **`AAPL,phandle`**: `439` (`0x1b7`) → phandle of [`/arm-io/aod3`](root__arm-io__aod3.md)
- **`compatible`**: `aod,t8101`, `aod,s5l8960x`
- **`default-tck`**: `100` (`0x64`)
- **`device_type`**: `aod`
- **`function-aod_swclk`**: 16 bytes
  - u32: `0x73 0x4750494f 0x5 0x100`
  - text inside: `OIPG`
  ```
  000000  73 00 00 00 4f 49 50 47 05 00 00 00 00 01 00 00  s...OIPG........
  ```
- **`function-aod_swdio`**: 16 bytes
  - u32: `0x73 0x4750494f 0x8 0x101`
  - text inside: `OIPG`
  ```
  000000  73 00 00 00 4f 49 50 47 08 00 00 00 01 01 00 00  s...OIPG........
  ```
- **`name`**: `aod3`
- **`probe-port`**: `7883` (`0x1ecb`)

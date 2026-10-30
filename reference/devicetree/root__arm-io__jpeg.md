# `/arm-io/jpeg`

- Name: `jpeg`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `294`
- compatible: `jpeg,t8101`, `jpeg,s5l8920x`
- device_type: `jpeg`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleJPEGDriver` | `AppleARMIODevice` | [`com.apple.driver.AppleJPEGDriver`](../kexts/com.apple.driver.AppleJPEGDriver.md) | `jpeg,s5l8920x` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x207000000` | `0x4000` (16,384 B) | `0x407000000`–`0x407003fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1282`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `get_valid_perf_states` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFG` | `0x2c 0x2` |
| `set_perf_state_floor` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFS` | `0x2c 0x2` |

## All properties (18) [DT]

- **`AAPL,phandle`**: `294` (`0x126`) → phandle of [`/arm-io/jpeg`](root__arm-io__jpeg.md)
- **`clock-gates`**: `44` (`0x2c`)
- **`clock-ids`**: `0x14900000148` (u64; as two u32: `0x148`, `0x149`)
- **`compatible`**: `jpeg,t8101`, `jpeg,s5l8920x`
- **`coprovider-group`**: `jpeg`
- **`device_type`**: `jpeg`
- **`function-get_valid_perf_states`**: 16 bytes
  - u32: `0x30 0x50524647 0x2c 0x2`
  - text inside: `GFRP,`
  ```
  000000  30 00 00 00 47 46 52 50 2c 00 00 00 02 00 00 00  0...GFRP,.......
  ```
- **`function-set_perf_state_floor`**: 16 bytes
  - u32: `0x30 0x50524653 0x2c 0x2`
  - text inside: `SFRP,`
  ```
  000000  30 00 00 00 53 46 52 50 2c 00 00 00 02 00 00 00  0...SFRP,.......
  ```
- **`hw-type`**: `130000`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1282` (`0x502`)
- **`iommu-parent`**: `296` (`0x128`) → phandle of [`/arm-io/dart-jpeg/mapper-jpeg`](root__arm-io__dart-jpeg__mapper-jpeg.md)
- **`name`**: `jpeg`
- **`power-gates`**: `44` (`0x2c`)
- **`reg`**: 16 bytes
  - u32: `0x7000000 0x2 0x4000 0x0`
  ```
  000000  00 00 00 07 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`service-gates`**: `44` (`0x2c`)
- **`service-reset`**: `16` (`0x10`)
- **`sptm-allow-reg`**: 16 bytes
  - u32: `0x6000000 0x2 0x1000000 0x0`
  ```
  000000  00 00 00 06 02 00 00 00 00 00 00 01 00 00 00 00  ................
  ```

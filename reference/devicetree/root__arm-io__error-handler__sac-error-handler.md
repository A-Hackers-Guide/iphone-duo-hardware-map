# `/arm-io/error-handler/sac-error-handler`

- Name: `sac-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `71`
- device_type: `sac-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `saca_dram` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x6472616d` |
| `avoid_perf_state` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `APRF` | `` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `71` (`0x47`) → phandle of [`/arm-io/error-handler/sac-error-handler`](root__arm-io__error-handler__sac-error-handler.md)
- **`device_type`**: `sac-error-handler`
- **`dram-saca-freqs`**: 36 bytes
  - u32: `0x0 0x0 0x0 0x0 0x0 0xc2d30 0x0 0x104028 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 30 2d 0c 00 00 00 00 00 28 40 10 00  ....0-......(@..
  000020  00 00 00 00                                      ....
  ```
- **`function-avoid_perf_state`**: `0x4150524600000030` (u64; as two u32: `0x30`, `0x41505246`)
- **`function-saca_dram`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x6472616d`
  - text inside: `ACASmard`
  ```
  000000  d2 01 00 00 41 43 41 53 6d 61 72 64              ....ACASmard
  ```
- **`name`**: `sac-error-handler`

# `/arm-io/aop/iop-aop-nub/prox`

- Name: `prox`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `95`
- device_type: `prox`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `saca` | [`/sacm-general`](root__sacm-general.md) | `SACA` | `0x70726f78` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `95` (`0x5f`) → phandle of [`/arm-io/aop/iop-aop-nub/prox`](root__arm-io__aop__iop-aop-nub__prox.md)
- **`device-usage`**: `8` (`0x8`)
- **`device-usage-page`**: `65280` (`0xff00`)
- **`device_type`**: `prox`
- **`function-saca`**: 12 bytes
  - u32: `0x1d2 0x53414341 0x70726f78`
  - text inside: `ACASxorp`
  ```
  000000  d2 01 00 00 41 43 41 53 78 6f 72 70              ....ACASxorp
  ```
- **`name`**: `prox`
- **`prox-calibration`**: `syscfg/PxCl` *(placeholder, filled in by iBoot at boot)*

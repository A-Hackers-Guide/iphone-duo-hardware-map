# `/arm-io/aop/iop-aop-nub/smc-control`

- Name: `smc-control`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `99`
- device_type: `smc-control`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleAOPSMCDriver` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `smc-control` |

## Referenced by (3) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-aop`](root__arm-io__smc__iop-smc-nub__smc-aop.md): function-link-data_param_set `datS`
- [`/arm-io/smc/iop-smc-nub/smc-aop`](root__arm-io__smc__iop-smc-nub__smc-aop.md): function-link-data_enable `enbl`
- [`/arm-io/smc/iop-smc-nub/smc-aop`](root__arm-io__smc__iop-smc-nub__smc-aop.md): function-link-data_param_get `datG`

## All properties (4) [DT]

- **`AAPL,phandle`**: `99` (`0x63`) → phandle of [`/arm-io/aop/iop-aop-nub/smc-control`](root__arm-io__aop__iop-aop-nub__smc-control.md)
- **`device_type`**: `smc-control`
- **`name`**: `smc-control`
- **`smc-aop-charge-config`**: 16 bytes
  - u32: `0x10640000 0x3 0x4 0x2a`
  ```
  000000  00 00 64 10 03 00 00 00 04 00 00 00 2a 00 00 00  ..d.........*...
  ```

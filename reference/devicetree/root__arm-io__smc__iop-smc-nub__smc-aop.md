# `/arm-io/smc/iop-smc-nub/smc-aop`

- Name: `smc-aop`
- Parent: [`/arm-io/smc/iop-smc-nub`](root__arm-io__smc__iop-smc-nub.md)
- phandle: `162`
- device_type: `smc-aop`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleAOPSMC` | `AppleSMCInterface` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | `smc-aop` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `link-data_param_set` | [`/arm-io/aop/iop-aop-nub/smc-control`](root__arm-io__aop__iop-aop-nub__smc-control.md) | `datS` | `` |
| `link-data_enable` | [`/arm-io/aop/iop-aop-nub/smc-control`](root__arm-io__aop__iop-aop-nub__smc-control.md) | `enbl` | `` |
| `link-data_param_get` | [`/arm-io/aop/iop-aop-nub/smc-control`](root__arm-io__aop__iop-aop-nub__smc-control.md) | `datG` | `` |

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `162` (`0xa2`) → phandle of [`/arm-io/smc/iop-smc-nub/smc-aop`](root__arm-io__smc__iop-smc-nub__smc-aop.md)
- **`device_type`**: `smc-aop`
- **`function-link-data_enable`**: `0x656e626c00000063` (u64; as two u32: `0x63`, `0x656e626c`)
- **`function-link-data_param_get`**: `0x6461744700000063` (u64; as two u32: `0x63`, `0x64617447`)
- **`function-link-data_param_set`**: `0x6461745300000063` (u64; as two u32: `0x63`, `0x64617453`)
- **`link-tx_config`**: 20 bytes
  - u32: `0xc640000 0x3 0x20 0x2d 0x1000`
  ```
  000000  00 00 64 0c 03 00 00 00 20 00 00 00 2d 00 00 00  ..d..... ...-...
  000010  00 10 00 00                                      ....
  ```
- **`name`**: `smc-aop`

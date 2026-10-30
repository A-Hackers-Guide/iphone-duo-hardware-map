# `/arm-io/aop/iop-aop-nub/grimaldi-control`

- Name: `grimaldi-control`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `106`
- device_type: `grimaldi-control`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPUGrimaldiDriver` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `grimaldi-control` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `flicker_bias` | [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md) | `flbs` | `` |

## Referenced by (4) [DT]

- [`/arm-io/grimaldi`](root__arm-io__grimaldi.md): function-grimaldi-power-set `pwrS`
- [`/arm-io/grimaldi`](root__arm-io__grimaldi.md): function-grimaldi-device-id `devI`
- [`/arm-io/grimaldi`](root__arm-io__grimaldi.md): function-grimaldi-power-get `pwrG`
- [`/arm-io/grimaldi`](root__arm-io__grimaldi.md): function-grimaldi-gain `gain`

## All properties (4) [DT]

- **`AAPL,phandle`**: `106` (`0x6a`) → phandle of [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md)
- **`device_type`**: `grimaldi-control`
- **`function-flicker_bias`**: `0x666c6273000000b5` (u64; as two u32: `0xb5`, `0x666c6273`)
- **`name`**: `grimaldi-control`

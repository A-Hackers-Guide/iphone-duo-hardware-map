# `/arm-io/grimaldi`

- Name: `grimaldi`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `444`
- compatible: `aop,h16,vd5b704`
- device_type: `grimaldi`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleCameraPhotonDetector` | `AppleARMIODevice` | [`com.apple.driver.AppleCameraPhotonDetector`](../kexts/com.apple.driver.AppleCameraPhotonDetector.md) | `aop,h16,vd5b704` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `grimaldi-power-set` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `pwrS` | `` |
| `grimaldi-device-id` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `devI` | `` |
| `grimaldi-power-get` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `pwrG` | `` |
| `grimaldi-gain` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `gain` | `` |

## All properties (9) [DT]

- **`AAPL,phandle`**: `444` (`0x1bc`) → phandle of [`/arm-io/grimaldi`](root__arm-io__grimaldi.md)
- **`compatible`**: `aop,h16,vd5b704`
- **`device_type`**: `grimaldi`
- **`function-grimaldi-device-id`**: `0x646576490000006a` (u64; as two u32: `0x6a`, `0x64657649`)
- **`function-grimaldi-gain`**: `0x6761696e0000006a` (u64; as two u32: `0x6a`, `0x6761696e`)
- **`function-grimaldi-power-get`**: `0x707772470000006a` (u64; as two u32: `0x6a`, `0x70777247`)
- **`function-grimaldi-power-set`**: `0x707772530000006a` (u64; as two u32: `0x6a`, `0x70777253`)
- **`host`**: `AOP`
- **`name`**: `grimaldi`

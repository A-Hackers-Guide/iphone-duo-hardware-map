# `/sacm-jasper`

- Name: `sacm-jasper`
- Parent: [`/`](root.md)
- phandle: `467`
- compatible: `sacm`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMSlowAdaptiveClockingManager` | `IOPlatformDevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `sacm` |

## Referenced by (3) [DT]

- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca5 `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca5 `SACA`
- [`/baseband`](root__baseband.md): function-jasper-sac `SACC`

## All properties (3) [DT]

- **`AAPL,phandle`**: `467` (`0x1d3`) → phandle of [`/sacm-jasper`](root__sacm-jasper.md)
- **`compatible`**: `sacm`
- **`name`**: `sacm-jasper`

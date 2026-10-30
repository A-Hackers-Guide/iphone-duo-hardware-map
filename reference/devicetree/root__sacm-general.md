# `/sacm-general`

- Name: `sacm-general`
- Parent: [`/`](root.md)
- phandle: `466`
- compatible: `sacm`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleARMSlowAdaptiveClockingManager` | `IOPlatformDevice` | [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md) | `sacm` |

## Referenced by (40) [DT]

- [`/arm-io/error-handler/sac-error-handler`](root__arm-io__error-handler__sac-error-handler.md): function-saca_dram `SACA`
- [`/arm-io/aop/iop-aop-nub/prox`](root__arm-io__aop__iop-aop-nub__prox.md): function-saca `SACA`
- [`/arm-io/dcp-sac-controller`](root__arm-io__dcp-sac-controller.md): function-saca_lcd0 `SACA`
- [`/arm-io/dcp-sac-controller`](root__arm-io__dcp-sac-controller.md): function-saca_lcd1 `SACA`
- [`/arm-io/dcpsec-sac-controller`](root__arm-io__dcpsec-sac-controller.md): function-saca_lcd0 `SACA`
- [`/arm-io/dcpsec-sac-controller`](root__arm-io__dcpsec-sac-controller.md): function-saca_lcd1 `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca0 `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca1 `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca2 `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca3 `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca4 `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca0b `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca0c `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca0d `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca1b `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca1c `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca2b `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca2c `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca2d `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca3b `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca4b `SACA`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-saca4c `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca0 `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca1 `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca2 `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca3 `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca4 `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca0b `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca0c `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca0d `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca1b `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca1c `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca2b `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca2c `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca2d `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca3b `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca4b `SACA`
- [`/arm-io/isp`](root__arm-io__isp.md): function-saca4c `SACA`
- [`/baseband`](root__baseband.md): function-sac `SACC`
- [`/centauri`](root__centauri.md): function-sac `SACC`

## All properties (3) [DT]

- **`AAPL,phandle`**: `466` (`0x1d2`) → phandle of [`/sacm-general`](root__sacm-general.md)
- **`compatible`**: `sacm`
- **`name`**: `sacm-general`

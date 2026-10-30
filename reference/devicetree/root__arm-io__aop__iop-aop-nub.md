# `/arm-io/aop/iop-aop-nub`

- Name: `iop-aop-nub`
- Parent: [`/arm-io/aop`](root__arm-io__aop.md)
- phandle: `80`
- compatible: `iop-nub,rtbuddy-v2`
- Children (27): [`/arm-io/aop/iop-aop-nub/aop-pio-filters`](root__arm-io__aop__iop-aop-nub__aop-pio-filters.md), [`/arm-io/aop/iop-aop-nub/aop-gapf-filters`](root__arm-io__aop__iop-aop-nub__aop-gapf-filters.md), [`/arm-io/aop/iop-aop-nub/als2a`](root__arm-io__aop__iop-aop-nub__als2a.md), [`/arm-io/aop/iop-aop-nub/als2b`](root__arm-io__aop__iop-aop-nub__als2b.md), [`/arm-io/aop/iop-aop-nub/accel_1`](root__arm-io__aop__iop-aop-nub__accel_1.md), [`/arm-io/aop/iop-aop-nub/gyro_1`](root__arm-io__aop__iop-aop-nub__gyro_1.md), [`/arm-io/aop/iop-aop-nub/hgaccel_1`](root__arm-io__aop__iop-aop-nub__hgaccel_1.md), [`/arm-io/aop/iop-aop-nub/accel`](root__arm-io__aop__iop-aop-nub__accel.md), [`/arm-io/aop/iop-aop-nub/hgaccel`](root__arm-io__aop__iop-aop-nub__hgaccel.md), [`/arm-io/aop/iop-aop-nub/gyro`](root__arm-io__aop__iop-aop-nub__gyro.md), [`/arm-io/aop/iop-aop-nub/compass`](root__arm-io__aop__iop-aop-nub__compass.md), [`/arm-io/aop/iop-aop-nub/compass_1`](root__arm-io__aop__iop-aop-nub__compass_1.md), [`/arm-io/aop/iop-aop-nub/pressure`](root__arm-io__aop__iop-aop-nub__pressure.md), [`/arm-io/aop/iop-aop-nub/spherecontrol`](root__arm-io__aop__iop-aop-nub__spherecontrol.md), [`/arm-io/aop/iop-aop-nub/prox`](root__arm-io__aop__iop-aop-nub__prox.md), [`/arm-io/aop/iop-aop-nub/SPUApp`](root__arm-io__aop__iop-aop-nub__SPUApp.md), [`/arm-io/aop/iop-aop-nub/aop-audio`](root__arm-io__aop__iop-aop-nub__aop-audio.md), [`/arm-io/aop/iop-aop-nub/aop-voicetrigger`](root__arm-io__aop__iop-aop-nub__aop-voicetrigger.md), [`/arm-io/aop/iop-aop-nub/smc-control`](root__arm-io__aop__iop-aop-nub__smc-control.md), [`/arm-io/aop/iop-aop-nub/aop-smart-cover`](root__arm-io__aop__iop-aop-nub__aop-smart-cover.md), [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md), [`/arm-io/aop/iop-aop-nub/jarvis`](root__arm-io__aop__iop-aop-nub__jarvis.md), [`/arm-io/aop/iop-aop-nub/als`](root__arm-io__aop__iop-aop-nub__als.md), [`/arm-io/aop/iop-aop-nub/gnss`](root__arm-io__aop__iop-aop-nub__gnss.md), [`/arm-io/aop/iop-aop-nub/dcp-control`](root__arm-io__aop__iop-aop-nub__dcp-control.md), [`/arm-io/aop/iop-aop-nub/grimaldi-control`](root__arm-io__aop__iop-aop-nub__grimaldi-control.md), [`/arm-io/aop/iop-aop-nub/cma`](root__arm-io__aop__iop-aop-nub__cma.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |
| `AppleLVBOOST` | `AppleA7IOPNub` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `iop-aop-nub` |
| `AppleSPUTimesyncV2` | `AppleA7IOPNub` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `iop-aop-nub` |

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (18) [DT]

- **`AAPL,phandle`**: `80` (`0x50`) → phandle of [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- **`aop-fr-timebase`**: `1` (`0x1`)
- **`aop-isp-v2protocol`**: (present, empty)
- **`aop-target`**: `1` (`0x1`)
- **`claim-wake`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`firmware-name`**: `v68aop`
- **`has-baseband`**: (present, empty)
- **`k2-int-opendrain`**: (present, empty)
- **`k2-pkg-id`**: (present, empty)
- **`name`**: `iop-aop-nub`
- **`no-shutdown`**: `1` (`0x1`)
- **`region-base`**: `0x290c00000` (u64; as two u32: `0x90c00000`, `0x2`)
- **`region-size`**: `:`
- **`routes`**: `108` (`0x6c`)
- **`sleep-on-hibernate`**: (present, empty)
- **`watchdog-enable`**: (present, empty)

# `/arm-io/haptics-support-interface`

- Name: `haptics-support-interface`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `441`
- compatible: `haptics-support,leap`
- device_type: `haptics-support-interface`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleHapticsSupportLEAP` | `AppleARMIODevice` | [`com.apple.driver.AppleHapticsSupportLEAP`](../kexts/com.apple.driver.AppleHapticsSupportLEAP.md) | `haptics-support,leap` |

## Referenced by (4) [DT]

- [`/arm-io/iop-audio-controller/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic.md): function-haptics_session `hpsc`
- [`/arm-io/iop-audio-controller/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic.md): function-thermal_budget `ther`
- [`/arm-io/iop-audio-controller/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic.md): function-power_peak_budget `pkpw`
- [`/arm-io/iop-audio-controller/audio-hpdbg`](root__arm-io__iop-audio-controller__audio-hpdbg.md): function-input-data-selectors `hdis`

## All properties (10) [DT]

- **`AAPL,phandle`**: `441` (`0x1b9`) → phandle of [`/arm-io/haptics-support-interface`](root__arm-io__haptics-support-interface.md)
- **`clcl-cal`**: `syscfg/CLCL` *(placeholder, filled in by iBoot at boot)*
- **`clcl-cal-mi`**: `syscfg-mismatch/CLCL` *(placeholder, filled in by iBoot at boot)*
- **`compatible`**: `haptics-support,leap`
- **`device_type`**: `haptics-support-interface`
- **`name`**: `haptics-support-interface`
- **`pscl-cal`**: `syscfg/PSCl` *(placeholder, filled in by iBoot at boot)*
- **`pscl-cal-mi`**: `syscfg-mismatch/PSCl` *(placeholder, filled in by iBoot at boot)*
- **`tcal-cal`**: `syscfg/TCal` *(placeholder, filled in by iBoot at boot)*
- **`tcal-cal-mi`**: `syscfg-mismatch/TCal` *(placeholder, filled in by iBoot at boot)*

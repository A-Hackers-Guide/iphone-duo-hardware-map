# `/arm-io/gfx-asc/iop-gfx-nub`

- Name: `iop-gfx-nub`
- Parent: [`/arm-io/gfx-asc`](root__arm-io__gfx-asc.md)
- phandle: `346`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## All properties (11) [DT]

- **`AAPL,phandle`**: `346` (`0x15a`) → phandle of [`/arm-io/gfx-asc/iop-gfx-nub`](root__arm-io__gfx-asc__iop-gfx-nub.md)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-copy-buffer`**: `32768` (`0x8000`)
- **`coredump-enable`**: `64` (`0x40`)
- **`coredump-rel-privacy-approved`**: (present, empty)
- **`data-isolation`**: `1` (`0x1`)
- **`firmware-name`**: `GFX`
- **`name`**: `iop-gfx-nub`
- **`no-firmware-service`**: (present, empty)
- **`shutdown-sleep`**: (present, empty)
- **`user-power-managed`**: `true`

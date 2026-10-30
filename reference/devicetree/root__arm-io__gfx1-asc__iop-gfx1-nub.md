# `/arm-io/gfx1-asc/iop-gfx1-nub`

- Name: `iop-gfx1-nub`
- Parent: [`/arm-io/gfx1-asc`](root__arm-io__gfx1-asc.md)
- phandle: `348`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## All properties (11) [DT]

- **`AAPL,phandle`**: `348` (`0x15c`) → phandle of [`/arm-io/gfx1-asc/iop-gfx1-nub`](root__arm-io__gfx1-asc__iop-gfx1-nub.md)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-copy-buffer`**: `32768` (`0x8000`)
- **`coredump-enable`**: `64` (`0x40`)
- **`coredump-rel-privacy-approved`**: (present, empty)
- **`data-isolation`**: `1` (`0x1`)
- **`firmware-name`**: `GFX1`
- **`name`**: `iop-gfx1-nub`
- **`no-firmware-service`**: (present, empty)
- **`power-managed`**: `true`
- **`shutdown-sleep`**: (present, empty)

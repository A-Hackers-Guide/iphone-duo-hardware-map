# `/arm-io/dcp/iop-dcp-nub`

- Name: `iop-dcp-nub`
- Parent: [`/arm-io/dcp`](root__arm-io__dcp.md)
- phandle: `231`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## Referenced by (2) [DT]

- [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md): `dart-options`
- [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md): `dart-options`

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (12) [DT]

- **`AAPL,phandle`**: `231` (`0xe7`) → phandle of [`/arm-io/dcp/iop-dcp-nub`](root__arm-io__dcp__iop-dcp-nub.md)
- **`automatic-rail-gating-enabled`**: `1` (`0x1`)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`internal-index`**: `0` (`0x0`)
- **`name`**: `iop-dcp-nub`
- **`no-firmware-service`**: (present, empty)
- **`quiesced`**: (present, empty)
- **`remote-only`**: (present, empty)
- **`routes`**: `251` (`0xfb`)
- **`shutdown-sleep`**: (present, empty)
- **`watchdog-enable`**: (present, empty)

# `/arm-io/dcpsec/iop-dcpsec-nub`

- Name: `iop-dcpsec-nub`
- Parent: [`/arm-io/dcpsec`](root__arm-io__dcpsec.md)
- phandle: `256`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## All properties (14) [DT]

- **`AAPL,phandle`**: `256` (`0x100`) → phandle of [`/arm-io/dcpsec/iop-dcpsec-nub`](root__arm-io__dcpsec__iop-dcpsec-nub.md)
- **`automatic-rail-gating-enabled`**: `1` (`0x1`)
- **`cold-boot-after-hibernate`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`internal-index`**: `1` (`0x1`)
- **`name`**: `iop-dcpsec-nub`
- **`no-firmware-service`**: (present, empty)
- **`no-hibernate-sleep`**: (present, empty)
- **`quiesced`**: (present, empty)
- **`remote-only`**: (present, empty)
- **`routes`**: `271` (`0x10f`)
- **`shutdown-sleep`**: (present, empty)
- **`watchdog-enable`**: (present, empty)

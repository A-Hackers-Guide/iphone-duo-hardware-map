# `/arm-io/dcpext0/iop-dcpext0-nub`

- Name: `iop-dcpext0-nub`
- Parent: [`/arm-io/dcpext0`](root__arm-io__dcpext0.md)
- phandle: `278`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## All properties (15) [DT]

- **`AAPL,phandle`**: `278` (`0x116`) → phandle of [`/arm-io/dcpext0/iop-dcpext0-nub`](root__arm-io__dcpext0__iop-dcpext0-nub.md)
- **`automatic-rail-gating-enabled`**: `1` (`0x1`)
- **`cold-boot-after-hibernate`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`external-index`**: `1` (`0x1`)
- **`name`**: `iop-dcpext0-nub`
- **`no-firmware-service`**: (present, empty)
- **`no-hibernate-sleep`**: (present, empty)
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`quiesced`**: (present, empty)
- **`remote-only`**: (present, empty)
- **`shutdown-sleep`**: (present, empty)
- **`watchdog-enable`**: (present, empty)

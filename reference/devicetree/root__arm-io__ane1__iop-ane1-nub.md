# `/arm-io/ane1/iop-ane1-nub`

- Name: `iop-ane1-nub`
- Parent: [`/arm-io/ane1`](root__arm-io__ane1.md)
- phandle: `331`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane1_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane1_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: ane1  Version: 1

## All properties (9) [DT]

- **`AAPL,phandle`**: `331` (`0x14b`) → phandle of [`/arm-io/ane1/iop-ane1-nub`](root__arm-io__ane1__iop-ane1-nub.md)
- **`ap-recoverable-panics`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`dont-power-on`**: (present, empty)
- **`name`**: `iop-ane1-nub`
- **`no-firmware-service`**: (present, empty)
- **`reconfig-firmware`**: (present, empty)
- **`user-power-managed`**: `1` (`0x1`)

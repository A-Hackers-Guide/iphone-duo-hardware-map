# `/arm-io/mtp/iop-mtp-nub`

- Name: `iop-mtp-nub`
- Parent: [`/arm-io/mtp`](root__arm-io__mtp.md)
- phandle: `170`
- compatible: `iop-nub,rtbuddy-v2`
- Children (5): [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](root__arm-io__mtp__iop-mtp-nub__multi-touch2.md), [`/arm-io/mtp/iop-mtp-nub/sync-agent`](root__arm-io__mtp__iop-mtp-nub__sync-agent.md), [`/arm-io/mtp/iop-mtp-nub/multi-touch`](root__arm-io__mtp__iop-mtp-nub__multi-touch.md), [`/arm-io/mtp/iop-mtp-nub/nova`](root__arm-io__mtp__iop-mtp-nub__nova.md), [`/arm-io/mtp/iop-mtp-nub/mtp`](root__arm-io__mtp__iop-mtp-nub__mtp.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## Firmware with a matching name [FW]

- [`Firmware/V68_MtpFirmware.im4p`](../firmware/Firmware__V68_MtpFirmware.im4p.md) (2,308,247 B) Tag: IM4P  Type: mtpf  Version: 1

## All properties (14) [DT]

- **`AAPL,phandle`**: `170` (`0xaa`) → phandle of [`/arm-io/mtp/iop-mtp-nub`](root__arm-io__mtp__iop-mtp-nub.md)
- **`agm-primary`**: `AppleHIDTransportDeviceMailbox`
- **`agm-secondary`**: `AppleHIDTransportDeviceMailbox`
- **`auth-supported`**: (present, empty)
- **`cold-boot-after-hibernate`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`fdr-classes`**: `TBCl/MdTh`, `nova-touch-cal`, `TBCl/NvFc`, `nova-force-cal`
- **`hid-merge-personality`**: `MTP_SYS`
- **`image-tag`**: `1836347494` (`0x6d747066`) (four-char code `mtpf`)
- **`name`**: `iop-mtp-nub`
- **`no-firmware-service`**: (present, empty)
- **`sleep-on-hibernate`**: (present, empty)
- **`watchdog-enable`**: (present, empty)

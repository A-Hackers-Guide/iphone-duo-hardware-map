# `/arm-io/ispRtb/iop-isp-nub`

- Name: `iop-isp-nub`
- Parent: [`/arm-io/ispRtb`](root__arm-io__ispRtb.md)
- phandle: `298`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## Firmware with a matching name [FW]

- [`Firmware/isp_bni/adc-boreas-v68.im4p`](../firmware/Firmware__isp_bni__adc-boreas-v68.im4p.md) (29,851,675 B) Tag: IM4P  Type: ispf  Version: 1

## All properties (8) [DT]

- **`AAPL,phandle`**: `298` (`0x12a`) → phandle of [`/arm-io/ispRtb/iop-isp-nub`](root__arm-io__ispRtb__iop-isp-nub.md)
- **`ap-recoverable-panics`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`coredump-enable`**: `64` (`0x40`)
- **`name`**: `iop-isp-nub`
- **`no-firmware-service`**: (present, empty)
- **`reboot-firmware`**: (present, empty)
- **`user-power-managed`**: `true`

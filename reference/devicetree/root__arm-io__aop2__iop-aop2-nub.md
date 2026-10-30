# `/arm-io/aop2/iop-aop2-nub`

- Name: `iop-aop2-nub`
- Parent: [`/arm-io/aop2`](root__arm-io__aop2.md)
- phandle: `111`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## Firmware with a matching name [FW]

- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (9) [DT]

- **`AAPL,phandle`**: `111` (`0x6f`) → phandle of [`/arm-io/aop2/iop-aop2-nub`](root__arm-io__aop2__iop-aop2-nub.md)
- **`claim-wake`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`name`**: `iop-aop2-nub`
- **`no-firmware-service`**: (present, empty)
- **`no-shutdown`**: `1` (`0x1`)
- **`routes`**: `112` (`0x70`)
- **`sleep-on-hibernate`**: (present, empty)
- **`watchdog-enable`**: (present, empty)

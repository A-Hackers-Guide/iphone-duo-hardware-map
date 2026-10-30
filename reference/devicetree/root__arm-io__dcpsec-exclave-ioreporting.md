# `/arm-io/dcpsec-exclave-ioreporting`

- Name: `dcpsec-exclave-ioreporting`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `272`
- compatible: `iop,secure-rtbuddy-ioreporting`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `SecureRTBuddyIOReporting` | `IOService` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | `iop,secure-rtbuddy-ioreporting` |

## All properties (7) [DT]

- **`AAPL,phandle`**: `272` (`0x110`) → phandle of [`/arm-io/dcpsec-exclave-ioreporting`](root__arm-io__dcpsec-exclave-ioreporting.md)
- **`compatible`**: `iop,secure-rtbuddy-ioreporting`
- **`exclave-assigned`**: (present, empty)
- **`exclave-endpoint`**: `153` (`0x99`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`name`**: `dcpsec-exclave-ioreporting`
- **`role`**: `DCPSEC-EXCLAVE`

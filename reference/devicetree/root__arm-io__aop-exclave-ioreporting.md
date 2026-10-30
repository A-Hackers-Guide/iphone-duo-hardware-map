# `/arm-io/aop-exclave-ioreporting`

- Name: `aop-exclave-ioreporting`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `109`
- compatible: `iop,secure-rtbuddy-ioreporting`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `SecureRTBuddyIOReporting` | `IOService` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | `iop,secure-rtbuddy-ioreporting` |

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `109` (`0x6d`) → phandle of [`/arm-io/aop-exclave-ioreporting`](root__arm-io__aop-exclave-ioreporting.md)
- **`compatible`**: `iop,secure-rtbuddy-ioreporting`
- **`exclave-assigned`**: (present, empty)
- **`exclave-endpoint`**: `77` (`0x4d`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`name`**: `aop-exclave-ioreporting`
- **`role`**: `AOP-EXCLAVE`

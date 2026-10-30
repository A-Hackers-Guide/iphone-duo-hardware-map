# `/arm-io/aop2-exclave-mailbox`

- Name: `aop2-exclave-mailbox`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `112`
- compatible: `iop,secure-rtbuddy-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `SecureRTBuddyProxy` | `IOService` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | `iop,secure-rtbuddy-proxy` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x2d6030000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`174, 214, 134`

## Firmware with a matching name [FW]

- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (16) [DT]

- **`AAPL,phandle`**: `112` (`0x70`) → phandle of [`/arm-io/aop2-exclave-mailbox`](root__arm-io__aop2-exclave-mailbox.md)
- **`claim-wake`**: (present, empty)
- **`claim-wake-endpoint-flags`**: 16 bytes
  - u32: `0x30 0x4 0x31 0x4`
  ```
  000000  30 00 00 00 04 00 00 00 31 00 00 00 04 00 00 00  0.......1.......
  ```
- **`compatible`**: `iop,secure-rtbuddy-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SecureRTBuddyAOP2_EDK`
- **`exclave-service`**: `com.apple.service.SecureRTBuddyAOP2`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xae 0xd6 0x86`
  ```
  000000  ae 00 00 00 d6 00 00 00 86 00 00 00              ............
  ```
- **`iommu-parent`**: `145` (`0x91`) → phandle of [`/arm-io/dart-sbr/mapper-exclave-aop2`](root__arm-io__dart-sbr__mapper-exclave-aop2.md)
- **`msgbox-mailbox-num`**: `20` (`0x14`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `aop2-exclave-mailbox`
- **`reg`**: 16 bytes
  - u32: `0xd6030000 0x2 0x4000 0x0`
  ```
  000000  00 00 03 d6 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`role`**: `AOP2-EXCLAVE`

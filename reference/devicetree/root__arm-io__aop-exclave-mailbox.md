# `/arm-io/aop-exclave-mailbox`

- Name: `aop-exclave-mailbox`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `108`
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

`173, 213, 133`

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (15) [DT]

- **`AAPL,phandle`**: `108` (`0x6c`) → phandle of [`/arm-io/aop-exclave-mailbox`](root__arm-io__aop-exclave-mailbox.md)
- **`claim-wake`**: (present, empty)
- **`compatible`**: `iop,secure-rtbuddy-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SecureRTBuddyAOP_EDK`
- **`exclave-service`**: `com.apple.service.SecureRTBuddyAOP`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xad 0xd5 0x85`
  ```
  000000  ad 00 00 00 d5 00 00 00 85 00 00 00              ............
  ```
- **`iommu-parent`**: `144` (`0x90`) → phandle of [`/arm-io/dart-sbr/mapper-exclave-aop`](root__arm-io__dart-sbr__mapper-exclave-aop.md)
- **`msgbox-mailbox-num`**: `19` (`0x13`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `aop-exclave-mailbox`
- **`reg`**: 16 bytes
  - u32: `0xd6030000 0x2 0x4000 0x0`
  ```
  000000  00 00 03 d6 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`role`**: `AOP-EXCLAVE`

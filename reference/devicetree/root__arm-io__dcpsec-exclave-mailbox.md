# `/arm-io/dcpsec-exclave-mailbox`

- Name: `dcpsec-exclave-mailbox`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `271`
- compatible: `iop,secure-rtbuddy-proxy`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `SecureRTBuddyProxy` | `IOService` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | `iop,secure-rtbuddy-proxy` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x2d6030000` | `0x10000` (65,536 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`184, 224, 144`

## All properties (14) [DT]

- **`AAPL,phandle`**: `271` (`0x10f`) → phandle of [`/arm-io/dcpsec-exclave-mailbox`](root__arm-io__dcpsec-exclave-mailbox.md)
- **`compatible`**: `iop,secure-rtbuddy-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SecureRTBuddyDCPSEC_EDK`
- **`exclave-service`**: `com.apple.service.SecureRTBuddyDCPSEC`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xb8 0xe0 0x90`
  ```
  000000  b8 00 00 00 e0 00 00 00 90 00 00 00              ............
  ```
- **`iommu-parent`**: `262` (`0x106`) → phandle of [`/arm-io/dart-dcpsec/mapper-dcpsec-exclave`](root__arm-io__dart-dcpsec__mapper-dcpsec-exclave.md)
- **`msgbox-mailbox-num`**: `30` (`0x1e`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `dcpsec-exclave-mailbox`
- **`reg`**: 16 bytes
  - u32: `0xd6030000 0x2 0x10000 0x0`
  ```
  000000  00 00 03 d6 02 00 00 00 00 00 01 00 00 00 00 00  ................
  ```
- **`role`**: `DCPSEC-EXCLAVE`

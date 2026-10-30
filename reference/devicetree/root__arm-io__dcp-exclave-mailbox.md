# `/arm-io/dcp-exclave-mailbox`

- Name: `dcp-exclave-mailbox`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `251`
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

`175, 215, 135`

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (14) [DT]

- **`AAPL,phandle`**: `251` (`0xfb`) → phandle of [`/arm-io/dcp-exclave-mailbox`](root__arm-io__dcp-exclave-mailbox.md)
- **`compatible`**: `iop,secure-rtbuddy-proxy`
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.SecureRTBuddyDCP_EDK`
- **`exclave-service`**: `com.apple.service.SecureRTBuddyDCP`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xaf 0xd7 0x87`
  ```
  000000  af 00 00 00 d7 00 00 00 87 00 00 00              ............
  ```
- **`iommu-parent`**: `237` (`0xed`) → phandle of [`/arm-io/dart-dcp/mapper-dcp-exclave`](root__arm-io__dart-dcp__mapper-dcp-exclave.md)
- **`msgbox-mailbox-num`**: `21` (`0x15`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `dcp-exclave-mailbox`
- **`reg`**: 16 bytes
  - u32: `0xd6030000 0x2 0x10000 0x0`
  ```
  000000  00 00 03 d6 02 00 00 00 00 00 01 00 00 00 00 00  ................
  ```
- **`role`**: `DCP-EXCLAVE`

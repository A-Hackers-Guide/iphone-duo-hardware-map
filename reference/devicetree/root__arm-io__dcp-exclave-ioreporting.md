# `/arm-io/dcp-exclave-ioreporting`

- Name: `dcp-exclave-ioreporting`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `252`
- compatible: `iop,secure-rtbuddy-ioreporting`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `SecureRTBuddyIOReporting` | `IOService` | [`com.apple.driver.SecureRTBuddyProxy`](../kexts/com.apple.driver.SecureRTBuddyProxy.md) | `iop,secure-rtbuddy-ioreporting` |

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `252` (`0xfc`) → phandle of [`/arm-io/dcp-exclave-ioreporting`](root__arm-io__dcp-exclave-ioreporting.md)
- **`compatible`**: `iop,secure-rtbuddy-ioreporting`
- **`exclave-assigned`**: (present, empty)
- **`exclave-endpoint`**: `78` (`0x4e`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`name`**: `dcp-exclave-ioreporting`
- **`role`**: `DCP-EXCLAVE`

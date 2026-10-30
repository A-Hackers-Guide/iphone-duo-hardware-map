# `/arm-io/dart-dcp/mapper-dcp-exclave`

- Name: `mapper-dcp-exclave`
- Parent: [`/arm-io/dart-dcp`](root__arm-io__dart-dcp.md)
- phandle: `237`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4` | | |

## Referenced by (1) [DT]

- [`/arm-io/dcp-exclave-mailbox`](root__arm-io__dcp-exclave-mailbox.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `237` (`0xed`) → phandle of [`/arm-io/dart-dcp/mapper-dcp-exclave`](root__arm-io__dart-dcp__mapper-dcp-exclave.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dcp-exclave`
- **`reg`**: `4` (`0x4`)

# `/arm-io/dart-dcp/mapper-dcp`

- Name: `mapper-dcp`
- Parent: [`/arm-io/dart-dcp`](root__arm-io__dart-dcp.md)
- phandle: `236`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x3` | | |

## Referenced by (1) [DT]

- [`/arm-io/dcp`](root__arm-io__dcp.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `236` (`0xec`) → phandle of [`/arm-io/dart-dcp/mapper-dcp`](root__arm-io__dart-dcp__mapper-dcp.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dcp`
- **`reg`**: `3` (`0x3`)

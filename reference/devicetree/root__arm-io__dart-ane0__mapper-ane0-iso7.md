# `/arm-io/dart-ane0/mapper-ane0-iso7`

- Name: `mapper-ane0-iso7`
- Parent: [`/arm-io/dart-ane0`](root__arm-io__dart-ane0.md)
- phandle: `328`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x7` | | |

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane0_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane0_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: anef  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `328` (`0x148`) → phandle of [`/arm-io/dart-ane0/mapper-ane0-iso7`](root__arm-io__dart-ane0__mapper-ane0-iso7.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-ane0-iso7`
- **`reg`**: `7` (`0x7`)

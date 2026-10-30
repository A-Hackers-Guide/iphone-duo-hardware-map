# `/arm-io/dart-ane1/mapper-ane1-iso1`

- Name: `mapper-ane1-iso1`
- Parent: [`/arm-io/dart-ane1`](root__arm-io__dart-ane1.md)
- phandle: `334`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1` | | |

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane1_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane1_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: ane1  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `334` (`0x14e`) → phandle of [`/arm-io/dart-ane1/mapper-ane1-iso1`](root__arm-io__dart-ane1__mapper-ane1-iso1.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-ane1-iso1`
- **`reg`**: `1` (`0x1`)

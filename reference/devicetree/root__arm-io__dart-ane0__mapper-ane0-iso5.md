# `/arm-io/dart-ane0/mapper-ane0-iso5`

- Name: `mapper-ane0-iso5`
- Parent: [`/arm-io/dart-ane0`](root__arm-io__dart-ane0.md)
- phandle: `326`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x5` | | |

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane0_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane0_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: anef  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `326` (`0x146`) → phandle of [`/arm-io/dart-ane0/mapper-ane0-iso5`](root__arm-io__dart-ane0__mapper-ane0-iso5.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-ane0-iso5`
- **`reg`**: `5` (`0x5`)

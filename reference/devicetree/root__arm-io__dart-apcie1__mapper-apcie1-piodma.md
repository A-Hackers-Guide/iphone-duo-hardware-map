# `/arm-io/dart-apcie1/mapper-apcie1-piodma`

- Name: `mapper-apcie1-piodma`
- Parent: [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md)
- phandle: `431`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x11` | | |

## Referenced by (1) [DT]

- [`/arm-io/apcie1-piodma`](root__arm-io__apcie1-piodma.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `431` (`0x1af`) → phandle of [`/arm-io/dart-apcie1/mapper-apcie1-piodma`](root__arm-io__dart-apcie1__mapper-apcie1-piodma.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-apcie1-piodma`
- **`reg`**: `17` (`0x11`)

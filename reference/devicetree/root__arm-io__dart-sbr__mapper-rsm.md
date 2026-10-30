# `/arm-io/dart-sbr/mapper-rsm`

- Name: `mapper-rsm`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `153`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x2f` | | |

## Referenced by (1) [DT]

- [`/arm-io/rsm`](root__arm-io__rsm.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `153` (`0x99`) → phandle of [`/arm-io/dart-sbr/mapper-rsm`](root__arm-io__dart-sbr__mapper-rsm.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-rsm`
- **`reg`**: `47` (`0x2f`)

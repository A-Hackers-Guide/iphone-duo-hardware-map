# `/arm-io/dart-dcpext0/mapper-dcpext0`

- Name: `mapper-dcpext0`
- Parent: [`/arm-io/dart-dcpext0`](root__arm-io__dart-dcpext0.md)
- phandle: `280`
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

- [`/arm-io/dcpext0`](root__arm-io__dcpext0.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `280` (`0x118`) → phandle of [`/arm-io/dart-dcpext0/mapper-dcpext0`](root__arm-io__dart-dcpext0__mapper-dcpext0.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dcpext0`
- **`reg`**: `3` (`0x3`)

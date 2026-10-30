# `/arm-io/dart-sbr/mapper-admac-base-ns`

- Name: `mapper-admac-base-ns`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `149`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x2e` | | |

## Referenced by (1) [DT]

- [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `149` (`0x95`) → phandle of [`/arm-io/dart-sbr/mapper-admac-base-ns`](root__arm-io__dart-sbr__mapper-admac-base-ns.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-admac-base-ns`
- **`reg`**: `46` (`0x2e`)

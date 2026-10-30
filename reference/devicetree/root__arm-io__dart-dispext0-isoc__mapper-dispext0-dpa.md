# `/arm-io/dart-dispext0-isoc/mapper-dispext0-dpa`

- Name: `mapper-dispext0-dpa`
- Parent: [`/arm-io/dart-dispext0-isoc`](root__arm-io__dart-dispext0-isoc.md)
- phandle: `286`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x0` | | |

## Referenced by (1) [DT]

- [`/arm-io/admac-dispext0`](root__arm-io__admac-dispext0.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `286` (`0x11e`) → phandle of [`/arm-io/dart-dispext0-isoc/mapper-dispext0-dpa`](root__arm-io__dart-dispext0-isoc__mapper-dispext0-dpa.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dispext0-dpa`
- **`reg`**: `0` (`0x0`)

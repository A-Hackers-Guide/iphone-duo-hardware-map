# `/arm-io/dart-jpeg/mapper-jpeg`

- Name: `mapper-jpeg`
- Parent: [`/arm-io/dart-jpeg`](root__arm-io__dart-jpeg.md)
- phandle: `296`
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

- [`/arm-io/jpeg`](root__arm-io__jpeg.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `296` (`0x128`) → phandle of [`/arm-io/dart-jpeg/mapper-jpeg`](root__arm-io__dart-jpeg__mapper-jpeg.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-jpeg`
- **`reg`**: `0` (`0x0`)
- **`tail-padding`**: `1` (`0x1`)

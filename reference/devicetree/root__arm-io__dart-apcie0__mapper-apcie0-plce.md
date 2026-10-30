# `/arm-io/dart-apcie0/mapper-apcie0-plce`

- Name: `mapper-apcie0-plce`
- Parent: [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md)
- phandle: `426`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x13` | | |

## Referenced by (1) [DT]

- [`/arm-io/apcie0-plce`](root__arm-io__apcie0-plce.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `426` (`0x1aa`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-plce`](root__arm-io__dart-apcie0__mapper-apcie0-plce.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-apcie0-plce`
- **`reg`**: `19` (`0x13`)

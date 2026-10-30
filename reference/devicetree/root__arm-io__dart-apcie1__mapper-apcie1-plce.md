# `/arm-io/dart-apcie1/mapper-apcie1-plce`

- Name: `mapper-apcie1-plce`
- Parent: [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md)
- phandle: `432`
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

- [`/arm-io/apcie1-plce`](root__arm-io__apcie1-plce.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `432` (`0x1b0`) → phandle of [`/arm-io/dart-apcie1/mapper-apcie1-plce`](root__arm-io__dart-apcie1__mapper-apcie1-plce.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-apcie1-plce`
- **`reg`**: `19` (`0x13`)

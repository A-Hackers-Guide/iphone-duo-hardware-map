# `/arm-io/dart-apcie0/mapper-apcie0-piodma`

- Name: `mapper-apcie0-piodma`
- Parent: [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md)
- phandle: `425`
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

- [`/arm-io/apcie0-piodma`](root__arm-io__apcie0-piodma.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `425` (`0x1a9`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-piodma`](root__arm-io__dart-apcie0__mapper-apcie0-piodma.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-apcie0-piodma`
- **`reg`**: `17` (`0x11`)

# `/arm-io/dart-sbr/mapper-admac-base-s`

- Name: `mapper-admac-base-s`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `151`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x2d` | | |

## All properties (5) [DT]

- **`AAPL,phandle`**: `151` (`0x97`) → phandle of [`/arm-io/dart-sbr/mapper-admac-base-s`](root__arm-io__dart-sbr__mapper-admac-base-s.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-admac-base-s`
- **`reg`**: `45` (`0x2d`)

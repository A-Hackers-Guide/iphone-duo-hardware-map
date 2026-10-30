# `/arm-io/dart-dcpsec/mapper-dcpsec`

- Name: `mapper-dcpsec`
- Parent: [`/arm-io/dart-dcpsec`](root__arm-io__dart-dcpsec.md)
- phandle: `261`
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

- [`/arm-io/dcpsec`](root__arm-io__dcpsec.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `261` (`0x105`) → phandle of [`/arm-io/dart-dcpsec/mapper-dcpsec`](root__arm-io__dart-dcpsec__mapper-dcpsec.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dcpsec`
- **`reg`**: `3` (`0x3`)

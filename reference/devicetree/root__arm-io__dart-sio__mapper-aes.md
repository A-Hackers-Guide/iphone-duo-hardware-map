# `/arm-io/dart-sio/mapper-aes`

- Name: `mapper-aes`
- Parent: [`/arm-io/dart-sio`](root__arm-io__dart-sio.md)
- phandle: `140`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1` | | |

## Referenced by (1) [DT]

- [`/arm-io/aes`](root__arm-io__aes.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `140` (`0x8c`) → phandle of [`/arm-io/dart-sio/mapper-aes`](root__arm-io__dart-sio__mapper-aes.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-aes`
- **`reg`**: `1` (`0x1`)

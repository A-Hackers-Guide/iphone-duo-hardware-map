# `/arm-io/dart-sio/mapper-sio`

- Name: `mapper-sio`
- Parent: [`/arm-io/dart-sio`](root__arm-io__dart-sio.md)
- phandle: `139`
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

- [`/arm-io/sio`](root__arm-io__sio.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `139` (`0x8b`) → phandle of [`/arm-io/dart-sio/mapper-sio`](root__arm-io__dart-sio__mapper-sio.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-sio`
- **`reg`**: `0` (`0x0`)

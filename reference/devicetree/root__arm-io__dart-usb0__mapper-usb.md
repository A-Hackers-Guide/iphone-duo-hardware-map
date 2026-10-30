# `/arm-io/dart-usb0/mapper-usb`

- Name: `mapper-usb`
- Parent: [`/arm-io/dart-usb0`](root__arm-io__dart-usb0.md)
- phandle: `224`
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

- [`/arm-io/usb-drd0`](root__arm-io__usb-drd0.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `224` (`0xe0`) → phandle of [`/arm-io/dart-usb0/mapper-usb`](root__arm-io__dart-usb0__mapper-usb.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-usb`
- **`reg`**: `1` (`0x1`)

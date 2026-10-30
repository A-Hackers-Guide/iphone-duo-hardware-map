# `/arm-io/dart-sbr/mapper-admac-leap-ns`

- Name: `mapper-admac-leap-ns`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `148`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x2c` | | |

## Referenced by (1) [DT]

- [`/arm-io/admac-leap-ns`](root__arm-io__admac-leap-ns.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (6) [DT]

- **`AAPL,phandle`**: `148` (`0x94`) → phandle of [`/arm-io/dart-sbr/mapper-admac-leap-ns`](root__arm-io__dart-sbr__mapper-admac-leap-ns.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-admac-leap-ns`
- **`reg`**: `44` (`0x2c`)

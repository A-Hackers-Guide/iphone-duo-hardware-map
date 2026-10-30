# `/arm-io/dart-disp0-isoc/mapper-disp0-dpa`

- Name: `mapper-disp0-dpa`
- Parent: [`/arm-io/dart-disp0-isoc`](root__arm-io__dart-disp0-isoc.md)
- phandle: `246`
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

- [`/arm-io/admac-dispint0`](root__arm-io__admac-dispint0.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `246` (`0xf6`) → phandle of [`/arm-io/dart-disp0-isoc/mapper-disp0-dpa`](root__arm-io__dart-disp0-isoc__mapper-disp0-dpa.md)
- **`allow-subpage-mapping`**: (present, empty)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-disp0-dpa`
- **`reg`**: `0` (`0x0`)

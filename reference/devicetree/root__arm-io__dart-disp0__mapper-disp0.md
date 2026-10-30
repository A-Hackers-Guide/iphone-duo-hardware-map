# `/arm-io/dart-disp0/mapper-disp0`

- Name: `mapper-disp0`
- Parent: [`/arm-io/dart-disp0`](root__arm-io__dart-disp0.md)
- phandle: `239`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0xb` | | |

## All properties (7) [DT]

- **`AAPL,phandle`**: `239` (`0xef`) → phandle of [`/arm-io/dart-disp0/mapper-disp0`](root__arm-io__dart-disp0__mapper-disp0.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-disp0`
- **`reg`**: `11` (`0xb`)

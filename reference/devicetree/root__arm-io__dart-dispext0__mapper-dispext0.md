# `/arm-io/dart-dispext0/mapper-dispext0`

- Name: `mapper-dispext0`
- Parent: [`/arm-io/dart-dispext0`](root__arm-io__dart-dispext0.md)
- phandle: `283`
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

- **`AAPL,phandle`**: `283` (`0x11b`) → phandle of [`/arm-io/dart-dispext0/mapper-dispext0`](root__arm-io__dart-dispext0__mapper-dispext0.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-dispext0`
- **`reg`**: `11` (`0xb`)

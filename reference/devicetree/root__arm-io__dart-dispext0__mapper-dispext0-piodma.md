# `/arm-io/dart-dispext0/mapper-dispext0-piodma`

- Name: `mapper-dispext0-piodma`
- Parent: [`/arm-io/dart-dispext0`](root__arm-io__dart-dispext0.md)
- phandle: `284`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x15` | | |

## All properties (7) [DT]

- **`AAPL,phandle`**: `284` (`0x11c`) → phandle of [`/arm-io/dart-dispext0/mapper-dispext0-piodma`](root__arm-io__dart-dispext0__mapper-dispext0-piodma.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-dispext0-piodma`
- **`reg`**: `21` (`0x15`)

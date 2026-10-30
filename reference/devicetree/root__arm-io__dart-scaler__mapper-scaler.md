# `/arm-io/dart-scaler/mapper-scaler`

- Name: `mapper-scaler`
- Parent: [`/arm-io/dart-scaler`](root__arm-io__dart-scaler.md)
- phandle: `292`
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

## All properties (7) [DT]

- **`AAPL,phandle`**: `292` (`0x124`) → phandle of [`/arm-io/dart-scaler/mapper-scaler`](root__arm-io__dart-scaler__mapper-scaler.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-scaler`
- **`reg`**: `0` (`0x0`)

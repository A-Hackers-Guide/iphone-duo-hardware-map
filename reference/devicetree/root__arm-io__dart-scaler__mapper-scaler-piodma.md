# `/arm-io/dart-scaler/mapper-scaler-piodma`

- Name: `mapper-scaler-piodma`
- Parent: [`/arm-io/dart-scaler`](root__arm-io__dart-scaler.md)
- phandle: `293`
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

## All properties (7) [DT]

- **`AAPL,phandle`**: `293` (`0x125`) → phandle of [`/arm-io/dart-scaler/mapper-scaler-piodma`](root__arm-io__dart-scaler__mapper-scaler-piodma.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-scaler-piodma`
- **`reg`**: `1` (`0x1`)

# `/arm-io/dart-dcpext0/mapper-dcpext0-exclave`

- Name: `mapper-dcpext0-exclave`
- Parent: [`/arm-io/dart-dcpext0`](root__arm-io__dart-dcpext0.md)
- phandle: `281`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4` | | |

## All properties (5) [DT]

- **`AAPL,phandle`**: `281` (`0x119`) → phandle of [`/arm-io/dart-dcpext0/mapper-dcpext0-exclave`](root__arm-io__dart-dcpext0__mapper-dcpext0-exclave.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dcpext0-exclave`
- **`reg`**: `4` (`0x4`)

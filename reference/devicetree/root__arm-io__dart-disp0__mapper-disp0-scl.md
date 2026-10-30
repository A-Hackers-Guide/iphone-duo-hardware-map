# `/arm-io/dart-disp0/mapper-disp0-scl`

- Name: `mapper-disp0-scl`
- Parent: [`/arm-io/dart-disp0`](root__arm-io__dart-disp0.md)
- phandle: `241`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0xe` | | |

## All properties (5) [DT]

- **`AAPL,phandle`**: `241` (`0xf1`) → phandle of [`/arm-io/dart-disp0/mapper-disp0-scl`](root__arm-io__dart-disp0__mapper-disp0-scl.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-disp0-scl`
- **`reg`**: `14` (`0xe`)

# `/arm-io/dart-disp0/mapper-disp0-sca`

- Name: `mapper-disp0-sca`
- Parent: [`/arm-io/dart-disp0`](root__arm-io__dart-disp0.md)
- phandle: `242`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0xf` | | |

## All properties (5) [DT]

- **`AAPL,phandle`**: `242` (`0xf2`) → phandle of [`/arm-io/dart-disp0/mapper-disp0-sca`](root__arm-io__dart-disp0__mapper-disp0-sca.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-disp0-sca`
- **`reg`**: `15` (`0xf`)

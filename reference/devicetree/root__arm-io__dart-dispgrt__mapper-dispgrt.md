# `/arm-io/dart-dispgrt/mapper-dispgrt`

- Name: `mapper-dispgrt`
- Parent: [`/arm-io/dart-dispgrt`](root__arm-io__dart-dispgrt.md)
- phandle: `244`
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

- **`AAPL,phandle`**: `244` (`0xf4`) → phandle of [`/arm-io/dart-dispgrt/mapper-dispgrt`](root__arm-io__dart-dispgrt__mapper-dispgrt.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-dispgrt`
- **`reg`**: `1` (`0x1`)

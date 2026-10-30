# `/arm-io/dart-dispsecgrt/mapper-dispsecgrt`

- Name: `mapper-dispsecgrt`
- Parent: [`/arm-io/dart-dispsecgrt`](root__arm-io__dart-dispsecgrt.md)
- phandle: `269`
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

- **`AAPL,phandle`**: `269` (`0x10d`) → phandle of [`/arm-io/dart-dispsecgrt/mapper-dispsecgrt`](root__arm-io__dart-dispsecgrt__mapper-dispsecgrt.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-dispsecgrt`
- **`reg`**: `1` (`0x1`)

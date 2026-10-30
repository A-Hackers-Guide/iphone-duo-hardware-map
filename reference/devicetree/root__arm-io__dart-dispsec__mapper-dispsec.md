# `/arm-io/dart-dispsec/mapper-dispsec`

- Name: `mapper-dispsec`
- Parent: [`/arm-io/dart-dispsec`](root__arm-io__dart-dispsec.md)
- phandle: `264`
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

- **`AAPL,phandle`**: `264` (`0x108`) → phandle of [`/arm-io/dart-dispsec/mapper-dispsec`](root__arm-io__dart-dispsec__mapper-dispsec.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-dispsec`
- **`reg`**: `11` (`0xb`)

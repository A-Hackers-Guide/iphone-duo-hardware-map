# `/arm-io/dart-dispsec/mapper-dispsec-scl`

- Name: `mapper-dispsec-scl`
- Parent: [`/arm-io/dart-dispsec`](root__arm-io__dart-dispsec.md)
- phandle: `266`
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

- **`AAPL,phandle`**: `266` (`0x10a`) → phandle of [`/arm-io/dart-dispsec/mapper-dispsec-scl`](root__arm-io__dart-dispsec__mapper-dispsec-scl.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dispsec-scl`
- **`reg`**: `14` (`0xe`)

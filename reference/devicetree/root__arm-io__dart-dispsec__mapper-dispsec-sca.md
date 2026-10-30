# `/arm-io/dart-dispsec/mapper-dispsec-sca`

- Name: `mapper-dispsec-sca`
- Parent: [`/arm-io/dart-dispsec`](root__arm-io__dart-dispsec.md)
- phandle: `267`
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

- **`AAPL,phandle`**: `267` (`0x10b`) → phandle of [`/arm-io/dart-dispsec/mapper-dispsec-sca`](root__arm-io__dart-dispsec__mapper-dispsec-sca.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-dispsec-sca`
- **`reg`**: `15` (`0xf`)

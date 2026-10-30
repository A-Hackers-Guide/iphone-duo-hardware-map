# `/arm-io/dart-apcie0/mapper-apcie0-alpha`

- Name: `mapper-apcie0-alpha`
- Parent: [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md)
- phandle: `423`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x2` | | |

## Referenced by (1) [DT]

- [`/arm-io/apcie/pci-bridge0/centauri-alpha`](root__arm-io__apcie__pci-bridge0__centauri-alpha.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `423` (`0x1a7`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-alpha`](root__arm-io__dart-apcie0__mapper-apcie0-alpha.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-apcie0-alpha`
- **`reg`**: `2` (`0x2`)
- **`vm-force`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)

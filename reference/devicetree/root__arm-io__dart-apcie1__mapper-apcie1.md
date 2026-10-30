# `/arm-io/dart-apcie1/mapper-apcie1`

- Name: `mapper-apcie1`
- Parent: [`/arm-io/dart-apcie1`](root__arm-io__dart-apcie1.md)
- phandle: `430`
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

## Referenced by (1) [DT]

- [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md): `iommu-parent`

## All properties (6) [DT]

- **`AAPL,phandle`**: `430` (`0x1ae`) → phandle of [`/arm-io/dart-apcie1/mapper-apcie1`](root__arm-io__dart-apcie1__mapper-apcie1.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-apcie1`
- **`reg`**: `1` (`0x1`)
- **`vm-force`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)

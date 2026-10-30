# `/arm-io/dart-sbr/mapper-scm`

- Name: `mapper-scm`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `152`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x19` | | |

## Referenced by (1) [DT]

- [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md): `iommu-parent`

## All properties (5) [DT]

- **`AAPL,phandle`**: `152` (`0x98`) → phandle of [`/arm-io/dart-sbr/mapper-scm`](root__arm-io__dart-sbr__mapper-scm.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-scm`
- **`reg`**: `25` (`0x19`)

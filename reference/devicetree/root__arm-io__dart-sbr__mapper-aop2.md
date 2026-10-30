# `/arm-io/dart-sbr/mapper-aop2`

- Name: `mapper-aop2`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `143`
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

- [`/arm-io/aop2`](root__arm-io__aop2.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `143` (`0x8f`) → phandle of [`/arm-io/dart-sbr/mapper-aop2`](root__arm-io__dart-sbr__mapper-aop2.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-aop2`
- **`reg`**: `2` (`0x2`)

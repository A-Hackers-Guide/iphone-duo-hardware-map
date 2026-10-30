# `/arm-io/dart-sbr/mapper-aop`

- Name: `mapper-aop`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `142`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x0` | | |

## Referenced by (1) [DT]

- [`/arm-io/aop`](root__arm-io__aop.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/AOP/aopfw-v68aop.RELEASE.im4p`](../firmware/Firmware__AOP__aopfw-v68aop.RELEASE.im4p.md) (5,546,009 B) Tag: IM4P  Type: aopf  Version: 1
- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `142` (`0x8e`) → phandle of [`/arm-io/dart-sbr/mapper-aop`](root__arm-io__dart-sbr__mapper-aop.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-aop`
- **`reg`**: `0` (`0x0`)

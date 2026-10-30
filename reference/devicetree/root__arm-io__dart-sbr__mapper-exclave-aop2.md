# `/arm-io/dart-sbr/mapper-exclave-aop2`

- Name: `mapper-exclave-aop2`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `145`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x3` | | |

## Referenced by (1) [DT]

- [`/arm-io/aop2-exclave-mailbox`](root__arm-io__aop2-exclave-mailbox.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p`](../firmware/Firmware__AOP2__aop2fw-v68aop2.RELEASE.im4p.md) (9,650,201 B) Tag: IM4P  Type: aop2  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `145` (`0x91`) → phandle of [`/arm-io/dart-sbr/mapper-exclave-aop2`](root__arm-io__dart-sbr__mapper-exclave-aop2.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-exclave-aop2`
- **`reg`**: `3` (`0x3`)

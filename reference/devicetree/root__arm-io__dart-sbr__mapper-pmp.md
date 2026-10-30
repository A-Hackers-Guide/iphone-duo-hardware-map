# `/arm-io/dart-sbr/mapper-pmp`

- Name: `mapper-pmp`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `147`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x6` | | |

## Referenced by (1) [DT]

- [`/arm-io/pmp`](root__arm-io__pmp.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/pmp/t8160pmp.im4p`](../firmware/Firmware__pmp__t8160pmp.im4p.md) (737,305 B) Tag: IM4P  Type: pmpf  Version: 0

## All properties (5) [DT]

- **`AAPL,phandle`**: `147` (`0x93`) → phandle of [`/arm-io/dart-sbr/mapper-pmp`](root__arm-io__dart-sbr__mapper-pmp.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-pmp`
- **`reg`**: `6` (`0x6`)

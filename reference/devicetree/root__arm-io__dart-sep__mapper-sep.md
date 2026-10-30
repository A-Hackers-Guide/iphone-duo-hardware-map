# `/arm-io/dart-sep/mapper-sep`

- Name: `mapper-sep`
- Parent: [`/arm-io/dart-sep`](root__arm-io__dart-sep.md)
- phandle: `132`
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

- [`/arm-io/sep`](root__arm-io__sep.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`](../firmware/Firmware__all_flash__sep-firmware.v68.RELEASE.im4p.md) (7,216,106 B) Tag: IM4P  Type: sepi  Version: 1
- [`Firmware/all_flash/sep-patches.v68.im4p`](../firmware/Firmware__all_flash__sep-patches.v68.im4p.md) (21,137 B) Tag: IM4P  Type: stg1  Version: AppleSEPROM-1483.0.0.100.14

## All properties (5) [DT]

- **`AAPL,phandle`**: `132` (`0x84`) → phandle of [`/arm-io/dart-sep/mapper-sep`](root__arm-io__dart-sep__mapper-sep.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-sep`
- **`reg`**: `0` (`0x0`)

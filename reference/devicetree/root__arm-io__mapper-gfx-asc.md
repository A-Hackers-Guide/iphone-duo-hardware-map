# `/arm-io/mapper-gfx-asc`

- Name: `mapper-gfx-asc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `349`
- compatible: `iommu-mapper,gfx`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AGXArmFirmwareMapper` | `AppleARMIODevice` | [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md) | `iommu-mapper,gfx` |

## Referenced by (2) [DT]

- [`/arm-io/gfx-asc`](root__arm-io__gfx-asc.md): `iommu-parent`
- [`/arm-io/gfx1-asc`](root__arm-io__gfx1-asc.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/SmartIOFirmware_ASCv8.im4p`](../firmware/Firmware__SmartIOFirmware_ASCv8.im4p.md) (1,149,397 B) Tag: IM4P  Type: siof  Version: 1.0.0

## All properties (3) [DT]

- **`AAPL,phandle`**: `349` (`0x15d`) → phandle of [`/arm-io/mapper-gfx-asc`](root__arm-io__mapper-gfx-asc.md)
- **`compatible`**: `iommu-mapper,gfx`
- **`name`**: `mapper-gfx-asc`

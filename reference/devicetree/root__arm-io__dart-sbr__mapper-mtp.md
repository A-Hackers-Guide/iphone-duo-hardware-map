# `/arm-io/dart-sbr/mapper-mtp`

- Name: `mapper-mtp`
- Parent: [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- phandle: `146`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4` | | |

## Referenced by (1) [DT]

- [`/arm-io/mtp`](root__arm-io__mtp.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/V68_MtpFirmware.im4p`](../firmware/Firmware__V68_MtpFirmware.im4p.md) (2,308,247 B) Tag: IM4P  Type: mtpf  Version: 1

## All properties (5) [DT]

- **`AAPL,phandle`**: `146` (`0x92`) → phandle of [`/arm-io/dart-sbr/mapper-mtp`](root__arm-io__dart-sbr__mapper-mtp.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`name`**: `mapper-mtp`
- **`reg`**: `4` (`0x4`)

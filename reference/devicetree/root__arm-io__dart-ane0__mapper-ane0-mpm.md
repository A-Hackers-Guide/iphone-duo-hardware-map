# `/arm-io/dart-ane0/mapper-ane0-mpm`

- Name: `mapper-ane0-mpm`
- Parent: [`/arm-io/dart-ane0`](root__arm-io__dart-ane0.md)
- phandle: `329`
- compatible: `iommu-mapper`
- device_type: `dart-mapper`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IODARTMapper` | `IODARTMapperNub` | [`com.apple.driver.IODARTFamily`](../kexts/com.apple.driver.IODARTFamily.md) | `iommu-mapper` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0xb` | | |

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane0_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane0_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: anef  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `329` (`0x149`) → phandle of [`/arm-io/dart-ane0/mapper-ane0-mpm`](root__arm-io__dart-ane0__mapper-ane0-mpm.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `512` (`0x200`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-ane0-mpm`
- **`reg`**: `11` (`0xb`)

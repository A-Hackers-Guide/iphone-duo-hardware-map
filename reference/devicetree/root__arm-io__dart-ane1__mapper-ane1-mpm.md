# `/arm-io/dart-ane1/mapper-ane1-mpm`

- Name: `mapper-ane1-mpm`
- Parent: [`/arm-io/dart-ane1`](root__arm-io__dart-ane1.md)
- phandle: `341`
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

- [`Firmware/ane/h19_ane1_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane1_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: ane1  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `341` (`0x155`) → phandle of [`/arm-io/dart-ane1/mapper-ane1-mpm`](root__arm-io__dart-ane1__mapper-ane1-mpm.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `512` (`0x200`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-ane1-mpm`
- **`reg`**: `11` (`0xb`)

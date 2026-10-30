# `/arm-io/dart-ave/mapper-ave`

- Name: `mapper-ave`
- Parent: [`/arm-io/dart-ave`](root__arm-io__dart-ave.md)
- phandle: `312`
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

- [`/arm-io/ave`](root__arm-io__ave.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/ave/AppleAVE2FW_H19.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19.im4p.md) (2,737,129 B) Tag: IM4P  Type: avef  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE0.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE0.im4p.md) (10,387 B) Tag: IM4P  Type: ave0  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE1.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE1.im4p.md) (17,563 B) Tag: IM4P  Type: ave1  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE2.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE2.im4p.md) (11,863 B) Tag: IM4P  Type: ave2  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE3.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE3.im4p.md) (9,975 B) Tag: IM4P  Type: ave3  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE4.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE4.im4p.md) (12,207 B) Tag: IM4P  Type: ave4  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE5.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE5.im4p.md) (11,911 B) Tag: IM4P  Type: ave5  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE6.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE6.im4p.md) (9,695 B) Tag: IM4P  Type: ave6  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE7.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE7.im4p.md) (12,915 B) Tag: IM4P  Type: ave7  Version: 1
- [`Firmware/ave/AppleAVE2FW_H19_AVE8.im4p`](../firmware/Firmware__ave__AppleAVE2FW_H19_AVE8.im4p.md) (26,311 B) Tag: IM4P  Type: ave8  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `312` (`0x138`) → phandle of [`/arm-io/dart-ave/mapper-ave`](root__arm-io__dart-ave__mapper-ave.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `512` (`0x200`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-ave`
- **`reg`**: `0` (`0x0`)

# `/arm-io/dart-avd/mapper-avd`

- Name: `mapper-avd`
- Parent: [`/arm-io/dart-avd`](root__arm-io__dart-avd.md)
- phandle: `315`
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

## Firmware with a matching name [FW]

- [`Firmware/avd/AppleAVDFW_H19P.im4p`](../firmware/Firmware__avd__AppleAVDFW_H19P.im4p.md) (107,464 B) Tag: IM4P  Type: avdf  Version: 280d6e11

## All properties (7) [DT]

- **`AAPL,phandle`**: `315` (`0x13b`) → phandle of [`/arm-io/dart-avd/mapper-avd`](root__arm-io__dart-avd__mapper-avd.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `64` (`0x40`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-avd`
- **`reg`**: `0` (`0x0`)

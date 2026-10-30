# `/arm-io/dart-isp/mapper-isp`

- Name: `mapper-isp`
- Parent: [`/arm-io/dart-isp`](root__arm-io__dart-isp.md)
- phandle: `301`
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

- [`Firmware/isp_bni/adc-boreas-v68.im4p`](../firmware/Firmware__isp_bni__adc-boreas-v68.im4p.md) (29,851,675 B) Tag: IM4P  Type: ispf  Version: 1

## All properties (7) [DT]

- **`AAPL,phandle`**: `301` (`0x12d`) → phandle of [`/arm-io/dart-isp/mapper-isp`](root__arm-io__dart-isp__mapper-isp.md)
- **`compatible`**: `iommu-mapper`
- **`device_type`**: `dart-mapper`
- **`iomd-cache-size`**: `1024` (`0x400`)
- **`iomd-cache-ttl`**: `2000` (`0x7d0`)
- **`name`**: `mapper-isp`
- **`reg`**: `0` (`0x0`)

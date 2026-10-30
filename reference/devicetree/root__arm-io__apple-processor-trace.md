# `/arm-io/apple-processor-trace`

- Name: `apple-processor-trace`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `450`
- compatible: `apple-processor-trace,t8160`
- device_type: `apple-processor-trace`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleProcessorTraceT8160` | `AppleARMIODevice` | [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md) | `apple-processor-trace,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x100f0000` | `0x10000` (65,536 B) | `0x2100f0000`–`0x2100fffff` |
| 1 | `0x101f0000` | `0x10000` (65,536 B) | `0x2101f0000`–`0x2101fffff` |
| 2 | `0x102f0000` | `0x10000` (65,536 B) | `0x2102f0000`–`0x2102fffff` |
| 3 | `0x103f0000` | `0x10000` (65,536 B) | `0x2103f0000`–`0x2103fffff` |
| 4 | `0x110f0000` | `0x10000` (65,536 B) | `0x2110f0000`–`0x2110fffff` |
| 5 | `0x111f0000` | `0x10000` (65,536 B) | `0x2111f0000`–`0x2111fffff` |
| 6 | `0x10ff0000` | `0x10000` (65,536 B) | `0x210ff0000`–`0x210ffffff` |
| 7 | `0x11ff0000` | `0x10000` (65,536 B) | `0x211ff0000`–`0x211ffffff` |
| 8 | `0x10e40000` | `0x10000` (65,536 B) | `0x210e40000`–`0x210e4ffff` |
| 9 | `0x11e40000` | `0x10000` (65,536 B) | `0x211e40000`–`0x211e4ffff` |
| 10 | `0x10e50000` | `0x10000` (65,536 B) | `0x210e50000`–`0x210e5ffff` |
| 11 | `0x11e50000` | `0x10000` (65,536 B) | `0x211e50000`–`0x211e5ffff` |
| 12 | `0x10e90000` | `0x10000` (65,536 B) | `0x210e90000`–`0x210e9ffff` |
| 13 | `0x11e90000` | `0x10000` (65,536 B) | `0x211e90000`–`0x211e9ffff` |
| 14 | `0x10eb0000` | `0x10000` (65,536 B) | `0x210eb0000`–`0x210ebffff` |
| 15 | `0x11eb0000` | `0x10000` (65,536 B) | `0x211eb0000`–`0x211ebffff` |

## Firmware with a matching name [FW]

- [`Firmware/AppleLPM/AppleLPM.v68.release.im4p`](../firmware/Firmware__AppleLPM__AppleLPM.v68.release.im4p.md) (1,925,273 B) Tag: IM4P  Type: alpm  Version: 1
- [`Firmware/all_flash/applelogo@2d~iphone.im4p`](../firmware/Firmware__all_flash__applelogo@2d~iphone.im4p.md) (38,343 B) Tag: IM4P  Type: logo  Version: EmbeddedImages-184.40.2
- [`Firmware/avd/AppleAVDFW_H19P.im4p`](../firmware/Firmware__avd__AppleAVDFW_H19P.im4p.md) (107,464 B) Tag: IM4P  Type: avdf  Version: 280d6e11
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

## All properties (5) [DT]

- **`AAPL,phandle`**: `450` (`0x1c2`) → phandle of [`/arm-io/apple-processor-trace`](root__arm-io__apple-processor-trace.md)
- **`compatible`**: `apple-processor-trace,t8160`
- **`device_type`**: `apple-processor-trace`
- **`name`**: `apple-processor-trace`
- **`reg`**: 256 bytes
  - u32: `0x100f0000 0x0 0x10000 0x0 0x101f0000 0x0 0x10000 0x0 0x102f0000 0x0 0x10000 0x0 0x103f0000 0x0 0x10000 0x0 0x110f0000 0x0 0x10000 0x0 0x111f0000 0x0 0x10000 0x0 0x10ff0000 0x0 0x10000 0x0 0x11ff0000 0x0 0x10000 0x0 0x10e40000 0x0 0x10000 0x0 0x11e40000 0x0 0x10000 0x0 0x10e50000 0x0 0x10000 0x0 0x11e50000 0x0 0x10000 0x0 0x10e90000 0x0 0x10000 0x0 0x11e90000 0x0 0x10000 0x0 0x10eb0000 0x0 0x10000 0x0 0x11eb0000 0x0 0x10000 0x0`
  ```
  000000  00 00 0f 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000010  00 00 1f 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000020  00 00 2f 10 00 00 00 00 00 00 01 00 00 00 00 00  ../.............
  000030  00 00 3f 10 00 00 00 00 00 00 01 00 00 00 00 00  ..?.............
  000040  00 00 0f 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000050  00 00 1f 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000060  00 00 ff 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000070  00 00 ff 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000080  00 00 e4 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000090  00 00 e4 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  0000a0  00 00 e5 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  0000b0  00 00 e5 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  0000c0  00 00 e9 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  0000d0  00 00 e9 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  0000e0  00 00 eb 10 00 00 00 00 00 00 01 00 00 00 00 00  ................
  0000f0  00 00 eb 11 00 00 00 00 00 00 01 00 00 00 00 00  ................
  ```

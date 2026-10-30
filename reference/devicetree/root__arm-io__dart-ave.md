# `/arm-io/dart-ave`

- Name: `dart-ave`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `311`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (1): [`/arm-io/dart-ave/mapper-ave`](root__arm-io__dart-ave__mapper-ave.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x203020000` | `0x20000` (131,072 B) | `0x403020000`–`0x40303ffff` |
| 1 | `0x203030000` | `0x4000` (16,384 B) | `0x403030000`–`0x403033fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1209`

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

## All properties (18) [DT]

- **`AAPL,phandle`**: `311` (`0x137`) → phandle of [`/arm-io/dart-ave`](root__arm-io__dart-ave.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: 32 bytes
  - u32: `0x44415254 0x0 0x54524144 0x0 0x44415046 0x0 0x5f555043 0x46504144`
  - text inside: `TRAD`, `DART`, `FPAD`, `CPU_DAPF`
  ```
  000000  54 52 41 44 00 00 00 00 44 41 52 54 00 00 00 00  TRAD....DART....
  000010  46 50 41 44 00 00 00 00 43 50 55 5f 44 41 50 46  FPAD....CPU_DAPF
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1209` (`0x4b9`)
- **`name`**: `dart-ave`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 32 bytes
  - u32: `0x3020000 0x2 0x20000 0x0 0x3030000 0x2 0x4000 0x0`
  ```
  000000  00 00 02 03 02 00 00 00 00 00 02 00 00 00 00 00  ................
  000010  00 00 03 03 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`remap`**: `1` (`0x1`)
- **`sid`**: `0` (`0x0`)
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x200` (u64; as two u32: `0x200`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

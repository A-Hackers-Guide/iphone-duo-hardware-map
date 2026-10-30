# `/arm-io/dart-avd`

- Name: `dart-avd`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `314`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (3): [`/arm-io/dart-avd/mapper-avd`](root__arm-io__dart-avd__mapper-avd.md), [`/arm-io/dart-avd/mapper-avd-piodma`](root__arm-io__dart-avd__mapper-avd-piodma.md), [`/arm-io/dart-avd/mapper-avd-adsbuf`](root__arm-io__dart-avd__mapper-avd-adsbuf.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x205020000` | `0x20000` (131,072 B) | `0x405020000`–`0x40503ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1183`

## Firmware with a matching name [FW]

- [`Firmware/avd/AppleAVDFW_H19P.im4p`](../firmware/Firmware__avd__AppleAVDFW_H19P.im4p.md) (107,464 B) Tag: IM4P  Type: avdf  Version: 280d6e11

## All properties (18) [DT]

- **`AAPL,phandle`**: `314` (`0x13a`) → phandle of [`/arm-io/dart-avd`](root__arm-io__dart-avd.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`ignore-secondary`**: (present, empty)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1183` (`0x49f`)
- **`name`**: `dart-avd`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x5020000 0x2 0x20000 0x0`
  ```
  000000  00 00 02 05 02 00 00 00 00 00 02 00 00 00 00 00  ................
  ```
- **`sid`**: 12 bytes
  - u32: `0x0 0x1 0x2`
  ```
  000000  00 00 00 00 01 00 00 00 02 00 00 00              ............
  ```
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x180` (u64; as two u32: `0x180`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

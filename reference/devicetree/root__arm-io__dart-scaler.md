# `/arm-io/dart-scaler`

- Name: `dart-scaler`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `291`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-scaler/mapper-scaler`](root__arm-io__dart-scaler__mapper-scaler.md), [`/arm-io/dart-scaler/mapper-scaler-piodma`](root__arm-io__dart-scaler__mapper-scaler-piodma.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x209260000` | `0x20000` (131,072 B) | `0x409260000`–`0x40927ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1291`

## All properties (18) [DT]

- **`AAPL,phandle`**: `291` (`0x123`) → phandle of [`/arm-io/dart-scaler`](root__arm-io__dart-scaler.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1291` (`0x50b`)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-scaler`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x9260000 0x2 0x20000 0x0`
  ```
  000000  00 00 26 09 02 00 00 00 00 00 02 00 00 00 00 00  ..&.............
  ```
- **`sid`**: `0x100000000` (u64; as two u32: `0x0`, `0x1`)
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x500` (u64; as two u32: `0x500`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

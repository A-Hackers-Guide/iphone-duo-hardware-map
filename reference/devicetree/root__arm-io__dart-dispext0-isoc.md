# `/arm-io/dart-dispext0-isoc`

- Name: `dart-dispext0-isoc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `285`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (1): [`/arm-io/dart-dispext0-isoc/mapper-dispext0-dpa`](root__arm-io__dart-dispext0-isoc__mapper-dispext0-dpa.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18e240000` | `0x20000` (131,072 B) | `0x38e240000`–`0x38e25ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1012`

## All properties (17) [DT]

- **`AAPL,phandle`**: `285` (`0x11d`) → phandle of [`/arm-io/dart-dispext0-isoc`](root__arm-io__dart-dispext0-isoc.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1012` (`0x3f4`)
- **`name`**: `dart-dispext0-isoc`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x8e240000 0x1 0x20000 0x0`
  ```
  000000  00 00 24 8e 01 00 00 00 00 00 02 00 00 00 00 00  ..$.............
  ```
- **`sid`**: `0` (`0x0`)
- **`sid-count`**: `1` (`0x1`)
- **`tlbi-aperture-offset`**: `0x300` (u64; as two u32: `0x300`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)

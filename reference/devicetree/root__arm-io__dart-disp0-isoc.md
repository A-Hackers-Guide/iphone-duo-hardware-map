# `/arm-io/dart-disp0-isoc`

- Name: `dart-disp0-isoc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `245`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (1): [`/arm-io/dart-disp0-isoc/mapper-disp0-dpa`](root__arm-io__dart-disp0-isoc__mapper-disp0-dpa.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x186240000` | `0x20000` (131,072 B) | `0x386240000`–`0x38625ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`794`

## All properties (17) [DT]

- **`AAPL,phandle`**: `245` (`0xf5`) → phandle of [`/arm-io/dart-disp0-isoc`](root__arm-io__dart-disp0-isoc.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `794` (`0x31a`)
- **`name`**: `dart-disp0-isoc`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x86240000 0x1 0x20000 0x0`
  ```
  000000  00 00 24 86 01 00 00 00 00 00 02 00 00 00 00 00  ..$.............
  ```
- **`sid`**: `0` (`0x0`)
- **`sid-count`**: `1` (`0x1`)
- **`tlbi-aperture-offset`**: `0x280` (u64; as two u32: `0x280`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)

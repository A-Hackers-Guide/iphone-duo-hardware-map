# `/arm-io/dart-jpeg`

- Name: `dart-jpeg`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `295`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (1): [`/arm-io/dart-jpeg/mapper-jpeg`](root__arm-io__dart-jpeg__mapper-jpeg.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x207020000` | `0xc000` (49,152 B) | `0x407020000`–`0x40702bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1283`

## All properties (17) [DT]

- **`AAPL,phandle`**: `295` (`0x127`) → phandle of [`/arm-io/dart-jpeg`](root__arm-io__dart-jpeg.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1283` (`0x503`)
- **`name`**: `dart-jpeg`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x7020000 0x2 0xc000 0x0`
  ```
  000000  00 00 02 07 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  ```
- **`sid`**: `0` (`0x0`)
- **`sid-count`**: `1` (`0x1`)
- **`tlbi-aperture-offset`**: `0x480` (u64; as two u32: `0x480`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

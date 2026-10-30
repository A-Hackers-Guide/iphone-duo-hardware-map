# `/arm-io/dart-sio`

- Name: `dart-sio`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `138`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-sio/mapper-sio`](root__arm-io__dart-sio__mapper-sio.md), [`/arm-io/dart-sio/mapper-aes`](root__arm-io__dart-sio__mapper-aes.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa5060000` | `0x20000` (131,072 B) | `0x2a5060000`–`0x2a507ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1356`

## All properties (17) [DT]

- **`AAPL,phandle`**: `138` (`0x8a`) → phandle of [`/arm-io/dart-sio`](root__arm-io__dart-sio.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1356` (`0x54c`)
- **`name`**: `dart-sio`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0xa5060000 0x0 0x20000 0x0`
  ```
  000000  00 00 06 a5 00 00 00 00 00 00 02 00 00 00 00 00  ................
  ```
- **`sid`**: `0x100000000` (u64; as two u32: `0x0`, `0x1`)
- **`sid-count`**: `2` (`0x2`)
- **`tlbi-aperture-offset`**: `0x780` (u64; as two u32: `0x780`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

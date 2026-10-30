# `/arm-io/dart-dcpext0`

- Name: `dart-dcpext0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `279`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-dcpext0/mapper-dcpext0`](root__arm-io__dart-dcpext0__mapper-dcpext0.md), [`/arm-io/dart-dcpext0/mapper-dcpext0-exclave`](root__arm-io__dart-dcpext0__mapper-dcpext0-exclave.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18e3c0000` | `0xc000` (49,152 B) | `0x38e3c0000`–`0x38e3cbfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`989`

## All properties (23) [DT]

- **`AAPL,phandle`**: `279` (`0x117`) → phandle of [`/arm-io/dart-dcpext0`](root__arm-io__dart-dcpext0.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: `4` (`0x4`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DARTASC`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `989` (`0x3dd`)
- **`ipce-hw-retention`**: (present, empty)
- **`name`**: `dart-dcpext0`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x8e3c0000 0x1 0xc000 0x0`
  ```
  000000  00 00 3c 8e 01 00 00 00 00 c0 00 00 00 00 00 00  ..<.............
  ```
- **`remap`**: 12 bytes
  - u32: `0x305 0x306 0x308`
  ```
  000000  05 03 00 00 06 03 00 00 08 03 00 00              ............
  ```
- **`retention`**: (present, empty)
- **`sid`**: `3` (`0x3`)
- **`sid-count`**: `15` (`0xf`)
- **`sid-trace`**: `9` (`0x9`)
- **`tlbi-aperture-offset`**: `0x300` (u64; as two u32: `0x300`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)
- **`vm-size-3`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)

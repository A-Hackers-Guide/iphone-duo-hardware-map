# `/arm-io/dart-dcpsec`

- Name: `dart-dcpsec`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `260`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-dcpsec/mapper-dcpsec`](root__arm-io__dart-dcpsec__mapper-dcpsec.md), [`/arm-io/dart-dcpsec/mapper-dcpsec-exclave`](root__arm-io__dart-dcpsec__mapper-dcpsec-exclave.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18a3c0000` | `0x20000` (131,072 B) | `0x38a3c0000`–`0x38a3dffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`880`

## All properties (28) [DT]

- **`AAPL,phandle`**: `260` (`0x104`) → phandle of [`/arm-io/dart-dcpsec`](root__arm-io__dart-dcpsec.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: `4` (`0x4`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DARTASC`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `880` (`0x370`)
- **`ipce-hw-retention`**: (present, empty)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-dcpsec`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x8a3c0000 0x1 0x20000 0x0`
  ```
  000000  00 00 3c 8a 01 00 00 00 00 00 02 00 00 00 00 00  ..<.............
  ```
- **`remap`**: 12 bytes
  - u32: `0x305 0x306 0x308`
  ```
  000000  05 03 00 00 06 03 00 00 08 03 00 00              ............
  ```
- **`retention`**: (present, empty)
- **`sid`**: `3` (`0x3`)
- **`sid-count`**: `15` (`0xf`)
- **`sid-mcw`**: `10` (`0xa`)
- **`sid-trace`**: `9` (`0x9`)
- **`tlbi-aperture-offset`**: `0x380` (u64; as two u32: `0x380`, `0x0`)
- **`tlbi-flushes-smmu`**: (present, empty)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-base-4`**: `0x20000000000` (u64; as two u32: `0x0`, `0x200`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)
- **`vm-size-3`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)
- **`vm-size-4`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)

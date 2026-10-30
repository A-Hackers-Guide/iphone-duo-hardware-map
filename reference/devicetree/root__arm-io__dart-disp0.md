# `/arm-io/dart-disp0`

- Name: `dart-disp0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `238`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (4): [`/arm-io/dart-disp0/mapper-disp0`](root__arm-io__dart-disp0__mapper-disp0.md), [`/arm-io/dart-disp0/mapper-disp0-piodma`](root__arm-io__dart-disp0__mapper-disp0-piodma.md), [`/arm-io/dart-disp0/mapper-disp0-scl`](root__arm-io__dart-disp0__mapper-disp0-scl.md), [`/arm-io/dart-disp0/mapper-disp0-sca`](root__arm-io__dart-disp0__mapper-disp0-sca.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x186380000` | `0xc000` (49,152 B) | `0x386380000`–`0x38638bfff` |
| 1 | `0x186394000` | `0x4000` (16,384 B) | `0x386394000`–`0x386397fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`771`

## All properties (31) [DT]

- **`AAPL,phandle`**: `238` (`0xee`) → phandle of [`/arm-io/dart-disp0`](root__arm-io__dart-disp0.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: `0xf0000000e` (u64; as two u32: `0xe`, `0xf`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`, `UMMS`, `SMMU`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `771` (`0x303`)
- **`ipce-hw-retention`**: (present, empty)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-disp0`
- **`page-size`**: `16384` (`0x4000`)
- **`real-time`**: (present, empty)
- **`reg`**: 32 bytes
  - u32: `0x86380000 0x1 0xc000 0x0 0x86394000 0x1 0x4000 0x0`
  ```
  000000  00 00 38 86 01 00 00 00 00 c0 00 00 00 00 00 00  ..8.............
  000010  00 40 39 86 01 00 00 00 00 40 00 00 00 00 00 00  .@9......@......
  ```
- **`remap`**: 28 bytes
  - u32: `0xb0c 0xb12 0xb01 0xb02 0xb13 0xb05 0x1517`
  ```
  000000  0c 0b 00 00 12 0b 00 00 01 0b 00 00 02 0b 00 00  ................
  000010  13 0b 00 00 05 0b 00 00 17 15 00 00              ............
  ```
- **`retention`**: (present, empty)
- **`sid`**: `0x150000000b` (u64; as two u32: `0xb`, `0x15`)
- **`sid-count`**: `31` (`0x1f`)
- **`tlbi-aperture-offset`**: `0x280` (u64; as two u32: `0x280`, `0x0`)
- **`tlbi-flushes-smmu`**: (present, empty)
- **`vm-alignment`**: 12 bytes
  - u32: `0x1 0x8 0x8`
  ```
  000000  01 00 00 00 08 00 00 00 08 00 00 00              ............
  ```
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-base-14`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-base-15`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)
- **`vm-size-11`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)
- **`vm-size-14`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)
- **`vm-size-15`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)
- **`vm-size-21`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)

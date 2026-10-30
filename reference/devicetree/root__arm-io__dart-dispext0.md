# `/arm-io/dart-dispext0`

- Name: `dart-dispext0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `282`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-dispext0/mapper-dispext0`](root__arm-io__dart-dispext0__mapper-dispext0.md), [`/arm-io/dart-dispext0/mapper-dispext0-piodma`](root__arm-io__dart-dispext0__mapper-dispext0-piodma.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18e380000` | `0xc000` (49,152 B) | `0x38e380000`–`0x38e38bfff` |
| 1 | `0x18e394000` | `0x4000` (16,384 B) | `0x38e394000`–`0x38e397fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`989`

## All properties (24) [DT]

- **`AAPL,phandle`**: `282` (`0x11a`) → phandle of [`/arm-io/dart-dispext0`](root__arm-io__dart-dispext0.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`, `UMMS`, `SMMU`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `989` (`0x3dd`)
- **`ipce-hw-retention`**: (present, empty)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-dispext0`
- **`page-size`**: `16384` (`0x4000`)
- **`real-time`**: (present, empty)
- **`reg`**: 32 bytes
  - u32: `0x8e380000 0x1 0xc000 0x0 0x8e394000 0x1 0x4000 0x0`
  ```
  000000  00 00 38 8e 01 00 00 00 00 c0 00 00 00 00 00 00  ..8.............
  000010  00 40 39 8e 01 00 00 00 00 40 00 00 00 00 00 00  .@9......@......
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
- **`tlbi-aperture-offset`**: `0x300` (u64; as two u32: `0x300`, `0x0`)
- **`tlbi-flushes-smmu`**: (present, empty)
- **`vm-alignment`**: 12 bytes
  - u32: `0x1 0x8 0x8`
  ```
  000000  01 00 00 00 08 00 00 00 08 00 00 00              ............
  ```
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)

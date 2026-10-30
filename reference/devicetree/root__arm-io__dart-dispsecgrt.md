# `/arm-io/dart-dispsecgrt`

- Name: `dart-dispsecgrt`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `268`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (1): [`/arm-io/dart-dispsecgrt/mapper-dispsecgrt`](root__arm-io__dart-dispsecgrt__mapper-dispsecgrt.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x18a3a0000` | `0xc000` (49,152 B) | `0x38a3a0000`–`0x38a3abfff` |
| 1 | `0x18a3b4000` | `0x4000` (16,384 B) | `0x38a3b4000`–`0x38a3b7fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`880`

## All properties (23) [DT]

- **`AAPL,phandle`**: `268` (`0x10c`) → phandle of [`/arm-io/dart-dispsecgrt`](root__arm-io__dart-dispsecgrt.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`, `UMMS`, `SMMU`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `880` (`0x370`)
- **`ipce-hw-retention`**: (present, empty)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-dispsecgrt`
- **`page-size`**: `16384` (`0x4000`)
- **`real-time`**: (present, empty)
- **`reg`**: 32 bytes
  - u32: `0x8a3a0000 0x1 0xc000 0x0 0x8a3b4000 0x1 0x4000 0x0`
  ```
  000000  00 00 3a 8a 01 00 00 00 00 c0 00 00 00 00 00 00  ..:.............
  000010  00 40 3b 8a 01 00 00 00 00 40 00 00 00 00 00 00  .@;......@......
  ```
- **`remap`**: `258` (`0x102`)
- **`retention`**: (present, empty)
- **`sid`**: `1` (`0x1`)
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x380` (u64; as two u32: `0x380`, `0x0`)
- **`tlbi-flushes-smmu`**: (present, empty)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)

# `/arm-io/dart-dcp`

- Name: `dart-dcp`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `235`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-dcp/mapper-dcp`](root__arm-io__dart-dcp__mapper-dcp.md), [`/arm-io/dart-dcp/mapper-dcp-exclave`](root__arm-io__dart-dcp__mapper-dcp-exclave.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x1863c0000` | `0x20000` (131,072 B) | `0x3863c0000`–`0x3863dffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`771`

## Firmware with a matching name [FW]

- [`Firmware/dcp/t8160dcp.im4p`](../firmware/Firmware__dcp__t8160dcp.im4p.md) (3,016,187 B) Tag: IM4P  Type: dcpf  Version: 1
- [`Firmware/dcp/t8160dcp_restore.im4p`](../firmware/Firmware__dcp__t8160dcp_restore.im4p.md) (3,016,667 B) Tag: IM4P  Type: dcpf  Version: 1

## All properties (26) [DT]

- **`AAPL,phandle`**: `235` (`0xeb`) → phandle of [`/arm-io/dart-dcp`](root__arm-io__dart-dcp.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `101` (`0x65`) → phandle of [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: `4` (`0x4`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DARTASC`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `771` (`0x303`)
- **`ipce-hw-retention`**: (present, empty)
- **`name`**: `dart-dcp`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x863c0000 0x1 0x20000 0x0`
  ```
  000000  00 00 3c 86 01 00 00 00 00 00 02 00 00 00 00 00  ..<.............
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
- **`tlbi-aperture-offset`**: `0x280` (u64; as two u32: `0x280`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-base-4`**: `0x20000000000` (u64; as two u32: `0x0`, `0x200`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)
- **`vm-size-3`**: `0x1000000000` (u64; as two u32: `0x0`, `0x10`)
- **`vm-size-4`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)

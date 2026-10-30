# `/arm-io/dart-usb0`

- Name: `dart-usb0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `223`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (1): [`/arm-io/dart-usb0/mapper-usb`](root__arm-io__dart-usb0__mapper-usb.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x323020000` | `0x20000` (131,072 B) | `0x323020000`–`0x32303ffff` |
| 1 | `0x323040000` | `0x20000` (131,072 B) | `0x323040000`–`0x32305ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1492`

## All properties (20) [DT]

- **`AAPL,phandle`**: `223` (`0xdf`) → phandle of [`/arm-io/dart-usb0`](root__arm-io__dart-usb0.md)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `39` (`0x27`) → phandle of [`/cpus/cpu5/:borneo_h19p_4`](root__cpus__cpu5___borneo_h19p_4.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: 32 bytes
  - u32: `0x44415254 0x0 0x54524144 0x544c4c 0x44415254 0x1 0x54524144 0x4b4c42`
  - text inside: `TRAD`, `DARTLLT`, `TRAD`, `DARTBLK`
  ```
  000000  54 52 41 44 00 00 00 00 44 41 52 54 4c 4c 54 00  TRAD....DARTLLT.
  000010  54 52 41 44 01 00 00 00 44 41 52 54 42 4c 4b 00  TRAD....DARTBLK.
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1492` (`0x5d4`)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-usb0`
- **`page-size`**: `16384` (`0x4000`)
- **`protection-granularity`**: `16` (`0x10`)
- **`reg`**: 32 bytes
  - u32: `0x23020000 0x3 0x20000 0x0 0x23040000 0x3 0x20000 0x0`
  ```
  000000  00 00 02 23 03 00 00 00 00 00 02 00 00 00 00 00  ...#............
  000010  00 00 04 23 03 00 00 00 00 00 02 00 00 00 00 00  ...#............
  ```
- **`remap`**: `256` (`0x100`)
- **`sid`**: `0xe00000001` (u64; as two u32: `0x1`, `0xe`)
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x100` (u64; as two u32: `0x100`, `0x0`)
- **`vm-base`**: `0x10000004000` (u64; as two u32: `0x4000`, `0x100`)
- **`vm-size`**: `0xffff0000` (u64; as two u32: `0xffff0000`, `0x0`)

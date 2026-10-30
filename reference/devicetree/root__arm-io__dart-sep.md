# `/arm-io/dart-sep`

- Name: `dart-sep`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `131`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (2): [`/arm-io/dart-sep/mapper-sep`](root__arm-io__dart-sep__mapper-sep.md), [`/arm-io/dart-sep/mapper-sep-exclave`](root__arm-io__dart-sep__mapper-sep-exclave.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa0c80000` | `0x20000` (131,072 B) | `0x2a0c80000`–`0x2a0c9ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`429`

## Firmware with a matching name [FW]

- [`Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`](../firmware/Firmware__all_flash__sep-firmware.v68.RELEASE.im4p.md) (7,216,106 B) Tag: IM4P  Type: sepi  Version: 1
- [`Firmware/all_flash/sep-patches.v68.im4p`](../firmware/Firmware__all_flash__sep-patches.v68.im4p.md) (21,137 B) Tag: IM4P  Type: stg1  Version: AppleSEPROM-1483.0.0.100.14

## All properties (29) [DT]

- **`AAPL,phandle`**: `131` (`0x83`) → phandle of [`/arm-io/dart-sep`](root__arm-io__dart-sep.md)
- **`allow-vm-reserve-mapping`**: (present, empty)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: `2` (`0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `429` (`0x1ad`)
- **`name`**: `dart-sep`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0xa0c80000 0x0 0x20000 0x0`
  ```
  000000  00 00 c8 a0 00 00 00 00 00 00 02 00 00 00 00 00  ................
  ```
- **`retention`**: (present, empty)
- **`sid`**: `0x100000000` (u64; as two u32: `0x0`, `0x1`)
- **`sid-count`**: `3` (`0x3`)
- **`tlbi-aperture-offset`**: `0x700` (u64; as two u32: `0x700`, `0x0`)
- **`txm-secure-channel-base`**: `0x10000004000` (u64; as two u32: `0x4000`, `0x100`)
- **`txm-secure-channel-size`**: `@`
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-base-0`**: `0x10000004000` (u64; as two u32: `0x4000`, `0x100`)
- **`vm-base-1`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-base-2`**: `0x20000004000` (u64; as two u32: `0x4000`, `0x200`)
- **`vm-reserve`**: 16 bytes
  - u32: `0x4000 0x100 0xc000 0x100`
  ```
  000000  00 40 00 00 00 01 00 00 00 c0 00 00 00 01 00 00  .@..............
  ```
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)
- **`vm-size-0`**: `0xffff0000` (u64; as two u32: `0xffff0000`, `0x0`)
- **`vm-size-1`**: `P`
- **`vm-size-2`**: `0xffff0000` (u64; as two u32: `0xffff0000`, `0x0`)

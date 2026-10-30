# `/arm-io/dart-apcie0`

- Name: `dart-apcie0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `421`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (5): [`/arm-io/dart-apcie0/mapper-apcie0-control`](root__arm-io__dart-apcie0__mapper-apcie0-control.md), [`/arm-io/dart-apcie0/mapper-apcie0-alpha`](root__arm-io__dart-apcie0__mapper-apcie0-alpha.md), [`/arm-io/dart-apcie0/mapper-apcie0-beta`](root__arm-io__dart-apcie0__mapper-apcie0-beta.md), [`/arm-io/dart-apcie0/mapper-apcie0-piodma`](root__arm-io__dart-apcie0__mapper-apcie0-piodma.md), [`/arm-io/dart-apcie0/mapper-apcie0-plce`](root__arm-io__dart-apcie0__mapper-apcie0-plce.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x108000000` | `0x20000` (131,072 B) | `0x308000000`–`0x30801ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1458`

## Referenced by (4) [DT]

- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-dart_force_active `Fact`
- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-dart_self `Self`
- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-dart_release_sid `SRel`
- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-dart_request_sid `SReq`

## All properties (24) [DT]

- **`AAPL,phandle`**: `421` (`0x1a5`) → phandle of [`/arm-io/dart-apcie0`](root__arm-io__dart-apcie0.md)
- **`bypass-16`**: (present, empty)
- **`bypass-18`**: (present, empty)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `231` (`0xe7`) → phandle of [`/arm-io/dcp/iop-dcp-nub`](root__arm-io__dcp__iop-dcp-nub.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1458` (`0x5b2`)
- **`ipce-hw-retention`**: (present, empty)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-apcie0`
- **`page-size`**: `16384` (`0x4000`)
- **`protection-granularity`**: `128` (`0x80`)
- **`reg`**: 16 bytes
  - u32: `0x8000000 0x1 0x20000 0x0`
  ```
  000000  00 00 00 08 01 00 00 00 00 00 02 00 00 00 00 00  ................
  ```
- **`retention`**: (present, empty)
- **`sid`**: 32 bytes
  - u32: `0x1 0x2 0x3 0x4 0x10 0x11 0x12 0x13`
  ```
  000000  01 00 00 00 02 00 00 00 03 00 00 00 04 00 00 00  ................
  000010  10 00 00 00 11 00 00 00 12 00 00 00 13 00 00 00  ................
  ```
- **`sid-count`**: `20` (`0x14`)
- **`tlbi-aperture-offset`**: `0x580` (u64; as two u32: `0x580`, `0x0`)
- **`vm-base`**: `0x10000100000` (u64; as two u32: `0x100000`, `0x100`)
- **`vm-offset`**: 16 bytes
  - u32: `0x0 0x0 0x8000000 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 08 00 00 00 00  ................
  ```
- **`vm-size`**: `0x3fe00000` (u64; as two u32: `0x3fe00000`, `0x0`)

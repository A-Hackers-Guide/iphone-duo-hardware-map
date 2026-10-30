# `/arm-io/dart-sbr`

- Name: `dart-sbr`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `141`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (12): [`/arm-io/dart-sbr/mapper-aop`](root__arm-io__dart-sbr__mapper-aop.md), [`/arm-io/dart-sbr/mapper-aop2`](root__arm-io__dart-sbr__mapper-aop2.md), [`/arm-io/dart-sbr/mapper-exclave-aop`](root__arm-io__dart-sbr__mapper-exclave-aop.md), [`/arm-io/dart-sbr/mapper-exclave-aop2`](root__arm-io__dart-sbr__mapper-exclave-aop2.md), [`/arm-io/dart-sbr/mapper-mtp`](root__arm-io__dart-sbr__mapper-mtp.md), [`/arm-io/dart-sbr/mapper-pmp`](root__arm-io__dart-sbr__mapper-pmp.md), [`/arm-io/dart-sbr/mapper-admac-leap-ns`](root__arm-io__dart-sbr__mapper-admac-leap-ns.md), [`/arm-io/dart-sbr/mapper-admac-base-ns`](root__arm-io__dart-sbr__mapper-admac-base-ns.md), [`/arm-io/dart-sbr/mapper-admac-leap-s`](root__arm-io__dart-sbr__mapper-admac-leap-s.md), [`/arm-io/dart-sbr/mapper-admac-base-s`](root__arm-io__dart-sbr__mapper-admac-base-s.md), [`/arm-io/dart-sbr/mapper-scm`](root__arm-io__dart-sbr__mapper-scm.md), [`/arm-io/dart-sbr/mapper-rsm`](root__arm-io__dart-sbr__mapper-rsm.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x98100000` | `0xc000` (49,152 B) | `0x298100000`–`0x29810bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`102`

## All properties (32) [DT]

- **`AAPL,phandle`**: `141` (`0x8d`) → phandle of [`/arm-io/dart-sbr`](root__arm-io__dart-sbr.md)
- **`always-on`**: (present, empty)
- **`compatible`**: `dart,t8110`
- **`dart-options`**: `229` (`0xe5`) → phandle of [`/arm-io/usb-drd0/:borneo_h19p_5/usb-drd0-port-ss`](root__arm-io__usb-drd0___borneo_h19p_5__usb-drd0-port-ss.md)
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: 16 bytes
  - u32: `0x1 0x3 0x2b 0x2d`
  ```
  000000  01 00 00 00 03 00 00 00 2b 00 00 00 2d 00 00 00  ........+...-...
  ```
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: `TRAD`, `DART`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `102` (`0x66`)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-sbr`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 16 bytes
  - u32: `0x98100000 0x0 0xc000 0x0`
  ```
  000000  00 00 10 98 00 00 00 00 00 c0 00 00 00 00 00 00  ................
  ```
- **`remap`**: 24 bytes
  - u32: `0x41a 0x41b 0x41c 0x41d 0x41e 0x41f`
  ```
  000000  1a 04 00 00 1b 04 00 00 1c 04 00 00 1d 04 00 00  ................
  000010  1e 04 00 00 1f 04 00 00                          ........
  ```
- **`retention`**: (present, empty)
- **`sid`**: 36 bytes
  - u32: `0x0 0x2 0x4 0x6 0x19 0x28 0x2c 0x2e 0x2f`
  ```
  000000  00 00 00 00 02 00 00 00 04 00 00 00 06 00 00 00  ................
  000010  19 00 00 00 28 00 00 00 2c 00 00 00 2e 00 00 00  ....(...,.......
  000020  2f 00 00 00                                      /...
  ```
- **`sid-count`**: `57` (`0x39`)
- **`sid-lft`**: `&`, `'`, `2`, `3`
- **`sid-mcw`**: `#`, `$`
- **`sid-ocla`**: `%`, `4`
- **`sid-trace`**: 20 bytes
  - u32: `0xa 0xa 0xb 0xc 0xd`
  ```
  000000  0a 00 00 00 0a 00 00 00 0b 00 00 00 0c 00 00 00  ................
  000010  0d 00 00 00                                      ....
  ```
- **`tlbi-aperture-offset`**: `0x680` (u64; as two u32: `0x680`, `0x0`)
- **`vm-base`**: `0x10040000000` (u64; as two u32: `0x40000000`, `0x100`)
- **`vm-base-1`**: `0x20000000000` (u64; as two u32: `0x0`, `0x200`)
- **`vm-base-3`**: `0x20000000000` (u64; as two u32: `0x0`, `0x200`)
- **`vm-base-43`**: `0x10040000000` (u64; as two u32: `0x40000000`, `0x100`)
- **`vm-size`**: `0x2ffc0000000` (u64; as two u32: `0xc0000000`, `0x2ff`)
- **`vm-size-1`**: ` `
- **`vm-size-3`**: ` `
- **`vm-size-43`**: `0xffff0000` (u64; as two u32: `0xffff0000`, `0x0`)

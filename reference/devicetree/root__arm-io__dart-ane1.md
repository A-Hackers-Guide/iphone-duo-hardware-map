# `/arm-io/dart-ane1`

- Name: `dart-ane1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `332`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (9): [`/arm-io/dart-ane1/mapper-ane1`](root__arm-io__dart-ane1__mapper-ane1.md), [`/arm-io/dart-ane1/mapper-ane1-iso1`](root__arm-io__dart-ane1__mapper-ane1-iso1.md), [`/arm-io/dart-ane1/mapper-ane1-iso2`](root__arm-io__dart-ane1__mapper-ane1-iso2.md), [`/arm-io/dart-ane1/mapper-ane1-iso3`](root__arm-io__dart-ane1__mapper-ane1-iso3.md), [`/arm-io/dart-ane1/mapper-ane1-iso4`](root__arm-io__dart-ane1__mapper-ane1-iso4.md), [`/arm-io/dart-ane1/mapper-ane1-iso5`](root__arm-io__dart-ane1__mapper-ane1-iso5.md), [`/arm-io/dart-ane1/mapper-ane1-iso6`](root__arm-io__dart-ane1__mapper-ane1-iso6.md), [`/arm-io/dart-ane1/mapper-ane1-iso7`](root__arm-io__dart-ane1__mapper-ane1-iso7.md), [`/arm-io/dart-ane1/mapper-ane1-mpm`](root__arm-io__dart-ane1__mapper-ane1-mpm.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x213040000` | `0xc000` (49,152 B) | `0x413040000`–`0x41304bfff` |
| 1 | `0x213060000` | `0xc000` (49,152 B) | `0x413060000`–`0x41306bfff` |
| 2 | `0x213080000` | `0xc000` (49,152 B) | `0x413080000`–`0x41308bfff` |
| 3 | `0x2130a0000` | `0xc000` (49,152 B) | `0x4130a0000`–`0x4130abfff` |
| 4 | `0x213050000` | `0x4000` (16,384 B) | `0x413050000`–`0x413053fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`727`

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane1_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane1_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: ane1  Version: 1

## All properties (24) [DT]

- **`AAPL,phandle`**: `332` (`0x14c`) → phandle of [`/arm-io/dart-ane1`](root__arm-io__dart-ane1.md)
- **`bypass-10`**: (present, empty)
- **`bypass-13`**: (present, empty)
- **`bypass-15`**: (present, empty)
- **`compatible`**: `dart,t8110`
- **`dapf-instance-0`**: 156 bytes
  - u32: `0x81618000 0x3 0x81618003 0x3 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x10300 0x80700840 0x2 0x80700843 0x2 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x10300 0x80710020 0x2 0x80710043 0x2 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x10300`
  ```
  000000  00 80 61 81 03 00 00 00 03 80 61 81 03 00 00 00  ..a.......a.....
  000010  01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000030  00 03 01 00 40 08 70 80 02 00 00 00 43 08 70 80  ....@.p.....C.p.
  000040  02 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00  ................
  000050  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000060  00 00 00 00 00 03 01 00 20 00 71 80 02 00 00 00  ........ .q.....
  000070  43 00 71 80 02 00 00 00 01 00 00 00 00 00 00 00  C.q.............
  000080  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000090  00 00 00 00 00 00 00 00 00 03 01 00              ............
  ```
- **`dart-options`**: `37` (`0x25`) → phandle of [`/cpus/cpu5`](root__cpus__cpu5.md)
- **`dead-mappings`**: 16 bytes
  - u32: `0xfffff000 0x3ff 0x1000 0x0`
  ```
  000000  00 f0 ff ff ff 03 00 00 00 10 00 00 00 00 00 00  ................
  ```
- **`device_type`**: `dart`
- **`error-reflector`**: `0x27f000000` (u64; as two u32: `0x7f000000`, `0x2`)
- **`exclave-sid`**: 28 bytes
  - u32: `0x1 0x2 0x3 0x4 0x5 0x6 0x7`
  ```
  000000  01 00 00 00 02 00 00 00 03 00 00 00 04 00 00 00  ................
  000010  05 00 00 00 06 00 00 00 07 00 00 00              ............
  ```
- **`flush-by-dva`**: `1` (`0x1`)
- **`instance`**: 80 bytes
  - u32: `0x44415254 0x0 0x54524144 0x544c4c 0x44415254 0x1 0x54524144 0x445242 0x44415254 0x2 0x54524144 0x445242 0x44415254 0x3 0x54524144 0x525742 0x44415046 0x0 0x46504144 0x544c4c`
  - text inside: `TRAD`, `DARTLLT`, `TRAD`, `DARTBRD`, `TRAD`, `DARTBRD`, `TRAD`, `DARTBWR`, `FPAD`, `DAPFLLT`
  ```
  000000  54 52 41 44 00 00 00 00 44 41 52 54 4c 4c 54 00  TRAD....DARTLLT.
  000010  54 52 41 44 01 00 00 00 44 41 52 54 42 52 44 00  TRAD....DARTBRD.
  000020  54 52 41 44 02 00 00 00 44 41 52 54 42 52 44 00  TRAD....DARTBRD.
  000030  54 52 41 44 03 00 00 00 44 41 52 54 42 57 52 00  TRAD....DARTBWR.
  000040  46 50 41 44 00 00 00 00 44 41 50 46 4c 4c 54 00  FPAD....DAPFLLT.
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `727` (`0x2d7`)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-ane1`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 80 bytes
  - u32: `0x13040000 0x2 0xc000 0x0 0x13060000 0x2 0xc000 0x0 0x13080000 0x2 0xc000 0x0 0x130a0000 0x2 0xc000 0x0 0x13050000 0x2 0x4000 0x0`
  ```
  000000  00 00 04 13 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000010  00 00 06 13 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000020  00 00 08 13 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000030  00 00 0a 13 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000040  00 00 05 13 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`sid`**: 20 bytes
  - u32: `0x0 0xa 0xb 0xd 0xf`
  ```
  000000  00 00 00 00 0a 00 00 00 0b 00 00 00 0d 00 00 00  ................
  000010  0f 00 00 00                                      ....
  ```
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x80` (u64; as two u32: `0x80`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

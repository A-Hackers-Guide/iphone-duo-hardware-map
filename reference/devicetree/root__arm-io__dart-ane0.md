# `/arm-io/dart-ane0`

- Name: `dart-ane0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `320`
- compatible: `dart,t8110`
- device_type: `dart`
- Children (9): [`/arm-io/dart-ane0/mapper-ane0`](root__arm-io__dart-ane0__mapper-ane0.md), [`/arm-io/dart-ane0/mapper-ane0-iso1`](root__arm-io__dart-ane0__mapper-ane0-iso1.md), [`/arm-io/dart-ane0/mapper-ane0-iso2`](root__arm-io__dart-ane0__mapper-ane0-iso2.md), [`/arm-io/dart-ane0/mapper-ane0-iso3`](root__arm-io__dart-ane0__mapper-ane0-iso3.md), [`/arm-io/dart-ane0/mapper-ane0-iso4`](root__arm-io__dart-ane0__mapper-ane0-iso4.md), [`/arm-io/dart-ane0/mapper-ane0-iso5`](root__arm-io__dart-ane0__mapper-ane0-iso5.md), [`/arm-io/dart-ane0/mapper-ane0-iso6`](root__arm-io__dart-ane0__mapper-ane0-iso6.md), [`/arm-io/dart-ane0/mapper-ane0-iso7`](root__arm-io__dart-ane0__mapper-ane0-iso7.md), [`/arm-io/dart-ane0/mapper-ane0-mpm`](root__arm-io__dart-ane0__mapper-ane0-mpm.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8110DART` | `AppleARMIODevice` | [`com.apple.driver.AppleT8110DART`](../kexts/com.apple.driver.AppleT8110DART.md) | `dart,t8110` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x20f040000` | `0xc000` (49,152 B) | `0x40f040000`–`0x40f04bfff` |
| 1 | `0x20f060000` | `0xc000` (49,152 B) | `0x40f060000`–`0x40f06bfff` |
| 2 | `0x20f080000` | `0xc000` (49,152 B) | `0x40f080000`–`0x40f08bfff` |
| 3 | `0x20f0a0000` | `0xc000` (49,152 B) | `0x40f0a0000`–`0x40f0abfff` |
| 4 | `0x20f050000` | `0x4000` (16,384 B) | `0x40f050000`–`0x40f053fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`679`

## Firmware with a matching name [FW]

- [`Firmware/ane/h19_ane0_fw_perses_v6x.im4p`](../firmware/Firmware__ane__h19_ane0_fw_perses_v6x.im4p.md) (1,556,505 B) Tag: IM4P  Type: anef  Version: 1

## All properties (24) [DT]

- **`AAPL,phandle`**: `320` (`0x140`) → phandle of [`/arm-io/dart-ane0`](root__arm-io__dart-ane0.md)
- **`bypass-10`**: (present, empty)
- **`bypass-13`**: (present, empty)
- **`bypass-15`**: (present, empty)
- **`compatible`**: `dart,t8110`
- **`dapf-instance-0`**: 156 bytes
  - u32: `0x81618000 0x3 0x81618003 0x3 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x10300 0x80700820 0x2 0x80700823 0x2 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x10300 0x8070c020 0x2 0x8070c043 0x2 0x1 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x10300`
  ```
  000000  00 80 61 81 03 00 00 00 03 80 61 81 03 00 00 00  ..a.......a.....
  000010  01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000030  00 03 01 00 20 08 70 80 02 00 00 00 23 08 70 80  .... .p.....#.p.
  000040  02 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00  ................
  000050  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000060  00 00 00 00 00 03 01 00 20 c0 70 80 02 00 00 00  ........ .p.....
  000070  43 c0 70 80 02 00 00 00 01 00 00 00 00 00 00 00  C.p.............
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
- **`interrupts`**: `679` (`0x2a7`)
- **`manual-availability`**: `1` (`0x1`)
- **`name`**: `dart-ane0`
- **`page-size`**: `16384` (`0x4000`)
- **`reg`**: 80 bytes
  - u32: `0xf040000 0x2 0xc000 0x0 0xf060000 0x2 0xc000 0x0 0xf080000 0x2 0xc000 0x0 0xf0a0000 0x2 0xc000 0x0 0xf050000 0x2 0x4000 0x0`
  ```
  000000  00 00 04 0f 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000010  00 00 06 0f 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000020  00 00 08 0f 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000030  00 00 0a 0f 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  000040  00 00 05 0f 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`sid`**: 20 bytes
  - u32: `0x0 0xa 0xb 0xd 0xf`
  ```
  000000  00 00 00 00 0a 00 00 00 0b 00 00 00 0d 00 00 00  ................
  000010  0f 00 00 00                                      ....
  ```
- **`sid-count`**: `16` (`0x10`)
- **`tlbi-aperture-offset`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
- **`vm-base`**: `0x10000000000` (u64; as two u32: `0x0`, `0x100`)
- **`vm-size`**: `0x30000000000` (u64; as two u32: `0x0`, `0x300`)

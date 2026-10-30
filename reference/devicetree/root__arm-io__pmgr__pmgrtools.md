# `/arm-io/pmgr/pmgrtools`

- Name: `pmgrtools`
- Parent: [`/arm-io/pmgr`](root__arm-io__pmgr.md)
- phandle: `49`
- compatible: `pmgrtools`
- device_type: `pmgrtools`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Interrupts [DT]

Controller: [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)

`1330861125, 1278297177`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `pmuaccess_L1DY` | [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md) | `pmuR` | `` |

## All properties (11) [DT]

- **`AAPL,phandle`**: `49` (`0x31`) → phandle of [`/arm-io/pmgr/pmgrtools`](root__arm-io__pmgr__pmgrtools.md)
- **`aon-ptd-supported`**: (present, empty)
- **`compatible`**: `pmgrtools`
- **`device_type`**: `pmgrtools`
- **`function-pmuaccess_L1DY`**: `0x706d7552000000c6` (u64; as two u32: `0xc6`, `0x706d7552`)
- **`interrupt-parent`**: `166` (`0xa6`) → phandle of [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)
- **`interrupts`**: `0x4c3144594f535445` (u64; as two u32: `0x4f535445`, `0x4c314459`)
- **`name`**: `pmgrtools`
- **`pmgrtools-version`**: `1` (`0x1`)
- **`pmu_mcom_offset_L1DY`**: `11104` (`0x2b60`)
- **`soc-device-ps-map`**: 260 bytes
  - u32: `0x67 0x584741 0x0 0x0 0x0 0xd 0x30454e41 0x0 0x0 0x0 0xe 0x31454e41 0x0 0x0 0x0 0x9 0x505349 0x0 0x0 0x0 0xa 0x50534944 0x30 0x0 0x0 0x5 0x50534944 0x31 0x0 0x0 0xb 0x50534944 0x545845 0x0 0x0 0xf 0x455641 0x0 0x0 0x0 0x10 0x445641 0x0 0x0 0x0 0xc 0x52534d 0x0 0x0 0x0 0x8 0x4745504a 0x0 0x0 0x0 0x6 0x524f5250 0x5345 0x0 0x0 0x63 0x435441 0x0 0x0 0x0`
  - text inside: `ANE0`, `ANE1`, `DISP0`, `DISP1`, `DISPEXT`, `JPEG`, `PRORES`
  ```
  000000  67 00 00 00 41 47 58 00 00 00 00 00 00 00 00 00  g...AGX.........
  000010  00 00 00 00 0d 00 00 00 41 4e 45 30 00 00 00 00  ........ANE0....
  000020  00 00 00 00 00 00 00 00 0e 00 00 00 41 4e 45 31  ............ANE1
  000030  00 00 00 00 00 00 00 00 00 00 00 00 09 00 00 00  ................
  000040  49 53 50 00 00 00 00 00 00 00 00 00 00 00 00 00  ISP.............
  000050  0a 00 00 00 44 49 53 50 30 00 00 00 00 00 00 00  ....DISP0.......
  000060  00 00 00 00 05 00 00 00 44 49 53 50 31 00 00 00  ........DISP1...
  000070  00 00 00 00 00 00 00 00 0b 00 00 00 44 49 53 50  ............DISP
  000080  45 58 54 00 00 00 00 00 00 00 00 00 0f 00 00 00  EXT.............
  000090  41 56 45 00 00 00 00 00 00 00 00 00 00 00 00 00  AVE.............
  0000a0  10 00 00 00 41 56 44 00 00 00 00 00 00 00 00 00  ....AVD.........
  0000b0  00 00 00 00 0c 00 00 00 4d 53 52 00 00 00 00 00  ........MSR.....
  0000c0  00 00 00 00 00 00 00 00 08 00 00 00 4a 50 45 47  ............JPEG
  0000d0  00 00 00 00 00 00 00 00 00 00 00 00 06 00 00 00  ................
  0000e0  50 52 4f 52 45 53 00 00 00 00 00 00 00 00 00 00  PRORES..........
  0000f0  63 00 00 00 41 54 43 00 00 00 00 00 00 00 00 00  c...ATC.........
  000100  00 00 00 00                                      ....
  ```

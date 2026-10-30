# `/core-brightness/brightness-secondary-doe1`

- Name: `brightness-secondary-doe1`
- Parent: [`/core-brightness`](root__core-brightness.md)
- phandle: `459`
- device_type: `brightness-control`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (100) [DT]

- **`AAPL,phandle`**: `459` (`0x1cb`) → phandle of [`/core-brightness/brightness-secondary-doe1`](root__core-brightness__brightness-secondary-doe1.md)
- **`aab-cap-e`**: 16 bytes
  - u32: `0x0 0x41f00000 0x447a0000 0x459c4000`
  ```
  000000  00 00 00 00 00 00 f0 41 00 00 7a 44 00 40 9c 45  .......A..zD.@.E
  ```
- **`aab-cap-l`**: 16 bytes
  - u32: `0x42480000 0x43960000 0x44098000 0xbf800000`
  ```
  000000  00 00 48 42 00 00 96 43 00 80 09 44 00 00 80 bf  ..HB...C...D....
  ```
- **`aab-constraint-e2`**: `600` (`0x258`)
- **`aab-constraint-emax`**: `5000` (`0x1388`)
- **`aab-constraint-l0b`**: `135` (`0x87`)
- **`aab-constraint-l2`**: `220` (`0xdc`)
- **`aab-constraint-lmax`**: `1060` (`0x424`)
- **`aml-lux-activation-threshold`**: `1133903872` (`0x43960000`)
- **`aml-lux-table`**: 72 bytes
  - u32: `0x42c80000 0x43960000 0x44160000 0x44480000 0x447a0000 0x453b8000 0x459c4000 0x461c4000 0x466a6000 0x46c35000 0x4708b800 0x472fc800 0x4756d800 0x477de800 0x479c4000 0x47b98c00 0x47d6d800 0x48127c00`
  ```
  000000  00 00 c8 42 00 00 96 43 00 00 16 44 00 00 48 44  ...B...C...D..HD
  000010  00 00 7a 44 00 80 3b 45 00 40 9c 45 00 40 1c 46  ..zD..;E.@.E.@.F
  000020  00 60 6a 46 00 50 c3 46 00 b8 08 47 00 c8 2f 47  .`jF.P.F...G../G
  000030  00 d8 56 47 00 e8 7d 47 00 40 9c 47 00 8c b9 47  ..VG..}G.@.G...G
  000040  00 d8 d6 47 00 7c 12 48                          ...G.|.H
  ```
- **`aml-nits-activation-threshold`**: `1120403456` (`0x42c80000`)
- **`aml-nits-table`**: 60 bytes
  - u32: `0x42c80000 0x43960000 0x43fa0000 0x442f0000 0x44610000 0x44898000 0x44a28000 0x44bb8000 0x44d48000 0x44ed8000 0x45034000 0x450fc000 0x451c4000 0x4528c000 0x453b8000`
  ```
  000000  00 00 c8 42 00 00 96 43 00 00 fa 43 00 00 2f 44  ...B...C...C../D
  000010  00 00 61 44 00 80 89 44 00 80 a2 44 00 80 bb 44  ..aD...D...D...D
  000020  00 80 d4 44 00 80 ed 44 00 40 03 45 00 c0 0f 45  ...D...D.@.E...E
  000030  00 40 1c 45 00 c0 28 45 00 80 3b 45              .@.E..(E..;E
  ```
- **`aml-ramp-aod-duration`**: `1073741824` (`0x40000000`)
- **`aml-ramp-bezier-anchors`**: 12 bytes
  - u32: `0x3e99999a 0x3f666666 0x3f59999a`
  - text inside: `>fff?`
  ```
  000000  9a 99 99 3e 66 66 66 3f 9a 99 59 3f              ...>fff?..Y?
  ```
- **`aml-ramp-down-duration`**: `1084227584` (`0x40a00000`)
- **`aml-ramp-down-lux-threshold`**: `1125515264` (`0x43160000`)
- **`aml-ramp-up-duration`**: `1084227584` (`0x40a00000`)
- **`aml-ramp-up-lux-threshold`**: `1125515264` (`0x43160000`)
- **`aml-ramp-update-rate`**: `1114636288` (`0x42700000`)
- **`aml-strength-table`**: 1080 bytes
  - text inside: `<~tj<o`, `>?="q`, `]=!v&=`, `=g~5=`, `|<>e6(>`, `KZ>9`, `:?@j3?`, `pM?+`, `V?0GO?w`, `G?'1@?'1@?'1@?'1@?'1@?'1@?'1@?'1@?'1@?`, `O?~W4?&`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000030  00 00 00 00 00 00 00 00 00 00 00 00 76 89 ea 3c  ............v..<
  000040  da e1 af 3c 7e 74 6a 3c 6f 9e ea 3b 00 00 00 00  ...<~tj<o..;....
  000050  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000060  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000070  00 00 00 00 00 00 00 00 03 3e 3f 3d 22 71 0f 3d  .........>?="q.=
  000080  87 33 bf 3c 87 33 3f 3c 00 00 00 00 00 00 00 00  .3.<.3?<........
  000090  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000a0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000b0  00 00 00 00 55 f6 5d 3d 21 76 26 3d d9 eb dd 3c  ....U.]=!v&=...<
  0000c0  d2 00 5e 3c 00 00 00 00 00 00 00 00 00 00 00 00  ..^<............
  0000d0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000e0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000f0  8f c2 75 3d ec 51 38 3d 8f c2 f5 3c 8f c2 75 3c  ..u=.Q8=...<..u<
  000100  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000110  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000120  00 00 00 00 00 00 00 00 00 00 00 00 a5 83 b5 3d  ...............=
  000130  6c 21 88 3d 67 7e 35 3d e3 88 b5 3c 00 00 00 00  l!.=g~5=...<....
  000140  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000150  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000160  00 00 00 00 00 00 00 00 f2 b0 d0 3d d1 91 9c 3d  ...........=...=
  000170  eb c5 50 3d 6f bb d0 3c 00 00 00 00 00 00 00 00  ..P=o..<........
  000180  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000190  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0001a0  00 00 00 00 c0 09 65 3e 4c c3 50 3e d9 7c 3c 3e  ......e>L.P>.|<>
  0001b0  65 36 28 3e f2 ef 13 3e f2 ef 13 3e f2 ef 13 3e  e6(>...>...>...>
  0001c0  f2 ef 13 3e f2 ef 13 3e f2 ef 13 3e f2 ef 13 3e  ...>...>...>...>
  0001d0  f2 ef 13 3e f2 ef 13 3e 77 d6 0e 3e fd bc 09 3e  ...>...>w..>...>
  0001e0  9a 7c a3 3e c1 6e 98 3e 66 6b 8d 3e dd 5e 82 3e  .|.>.n.>fk.>.^.>
  0001f0  63 b4 6e 3e 63 b4 6e 3e 63 b4 6e 3e 63 b4 6e 3e  c.n>c.n>c.n>c.n>
  000200  63 b4 6e 3e 63 b4 6e 3e 63 b4 6e 3e 63 b4 6e 3e  c.n>c.n>c.n>c.n>
  000210  63 b4 6e 3e 6f 81 64 3e dc 4b 5a 3e 39 ee e4 3e  c.n>o.d>.KZ>9..>
  000220  f4 c3 d8 3e af 99 cc 3e 96 78 c0 3e 51 4e b4 3e  ...>...>.x.>QN.>
  000230  51 4e b4 3e 51 4e b4 3e 51 4e b4 3e 51 4e b4 3e  QN.>QN.>QN.>QN.>
  000240  51 4e b4 3e 51 4e b4 3e 51 4e b4 3e 51 4e b4 3e  QN.>QN.>QN.>QN.>
  000250  5c 1b aa 3e 19 e7 9f 3e 82 c5 09 3f 59 51 03 3f  \..>...>...?YQ.?
  000260  5e ba f9 3e e8 d9 ec 3e 95 f1 df 3e 95 f1 df 3e  ^..>...>...>...>
  000270  95 f1 df 3e 95 f1 df 3e 95 f1 df 3e 95 f1 df 3e  ...>...>...>...>
  000280  95 f1 df 3e 95 f1 df 3e 95 f1 df 3e 38 a1 d0 3e  ...>...>...>8..>
  000290  7a 53 c1 3e fb 74 1c 3f 5a bb 15 3f 60 02 0f 3f  zS.>.t.?Z..?`..?
  0002a0  bf 48 08 3f 1d 8f 01 3f 1d 8f 01 3f 1d 8f 01 3f  .H.?...?...?...?
  0002b0  1d 8f 01 3f 1d 8f 01 3f 1d 8f 01 3f 1d 8f 01 3f  ...?...?...?...?
  0002c0  1d 8f 01 3f 1d 8f 01 3f 14 b3 ee 3e dc 4b da 3e  ...?...?...>.K.>
  0002d0  e0 67 2c 3f e2 75 25 3f 8c 84 1e 3f 8e 92 17 3f  .g,?.u%?...?...?
  0002e0  90 a0 10 3f 90 a0 10 3f 90 a0 10 3f 90 a0 10 3f  ...?...?...?...?
  0002f0  90 a0 10 3f 90 a0 10 3f 90 a0 10 3f 90 a0 10 3f  ...?...?...?...?
  000300  90 a0 10 3f 37 e0 03 3f cd 3b ee 3e 6e 8b 3a 3f  ...?7..?.;.>n.:?
  000310  40 6a 33 3f 13 49 2c 3f e5 27 25 3f 10 06 1e 3f  @j3?.I,?.'%?...?
  000320  10 06 1e 3f 10 06 1e 3f 10 06 1e 3f 10 06 1e 3f  ...?...?...?...?
  000330  10 06 1e 3f 10 06 1e 3f 10 06 1e 3f 10 06 1e 3f  ...?...?...?...?
  000340  fa b8 0e 3f d8 d3 fe 3e a4 70 4d 3f 2b 13 46 3f  ...?...>.pM?+.F?
  000350  a1 b9 3e 3f 81 5b 37 3f f7 01 30 3f f7 01 30 3f  ..>?.[7?..0?..0?
  000360  f7 01 30 3f f7 01 30 3f f7 01 30 3f f7 01 30 3f  ..0?..0?..0?..0?
  000370  f7 01 30 3f f7 01 30 3f f7 01 30 3f d7 dd 1c 3f  ..0?..0?..0?...?
  000380  56 bc 09 3f 9c e1 56 3f 28 d5 56 3f 30 47 4f 3f  V..?..V?(.V?0GO?
  000390  77 be 47 3f 27 31 40 3f 27 31 40 3f 27 31 40 3f  w.G?'1@?'1@?'1@?
  0003a0  27 31 40 3f 27 31 40 3f 27 31 40 3f 27 31 40 3f  '1@?'1@?'1@?'1@?
  0003b0  27 31 40 3f 27 31 40 3f 93 3a 29 3f a6 44 12 3f  '1@?'1@?.:)?.D.?
  0003c0  7b 88 5e 3f 7b 88 5e 3f 7b 88 5e 3f d8 d3 56 3f  {.^?{.^?{.^?..V?
  0003d0  de 1f 4f 3f de 1f 4f 3f de 1f 4f 3f de 1f 4f 3f  ..O?..O?..O?..O?
  0003e0  de 1f 4f 3f de 1f 4f 3f de 1f 4f 3f de 1f 4f 3f  ..O?..O?..O?..O?
  0003f0  de 1f 4f 3f 7e 57 34 3f 26 8d 19 3f aa f1 72 3f  ..O?~W4?&..?..r?
  000400  aa f1 72 3f aa f1 72 3f aa f1 72 3f aa f1 72 3f  ..r?..r?..r?..r?
  000410  aa f1 72 3f aa f1 72 3f aa f1 72 3f aa f1 72 3f  ..r?..r?..r?..r?
  000420  aa f1 72 3f aa f1 72 3f aa f1 72 3f aa f1 72 3f  ..r?..r?..r?..r?
  000430  b6 f3 4d 3f c3 f5 28 3f                          ..M?..(?
  ```
- **`aml-supported`**: `1` (`0x1`)
- **`aurora-cltm-enter-multiplier`**: `1067869798` (`0x3fa66666`)
- **`aurora-cltm-threshold`**: `1125842944` (`0x431b0000`)
- **`aurora-enter-lux`**: 12 bytes
  - u32: `0x45b0c800 0x45b0c800 0x45b0c800`
  ```
  000000  00 c8 b0 45 00 c8 b0 45 00 c8 b0 45              ...E...E...E
  ```
- **`aurora-exit-lux`**: 12 bytes
  - u32: `0x45a08800 0x45a08800 0x45a08800`
  ```
  000000  00 88 a0 45 00 88 a0 45 00 88 a0 45              ...E...E...E
  ```
- **`aurora-ramp-down-tap-points`**: `0x3ecccccd3e4ccccd` (u64; as two u32: `0x3e4ccccd`, `0x3ecccccd`)
- **`aurora-ramp-up-speed`**: `1073741824` (`0x40000000`)
- **`aurora-ramp-up-tap-points`**: `0x3eb333333e3851ec` (u64; as two u32: `0x3e3851ec`, `0x3eb33333`)
- **`aurora-saturation-lux`**: 12 bytes
  - u32: `0x4682ce00 0x4682ce00 0x4682ce00`
  ```
  000000  00 ce 82 46 00 ce 82 46 00 ce 82 46              ...F...F...F
  ```
- **`aurora-session-limit`**: `1133903872` (`0x43960000`)
- **`aurora-supported`**: `1` (`0x1`)
- **`aurora-upo-enter-multiplier`**: `1068062736` (`0x3fa95810`)
- **`aurora-upo-threshold`**: `1150681088` (`0x44960000`)
- **`bdm-nits1`**: `1146388480` (`0x44548000`)
- **`bdm-nits2`**: `1153957888` (`0x44c80000`)
- **`bdm-supported`**: `1` (`0x1`)
- **`blr-cct-warning`**: `2700` (`0xa8c`)
- **`boost-enabled`**: `1` (`0x1`)
- **`dcp-brightness-node`**: `DCPSEC`
- **`device_type`**: `brightness-control`
- **`display-id`**: `1` (`0x1`)
- **`ds-max-factor-aab-off`**: `1062031327` (`0x3f4d4fdf`)
- **`ds-max-factors`**: 24 bytes
  - u32: `0x3e75c28f 0x3f051eb8 0x3f051eb8 0x3f051eb8 0x3f170a3d 0x3f800000`
  ```
  000000  8f c2 75 3e b8 1e 05 3f b8 1e 05 3f b8 1e 05 3f  ..u>...?...?...?
  000010  3d 0a 17 3f 00 00 80 3f                          =..?...?
  ```
- **`ds-max-fall-time`**: `1092616192` (`0x41200000`)
- **`ds-max-pivot`**: `1106247680` (`0x41f00000`)
- **`ds-max-rise-time`**: `1084227584` (`0x40a00000`)
- **`ds-max-rise-time-fast`**: `1077936128` (`0x40400000`)
- **`ds-max-rise-time-fast-thr`**: `1065017672` (`0x3f7ae148`)
- **`ds-max-thresholds`**: 24 bytes
  - u32: `0x3f800000 0x41f00000 0x44160000 0x447a0000 0x45535000 0x45b0c800`
  ```
  000000  00 00 80 3f 00 00 f0 41 00 00 16 44 00 00 7a 44  ...?...A...D..zD
  000010  00 50 53 45 00 c8 b0 45                          .PSE...E
  ```
- **`ds-min-factors`**: 24 bytes
  - u32: `0x3f800000 0x40000000 0x40c00000 0x40c00000 0x41400000 0x42a00000`
  ```
  000000  00 00 80 3f 00 00 00 40 00 00 c0 40 00 00 c0 40  ...?...@...@...@
  000010  00 00 40 41 00 00 a0 42                          ..@A...B
  ```
- **`ds-min-fall-time`**: `1092616192` (`0x41200000`)
- **`ds-min-pivot`**: `1122369536` (`0x42e60000`)
- **`ds-min-rise-time`**: `1084227584` (`0x40a00000`)
- **`ds-min-thresholds`**: 24 bytes
  - u32: `0x40a00000 0x41f00000 0x42c80000 0x43fa0000 0x447a0000 0x477fff00`
  ```
  000000  00 00 a0 40 00 00 f0 41 00 00 c8 42 00 00 fa 43  ...@...A...B...C
  000010  00 00 7a 44 00 ff 7f 47                          ..zD...G
  ```
- **`edr-exit-seconds-per-stop`**: `1061158912` (`0x3f400000`)
- **`edr-max-nits`**: `1153957888` (`0x44c80000`)
- **`edr-potential-headroom`**: `1090519040` (`0x41000000`)
- **`edr-reference-headroom`**: `1094713344` (`0x41400000`)
- **`edr-seconds-per-stop`**: `1036831949` (`0x3dcccccd`)
- **`energy-consumption-target`**: 12 bytes
  - u32: `0x49371b00 0x49371b00 0x495bba00`
  ```
  000000  00 1b 37 49 00 1b 37 49 00 ba 5b 49              ..7I..7I..[I
  ```
- **`gcp-supported`**: `1` (`0x1`)
- **`grimaldi-sampling-strategy`**: `1` (`0x1`)
- **`gs-b-min`**: `1063675494` (`0x3f666666`) (four-char code `?fff`)
- **`gs-i-nominal`**: `1059648963` (`0x3f28f5c3`)
- **`gs-i-threshold`**: `1065604874` (`0x3f83d70a`)
- **`gs-pab-index`**: `279` (`0x117`)
- **`gs-slope`**: `1056964608` (`0x3f000000`)
- **`max-aurora-gain`**: 12 bytes
  - u32: `0x40200000 0x40351eb8 0x40351eb8`
  ```
  000000  00 00 20 40 b8 1e 35 40 b8 1e 35 40              .. @..5@..5@
  ```
- **`name`**: `brightness-secondary-doe1`
- **`paa-sdr-lut`**: 12 bytes
  - u32: `0x44548000 0x447a0000 0x44848000`
  ```
  000000  00 80 54 44 00 00 7a 44 00 80 84 44              ..TD..zD...D
  ```
- **`pcc-table`**: `3` (`0x3`)
- **`plt-logic-version`**: `2` (`0x2`)
- **`ramp-down-max-tap-point`**: 12 bytes
  - u32: `0x3ecccccd 0x3ecccccd 0x3ecccccd`
  ```
  000000  cd cc cc 3e cd cc cc 3e cd cc cc 3e              ...>...>...>
  ```
- **`ramp-down-min-tap-point`**: 12 bytes
  - u32: `0x3e4ccccd 0x3e4ccccd 0x3e4ccccd`
  ```
  000000  cd cc 4c 3e cd cc 4c 3e cd cc 4c 3e              ..L>..L>..L>
  ```
- **`ramp-up-max-tap-point`**: 12 bytes
  - u32: `0x3eb33333 0x3eb33333 0x3eb33333`
  ```
  000000  33 33 b3 3e 33 33 b3 3e 33 33 b3 3e              33.>33.>33.>
  ```
- **`ramp-up-min-tap-point`**: 12 bytes
  - u32: `0x3e3851ec 0x3e3851ec 0x3e3851ec`
  ```
  000000  ec 51 38 3e ec 51 38 3e ec 51 38 3e              .Q8>.Q8>.Q8>
  ```
- **`ring-light-supported`**: `1` (`0x1`)
- **`rtplc-apce-table`**: 16 bytes
  - u32: `0x0 0x3f19999a 0x3f666666 0x3f800000`
  - text inside: `?fff?`
  ```
  000000  00 00 00 00 9a 99 19 3f 66 66 66 3f 00 00 80 3f  .......?fff?...?
  ```
- **`rtplc-nits-table`**: 16 bytes
  - u32: `0x44c80000 0x44c80000 0x44960000 0x44960000`
  ```
  000000  00 00 c8 44 00 00 c8 44 00 00 96 44 00 00 96 44  ...D...D...D...D
  ```
- **`rtplc-supported`**: `1` (`0x1`)
- **`slider-mapping`**: 404 bytes
  - u32: `0x3f800000 0x3f8a3d71 0x3f95c28f 0x3fa147ae 0x3faccccd 0x3fb9999a 0x3fc66666 0x3fd33333 0x3fe147ae 0x3ff0a3d7 0x3ffeb852 0x4007ae14 0x4010a3d7 0x401ccccd 0x402d70a4 0x40428f5c 0x405eb852 0x4081999a 0x4098f5c3 0x40b851ec 0x40e3d70a 0x410eb852 0x4132b852 0x415d47ae 0x41870a3d 0x41a23d71 0x41c0147b 0x41e03d71 0x42015c29 0x4213999a 0x4226cccd 0x423ae148 0x424fb852 0x42653d71 0x427b6666 0x4289051f 0x42948f5c 0x42a047ae 0x42ac23d7 0x42b8147b 0x42c40f5c 0x42d00f5c 0x42dc051f 0x42e7e148 0x42f3a3d7 0x42ff3852 0x43054a3d 0x430ad99a 0x4310451f 0x4315828f 0x431b0000 0x432e1c29 0x4341f5c3 0x4356947b 0x436c028f 0x4381251f 0x438cb70a 0x4398beb8 0x43a5428f 0x43b23c29 0x43bfbc29 0x43cdc7ae 0x43dc599a 0x43eb8148 0x43fb4000 0x4405ceb8 0x440e4ccd 0x4417228f 0x442051ec 0x4429dccd 0x4433c666 0x443e13d7 0x4448c99a 0x4453eae1 0x445f7a3d 0x446b7eb8 0x4477fc29 0x44827ae1 0x448938f6 0x44903a8f 0x44978385 0x449f1429 0x44a6f1ec 0x44af1dc3 0x44b79c29 0x44c06fae 0x44c99bd7 0x44d32333 0x44dd0b33 0x44e755c3 0x44f20800 0x44fd2614 0x450459c3 0x450a5a66 0x45109733 0x451712b8 0x451dcee1 0x4524cf0a 0x452c1571 0x4533a47b 0x453b8000`
  - text inside: `p-@\`, `G]A=`, `OBq=eBff{B`, `SD=z_D`, `~kD)`
  ```
  000000  00 00 80 3f 71 3d 8a 3f 8f c2 95 3f ae 47 a1 3f  ...?q=.?...?.G.?
  000010  cd cc ac 3f 9a 99 b9 3f 66 66 c6 3f 33 33 d3 3f  ...?...?ff.?33.?
  000020  ae 47 e1 3f d7 a3 f0 3f 52 b8 fe 3f 14 ae 07 40  .G.?...?R..?...@
  000030  d7 a3 10 40 cd cc 1c 40 a4 70 2d 40 5c 8f 42 40  ...@...@.p-@\.B@
  000040  52 b8 5e 40 9a 99 81 40 c3 f5 98 40 ec 51 b8 40  R.^@...@...@.Q.@
  000050  0a d7 e3 40 52 b8 0e 41 52 b8 32 41 ae 47 5d 41  ...@R..AR.2A.G]A
  000060  3d 0a 87 41 71 3d a2 41 7b 14 c0 41 71 3d e0 41  =..Aq=.A{..Aq=.A
  000070  29 5c 01 42 9a 99 13 42 cd cc 26 42 48 e1 3a 42  )\.B...B..&BH.:B
  000080  52 b8 4f 42 71 3d 65 42 66 66 7b 42 1f 05 89 42  R.OBq=eBff{B...B
  000090  5c 8f 94 42 ae 47 a0 42 d7 23 ac 42 7b 14 b8 42  \..B.G.B.#.B{..B
  0000a0  5c 0f c4 42 5c 0f d0 42 1f 05 dc 42 48 e1 e7 42  \..B\..B...BH..B
  0000b0  d7 a3 f3 42 52 38 ff 42 3d 4a 05 43 9a d9 0a 43  ...BR8.B=J.C...C
  0000c0  1f 45 10 43 8f 82 15 43 00 00 1b 43 29 1c 2e 43  .E.C...C...C)..C
  0000d0  c3 f5 41 43 7b 94 56 43 8f 02 6c 43 1f 25 81 43  ..AC{.VC..lC.%.C
  0000e0  0a b7 8c 43 b8 be 98 43 8f 42 a5 43 29 3c b2 43  ...C...C.B.C)<.C
  0000f0  29 bc bf 43 ae c7 cd 43 9a 59 dc 43 48 81 eb 43  )..C...C.Y.CH..C
  000100  00 40 fb 43 b8 ce 05 44 cd 4c 0e 44 8f 22 17 44  .@.C...D.L.D.".D
  000110  ec 51 20 44 cd dc 29 44 66 c6 33 44 d7 13 3e 44  .Q D..)Df.3D..>D
  000120  9a c9 48 44 e1 ea 53 44 3d 7a 5f 44 b8 7e 6b 44  ..HD..SD=z_D.~kD
  000130  29 fc 77 44 e1 7a 82 44 f6 38 89 44 8f 3a 90 44  ).wD.z.D.8.D.:.D
  000140  85 83 97 44 29 14 9f 44 ec f1 a6 44 c3 1d af 44  ...D)..D...D...D
  000150  29 9c b7 44 ae 6f c0 44 d7 9b c9 44 33 23 d3 44  )..D.o.D...D3#.D
  000160  33 0b dd 44 c3 55 e7 44 00 08 f2 44 14 26 fd 44  3..D.U.D...D.&.D
  000170  c3 59 04 45 66 5a 0a 45 33 97 10 45 b8 12 17 45  .Y.EfZ.E3..E...E
  000180  e1 ce 1d 45 0a cf 24 45 71 15 2c 45 7b a4 33 45  ...E..$Eq.,E{.3E
  000190  00 80 3b 45                                      ..;E
  ```
- **`supports-ammolite`**: `1` (`0x1`)
- **`supports-cltm-aware-aurora`**: `1` (`0x1`)
- **`supports-twilight`**: `1` (`0x1`)
- **`truetone-strength`**: 24 bytes
  - u32: `0x0 0x3e8a3d71 0x3e8a3d71 0x3e4ccccd 0x3e4ccccd 0x3e4ccccd`
  ```
  000000  00 00 00 00 71 3d 8a 3e 71 3d 8a 3e cd cc 4c 3e  ....q=.>q=.>..L>
  000010  cd cc 4c 3e cd cc 4c 3e                          ..L>..L>
  ```
- **`tw-lux-activation-threshold`**: `1120403443` (`0x42c7fff3`)
- **`tw-lux-table`**: 36 bytes
  - u32: `0x0 0x41200000 0x41a00000 0x41f00000 0x42200000 0x425c0000 0x428c0000 0x42aa0000 0x42c7fff3`
  ```
  000000  00 00 00 00 00 00 20 41 00 00 a0 41 00 00 f0 41  ...... A...A...A
  000010  00 00 20 42 00 00 5c 42 00 00 8c 42 00 00 aa 42  .. B..\B...B...B
  000020  f3 ff c7 42                                      ...B
  ```
- **`tw-nits-activation-threshold`**: `1092616192` (`0x41200000`)
- **`tw-nits-table`**: 40 bytes
  - u32: `0x3f800000 0x40000000 0x40400000 0x40800000 0x40a00000 0x40c00000 0x40e00000 0x41000000 0x41100000 0x41200000`
  ```
  000000  00 00 80 3f 00 00 00 40 00 00 40 40 00 00 80 40  ...?...@..@@...@
  000010  00 00 a0 40 00 00 c0 40 00 00 e0 40 00 00 00 41  ...@...@...@...A
  000020  00 00 10 41 00 00 20 41                          ...A.. A
  ```
- **`tw-ramp-aod-duration`**: `1073741824` (`0x40000000`)
- **`tw-ramp-bezier-anchors`**: 12 bytes
  - u32: `0x3e99999a 0x3f666666 0x3f59999a`
  - text inside: `>fff?`
  ```
  000000  9a 99 99 3e 66 66 66 3f 9a 99 59 3f              ...>fff?..Y?
  ```
- **`tw-ramp-down-duration`**: `1084227584` (`0x40a00000`)
- **`tw-ramp-down-lux-threshold`**: `1099956224` (`0x41900000`)
- **`tw-ramp-up-duration`**: `1084227584` (`0x40a00000`)
- **`tw-ramp-up-lux-threshold`**: `1097859072` (`0x41700000`)
- **`tw-ramp-update-rate`**: `1114636288` (`0x42700000`)
- **`tw-strength-table`**: 360 bytes
  - u32: `0x3f400000 0x3f2aa64c 0x3f155326 0x3f000000 0x3ed559b4 0x3eaaa64c 0x3e7fe5c9 0x3e2a9931 0x3daa9931 0x0 0x3f400000 0x3f2aa64c 0x3f155326 0x3f000000 0x3ed559b4 0x3eaaa64c 0x3e7fe5c9 0x3e2a9931 0x3daa9931 0x0 0x3f400000 0x3f2aa64c 0x3f155326 0x3f000000 0x3ed559b4 0x3eaaa64c 0x3e7fe5c9 0x3e2a9931 0x3daa9931 0x0 0x3f400000 0x3f2aa64c 0x3f155326 0x3f000000 0x3ed559b4 0x3eaaa64c 0x3e7fe5c9 0x3e2a9931 0x3daa9931 0x0 0x3f248e8a 0x3f124745 0x3f000000 0x3edb645a 0x3eb6d5d0 0x3e91eb85 0x3e5b573f 0x3e123a2a 0x3d923a2a 0x0 0x3ef6d5d0 0x3edb645a 0x3ebd70a4 0x3ea48e8a 0x3e891d15 0x3e5b573f 0x3e248e8a 0x3ddb573f 0x3d5b8bac 0x0 0x3ea48e8a 0x3e91eb85 0x3e7fe5c9 0x3e5b573f 0x3e36c8b4 0x3e123a2a 0x3ddb573f 0x3d923a2a 0x3d123a2a 0x0 0x3e248e8a 0x3e123a2a 0x3e000000 0x3ddb573f 0x3db645a2 0x3d923a2a 0x3d5b8bac 0x3d123a2a 0x3c92a305 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0`
  - text inside: `*?&S`, `*?&S`, `*?&S`, `*?&S`, `$?EG`, `>?W[>*:`, `>?W[>`, `$>?W`, `>?W[>`, `6>*:`, `$>*:`, `[=*:`
  ```
  000000  00 00 40 3f 4c a6 2a 3f 26 53 15 3f 00 00 00 3f  ..@?L.*?&S.?...?
  000010  b4 59 d5 3e 4c a6 aa 3e c9 e5 7f 3e 31 99 2a 3e  .Y.>L..>...>1.*>
  000020  31 99 aa 3d 00 00 00 00 00 00 40 3f 4c a6 2a 3f  1..=......@?L.*?
  000030  26 53 15 3f 00 00 00 3f b4 59 d5 3e 4c a6 aa 3e  &S.?...?.Y.>L..>
  000040  c9 e5 7f 3e 31 99 2a 3e 31 99 aa 3d 00 00 00 00  ...>1.*>1..=....
  000050  00 00 40 3f 4c a6 2a 3f 26 53 15 3f 00 00 00 3f  ..@?L.*?&S.?...?
  000060  b4 59 d5 3e 4c a6 aa 3e c9 e5 7f 3e 31 99 2a 3e  .Y.>L..>...>1.*>
  000070  31 99 aa 3d 00 00 00 00 00 00 40 3f 4c a6 2a 3f  1..=......@?L.*?
  000080  26 53 15 3f 00 00 00 3f b4 59 d5 3e 4c a6 aa 3e  &S.?...?.Y.>L..>
  000090  c9 e5 7f 3e 31 99 2a 3e 31 99 aa 3d 00 00 00 00  ...>1.*>1..=....
  0000a0  8a 8e 24 3f 45 47 12 3f 00 00 00 3f 5a 64 db 3e  ..$?EG.?...?Zd.>
  0000b0  d0 d5 b6 3e 85 eb 91 3e 3f 57 5b 3e 2a 3a 12 3e  ...>...>?W[>*:.>
  0000c0  2a 3a 92 3d 00 00 00 00 d0 d5 f6 3e 5a 64 db 3e  *:.=.......>Zd.>
  0000d0  a4 70 bd 3e 8a 8e a4 3e 15 1d 89 3e 3f 57 5b 3e  .p.>...>...>?W[>
  0000e0  8a 8e 24 3e 3f 57 db 3d ac 8b 5b 3d 00 00 00 00  ..$>?W.=..[=....
  0000f0  8a 8e a4 3e 85 eb 91 3e c9 e5 7f 3e 3f 57 5b 3e  ...>...>...>?W[>
  000100  b4 c8 36 3e 2a 3a 12 3e 3f 57 db 3d 2a 3a 92 3d  ..6>*:.>?W.=*:.=
  000110  2a 3a 12 3d 00 00 00 00 8a 8e 24 3e 2a 3a 12 3e  *:.=......$>*:.>
  000120  00 00 00 3e 3f 57 db 3d a2 45 b6 3d 2a 3a 92 3d  ...>?W.=.E.=*:.=
  000130  ac 8b 5b 3d 2a 3a 12 3d 05 a3 92 3c 00 00 00 00  ..[=*:.=...<....
  000140  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000150  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000160  00 00 00 00 00 00 00 00                          ........
  ```
- **`tw-supported`**: `1` (`0x1`)
- **`use-modern-cpms`**: `1` (`0x1`)
- **`user-accessible-max-nits`**: `69468160` (`0x4240000`)

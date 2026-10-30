# `/core-brightness/brightness-secondary`

- Name: `brightness-secondary`
- Parent: [`/core-brightness`](root__core-brightness.md)
- phandle: `458`
- device_type: `brightness-control`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (85) [DT]

- **`AAPL,phandle`**: `458` (`0x1ca`) → phandle of [`/core-brightness/brightness-secondary`](root__core-brightness__brightness-secondary.md)
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
- **`aml-lux-activation-threshold`**: `1167867904` (`0x459c4000`)
- **`aml-lux-table`**: 48 bytes
  - u32: `0x459c4000 0x461c4000 0x466a6000 0x46c35000 0x4708b800 0x472fc800 0x4756d800 0x477de800 0x479c4000 0x47b98c00 0x47d6d800 0x48127c00`
  ```
  000000  00 40 9c 45 00 40 1c 46 00 60 6a 46 00 50 c3 46  .@.E.@.F.`jF.P.F
  000010  00 b8 08 47 00 c8 2f 47 00 d8 56 47 00 e8 7d 47  ...G../G..VG..}G
  000020  00 40 9c 47 00 8c b9 47 00 d8 d6 47 00 7c 12 48  .@.G...G...G.|.H
  ```
- **`aml-nits-activation-threshold`**: `1120403456` (`0x42c80000`)
- **`aml-nits-table`**: 44 bytes
  - u32: `0x42c80000 0x43960000 0x43fa0000 0x442f0000 0x44610000 0x44898000 0x44a28000 0x44bb8000 0x44d48000 0x44ed8000 0x4507f000`
  ```
  000000  00 00 c8 42 00 00 96 43 00 00 fa 43 00 00 2f 44  ...B...C...C../D
  000010  00 00 61 44 00 80 89 44 00 80 a2 44 00 80 bb 44  ..aD...D...D...D
  000020  00 80 d4 44 00 80 ed 44 00 f0 07 45              ...D...D...E
  ```
- **`aml-ramp-aod-duration`**: `1073741824` (`0x40000000`)
- **`aml-ramp-bezier-anchors`**: 12 bytes
  - u32: `0x3e99999a 0x3f666666 0x3f59999a`
  - text inside: `>fff?`
  ```
  000000  9a 99 99 3e 66 66 66 3f 9a 99 59 3f              ...>fff?..Y?
  ```
- **`aml-ramp-down-duration`**: `1084227584` (`0x40a00000`)
- **`aml-ramp-down-lux-threshold`**: `1165623296` (`0x457a0000`)
- **`aml-ramp-up-duration`**: `1084227584` (`0x40a00000`)
- **`aml-ramp-up-lux-threshold`**: `1165623296` (`0x457a0000`)
- **`aml-ramp-update-rate`**: `1114636288` (`0x42700000`)
- **`aml-strength-table`**: 528 bytes
  - text inside: `S=%@`, `0>8g`, `X9>,e`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000030  18 3f 0d 3c e7 3a 8d 3c 5a d8 d3 3c e7 3a 0d 3d  .?.<.:.<Z..<.:.=
  000040  e7 3a 0d 3d e7 3a 0d 3d e7 3a 0d 3d e7 3a 0d 3d  .:.=.:.=.:.=.:.=
  000050  e7 3a 0d 3d e7 3a 0d 3d 00 00 00 00 e7 3a 8d 3c  .:.=.:.=.....:.<
  000060  e7 3a 0d 3d 5a d8 53 3d 25 40 8d 3d 25 40 8d 3d  .:.=Z.S=%@.=%@.=
  000070  25 40 8d 3d 25 40 8d 3d 25 40 8d 3d 25 40 8d 3d  %@.=%@.=%@.=%@.=
  000080  25 40 8d 3d 00 00 00 00 e7 3a 0d 3d 25 40 8d 3d  %@.=.....:.=%@.=
  000090  61 c3 d3 3d a8 35 0d 3e a8 35 0d 3e a8 35 0d 3e  a..=.5.>.5.>.5.>
  0000a0  a8 35 0d 3e a8 35 0d 3e a8 35 0d 3e a8 35 0d 3e  .5.>.5.>.5.>.5.>
  0000b0  00 00 00 00 5a d8 53 3d 61 c3 d3 3d c0 ec 1e 3e  ....Z.S=a..=...>
  0000c0  98 dd 53 3e 98 dd 53 3e 98 dd 53 3e 98 dd 53 3e  ..S>..S>..S>..S>
  0000d0  98 dd 53 3e 98 dd 53 3e 98 dd 53 3e 00 00 00 00  ..S>..S>..S>....
  0000e0  25 40 8d 3d a8 35 0d 3e 98 dd 53 3e c4 42 8d 3e  %@.=.5.>..S>.B.>
  0000f0  c4 42 8d 3e c4 42 8d 3e c4 42 8d 3e c4 42 8d 3e  .B.>.B.>.B.>.B.>
  000100  c4 42 8d 3e c4 42 8d 3e 00 00 00 00 de 8e b0 3d  .B.>.B.>.......=
  000110  a0 89 30 3e 38 67 84 3e a0 89 b0 3e a0 89 b0 3e  ..0>8g.>...>...>
  000120  a0 89 b0 3e a0 89 b0 3e a0 89 b0 3e a0 89 b0 3e  ...>...>...>...>
  000130  a0 89 b0 3e 00 00 00 00 61 c3 d3 3d 98 dd 53 3e  ...>....a..=..S>
  000140  a4 df 9e 3e 98 dd d3 3e 98 dd d3 3e 98 dd d3 3e  ...>...>...>...>
  000150  98 dd d3 3e 98 dd d3 3e 98 dd d3 3e 98 dd d3 3e  ...>...>...>...>
  000160  00 00 00 00 38 67 04 3e 38 67 84 3e d4 9a c6 3e  ....8g.>8g.>...>
  000170  38 67 04 3f 38 67 04 3f 38 67 04 3f 38 67 04 3f  8g.?8g.?8g.?8g.?
  000180  38 67 04 3f 38 67 04 3f 38 67 04 3f 00 00 00 00  8g.?8g.?8g.?....
  000190  c0 ec 1e 3e a4 df 9e 3e 04 56 ee 3e 32 e6 1e 3f  ...>...>.V.>2..?
  0001a0  32 e6 1e 3f 32 e6 1e 3f 32 e6 1e 3f 32 e6 1e 3f  2..?2..?2..?2..?
  0001b0  32 e6 1e 3f 32 e6 1e 3f 00 00 00 00 10 58 39 3e  2..?2..?.....X9>
  0001c0  2c 65 b9 3e 9a 08 0b 3f 9e 5e 39 3f 9e 5e 39 3f  ,e.>...?.^9?.^9?
  0001d0  9e 5e 39 3f 9e 5e 39 3f 9e 5e 39 3f 9e 5e 39 3f  .^9?.^9?.^9?.^9?
  0001e0  9e 5e 39 3f 00 00 00 00 00 00 80 3e 00 00 00 3f  .^9?.......>...?
  0001f0  00 00 40 3f 00 00 80 3f 00 00 80 3f 00 00 80 3f  ..@?...?...?...?
  000200  00 00 80 3f 00 00 80 3f 00 00 80 3f 00 00 80 3f  ...?...?...?...?
  ```
- **`aml-supported`**: `1` (`0x1`)
- **`aurora-ramp-down-tap-points`**: `0x3ecccccd3e4ccccd` (u64; as two u32: `0x3e4ccccd`, `0x3ecccccd`)
- **`aurora-ramp-up-speed`**: `1073741824` (`0x40000000`)
- **`aurora-ramp-up-tap-points`**: `0x3eb333333e3851ec` (u64; as two u32: `0x3e3851ec`, `0x3eb33333`)
- **`aurora-saturation-lux`**: 12 bytes
  - u32: `0x46bb8000 0x46bb8000 0x46bb8000`
  ```
  000000  00 80 bb 46 00 80 bb 46 00 80 bb 46              ...F...F...F
  ```
- **`aurora-session-limit`**: `1133903872` (`0x43960000`)
- **`aurora-supported`**: `1` (`0x1`)
- **`bdm-nits1`**: `1146388480` (`0x44548000`)
- **`bdm-nits2`**: `1153957888` (`0x44c80000`)
- **`bdm-supported`**: `1` (`0x1`)
- **`blr-cct-warning`**: `2700` (`0xa8c`)
- **`dcp-brightness-node`**: `DCPSEC`
- **`device_type`**: `brightness-control`
- **`display-id`**: `1` (`0x1`)
- **`ds-max-factor-aab-off`**: `1062031327` (`0x3f4d4fdf`)
- **`ds-max-factors`**: 24 bytes
  - u32: `0x3e75c28f 0x3f051eb8 0x3f051eb8 0x3f051eb8 0x3f23d70a 0x3f800000`
  ```
  000000  8f c2 75 3e b8 1e 05 3f b8 1e 05 3f b8 1e 05 3f  ..u>...?...?...?
  000010  0a d7 23 3f 00 00 80 3f                          ..#?...?
  ```
- **`ds-max-fall-time`**: `1092616192` (`0x41200000`)
- **`ds-max-pivot`**: `1106247680` (`0x41f00000`)
- **`ds-max-rise-time`**: `1084227584` (`0x40a00000`)
- **`ds-max-rise-time-fast`**: `1077936128` (`0x40400000`)
- **`ds-max-rise-time-fast-thr`**: `1065017672` (`0x3f7ae148`)
- **`ds-max-thresholds`**: 24 bytes
  - u32: `0x3f800000 0x41f00000 0x44160000 0x447a0000 0x459c4000 0x45fc8000`
  ```
  000000  00 00 80 3f 00 00 f0 41 00 00 16 44 00 00 7a 44  ...?...A...D..zD
  000010  00 40 9c 45 00 80 fc 45                          .@.E...E
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
- **`gcp-supported`**: `1` (`0x1`)
- **`grimaldi-sampling-strategy`**: `1` (`0x1`)
- **`gs-b-min`**: `1063675494` (`0x3f666666`) (four-char code `?fff`)
- **`gs-i-nominal`**: `1059648963` (`0x3f28f5c3`)
- **`gs-i-threshold`**: `1065604874` (`0x3f83d70a`)
- **`gs-pab-index`**: `279` (`0x117`)
- **`gs-slope`**: `1056964608` (`0x3f000000`)
- **`name`**: `brightness-secondary`
- **`pcc-table`**: `3` (`0x3`)
- **`plt-logic-version`**: `2` (`0x2`)
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
  - u32: `0x3f800000 0x3f8a3d71 0x3f95c28f 0x3fa147ae 0x3faccccd 0x3fb9999a 0x3fc66666 0x3fd33333 0x3fe147ae 0x3ff0a3d7 0x3ffeb852 0x4007ae14 0x4010a3d7 0x401ccccd 0x402d70a4 0x40428f5c 0x405eb852 0x4081999a 0x4098f5c3 0x40b851ec 0x40e3d70a 0x410eb852 0x4132b852 0x415d47ae 0x41870a3d 0x41a23d71 0x41c0147b 0x41e03d71 0x42015c29 0x4213999a 0x4226cccd 0x423ae148 0x424fb852 0x42653d71 0x427b6666 0x4289051f 0x42948f5c 0x42a047ae 0x42ac23d7 0x42b8147b 0x42c40f5c 0x42d00f5c 0x42dc051f 0x42e7e148 0x42f3a3d7 0x42ff3852 0x43054a3d 0x430ad99a 0x4310451f 0x4315828f 0x431b0000 0x432891ec 0x4336a8f6 0x43454ccd 0x4354851f 0x4364570a 0x4374c51f 0x4382eccd 0x438bcf5c 0x43950666 0x439e9c29 0x43a8947b 0x43b2eccd 0x43bdaf5c 0x43c8dd71 0x43d47c29 0x43e08b85 0x43ed170a 0x43fa228f 0x4403d7ae 0x440ae148 0x441231ec 0x4419cccd 0x4421b3d7 0x4429e8f6 0x44327148 0x443b4f5c 0x444485c3 0x444e18f6 0x44580c29 0x4462647b 0x446d228f 0x44784e14 0x4481f429 0x4487fc29 0x448e4052 0x4494c385 0x449b87ae 0x44a29052 0x44a9deb8 0x44b1770a 0x44b95bd7 0x44c18fae 0x44ca15c3 0x44d2f148 0x44dc25c3 0x44e5b614 0x44efa70a 0x44f9fbd7 0x45025bd7 0x4507f000`
  - text inside: `p-@\`, `G]A=`, `OBq=eBff{B`, `)DHq2D\O;D`, `XD{dbD`, `NxD)`
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
  0000c0  1f 45 10 43 8f 82 15 43 00 00 1b 43 ec 91 28 43  .E.C...C...C..(C
  0000d0  f6 a8 36 43 cd 4c 45 43 1f 85 54 43 0a 57 64 43  ..6C.LEC..TC.WdC
  0000e0  1f c5 74 43 cd ec 82 43 5c cf 8b 43 66 06 95 43  ..tC...C\..Cf..C
  0000f0  29 9c 9e 43 7b 94 a8 43 cd ec b2 43 5c af bd 43  )..C{..C...C\..C
  000100  71 dd c8 43 29 7c d4 43 85 8b e0 43 0a 17 ed 43  q..C)|.C...C...C
  000110  8f 22 fa 43 ae d7 03 44 48 e1 0a 44 ec 31 12 44  .".C...DH..D.1.D
  000120  cd cc 19 44 d7 b3 21 44 f6 e8 29 44 48 71 32 44  ...D..!D..)DHq2D
  000130  5c 4f 3b 44 c3 85 44 44 f6 18 4e 44 29 0c 58 44  \O;D..DD..ND).XD
  000140  7b 64 62 44 8f 22 6d 44 14 4e 78 44 29 f4 81 44  {dbD."mD.NxD)..D
  000150  29 fc 87 44 52 40 8e 44 85 c3 94 44 ae 87 9b 44  )..DR@.D...D...D
  000160  52 90 a2 44 b8 de a9 44 0a 77 b1 44 d7 5b b9 44  R..D...D.w.D.[.D
  000170  ae 8f c1 44 c3 15 ca 44 48 f1 d2 44 c3 25 dc 44  ...D...DH..D.%.D
  000180  14 b6 e5 44 0a a7 ef 44 d7 fb f9 44 d7 5b 02 45  ...D...D...D.[.E
  000190  00 f0 07 45                                      ...E
  ```
- **`supports-ammolite`**: `1` (`0x1`)
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

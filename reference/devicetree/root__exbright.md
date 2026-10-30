# `/exbright`

- Name: `exbright`
- Parent: [`/`](root.md)
- phandle: `460`
- Children (2): [`/exbright/contrast-indicator-0`](root__exbright__contrast-indicator-0.md), [`/exbright/contrast-indicator-1`](root__exbright__contrast-indicator-1.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `EXBrightKext` | `IOService` | [`com.apple.EXBrightKext`](../kexts/com.apple.EXBrightKext.md) | `exbright` |

## All properties (24) [DT]

- **`AAPL,phandle`**: `460` (`0x1cc`) → phandle of [`/exbright`](root__exbright.md)
- **`DBVMax`**: `2047` (`0x7ff`)
- **`DBVMin`**: `117` (`0x75`)
- **`LmaxProduct`**: `196608000` (`0xbb80000`)
- **`LminProduct`**: `655360` (`0xa0000`)
- **`als-new-calibration-path`**: `1` (`0x1`)
- **`als-types`**: 12 bytes
  - u32: `0x9 0x9 0x9`
  ```
  000000  09 00 00 00 09 00 00 00 09 00 00 00              ............
  ```
- **`calibration-source`**: `1` (`0x1`)
- **`dcp-types`**: `0x100000000` (u64; as two u32: `0x0`, `0x1`)
- **`exclave-assigned`**: (present, empty)
- **`exclave-edk-service`**: `com.apple.service.EXBrightCore_EDK`
- **`exclave-service`**: `com.apple.service.EXBrightCore`
- **`fdr-class`**: `1` (`0x1`)
- **`formula-max-nits`**: `212992000` (`0xcb20000`)
- **`mib-curve-lux`**: 124 bytes
  - u32: `0x0 0x1 0x2 0x5 0xa 0x14 0x1e 0x28 0x32 0x64 0xc8 0x12c 0x190 0x1f4 0x258 0x2bc 0x320 0x384 0x3e8 0x9c4 0xbb8 0xdac 0xfa0 0x1194 0x1388 0x1900 0x1f90 0x4e20 0x9c40 0xfde8 0x186a0`
  ```
  000000  00 00 00 00 01 00 00 00 02 00 00 00 05 00 00 00  ................
  000010  0a 00 00 00 14 00 00 00 1e 00 00 00 28 00 00 00  ............(...
  000020  32 00 00 00 64 00 00 00 c8 00 00 00 2c 01 00 00  2...d.......,...
  000030  90 01 00 00 f4 01 00 00 58 02 00 00 bc 02 00 00  ........X.......
  000040  20 03 00 00 84 03 00 00 e8 03 00 00 c4 09 00 00   ...............
  000050  b8 0b 00 00 ac 0d 00 00 a0 0f 00 00 94 11 00 00  ................
  000060  88 13 00 00 00 19 00 00 90 1f 00 00 20 4e 00 00  ............ N..
  000070  40 9c 00 00 e8 fd 00 00 a0 86 01 00              @...........
  ```
- **`mib-curve-lux-1`**: 124 bytes
  - u32: `0x0 0x1 0x2 0x5 0xa 0x14 0x1e 0x28 0x32 0x64 0xc8 0x12c 0x190 0x1f4 0x258 0x2bc 0x320 0x384 0x3e8 0x9c4 0xbb8 0xdac 0xfa0 0x1194 0x1388 0x1900 0x1f90 0x4e20 0x9c40 0xfde8 0x186a0`
  ```
  000000  00 00 00 00 01 00 00 00 02 00 00 00 05 00 00 00  ................
  000010  0a 00 00 00 14 00 00 00 1e 00 00 00 28 00 00 00  ............(...
  000020  32 00 00 00 64 00 00 00 c8 00 00 00 2c 01 00 00  2...d.......,...
  000030  90 01 00 00 f4 01 00 00 58 02 00 00 bc 02 00 00  ........X.......
  000040  20 03 00 00 84 03 00 00 e8 03 00 00 c4 09 00 00   ...............
  000050  b8 0b 00 00 ac 0d 00 00 a0 0f 00 00 94 11 00 00  ................
  000060  88 13 00 00 00 19 00 00 90 1f 00 00 20 4e 00 00  ............ N..
  000070  40 9c 00 00 e8 fd 00 00 a0 86 01 00              @...........
  ```
- **`mib-curve-nits`**: 124 bytes
  - u32: `0x2851e 0x2851e 0x32666 0x49eb8 0x6b851 0xa147a 0xc9999 0xff5c2 0x150000 0x1d6666 0x219999 0x25cccc 0x2a0000 0x2c1999 0x2e3333 0x304ccc 0x3123d7 0x318f5c 0x326666 0x433333 0x476666 0x4fcccc 0x540000 0x583333 0x5a4ccc 0x5c6666 0x609999 0x8ecccc 0xd20000 0x1260000 0x1a40000`
  ```
  000000  1e 85 02 00 1e 85 02 00 66 26 03 00 b8 9e 04 00  ........f&......
  000010  51 b8 06 00 7a 14 0a 00 99 99 0c 00 c2 f5 0f 00  Q...z...........
  000020  00 00 15 00 66 66 1d 00 99 99 21 00 cc cc 25 00  ....ff....!...%.
  000030  00 00 2a 00 99 19 2c 00 33 33 2e 00 cc 4c 30 00  ..*...,.33...L0.
  000040  d7 23 31 00 5c 8f 31 00 66 66 32 00 33 33 43 00  .#1.\.1.ff2.33C.
  000050  66 66 47 00 cc cc 4f 00 00 00 54 00 33 33 58 00  ffG...O...T.33X.
  000060  cc 4c 5a 00 66 66 5c 00 99 99 60 00 cc cc 8e 00  .LZ.ff\...`.....
  000070  00 00 d2 00 00 00 26 01 00 00 a4 01              ......&.....
  ```
- **`mib-curve-nits-1`**: 124 bytes
  - u32: `0x2a666 0x2a666 0x351eb 0x4deb8 0x70f5c 0xa947a 0xd3ae1 0x10c28f 0x16170a 0x1ee8f5 0x235c28 0x27d1eb 0x2c451e 0x2e8a3d 0x30c28f 0x3307ae 0x33f333 0x346b85 0x35570a 0x479c28 0x4c3ae1 0x55428f 0x59e147 0x5e8000 0x60f0a3 0x63b5c2 0x68d47a 0x9e570a 0xed4ccc 0x1500000 0x1e30000`
  ```
  000000  66 a6 02 00 66 a6 02 00 eb 51 03 00 b8 de 04 00  f...f....Q......
  000010  5c 0f 07 00 7a 94 0a 00 e1 3a 0d 00 8f c2 10 00  \...z....:......
  000020  0a 17 16 00 f5 e8 1e 00 28 5c 23 00 eb d1 27 00  ........(\#...'.
  000030  1e 45 2c 00 3d 8a 2e 00 8f c2 30 00 ae 07 33 00  .E,.=.....0...3.
  000040  33 f3 33 00 85 6b 34 00 0a 57 35 00 28 9c 47 00  3.3..k4..W5.(.G.
  000050  e1 3a 4c 00 8f 42 55 00 47 e1 59 00 00 80 5e 00  .:L..BU.G.Y...^.
  000060  a3 f0 60 00 c2 b5 63 00 7a d4 68 00 0a 57 9e 00  ..`...c.z.h..W..
  000070  cc 4c ed 00 00 00 50 01 00 00 e3 01              .L....P.....
  ```
- **`mib-nits-scaling-factor`**: `27525` (`0x6b85`)
- **`mib-nits-scaling-factor-1`**: `27525` (`0x6b85`)
- **`name`**: `exbright`
- **`panel-gamma`**: `2200` (`0x898`)
- **`panel-typical-freq`**: `120` (`0x78`)
- **`user-accessible-max-nits`**: `69468160` (`0x4240000`)

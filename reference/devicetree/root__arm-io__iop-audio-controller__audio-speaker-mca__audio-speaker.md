# `/arm-io/iop-audio-controller/audio-speaker-mca/audio-speaker`

- Name: `audio-speaker`
- Parent: [`/arm-io/iop-audio-controller/audio-speaker-mca`](root__arm-io__iop-audio-controller__audio-speaker-mca.md)
- phandle: `369`
- compatible: `audio-data,cs35l28`
- device_type: `audio-data`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x5211 0x1100c 0xb71b00 0x100fa 0x10030 0x3 0xfff 0x10100c02 0x10100100` | | |

## All properties (6) [DT]

- **`AAPL,phandle`**: `369` (`0x171`) → phandle of [`/arm-io/iop-audio-controller/audio-speaker-mca/audio-speaker`](root__arm-io__iop-audio-controller__audio-speaker-mca__audio-speaker.md)
- **`compatible`**: `audio-data,cs35l28`
- **`device_type`**: `audio-data`
- **`isolated-audio-service-output`**: `406` (`0x196`)
- **`name`**: `audio-speaker`
- **`reg`**: 36 bytes
  - u32: `0x5211 0x1100c 0xb71b00 0x100fa 0x10030 0x3 0xfff 0x10100c02 0x10100100`
  ```
  000000  11 52 00 00 0c 10 01 00 00 1b b7 00 fa 00 01 00  .R..............
  000010  30 00 01 00 03 00 00 00 ff 0f 00 00 02 0c 10 10  0...............
  000020  00 01 10 10                                      ....
  ```

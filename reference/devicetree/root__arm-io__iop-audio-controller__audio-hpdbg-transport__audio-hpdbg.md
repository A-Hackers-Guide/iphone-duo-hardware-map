# `/arm-io/iop-audio-controller/audio-hpdbg-transport/audio-hpdbg`

- Name: `audio-hpdbg`
- Parent: [`/arm-io/iop-audio-controller/audio-hpdbg-transport`](root__arm-io__iop-audio-controller__audio-hpdbg-transport.md)
- phandle: `379`
- compatible: `audio-data,audio-iop-hpdbg`
- device_type: `leap-audio-data`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1211 0x20008 0xbb8000 0x10100 0x10030 0x0 0xff 0x10100800 0x101` | | |

## All properties (6) [DT]

- **`AAPL,phandle`**: `379` (`0x17b`) → phandle of [`/arm-io/iop-audio-controller/audio-hpdbg-transport/audio-hpdbg`](root__arm-io__iop-audio-controller__audio-hpdbg-transport__audio-hpdbg.md)
- **`audio-stream-formatter`**: `1818583408` (`0x6c656170`) (four-char code `leap`)
- **`compatible`**: `audio-data,audio-iop-hpdbg`
- **`device_type`**: `leap-audio-data`
- **`name`**: `audio-hpdbg`
- **`reg`**: 36 bytes
  - u32: `0x1211 0x20008 0xbb8000 0x10100 0x10030 0x0 0xff 0x10100800 0x101`
  ```
  000000  11 12 00 00 08 00 02 00 00 80 bb 00 00 01 01 00  ................
  000010  30 00 01 00 00 00 00 00 ff 00 00 00 00 08 10 10  0...............
  000020  01 01 00 00                                      ....
  ```

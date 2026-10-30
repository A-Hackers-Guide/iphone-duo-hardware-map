# `/arm-io/iop-audio-controller/audio-hp/audio-codec`

- Name: `audio-codec`
- Parent: [`/arm-io/iop-audio-controller/audio-hp`](root__arm-io__iop-audio-controller__audio-hp.md)
- phandle: `352`
- compatible: `audio-data,cs42l79`
- device_type: `audio-data`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1210 0x11804 0xb71b00 0x100fa 0x10030 0x0 0xf 0x18000400 0x0` | | |

## All properties (9) [DT]

- **`AAPL,phandle`**: `352` (`0x160`) → phandle of [`/arm-io/iop-audio-controller/audio-hp/audio-codec`](root__arm-io__iop-audio-controller__audio-hp__audio-codec.md)
- **`compatible`**: `audio-data,cs42l79`
- **`data-sources`**: 27 bytes
  - text inside: `a2pa`, `HPMics`
  ```
  000000  61 32 70 61 08 00 01 00 01 00 01 00 00 00 00 00  a2pa............
  000010  80 bb 00 00 48 50 4d 69 63 73 00                 ....HPMics.
  ```
- **`device-name`**: `HPMic`
- **`device-uid`**: `HPMic`
- **`device_type`**: `audio-data`
- **`isolated-audio-service-input`**: `412` (`0x19c`)
- **`name`**: `audio-codec`
- **`reg`**: 36 bytes
  - u32: `0x1210 0x11804 0xb71b00 0x100fa 0x10030 0x0 0xf 0x18000400 0x0`
  ```
  000000  10 12 00 00 04 18 01 00 00 1b b7 00 fa 00 01 00  ................
  000010  30 00 01 00 00 00 00 00 0f 00 00 00 00 04 00 18  0...............
  000020  00 00 00 00                                      ....
  ```

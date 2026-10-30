# `/arm-io/iop-audio-controller/audio-haptic-transport/audio-haptic`

- Name: `audio-haptic`
- Parent: [`/arm-io/iop-audio-controller/audio-haptic-transport`](root__arm-io__iop-audio-controller__audio-haptic-transport.md)
- phandle: `375`
- compatible: `audio-data,audio-iop-haptics`
- device_type: `leap-audio-data`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4310 0x12001 0xb71b00 0x100fa 0x10030 0x1 0x0 0x200001 0x2` | | |

## Firmware with a matching name [FW]

- [`Firmware/V68_HapticAssets.im4p`](../firmware/Firmware__V68_HapticAssets.im4p.md) (1,174 B) Tag: IM4P  Type: hpas  Version: 1

## All properties (6) [DT]

- **`AAPL,phandle`**: `375` (`0x177`) → phandle of [`/arm-io/iop-audio-controller/audio-haptic-transport/audio-haptic`](root__arm-io__iop-audio-controller__audio-haptic-transport__audio-haptic.md)
- **`audio-stream-formatter`**: `1818583408` (`0x6c656170`) (four-char code `leap`)
- **`compatible`**: `audio-data,audio-iop-haptics`
- **`device_type`**: `leap-audio-data`
- **`name`**: `audio-haptic`
- **`reg`**: 36 bytes
  - u32: `0x4310 0x12001 0xb71b00 0x100fa 0x10030 0x1 0x0 0x200001 0x2`
  ```
  000000  10 43 00 00 01 20 01 00 00 1b b7 00 fa 00 01 00  .C... ..........
  000010  30 00 01 00 01 00 00 00 00 00 00 00 01 00 20 00  0............. .
  000020  02 00 00 00                                      ....
  ```

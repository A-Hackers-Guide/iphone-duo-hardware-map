# `/arm-io/iop-audio-controller/audio-speaker-tap/audio-speaker-tap`

- Name: `audio-speaker-tap`
- Parent: [`/arm-io/iop-audio-controller/audio-speaker-tap`](root__arm-io__iop-audio-controller__audio-speaker-tap.md)
- phandle: `371`
- compatible: `audio-data,external`
- device_type: `audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExternalSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,external` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1201 0x20002 0xb71b00 0x100fa 0x10030 0x0 0x3 0x10000200 0x10000201` | | |

## All properties (8) [DT]

- **`AAPL,phandle`**: `371` (`0x173`) → phandle of [`/arm-io/iop-audio-controller/audio-speaker-tap/audio-speaker-tap`](root__arm-io__iop-audio-controller__audio-speaker-tap__audio-speaker-tap.md)
- **`compatible`**: `audio-data,external`
- **`data-sources`**: 31 bytes
  - text inside: `a2pa`, `SpeakerTap`
  ```
  000000  61 32 70 61 02 00 00 00 00 00 01 00 00 00 00 00  a2pa............
  000010  80 bb 00 00 53 70 65 61 6b 65 72 54 61 70 00     ....SpeakerTap.
  ```
- **`device-name`**: `SpeakerTap`
- **`device-uid`**: `SpeakerTap`
- **`device_type`**: `audio-data`
- **`name`**: `audio-speaker-tap`
- **`reg`**: 36 bytes
  - u32: `0x1201 0x20002 0xb71b00 0x100fa 0x10030 0x0 0x3 0x10000200 0x10000201`
  ```
  000000  01 12 00 00 02 00 02 00 00 1b b7 00 fa 00 01 00  ................
  000010  30 00 01 00 00 00 00 00 03 00 00 00 00 02 00 10  0...............
  000020  01 02 00 10                                      ....
  ```

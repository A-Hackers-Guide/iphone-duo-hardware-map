# `/arm-io/iop-audio-controller/audio-flicker/audio-flicker`

- Name: `audio-flicker`
- Parent: [`/arm-io/iop-audio-controller/audio-flicker`](root__arm-io__iop-audio-controller__audio-flicker.md)
- phandle: `360`
- compatible: `audio-data,external`
- device_type: `audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExternalSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,external` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1300 0x11009 0xb71b00 0x100fa 0x10030 0x0 0x3 0x10000200 0x0` | | |

## Referenced by (1) [DT]

- [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md): function-Flicker_master `AUD1`

## All properties (9) [DT]

- **`AAPL,phandle`**: `360` (`0x168`) → phandle of [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md)
- **`compatible`**: `audio-data,external`
- **`data-sources`**: 28 bytes
  - u32: `0x61703266 0x40002 0x10002 0x0 0xbb80 0x63696c46 0x72656b`
  - text inside: `f2pa`, `Flicker`
  ```
  000000  66 32 70 61 02 00 04 00 02 00 01 00 00 00 00 00  f2pa............
  000010  80 bb 00 00 46 6c 69 63 6b 65 72 00              ....Flicker.
  ```
- **`device-name`**: `Flicker`
- **`device-uid`**: `Flicker`
- **`device_type`**: `audio-data`
- **`name`**: `audio-flicker`
- **`reg`**: 36 bytes
  - u32: `0x1300 0x11009 0xb71b00 0x100fa 0x10030 0x0 0x3 0x10000200 0x0`
  ```
  000000  00 13 00 00 09 10 01 00 00 1b b7 00 fa 00 01 00  ................
  000010  30 00 01 00 00 00 00 00 03 00 00 00 00 02 00 10  0...............
  000020  00 00 00 00                                      ....
  ```
- **`registerWithPrimary`**: (present, empty)

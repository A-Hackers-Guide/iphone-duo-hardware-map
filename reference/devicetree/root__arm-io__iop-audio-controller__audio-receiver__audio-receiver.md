# `/arm-io/iop-audio-controller/audio-receiver/audio-receiver`

- Name: `audio-receiver`
- Parent: [`/arm-io/iop-audio-controller/audio-receiver`](root__arm-io__iop-audio-controller__audio-receiver.md)
- phandle: `358`
- compatible: `audio-data,external`
- device_type: `audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExternalSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,external` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1210 0x11804 0xb71b00 0x100fa 0x10030 0x1 0x0 0x180001 0x0` | | |

## Referenced by (1) [DT]

- [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md): function-Receiver_master `AUD1`

## All properties (11) [DT]

- **`AAPL,phandle`**: `358` (`0x166`) → phandle of [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md)
- **`compatible`**: `audio-data,external`
- **`data-sources`**: 29 bytes
  - text inside: `r2pa`, `Receiver`
  ```
  000000  72 32 70 61 00 01 00 00 00 00 01 00 00 00 00 00  r2pa............
  000010  80 bb 00 00 52 65 63 65 69 76 65 72 00           ....Receiver.
  ```
- **`device-name`**: `Receiver`
- **`device-uid`**: `Receiver`
- **`device_type`**: `audio-data`
- **`isolated-audio-service-output`**: `407` (`0x197`)
- **`name`**: `audio-receiver`
- **`private`**: `1`
- **`reg`**: 36 bytes
  - u32: `0x1210 0x11804 0xb71b00 0x100fa 0x10030 0x1 0x0 0x180001 0x0`
  ```
  000000  10 12 00 00 04 18 01 00 00 1b b7 00 fa 00 01 00  ................
  000010  30 00 01 00 01 00 00 00 00 00 00 00 01 00 18 00  0...............
  000020  00 00 00 00                                      ....
  ```
- **`registerWithPrimary`**: (present, empty)

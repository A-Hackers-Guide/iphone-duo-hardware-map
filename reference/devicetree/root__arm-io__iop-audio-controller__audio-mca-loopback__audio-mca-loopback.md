# `/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`

- Name: `audio-mca-loopback`
- Parent: [`/arm-io/iop-audio-controller/audio-mca-loopback`](root__arm-io__iop-audio-controller__audio-mca-loopback.md)
- phandle: `356`
- compatible: `audio-data,audio-loopback`
- device_type: `audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,audio-loopback` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1201 0x11002 0xb71b00 0x100fa 0x10030 0x3 0x3 0x10100202 0x3` | | |

## All properties (8) [DT]

- **`AAPL,phandle`**: `356` (`0x164`) → phandle of [`/arm-io/iop-audio-controller/audio-mca-loopback/audio-mca-loopback`](root__arm-io__iop-audio-controller__audio-mca-loopback__audio-mca-loopback.md)
- **`compatible`**: `audio-data,audio-loopback`
- **`data-sources`**: 43 bytes
  - text inside: `c2pa`, `NonSecure MCA Loopback`
  ```
  000000  63 32 70 61 02 02 00 00 00 00 01 00 00 00 00 00  c2pa............
  000010  80 bb 00 00 4e 6f 6e 53 65 63 75 72 65 20 4d 43  ....NonSecure MC
  000020  41 20 4c 6f 6f 70 62 61 63 6b 00                 A Loopback.
  ```
- **`device-name`**: `NonSecure MCA Loopback`
- **`device-uid`**: `NonSecure MCA Loopback`
- **`device_type`**: `audio-data`
- **`name`**: `audio-mca-loopback`
- **`reg`**: 36 bytes
  - u32: `0x1201 0x11002 0xb71b00 0x100fa 0x10030 0x3 0x3 0x10100202 0x3`
  ```
  000000  01 12 00 00 02 10 01 00 00 1b b7 00 fa 00 01 00  ................
  000010  30 00 01 00 03 00 00 00 03 00 00 00 02 02 10 10  0...............
  000020  03 00 00 00                                      ....
  ```

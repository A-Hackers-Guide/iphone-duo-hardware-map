# `/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`

- Name: `audio-leap-internal-loopback`
- Parent: [`/arm-io/iop-audio-controller/audio-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-leap-internal-loopback.md)
- phandle: `354`
- compatible: `audio-data,external`
- device_type: `leap-audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExternalSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,external` |
| `AppleAOPAudioClientManager` | `AppleAOPAudioDeviceNode` | [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md) | `audio-leap-internal-loopback` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4201 0x11002 0xb71b00 0x100fa 0x10030 0x3 0x3 0x20200202 0x3` | | |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (9) [DT]

- **`AAPL,phandle`**: `354` (`0x162`) → phandle of [`/arm-io/iop-audio-controller/audio-leap-internal-loopback/audio-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-leap-internal-loopback__audio-leap-internal-loopback.md)
- **`audio-stream-formatter`**: `1818583408` (`0x6c656170`) (four-char code `leap`)
- **`compatible`**: `audio-data,external`
- **`data-sources`**: 48 bytes
  - u32: `0x61703261 0x40202 0x10002 0x0 0xbb80 0x536e6f4e 0x72756365 0x434d2065 0x454c2041 0x4c205041 0x62706f6f 0x6b6361`
  - text inside: `a2pa`, `NonSecure MCA LEAP Loopback`
  ```
  000000  61 32 70 61 02 02 04 00 02 00 01 00 00 00 00 00  a2pa............
  000010  80 bb 00 00 4e 6f 6e 53 65 63 75 72 65 20 4d 43  ....NonSecure MC
  000020  41 20 4c 45 41 50 20 4c 6f 6f 70 62 61 63 6b 00  A LEAP Loopback.
  ```
- **`device-name`**: `NonSecure MCA LEAP Loopback`
- **`device-uid`**: `NonSecure MCA LEAP Loopback`
- **`device_type`**: `leap-audio-data`
- **`name`**: `audio-leap-internal-loopback`
- **`reg`**: 36 bytes
  - u32: `0x4201 0x11002 0xb71b00 0x100fa 0x10030 0x3 0x3 0x20200202 0x3`
  ```
  000000  01 42 00 00 02 10 01 00 00 1b b7 00 fa 00 01 00  .B..............
  000010  30 00 01 00 03 00 00 00 03 00 00 00 02 02 20 20  0.............  
  000020  03 00 00 00                                      ....
  ```

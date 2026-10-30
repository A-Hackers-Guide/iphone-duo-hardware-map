# `/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`

- Name: `audio-s-leap-internal-loopback`
- Parent: [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback.md)
- phandle: `362`
- compatible: `audio-data,external`
- device_type: `leap-audio-data`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleExternalSecondaryAudio` | `AppleARMIISDevice` | [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md) | `audio-data,external` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x4201 0x12002 0xb71b00 0x100fa 0x10030 0x3 0x3 0x20200202 0x3` | | |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (12) [DT]

- **`AAPL,phandle`**: `362` (`0x16a`) → phandle of [`/arm-io/iop-audio-controller/audio-s-leap-internal-loopback/audio-s-leap-internal-loopback`](root__arm-io__iop-audio-controller__audio-s-leap-internal-loopback__audio-s-leap-internal-loopback.md)
- **`audio-stream-formatter`**: `1818583408` (`0x6c656170`) (four-char code `leap`)
- **`compatible`**: `audio-data,external`
- **`data-sources`**: 41 bytes
  - text inside: `a2pa`, `Secure LEAP Loopback`
  ```
  000000  61 32 70 61 02 02 04 00 02 00 01 00 00 00 00 00  a2pa............
  000010  80 bb 00 00 53 65 63 75 72 65 20 4c 45 41 50 20  ....Secure LEAP 
  000020  4c 6f 6f 70 62 61 63 6b 00                       Loopback.
  ```
- **`device-name`**: `Secure LEAP Loopback`
- **`device-uid`**: `Secure LEAP Loopback`
- **`device_type`**: `leap-audio-data`
- **`is-development-only`**: (present, empty)
- **`isolated-audio-service-input`**: `409` (`0x199`)
- **`name`**: `audio-s-leap-internal-loopback`
- **`private`**: `1`
- **`reg`**: 36 bytes
  - u32: `0x4201 0x12002 0xb71b00 0x100fa 0x10030 0x3 0x3 0x20200202 0x3`
  ```
  000000  01 42 00 00 02 20 01 00 00 1b b7 00 fa 00 01 00  .B... ..........
  000010  30 00 01 00 03 00 00 00 03 00 00 00 02 02 20 20  0.............  
  000020  03 00 00 00                                      ....
  ```

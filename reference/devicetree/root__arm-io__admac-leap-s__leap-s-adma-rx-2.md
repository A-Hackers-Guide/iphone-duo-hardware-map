# `/arm-io/admac-leap-s/leap-s-adma-rx-2`

- Name: `leap-s-adma-rx-2`
- Parent: [`/arm-io/admac-leap-s`](root__arm-io__admac-leap-s.md)
- phandle: `411`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293188000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293114008` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293114108` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293114208` | `0x4` (4 B) | not memory-mapped (bus address) |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (15) [DT]

- **`AAPL,phandle`**: `411` (`0x19b`) → phandle of [`/arm-io/admac-leap-s/leap-s-adma-rx-2`](root__arm-io__admac-leap-s__leap-s-adma-rx-2.md)
- **`channel-buffer-size`**: (present, empty)
- **`channel-is-development-only`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `32` (`0x20`)
- **`max-channel-count`**: `2` (`0x2`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `leap-s-adma-rx-2`
- **`reg`**: 64 bytes
  - u32: `0x93188000 0x2 0x4000 0x0 0x93114008 0x2 0x4 0x0 0x93114108 0x2 0x4 0x0 0x93114208 0x2 0x4 0x0`
  ```
  000000  00 80 18 93 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  08 40 11 93 02 00 00 00 04 00 00 00 00 00 00 00  .@..............
  000020  08 41 11 93 02 00 00 00 04 00 00 00 00 00 00 00  .A..............
  000030  08 42 11 93 02 00 00 00 04 00 00 00 00 00 00 00  .B..............
  ```
- **`role`**: `1279610451` (`0x4c454e53`) (four-char code `LENS`)
- **`service-exclave_proxy`**: `DMAChannelProxy@admac-sllb-ec-proxy`

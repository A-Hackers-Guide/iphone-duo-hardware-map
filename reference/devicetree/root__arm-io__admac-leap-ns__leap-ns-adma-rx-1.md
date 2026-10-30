# `/arm-io/admac-leap-ns/leap-ns-adma-rx-1`

- Name: `leap-ns-adma-rx-1`
- Parent: [`/arm-io/admac-leap-ns`](root__arm-io__admac-leap-ns.md)
- phandle: `395`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293384000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293314004` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293314104` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293314204` | `0x4` (4 B) | not memory-mapped (bus address) |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (13) [DT]

- **`AAPL,phandle`**: `395` (`0x18b`) → phandle of [`/arm-io/admac-leap-ns/leap-ns-adma-rx-1`](root__arm-io__admac-leap-ns__leap-ns-adma-rx-1.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `32` (`0x20`)
- **`max-channel-count`**: `8` (`0x8`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `leap-ns-adma-rx-1`
- **`reg`**: 64 bytes
  - u32: `0x93384000 0x2 0x4000 0x0 0x93314004 0x2 0x4 0x0 0x93314104 0x2 0x4 0x0 0x93314204 0x2 0x4 0x0`
  ```
  000000  00 40 38 93 02 00 00 00 00 40 00 00 00 00 00 00  .@8......@......
  000010  04 40 31 93 02 00 00 00 04 00 00 00 00 00 00 00  .@1.............
  000020  04 41 31 93 02 00 00 00 04 00 00 00 00 00 00 00  .A1.............
  000030  04 42 31 93 02 00 00 00 04 00 00 00 00 00 00 00  .B1.............
  ```
- **`role`**: `1279610451` (`0x4c454e53`) (four-char code `LENS`)

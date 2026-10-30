# `/arm-io/admac-leap-ns/leap-ns-adma-tx-1`

- Name: `leap-ns-adma-tx-1`
- Parent: [`/arm-io/admac-leap-ns`](root__arm-io__admac-leap-ns.md)
- phandle: `394`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293344000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293310004` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293310104` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293310204` | `0x4` (4 B) | not memory-mapped (bus address) |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (13) [DT]

- **`AAPL,phandle`**: `394` (`0x18a`) → phandle of [`/arm-io/admac-leap-ns/leap-ns-adma-tx-1`](root__arm-io__admac-leap-ns__leap-ns-adma-tx-1.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `32` (`0x20`)
- **`max-channel-count`**: `1` (`0x1`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `leap-ns-adma-tx-1`
- **`reg`**: 64 bytes
  - u32: `0x93344000 0x2 0x4000 0x0 0x93310004 0x2 0x4 0x0 0x93310104 0x2 0x4 0x0 0x93310204 0x2 0x4 0x0`
  ```
  000000  00 40 34 93 02 00 00 00 00 40 00 00 00 00 00 00  .@4......@......
  000010  04 00 31 93 02 00 00 00 04 00 00 00 00 00 00 00  ..1.............
  000020  04 01 31 93 02 00 00 00 04 00 00 00 00 00 00 00  ..1.............
  000030  04 02 31 93 02 00 00 00 04 00 00 00 00 00 00 00  ..1.............
  ```
- **`role`**: `1279610451` (`0x4c454e53`) (four-char code `LENS`)

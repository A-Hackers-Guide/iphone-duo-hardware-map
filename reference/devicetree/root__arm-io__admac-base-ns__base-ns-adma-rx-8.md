# `/arm-io/admac-base-ns/base-ns-adma-rx-8`

- Name: `base-ns-adma-rx-8`
- Parent: [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md)
- phandle: `392`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x2939a0000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293914020` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293914120` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293914220` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (13) [DT]

- **`AAPL,phandle`**: `392` (`0x188`) → phandle of [`/arm-io/admac-base-ns/base-ns-adma-rx-8`](root__arm-io__admac-base-ns__base-ns-adma-rx-8.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `16` (`0x10`)
- **`max-channel-count`**: `2` (`0x2`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `base-ns-adma-rx-8`
- **`reg`**: 64 bytes
  - u32: `0x939a0000 0x2 0x4000 0x0 0x93914020 0x2 0x4 0x0 0x93914120 0x2 0x4 0x0 0x93914220 0x2 0x4 0x0`
  ```
  000000  00 00 9a 93 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  20 40 91 93 02 00 00 00 04 00 00 00 00 00 00 00   @..............
  000020  20 41 91 93 02 00 00 00 04 00 00 00 00 00 00 00   A..............
  000030  20 42 91 93 02 00 00 00 04 00 00 00 00 00 00 00   B..............
  ```
- **`role`**: `1111576147` (`0x42414e53`) (four-char code `BANS`)

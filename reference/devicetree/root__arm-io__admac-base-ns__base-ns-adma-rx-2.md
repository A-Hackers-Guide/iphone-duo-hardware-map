# `/arm-io/admac-base-ns/base-ns-adma-rx-2`

- Name: `base-ns-adma-rx-2`
- Parent: [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md)
- phandle: `386`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293988000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293914008` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293914108` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293914208` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (13) [DT]

- **`AAPL,phandle`**: `386` (`0x182`) → phandle of [`/arm-io/admac-base-ns/base-ns-adma-rx-2`](root__arm-io__admac-base-ns__base-ns-adma-rx-2.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `16` (`0x10`)
- **`max-channel-count`**: `12` (`0xc`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `base-ns-adma-rx-2`
- **`reg`**: 64 bytes
  - u32: `0x93988000 0x2 0x4000 0x0 0x93914008 0x2 0x4 0x0 0x93914108 0x2 0x4 0x0 0x93914208 0x2 0x4 0x0`
  ```
  000000  00 80 98 93 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  08 40 91 93 02 00 00 00 04 00 00 00 00 00 00 00  .@..............
  000020  08 41 91 93 02 00 00 00 04 00 00 00 00 00 00 00  .A..............
  000030  08 42 91 93 02 00 00 00 04 00 00 00 00 00 00 00  .B..............
  ```
- **`role`**: `1111576147` (`0x42414e53`) (four-char code `BANS`)

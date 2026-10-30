# `/arm-io/admac-base-s/base-s-adma-tx-2`

- Name: `base-s-adma-tx-2`
- Parent: [`/arm-io/admac-base-s`](root__arm-io__admac-base-s.md)
- phandle: `400`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293748000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293710008` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293710108` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293710208` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (16) [DT]

- **`AAPL,phandle`**: `400` (`0x190`) → phandle of [`/arm-io/admac-base-s/base-s-adma-tx-2`](root__arm-io__admac-base-s__base-s-adma-tx-2.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`initial-trigger-bytes`**: `96` (`0x60`)
- **`max-bit-depth-bits`**: `16` (`0x10`)
- **`max-channel-count`**: `2` (`0x2`)
- **`max-fifo-depth-bytes`**: `160` (`0xa0`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `base-s-adma-tx-2`
- **`reg`**: 64 bytes
  - u32: `0x93748000 0x2 0x4000 0x0 0x93710008 0x2 0x4 0x0 0x93710108 0x2 0x4 0x0 0x93710208 0x2 0x4 0x0`
  ```
  000000  00 80 74 93 02 00 00 00 00 40 00 00 00 00 00 00  ..t......@......
  000010  08 00 71 93 02 00 00 00 04 00 00 00 00 00 00 00  ..q.............
  000020  08 01 71 93 02 00 00 00 04 00 00 00 00 00 00 00  ..q.............
  000030  08 02 71 93 02 00 00 00 04 00 00 00 00 00 00 00  ..q.............
  ```
- **`role`**: `1111577427` (`0x42415353`) (four-char code `BASS`)
- **`service-exclave_proxy`**: `DMAChannelProxy@admac-speaker-tx-ec-proxy`

# `/arm-io/admac-base-s/base-s-adma-tx-3`

- Name: `base-s-adma-tx-3`
- Parent: [`/arm-io/admac-base-s`](root__arm-io__admac-base-s.md)
- phandle: `401`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x29374c000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x29371000c` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x29371010c` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x29371020c` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (16) [DT]

- **`AAPL,phandle`**: `401` (`0x191`) → phandle of [`/arm-io/admac-base-s/base-s-adma-tx-3`](root__arm-io__admac-base-s__base-s-adma-tx-3.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`initial-trigger-bytes`**: `96` (`0x60`)
- **`max-bit-depth-bits`**: `32` (`0x20`)
- **`max-channel-count`**: `1` (`0x1`)
- **`max-fifo-depth-bytes`**: `160` (`0xa0`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `base-s-adma-tx-3`
- **`reg`**: 64 bytes
  - u32: `0x9374c000 0x2 0x4000 0x0 0x9371000c 0x2 0x4 0x0 0x9371010c 0x2 0x4 0x0 0x9371020c 0x2 0x4 0x0`
  ```
  000000  00 c0 74 93 02 00 00 00 00 40 00 00 00 00 00 00  ..t......@......
  000010  0c 00 71 93 02 00 00 00 04 00 00 00 00 00 00 00  ..q.............
  000020  0c 01 71 93 02 00 00 00 04 00 00 00 00 00 00 00  ..q.............
  000030  0c 02 71 93 02 00 00 00 04 00 00 00 00 00 00 00  ..q.............
  ```
- **`role`**: `1111577427` (`0x42415353`) (four-char code `BASS`)
- **`service-exclave_proxy`**: `DMAChannelProxy@admac-receiver-tx-ec-proxy`

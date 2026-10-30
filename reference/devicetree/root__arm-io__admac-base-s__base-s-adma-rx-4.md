# `/arm-io/admac-base-s/base-s-adma-rx-4`

- Name: `base-s-adma-rx-4`
- Parent: [`/arm-io/admac-base-s`](root__arm-io__admac-base-s.md)
- phandle: `402`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293790000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293714010` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293714110` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293714210` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (14) [DT]

- **`AAPL,phandle`**: `402` (`0x192`) → phandle of [`/arm-io/admac-base-s/base-s-adma-rx-4`](root__arm-io__admac-base-s__base-s-adma-rx-4.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `32` (`0x20`)
- **`max-channel-count`**: `4` (`0x4`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `base-s-adma-rx-4`
- **`reg`**: 64 bytes
  - u32: `0x93790000 0x2 0x4000 0x0 0x93714010 0x2 0x4 0x0 0x93714110 0x2 0x4 0x0 0x93714210 0x2 0x4 0x0`
  ```
  000000  00 00 79 93 02 00 00 00 00 40 00 00 00 00 00 00  ..y......@......
  000010  10 40 71 93 02 00 00 00 04 00 00 00 00 00 00 00  .@q.............
  000020  10 41 71 93 02 00 00 00 04 00 00 00 00 00 00 00  .Aq.............
  000030  10 42 71 93 02 00 00 00 04 00 00 00 00 00 00 00  .Bq.............
  ```
- **`role`**: `1111577427` (`0x42415353`) (four-char code `BASS`)
- **`service-exclave_proxy`**: `DMAChannelProxy@admac-hp-mic-ec-proxy`

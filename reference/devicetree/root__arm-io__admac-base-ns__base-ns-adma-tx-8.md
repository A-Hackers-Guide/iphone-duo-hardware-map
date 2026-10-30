# `/arm-io/admac-base-ns/base-ns-adma-tx-8`

- Name: `base-ns-adma-tx-8`
- Parent: [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md)
- phandle: `391`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x293960000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x293910020` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x293910120` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x293910220` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (13) [DT]

- **`AAPL,phandle`**: `391` (`0x187`) → phandle of [`/arm-io/admac-base-ns/base-ns-adma-tx-8`](root__arm-io__admac-base-ns__base-ns-adma-tx-8.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `16` (`0x10`)
- **`max-channel-count`**: `2` (`0x2`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `base-ns-adma-tx-8`
- **`reg`**: 64 bytes
  - u32: `0x93960000 0x2 0x4000 0x0 0x93910020 0x2 0x4 0x0 0x93910120 0x2 0x4 0x0 0x93910220 0x2 0x4 0x0`
  ```
  000000  00 00 96 93 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  20 00 91 93 02 00 00 00 04 00 00 00 00 00 00 00   ...............
  000020  20 01 91 93 02 00 00 00 04 00 00 00 00 00 00 00   ...............
  000030  20 02 91 93 02 00 00 00 04 00 00 00 00 00 00 00   ...............
  ```
- **`role`**: `1111576147` (`0x42414e53`) (four-char code `BANS`)

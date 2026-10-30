# `/arm-io/admac-base-ns/base-ns-adma-tx-7`

- Name: `base-ns-adma-tx-7`
- Parent: [`/arm-io/admac-base-ns`](root__arm-io__admac-base-ns.md)
- phandle: `390`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x29395c000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x29391001c` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x29391011c` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x29391021c` | `0x4` (4 B) | not memory-mapped (bus address) |

## All properties (13) [DT]

- **`AAPL,phandle`**: `390` (`0x186`) → phandle of [`/arm-io/admac-base-ns/base-ns-adma-tx-7`](root__arm-io__admac-base-ns__base-ns-adma-tx-7.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `16` (`0x10`)
- **`max-channel-count`**: `4` (`0x4`)
- **`max-sample-rate-hz`**: `16000` (`0x3e80`)
- **`name`**: `base-ns-adma-tx-7`
- **`reg`**: 64 bytes
  - u32: `0x9395c000 0x2 0x4000 0x0 0x9391001c 0x2 0x4 0x0 0x9391011c 0x2 0x4 0x0 0x9391021c 0x2 0x4 0x0`
  ```
  000000  00 c0 95 93 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  1c 00 91 93 02 00 00 00 04 00 00 00 00 00 00 00  ................
  000020  1c 01 91 93 02 00 00 00 04 00 00 00 00 00 00 00  ................
  000030  1c 02 91 93 02 00 00 00 04 00 00 00 00 00 00 00  ................
  ```
- **`role`**: `1111576147` (`0x42414e53`) (four-char code `BANS`)

# `/arm-io/admac-leap-ns/leap-ns-adma-rx-3`

- Name: `leap-ns-adma-rx-3`
- Parent: [`/arm-io/admac-leap-ns`](root__arm-io__admac-leap-ns.md)
- phandle: `398`
- compatible: `audio-dma-channel,v4p0`
- device_type: `adma-ch`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x29338c000` | `0x4000` (16,384 B) | not memory-mapped (bus address) |
| 1 | `0x29331400c` | `0x4` (4 B) | not memory-mapped (bus address) |
| 2 | `0x29331410c` | `0x4` (4 B) | not memory-mapped (bus address) |
| 3 | `0x29331420c` | `0x4` (4 B) | not memory-mapped (bus address) |

## Firmware with a matching name [FW]

- [`Firmware/V68_LeapHapticsFirmware.im4p`](../firmware/Firmware__V68_LeapHapticsFirmware.im4p.md) (283,085 B) Tag: IM4P  Type: lphp  Version: 1

## All properties (13) [DT]

- **`AAPL,phandle`**: `398` (`0x18e`) → phandle of [`/arm-io/admac-leap-ns/leap-ns-adma-rx-3`](root__arm-io__admac-leap-ns__leap-ns-adma-rx-3.md)
- **`channel-buffer-size`**: (present, empty)
- **`compatible`**: `audio-dma-channel,v4p0`
- **`device_type`**: `adma-ch`
- **`direction`**: (present, empty)
- **`dma-stream-type`**: `1230196547` (`0x49534f43`) (four-char code `ISOC`)
- **`index`**: (present, empty)
- **`max-bit-depth-bits`**: `32` (`0x20`)
- **`max-channel-count`**: `2` (`0x2`)
- **`max-sample-rate-hz`**: `48000` (`0xbb80`)
- **`name`**: `leap-ns-adma-rx-3`
- **`reg`**: 64 bytes
  - u32: `0x9338c000 0x2 0x4000 0x0 0x9331400c 0x2 0x4 0x0 0x9331410c 0x2 0x4 0x0 0x9331420c 0x2 0x4 0x0`
  ```
  000000  00 c0 38 93 02 00 00 00 00 40 00 00 00 00 00 00  ..8......@......
  000010  0c 40 31 93 02 00 00 00 04 00 00 00 00 00 00 00  .@1.............
  000020  0c 41 31 93 02 00 00 00 04 00 00 00 00 00 00 00  .A1.............
  000030  0c 42 31 93 02 00 00 00 04 00 00 00 00 00 00 00  .B1.............
  ```
- **`role`**: `1279610451` (`0x4c454e53`) (four-char code `LENS`)

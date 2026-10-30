# `/product/facetime`

- Name: `facetime`
- Parent: [`/product`](root__product.md)
- phandle: `474`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (11) [DT]

- **`AAPL,phandle`**: `474` (`0x1da`) → phandle of [`/product/facetime`](root__product__facetime.md)
- **`bitrate-2g`**: `100` (`0x64`)
- **`bitrate-3g`**: `228` (`0xe4`)
- **`bitrate-lte`**: `228` (`0xe4`)
- **`bitrate-wifi`**: `2000` (`0x7d0`)
- **`decoding`**: 48 bytes
  - u32: `0x140 0xf0000f 0x140 0xf0001e 0x1e0 0x170000f 0x1e0 0x170001e 0x280 0x1e0001e 0x400 0x300001e`
  ```
  000000  40 01 00 00 0f 00 f0 00 40 01 00 00 1e 00 f0 00  @.......@.......
  000010  e0 01 00 00 0f 00 70 01 e0 01 00 00 1e 00 70 01  ......p.......p.
  000020  80 02 00 00 1e 00 e0 01 00 04 00 00 1e 00 00 03  ................
  ```
- **`encoding`**: 56 bytes
  - u32: `0x140 0xf0000f 0x140 0xf0001e 0x1e0 0x170000f 0x1e0 0x170001e 0x280 0x1e0001e 0x400 0x300001e 0x500 0x2d0001e`
  ```
  000000  40 01 00 00 0f 00 f0 00 40 01 00 00 1e 00 f0 00  @.......@.......
  000010  e0 01 00 00 0f 00 70 01 e0 01 00 00 1e 00 70 01  ......p.......p.
  000020  80 02 00 00 1e 00 e0 01 00 04 00 00 1e 00 00 03  ................
  000030  00 05 00 00 1e 00 d0 02                          ........
  ```
- **`name`**: `facetime`
- **`pref-decoding`**: `0x300001e00000400` (u64; as two u32: `0x400`, `0x300001e`)
- **`tnr-mode-back`**: `10` (`0xa`)
- **`tnr-mode-front`**: `10` (`0xa`)

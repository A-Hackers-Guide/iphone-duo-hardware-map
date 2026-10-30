# `/product/display1`

- Name: `display1`
- Parent: [`/product`](root__product.md)
- phandle: `471`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (22) [DT]

- **`AAPL,phandle`**: `471` (`0x1d7`) → phandle of [`/product/display1`](root__product__display1.md)
- **`camera-button-location`**: 24 bytes
  - u32: `0x180984 0x10e834 0xb228c 0x29bd0 0x2710 0x1`
  ```
  000000  84 09 18 00 34 e8 10 00 8c 22 0b 00 d0 9b 02 00  ....4...."......
  000010  10 27 00 00 01 00 00 00                          .'......
  ```
- **`chrome-identifier`**: `com.apple.dt.devicekit.chrome.phone14`
- **`display-corner-radius`**: 16 bytes
  - u32: `0x425c0000 0x425c0000 0x425c0000 0x425c0000`
  ```
  000000  00 00 5c 42 00 00 5c 42 00 00 5c 42 00 00 5c 42  ..\B..\B..\B..\B
  ```
- **`display-index`**: `1` (`0x1`)
- **`display-rotation`**: `270` (`0x10e`)
- **`display-scale`**: `3` (`0x3`)
- **`framebuffer-identifier`**: `BF0DC480-5EE2-4EC1-B02B-C75E94759832`
- **`front-cam-offset-from-center`**: 20 bytes
  - u32: `0x117a6 0xbc66 0xe56 0x3e8 0x0`
  ```
  000000  a6 17 01 00 66 bc 00 00 56 0e 00 00 e8 03 00 00  ....f...V.......
  000010  00 00 00 00                                      ....
  ```
- **`has-prox`**: `0` (`0x0`)
- **`name`**: `display1`
- **`rear-cam-offset-from-center`**: 20 bytes
  - u32: `0xc058 0xaa51 0x7da 0x3e8 0x0`
  ```
  000000  58 c0 00 00 51 aa 00 00 da 07 00 00 e8 03 00 00  X...Q...........
  000010  00 00 00 00                                      ....
  ```
- **`side-button-location`**: 24 bytes
  - u32: `0x180984 0x10e834 0x49741 0x2d956 0x2710 0x1`
  ```
  000000  84 09 18 00 34 e8 10 00 41 97 04 00 56 d9 02 00  ....4...A...V...
  000010  10 27 00 00 01 00 00 00                          .'......
  ```
- **`special-region-0-corner-curve`**: `circular`
- **`special-region-0-frame`**: 16 bytes
  - u32: `0x427c0000 0x44318000 0x42de0000 0x42de0000`
  ```
  000000  00 00 7c 42 00 80 31 44 00 00 de 42 00 00 de 42  ..|B..1D...B...B
  ```
- **`special-region-0-type`**: `BlankableRR`
- **`special-region-1-frame`**: 16 bytes
  - u32: `0x0 0x44a6e000 0x44eac000 0x0`
  ```
  000000  00 00 00 00 00 e0 a6 44 00 c0 ea 44 00 00 00 00  .......D...D....
  ```
- **`special-region-1-type`**: `Fold`
- **`special-regions-count`**: `2` (`0x2`)
- **`surface-type`**: `2` (`0x2`)
- **`volume-down-button-location`**: 24 bytes
  - u32: `0x180984 0x10e834 0x4b212 0x1a900 0x2710 0x0`
  ```
  000000  84 09 18 00 34 e8 10 00 12 b2 04 00 00 a9 01 00  ....4...........
  000010  10 27 00 00 00 00 00 00                          .'......
  ```
- **`volume-up-button-location`**: 24 bytes
  - u32: `0x180984 0x10e834 0x2a76a 0x1a900 0x2710 0x0`
  ```
  000000  84 09 18 00 34 e8 10 00 6a a7 02 00 00 a9 01 00  ....4...j.......
  000010  10 27 00 00 00 00 00 00                          .'......
  ```

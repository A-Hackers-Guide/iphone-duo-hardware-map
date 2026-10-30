# `/product/display0`

- Name: `display0`
- Parent: [`/product`](root__product.md)
- phandle: `470`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (20) [DT]

- **`AAPL,phandle`**: `470` (`0x1d6`) → phandle of [`/product/display0`](root__product__display0.md)
- **`camera-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0xb4069 0x29bd0 0x2710 0x1`
  ```
  000000  74 c6 0b 00 d2 21 11 00 69 40 0b 00 d0 9b 02 00  t....!..i@......
  000010  10 27 00 00 01 00 00 00                          .'......
  ```
- **`chrome-identifier`**: `com.apple.dt.devicekit.chrome.phone15`
- **`display-corner-radius`**: 16 bytes
  - u32: `0x41000000 0x41000000 0x426c0000 0x426c0000`
  ```
  000000  00 00 00 41 00 00 00 41 00 00 6c 42 00 00 6c 42  ...A...A..lB..lB
  ```
- **`display-index`**: `0` (`0x0`)
- **`display-rotation`**: `0` (`0x0`)
- **`display-scale`**: `3` (`0x3`)
- **`framebuffer-identifier`**: `1C896A2B-F0D7-405C-8D0F-66E4B80AD044`
- **`front-cam-offset-from-center`**: 20 bytes
  - u32: `0xbc66 0x7710 0xe56 0x3e8 0x0`
  ```
  000000  66 bc 00 00 10 77 00 00 56 0e 00 00 e8 03 00 00  f....w..V.......
  000010  00 00 00 00                                      ....
  ```
- **`has-prox`**: `1` (`0x1`)
- **`name`**: `display0`
- **`rear-cam-offset-from-center`**: 20 bytes
  - u32: `0xaa51 0x1fc4 0x1e82 0x3e8 0x0`
  ```
  000000  51 aa 00 00 c4 1f 00 00 82 1e 00 00 e8 03 00 00  Q...............
  000010  00 00 00 00                                      ....
  ```
- **`side-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0x4b51e 0x2d956 0x2710 0x1`
  ```
  000000  74 c6 0b 00 d2 21 11 00 1e b5 04 00 56 d9 02 00  t....!......V...
  000010  10 27 00 00 01 00 00 00                          .'......
  ```
- **`special-region-0-corner-curve`**: `circular`
- **`special-region-0-frame`**: 16 bytes
  - u32: `0x4495e000 0x42b00000 0x42de0000 0x42de0000`
  ```
  000000  00 e0 95 44 00 00 b0 42 00 00 de 42 00 00 de 42  ...D...B...B...B
  ```
- **`special-region-0-type`**: `Jindo`
- **`special-regions-count`**: `1` (`0x1`)
- **`surface-type`**: `1` (`0x1`)
- **`volume-down-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0x4cee6 0x1a900 0x2710 0x0`
  ```
  000000  74 c6 0b 00 d2 21 11 00 e6 ce 04 00 00 a9 01 00  t....!..........
  000010  10 27 00 00 00 00 00 00                          .'......
  ```
- **`volume-up-button-location`**: 24 bytes
  - u32: `0xbc674 0x1121d2 0x2c43e 0x1a900 0x2710 0x0`
  ```
  000000  74 c6 0b 00 d2 21 11 00 3e c4 02 00 00 a9 01 00  t....!..>.......
  000010  10 27 00 00 00 00 00 00                          .'......
  ```

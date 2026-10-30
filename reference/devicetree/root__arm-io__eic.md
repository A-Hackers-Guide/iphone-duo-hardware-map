# `/arm-io/eic`

- Name: `eic`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `309`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (16) [DT]

- **`AAPL,phandle`**: `309` (`0x135`) → phandle of [`/arm-io/eic`](root__arm-io__eic.md)
- **`cil`**: `1` (`0x1`)
- **`exclave-assigned`**: (present, empty)
- **`mil`**: `1` (`0x1`)
- **`mmio-fpwm`**: 16 bytes
  - u32: `0xe5040000 0x2 0xc000 0x0`
  ```
  000000  00 00 04 e5 02 00 00 00 00 c0 00 00 00 00 00 00  ................
  ```
- **`mmio-gltb`**: 16 bytes
  - u32: `0xc82a8000 0x2 0x4000 0x0`
  ```
  000000  00 80 2a c8 02 00 00 00 00 40 00 00 00 00 00 00  ..*......@......
  ```
- **`mmio-gpio`**: 16 bytes
  - u32: `0xda000000 0x2 0x4000 0x0`
  ```
  000000  00 00 00 da 02 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`mmio-ps`**: 16 bytes
  - u32: `0xc0700000 0x2 0x1c000 0x0`
  ```
  000000  00 00 70 c0 02 00 00 00 00 c0 01 00 00 00 00 00  ..p.............
  ```
- **`mmio-wd-e`**: 16 bytes
  - u32: `0xc82b0000 0x2 0x4000 0x0`
  ```
  000000  00 00 2b c8 02 00 00 00 00 40 00 00 00 00 00 00  ..+......@......
  ```
- **`mmio-wd-isp`**: 16 bytes
  - u32: `0xc3b10000 0x3 0x8000 0x0`
  ```
  000000  00 00 b1 c3 03 00 00 00 00 80 00 00 00 00 00 00  ................
  ```
- **`name`**: `eic`
- **`policy-allow-accessory`**: `1` (`0x1`)
- **`policy-allow-prox-suppression`**: `1` (`0x1`)
- **`policy-alt-indicator`**: `1` (`0x1`)
- **`policy-override-chill-pill`**: `1000` (`0x3e8`)
- **`policy-sensor-control`**: `0` (`0x0`)

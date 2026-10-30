# `/arm-io/error-handler/dcs-error-handler`

- Name: `dcs-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `57`
- device_type: `dcs-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x21000000 0x0 0x30000 0x0 0x21200000 0x0 0x30000 0x0 0x211fc000 0x0 0x4000 0x0 0x21400000 0x0 0x30000 0x0 0x21600000 0x0 0x30000 0x0 0x215fc000 0x0 0x4000 0x0 0x21800000 0x0 0x30000 0x0 0x21a00000 0x0 0x30000 0x0 0x219fc000 0x0 0x4000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`362, 363, 365, 366, 368, 369`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `57` (`0x39`) → phandle of [`/arm-io/error-handler/dcs-error-handler`](root__arm-io__error-handler__dcs-error-handler.md)
- **`device_type`**: `dcs-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 24 bytes
  - u32: `0x16a 0x16b 0x16d 0x16e 0x170 0x171`
  ```
  000000  6a 01 00 00 6b 01 00 00 6d 01 00 00 6e 01 00 00  j...k...m...n...
  000010  70 01 00 00 71 01 00 00                          p...q...
  ```
- **`name`**: `dcs-error-handler`
- **`nametag`**: `1684239136` (`0x64637320`) (four-char code `dcs `)
- **`reg`**: 144 bytes
  - u32: `0x21000000 0x0 0x30000 0x0 0x21200000 0x0 0x30000 0x0 0x211fc000 0x0 0x4000 0x0 0x21400000 0x0 0x30000 0x0 0x21600000 0x0 0x30000 0x0 0x215fc000 0x0 0x4000 0x0 0x21800000 0x0 0x30000 0x0 0x21a00000 0x0 0x30000 0x0 0x219fc000 0x0 0x4000 0x0`
  ```
  000000  00 00 00 21 00 00 00 00 00 00 03 00 00 00 00 00  ...!............
  000010  00 00 20 21 00 00 00 00 00 00 03 00 00 00 00 00  .. !............
  000020  00 c0 1f 21 00 00 00 00 00 40 00 00 00 00 00 00  ...!.....@......
  000030  00 00 40 21 00 00 00 00 00 00 03 00 00 00 00 00  ..@!............
  000040  00 00 60 21 00 00 00 00 00 00 03 00 00 00 00 00  ..`!............
  000050  00 c0 5f 21 00 00 00 00 00 40 00 00 00 00 00 00  .._!.....@......
  000060  00 00 80 21 00 00 00 00 00 00 03 00 00 00 00 00  ...!............
  000070  00 00 a0 21 00 00 00 00 00 00 03 00 00 00 00 00  ...!............
  000080  00 c0 9f 21 00 00 00 00 00 40 00 00 00 00 00 00  ...!.....@......
  ```

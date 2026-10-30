# `/arm-io/error-handler/pmgr-error-handler`

- Name: `pmgr-error-handler`
- Parent: [`/arm-io/error-handler`](root__arm-io__error-handler.md)
- phandle: `58`
- device_type: `pmgr-error-handler`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x80000000 0x0 0x40000 0x0 0x80728000 0x0 0x4000 0x0 0x80768000 0x0 0x4000 0x0 0x882c8000 0x0 0x4000 0x0 0x82000000 0x0 0x1000000 0x0 0x803d0000 0x0 0x4000 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1118, 1112`

## All properties (10) [DT]

- **`#address-cells`**: `2` (`0x2`)
- **`#size-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `58` (`0x3a`) → phandle of [`/arm-io/error-handler/pmgr-error-handler`](root__arm-io__error-handler__pmgr-error-handler.md)
- **`device_type`**: `pmgr-error-handler`
- **`flags`**: `0` (`0x0`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x4580000045e` (u64; as two u32: `0x45e`, `0x458`)
- **`name`**: `pmgr-error-handler`
- **`nametag`**: `1886218098` (`0x706d6772`) (four-char code `pmgr`)
- **`reg`**: 96 bytes
  - u32: `0x80000000 0x0 0x40000 0x0 0x80728000 0x0 0x4000 0x0 0x80768000 0x0 0x4000 0x0 0x882c8000 0x0 0x4000 0x0 0x82000000 0x0 0x1000000 0x0 0x803d0000 0x0 0x4000 0x0`
  ```
  000000  00 00 00 80 00 00 00 00 00 00 04 00 00 00 00 00  ................
  000010  00 80 72 80 00 00 00 00 00 40 00 00 00 00 00 00  ..r......@......
  000020  00 80 76 80 00 00 00 00 00 40 00 00 00 00 00 00  ..v......@......
  000030  00 80 2c 88 00 00 00 00 00 40 00 00 00 00 00 00  ..,......@......
  000040  00 00 00 82 00 00 00 00 00 00 00 01 00 00 00 00  ................
  000050  00 00 3d 80 00 00 00 00 00 40 00 00 00 00 00 00  ..=......@......
  ```

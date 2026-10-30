# `/arm-io/apcie1-piodma`

- Name: `apcie1-piodma`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `433`
- compatible: `pcie-apiodma,gen3p0`
- device_type: `apcie1-piodma`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ApplePCIePIODMA` | `AppleARMIODevice` | [`com.apple.driver.ApplePCIePIODMAGen3p0`](../kexts/com.apple.driver.ApplePCIePIODMAGen3p0.md) | `pcie-apiodma,gen3p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x109048000` | `0x4000` (16,384 B) | `0x309048000`–`0x30904bfff` |
| 1 | `0x10904c000` | `0x4000` (16,384 B) | `0x30904c000`–`0x30904ffff` |
| 2 | `0x109050000` | `0x4000` (16,384 B) | `0x309050000`–`0x309053fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1471`

## All properties (15) [DT]

- **`AAPL,phandle`**: `433` (`0x1b1`) → phandle of [`/arm-io/apcie1-piodma`](root__arm-io__apcie1-piodma.md)
- **`compatible`**: `pcie-apiodma,gen3p0`
- **`device_type`**: `apcie1-piodma`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1471` (`0x5bf`)
- **`iommu-parent`**: `431` (`0x1af`) → phandle of [`/arm-io/dart-apcie1/mapper-apcie1-piodma`](root__arm-io__dart-apcie1__mapper-apcie1-piodma.md)
- **`name`**: `apcie1-piodma`
- **`piodma-base-address`**: 24 bytes
  - u32: `0xb0000000 0x1c 0xc0000000 0xb 0x80000000 0xb`
  ```
  000000  00 00 00 b0 1c 00 00 00 00 00 00 c0 0b 00 00 00  ................
  000010  00 00 00 80 0b 00 00 00                          ........
  ```
- **`piodma-byte-alignment`**: `16` (`0x10`)
- **`piodma-fifo-size`**: `16` (`0x10`)
- **`piodma-id`**: `1` (`0x1`)
- **`piodma-max-segment-size`**: `0` (`0x0`)
- **`piodma-max-transfer-size`**: `128` (`0x80`)
- **`piodma-num-address-bits`**: `42` (`0x2a`)
- **`reg`**: 48 bytes
  - u32: `0x9048000 0x1 0x4000 0x0 0x904c000 0x1 0x4000 0x0 0x9050000 0x1 0x4000 0x0`
  ```
  000000  00 80 04 09 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  00 c0 04 09 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 05 09 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

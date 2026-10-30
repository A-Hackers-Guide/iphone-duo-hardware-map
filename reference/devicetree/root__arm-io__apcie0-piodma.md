# `/arm-io/apcie0-piodma`

- Name: `apcie0-piodma`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `427`
- compatible: `pcie-apiodma,gen3p0`
- device_type: `apcie0-piodma`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ApplePCIePIODMA` | `AppleARMIODevice` | [`com.apple.driver.ApplePCIePIODMAGen3p0`](../kexts/com.apple.driver.ApplePCIePIODMAGen3p0.md) | `pcie-apiodma,gen3p0` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x108048000` | `0x4000` (16,384 B) | `0x308048000`–`0x30804bfff` |
| 1 | `0x10804c000` | `0x4000` (16,384 B) | `0x30804c000`–`0x30804ffff` |
| 2 | `0x108050000` | `0x4000` (16,384 B) | `0x308050000`–`0x308053fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1459`

## All properties (15) [DT]

- **`AAPL,phandle`**: `427` (`0x1ab`) → phandle of [`/arm-io/apcie0-piodma`](root__arm-io__apcie0-piodma.md)
- **`compatible`**: `pcie-apiodma,gen3p0`
- **`device_type`**: `apcie0-piodma`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1459` (`0x5b3`)
- **`iommu-parent`**: `425` (`0x1a9`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-piodma`](root__arm-io__dart-apcie0__mapper-apcie0-piodma.md)
- **`name`**: `apcie0-piodma`
- **`piodma-base-address`**: 24 bytes
  - u32: `0xb0000000 0x1c 0xc0000000 0xb 0x80000000 0xb`
  ```
  000000  00 00 00 b0 1c 00 00 00 00 00 00 c0 0b 00 00 00  ................
  000010  00 00 00 80 0b 00 00 00                          ........
  ```
- **`piodma-byte-alignment`**: `16` (`0x10`)
- **`piodma-fifo-size`**: `16` (`0x10`)
- **`piodma-id`**: `0` (`0x0`)
- **`piodma-max-segment-size`**: `0` (`0x0`)
- **`piodma-max-transfer-size`**: `128` (`0x80`)
- **`piodma-num-address-bits`**: `42` (`0x2a`)
- **`reg`**: 48 bytes
  - u32: `0x8048000 0x1 0x4000 0x0 0x804c000 0x1 0x4000 0x0 0x8050000 0x1 0x4000 0x0`
  ```
  000000  00 80 04 08 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  00 c0 04 08 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 05 08 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

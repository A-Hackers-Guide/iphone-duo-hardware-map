# `/arm-io/spi1`

- Name: `spi1`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `76`
- compatible: `spi-1,spimc`
- device_type: `spi`
- Children (1): [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPIMCController` | `AppleARMIODevice` | [`com.apple.driver.AppleSPIMC`](../kexts/com.apple.driver.AppleSPIMC.md) | `spi-1,spimc` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa5104000` | `0x4000` (16,384 B) | `0x2a5104000`–`0x2a5107fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1337`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `spi_cs0` | [`/`](root.md) | `null` | `` |

## All properties (15) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `7` (`0x7`)
- **`AAPL,phandle`**: `76` (`0x4c`) → phandle of [`/arm-io/spi1`](root__arm-io__spi1.md)
- **`clock-ids`**: `404` (`0x194`)
- **`compatible`**: `spi-1,spimc`
- **`device_type`**: `spi`
- **`dma-channels`**: 64 bytes
  - u32: `0x16 0x0 0x0 0x80 0x40 0x0 0x0 0x0 0x17 0x0 0x0 0x80 0x40 0x0 0x0 0x0`
  ```
  000000  16 00 00 00 00 00 00 00 00 00 00 00 80 00 00 00  ................
  000010  40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  @...............
  000020  17 00 00 00 00 00 00 00 00 00 00 00 80 00 00 00  ................
  000030  40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  @...............
  ```
- **`dma-parent`**: `137` (`0x89`) → phandle of [`/arm-io/sio/iop-sio-nub/sio-dma`](root__arm-io__sio__iop-sio-nub__sio-dma.md)
- **`function-spi_cs0`**: `0x6e756c6c00000001` (u64; as two u32: `0x1`, `0x6e756c6c`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1337` (`0x539`)
- **`name`**: `spi1`
- **`reg`**: 16 bytes
  - u32: `0xa5104000 0x0 0x4000 0x0`
  ```
  000000  00 40 10 a5 00 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  ```
- **`service-gates`**: `18` (`0x12`)
- **`spi-version`**: `1` (`0x1`)

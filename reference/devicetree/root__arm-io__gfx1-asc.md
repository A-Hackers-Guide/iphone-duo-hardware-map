# `/arm-io/gfx1-asc`

- Name: `gfx1-asc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `347`
- compatible: `iop,ascwrap-v8`
- device_type: `gfx-asc`
- Children (1): [`/arm-io/gfx1-asc/iop-gfx1-nub`](root__arm-io__gfx1-asc__iop-gfx1-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xaae00000` | `0x74000` (475,136 B) | `0x2aae00000`–`0x2aae73fff` |
| 1 | `0xaa850000` | `0x8` (8 B) | `0x2aa850000`–`0x2aa850007` |
| 2 | `0x96000000` | `0x1c000` (114,688 B) | `0x296000000`–`0x29601bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`200, 160`

## Firmware with a matching name [FW]

- [`Firmware/SmartIOFirmware_ASCv8.im4p`](../firmware/Firmware__SmartIOFirmware_ASCv8.im4p.md) (1,149,397 B) Tag: IM4P  Type: siof  Version: 1.0.0

## All properties (16) [DT]

- **`AAPL,phandle`**: `347` (`0x15b`) → phandle of [`/arm-io/gfx1-asc`](root__arm-io__gfx1-asc.md)
- **`clock-gates`**: `61` (`0x3d`)
- **`clock-ids`**: `342` (`0x156`)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `gfx-asc`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0xa0000000c8` (u64; as two u32: `0xc8`, `0xa0`)
- **`iommu-parent`**: `349` (`0x15d`) → phandle of [`/arm-io/mapper-gfx-asc`](root__arm-io__mapper-gfx-asc.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `6` (`0x6`)
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `gfx1-asc`
- **`power-gates`**: `61` (`0x3d`)
- **`reg`**: 48 bytes
  - u32: `0xaae00000 0x0 0x74000 0x0 0xaa850000 0x0 0x8 0x0 0x96000000 0x0 0x1c000 0x0`
  ```
  000000  00 00 e0 aa 00 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 aa 00 00 00 00 08 00 00 00 00 00 00 00  ................
  000020  00 00 00 96 00 00 00 00 00 c0 01 00 00 00 00 00  ................
  ```
- **`role`**: `GFX1`
- **`service-gates`**: `61` (`0x3d`)

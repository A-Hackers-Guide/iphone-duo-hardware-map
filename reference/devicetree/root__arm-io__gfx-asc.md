# `/arm-io/gfx-asc`

- Name: `gfx-asc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `345`
- compatible: `iop,ascwrap-v8`
- device_type: `gfx-asc`
- Children (1): [`/arm-io/gfx-asc/iop-gfx-nub`](root__arm-io__gfx-asc__iop-gfx-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xaa600000` | `0x74000` (475,136 B) | `0x2aa600000`–`0x2aa673fff` |
| 1 | `0xaa050000` | `0x8` (8 B) | `0x2aa050000`–`0x2aa050007` |
| 2 | `0x96000000` | `0x1c000` (114,688 B) | `0x296000000`–`0x29601bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`199, 159`

## Firmware with a matching name [FW]

- [`Firmware/SmartIOFirmware_ASCv8.im4p`](../firmware/Firmware__SmartIOFirmware_ASCv8.im4p.md) (1,149,397 B) Tag: IM4P  Type: siof  Version: 1.0.0

## All properties (16) [DT]

- **`AAPL,phandle`**: `345` (`0x159`) → phandle of [`/arm-io/gfx-asc`](root__arm-io__gfx-asc.md)
- **`clock-gates`**: `60` (`0x3c`)
- **`clock-ids`**: `342` (`0x156`)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `gfx-asc`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x9f000000c7` (u64; as two u32: `0xc7`, `0x9f`)
- **`iommu-parent`**: `349` (`0x15d`) → phandle of [`/arm-io/mapper-gfx-asc`](root__arm-io__mapper-gfx-asc.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `5` (`0x5`)
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `gfx-asc`
- **`power-gates`**: `60` (`0x3c`)
- **`reg`**: 48 bytes
  - u32: `0xaa600000 0x0 0x74000 0x0 0xaa050000 0x0 0x8 0x0 0x96000000 0x0 0x1c000 0x0`
  ```
  000000  00 00 60 aa 00 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 aa 00 00 00 00 08 00 00 00 00 00 00 00  ................
  000020  00 00 00 96 00 00 00 00 00 c0 01 00 00 00 00 00  ................
  ```
- **`role`**: `GFX`
- **`service-gates`**: `60` (`0x3c`)

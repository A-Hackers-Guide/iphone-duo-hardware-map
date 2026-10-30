# `/arm-io/smc`

- Name: `smc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `157`
- compatible: `iop,ascwrap-v8`
- device_type: `smc`
- Children (1): [`/arm-io/smc/iop-smc-nub`](root__arm-io__smc__iop-smc-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x8c600000` | `0x74000` (475,136 B) | `0x28c600000`–`0x28c673fff` |
| 1 | `0x8c050000` | `0x4000` (16,384 B) | `0x28c050000`–`0x28c053fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x8c810000` | `0x100` (256 B) | `0x28c810000`–`0x28c8100ff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`196, 156, 116`

## All properties (17) [DT]

- **`AAPL,phandle`**: `157` (`0x9d`) → phandle of [`/arm-io/smc`](root__arm-io__smc.md)
- **`aot-power`**: `1` (`0x1`)
- **`clock-gates`**: (present, empty)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `smc`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xc4 0x9c 0x74`
  ```
  000000  c4 00 00 00 9c 00 00 00 74 00 00 00              ........t...
  ```
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `2` (`0x2`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `smc`
- **`power-gates`**: (present, empty)
- **`reg`**: 64 bytes
  - u32: `0x8c600000 0x0 0x74000 0x0 0x8c050000 0x0 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x8c810000 0x0 0x100 0x0`
  ```
  000000  00 00 60 8c 00 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 8c 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 00 81 8c 00 00 00 00 00 01 00 00 00 00 00 00  ................
  ```
- **`role`**: `SMC`
- **`timers-reg-index`**: `3` (`0x3`)

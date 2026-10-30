# `/arm-io/pmp`

- Name: `pmp`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `118`
- compatible: `iop,ascwrap-v8`
- device_type: `pmp`
- Children (1): [`/arm-io/pmp/iop-pmp-nub`](root__arm-io__pmp__iop-pmp-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x80e00000` | `0x74000` (475,136 B) | `0x280e00000`–`0x280e73fff` |
| 1 | `0x80850000` | `0x4000` (16,384 B) | `0x280850000`–`0x280853fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x80500000` | `0xb0000` (720,896 B) | `0x280500000`–`0x2805affff` |
| 4 | `0x803d0000` | `0x4000` (16,384 B) | `0x2803d0000`–`0x2803d3fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`198, 158, 118`

## Firmware with a matching name [FW]

- [`Firmware/pmp/t8160pmp.im4p`](../firmware/Firmware__pmp__t8160pmp.im4p.md) (737,305 B) Tag: IM4P  Type: pmpf  Version: 0

## All properties (21) [DT]

- **`AAPL,phandle`**: `118` (`0x76`) → phandle of [`/arm-io/pmp`](root__arm-io__pmp.md)
- **`clock-gates`**: `0x9800000097` (u64; as two u32: `0x97`, `0x98`)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `pmp`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xc6 0x9e 0x76`
  ```
  000000  c6 00 00 00 9e 00 00 00 76 00 00 00              ........v...
  ```
- **`iommu-parent`**: `147` (`0x93`) → phandle of [`/arm-io/dart-sbr/mapper-pmp`](root__arm-io__dart-sbr__mapper-pmp.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `4` (`0x4`)
- **`msgbox-using-alias`**: `1` (`0x1`)
- **`msgbox-using-postoffice`**: `1` (`0x1`)
- **`name`**: `pmp`
- **`pio-vm-base`**: `0xc0000000` (u64; as two u32: `0xc0000000`, `0x0`)
- **`pio-vm-size`**: `@`
- **`power-gates`**: `0x9800000097` (u64; as two u32: `0x97`, `0x98`)
- **`ptd-update-reg-index`**: `4` (`0x4`)
- **`reg`**: 80 bytes
  - u32: `0x80e00000 0x0 0x74000 0x0 0x80850000 0x0 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x80500000 0x0 0xb0000 0x0 0x803d0000 0x0 0x4000 0x0`
  ```
  000000  00 00 e0 80 00 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 80 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 00 50 80 00 00 00 00 00 00 0b 00 00 00 00 00  ..P.............
  000040  00 00 3d 80 00 00 00 00 00 40 00 00 00 00 00 00  ..=......@......
  ```
- **`role`**: `PMP`
- **`service-gates`**: `0x9800000097` (u64; as two u32: `0x97`, `0x98`)
- **`sram-index`**: `1` (`0x1`)

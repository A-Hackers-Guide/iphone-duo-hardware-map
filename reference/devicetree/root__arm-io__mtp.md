# `/arm-io/mtp`

- Name: `mtp`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `169`
- compatible: `iop,ascwrap-v8`
- device_type: `mtp`
- Children (1): [`/arm-io/mtp/iop-mtp-nub`](root__arm-io__mtp__iop-mtp-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x94600000` | `0x74000` (475,136 B) | `0x294600000`–`0x294673fff` |
| 1 | `0x94050000` | `0x4000` (16,384 B) | `0x294050000`–`0x294053fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`197, 157, 117`

## Firmware with a matching name [FW]

- [`Firmware/V68_MtpFirmware.im4p`](../firmware/Firmware__V68_MtpFirmware.im4p.md) (2,308,247 B) Tag: IM4P  Type: mtpf  Version: 1

## All properties (17) [DT]

- **`AAPL,phandle`**: `169` (`0xa9`) → phandle of [`/arm-io/mtp`](root__arm-io__mtp.md)
- **`clock-gates`**: (present, empty)
- **`clock-ids`**: (present, empty)
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `mtp`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xc5 0x9d 0x75`
  ```
  000000  c5 00 00 00 9d 00 00 00 75 00 00 00              ........u...
  ```
- **`iommu-parent`**: `146` (`0x92`) → phandle of [`/arm-io/dart-sbr/mapper-mtp`](root__arm-io__dart-sbr__mapper-mtp.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `3` (`0x3`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `mtp`
- **`power-gates`**: (present, empty)
- **`reg`**: 48 bytes
  - u32: `0x94600000 0x0 0x74000 0x0 0x94050000 0x0 0x4000 0x0 0x96020000 0x0 0x10000 0x0`
  ```
  000000  00 00 60 94 00 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 94 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  ```
- **`role`**: `MTP`
- **`sptm-allow-reg`**: 16 bytes
  - u32: `0x94c00000 0x0 0x280000 0x0`
  ```
  000000  00 00 c0 94 00 00 00 00 00 00 28 00 00 00 00 00  ..........(.....
  ```

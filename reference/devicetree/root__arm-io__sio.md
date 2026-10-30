# `/arm-io/sio`

- Name: `sio`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `135`
- compatible: `iop,ascwrap-v8`
- device_type: `sio`
- Children (1): [`/arm-io/sio/iop-sio-nub`](root__arm-io__sio__iop-sio-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa5e00000` | `0x74000` (475,136 B) | `0x2a5e00000`–`0x2a5e73fff` |
| 1 | `0xa5850000` | `0x4000` (16,384 B) | `0x2a5850000`–`0x2a5853fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`202, 162, 122`

## All properties (21) [DT]

- **`AAPL,phandle`**: `135` (`0x87`) → phandle of [`/arm-io/sio`](root__arm-io__sio.md)
- **`clock-gates`**: `24` (`0x18`)
- **`clock-ids`**: 12 bytes
  - u32: `0x166 0x164 0x165`
  ```
  000000  66 01 00 00 64 01 00 00 65 01 00 00              f...d...e...
  ```
- **`compatible`**: `iop,ascwrap-v8`
- **`device-type`**: 24 bytes
  - u32: `0x64535049 0x4 0x0 0x64554152 0x6 0x0`
  - text inside: `IPSd`, `RAUd`
  ```
  000000  49 50 53 64 04 00 00 00 00 00 00 00 52 41 55 64  IPSd........RAUd
  000010  06 00 00 00 00 00 00 00                          ........
  ```
- **`device_type`**: `sio`
- **`dmashim`**: 72 bytes
  - u32: `0x53535049 0xa5100000 0x2 0x100000 0x0 0xd 0xe 0xf 0x4000 0x53554152 0xa5200000 0x2 0x100000 0x0 0x1 0x2 0x3 0x1000`
  - text inside: `IPSS`, `RAUS`
  ```
  000000  49 50 53 53 00 00 10 a5 02 00 00 00 00 00 10 00  IPSS............
  000010  00 00 00 00 0d 00 00 00 0e 00 00 00 0f 00 00 00  ................
  000020  00 40 00 00 52 41 55 53 00 00 20 a5 02 00 00 00  .@..RAUS.. .....
  000030  00 00 10 00 00 00 00 00 01 00 00 00 02 00 00 00  ................
  000040  03 00 00 00 00 10 00 00                          ........
  ```
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 12 bytes
  - u32: `0xca 0xa2 0x7a`
  ```
  000000  ca 00 00 00 a2 00 00 00 7a 00 00 00              ........z...
  ```
- **`iommu-parent`**: `139` (`0x8b`) → phandle of [`/arm-io/dart-sio/mapper-sio`](root__arm-io__dart-sio__mapper-sio.md)
- **`iop-version`**: `1` (`0x1`)
- **`map-range`**: 20 bytes
  - u32: `0x4d495343 0xa5000000 0x2 0x4000 0x0`
  - text inside: `CSIM`
  ```
  000000  43 53 49 4d 00 00 00 a5 02 00 00 00 00 40 00 00  CSIM.........@..
  000010  00 00 00 00                                      ....
  ```
- **`msgbox-mailbox-num`**: `8` (`0x8`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `sio`
- **`power-gates`**: `24` (`0x18`)
- **`reg`**: 48 bytes
  - u32: `0xa5e00000 0x0 0x74000 0x0 0xa5850000 0x0 0x4000 0x0 0x96020000 0x0 0x10000 0x0`
  ```
  000000  00 00 e0 a5 00 00 00 00 00 40 07 00 00 00 00 00  .........@......
  000010  00 00 85 a5 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  ```
- **`role`**: `SIO`
- **`service-gates`**: `24` (`0x18`)
- **`service-reset`**: `20` (`0x14`)

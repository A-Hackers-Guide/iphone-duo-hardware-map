# `/arm-io/aes`

- Name: `aes`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `78`
- compatible: `aes,s8000`
- device_type: `aes`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleS8000AESAccelerator` | `AppleARMIODevice` | [`com.apple.driver.AppleS8000AES`](../kexts/com.apple.driver.AppleS8000AES.md) | `aes,s8000` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xa500c000` | `0x4000` (16,384 B) | `0x2a500c000`–`0x2a500ffff` |
| 1 | `0x882dc000` | `0x8000` (32,768 B) | `0x2882dc000`–`0x2882e3fff` |
| 2 | `0x88078000` | `0x4000` (16,384 B) | `0x288078000`–`0x28807bfff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1343`

## All properties (16) [DT]

- **`AAPL,phandle`**: `78` (`0x4e`) → phandle of [`/arm-io/aes`](root__arm-io__aes.md)
- **`address-width`**: `42` (`0x2a`)
- **`aes-version`**: `6` (`0x6`)
- **`clock-gates`**: `25` (`0x19`)
- **`compatible`**: `aes,s8000`
- **`device_type`**: `aes`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `1343` (`0x53f`)
- **`iommu-parent`**: `140` (`0x8c`) → phandle of [`/arm-io/dart-sio/mapper-aes`](root__arm-io__dart-sio__mapper-aes.md)
- **`name`**: `aes`
- **`reg`**: 48 bytes
  - u32: `0xa500c000 0x0 0x4000 0x0 0x882dc000 0x0 0x8000 0x0 0x88078000 0x0 0x4000 0x0`
  ```
  000000  00 c0 00 a5 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000010  00 c0 2d 88 00 00 00 00 00 80 00 00 00 00 00 00  ..-.............
  000020  00 80 07 88 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`service-gates`**: `25` (`0x19`)
- **`sioaesdisable-offset`**: `0` (`0x0`)
- **`sioaesdisablegid0-offset`**: `8` (`0x8`)
- **`sioaesdisablegid1-offset`**: `12` (`0xc`)
- **`sioaesdisableuid1-offset`**: `4` (`0x4`)

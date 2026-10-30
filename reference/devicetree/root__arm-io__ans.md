# `/arm-io/ans`

- Name: `ans`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `154`
- compatible: `iop,ascwrap-v8`
- device_type: `ans`
- Children (1): [`/arm-io/ans/iop-ans-nub`](root__arm-io__ans__iop-ans-nub.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleASCWrapV8` | `AppleARMIODevice` | [`com.apple.driver.AppleA7IOP-ASCWrap-v8`](../kexts/com.apple.driver.AppleA7IOP-ASCWrap-v8.md) | `iop,ascwrap-v8` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x101600000` | `0x74000` (475,136 B) | `0x301600000`–`0x301673fff` |
| 1 | `0x101050000` | `0x4000` (16,384 B) | `0x301050000`–`0x301053fff` |
| 2 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |
| 3 | `0x105cc0000` | `0x60000` (393,216 B) | `0x305cc0000`–`0x305d1ffff` |
| 4 | `0x103000000` | `0x1000000` (16,777,216 B) | `0x303000000`–`0x303ffffff` |
| 5 | `0x105b90000` | `0x10000` (65,536 B) | `0x305b90000`–`0x305b9ffff` |
| 6 | `0x105d47c00` | `0x4000` (16,384 B) | `0x305d47c00`–`0x305d4bbff` |
| 7 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 8 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 9 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 10 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 11 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 12 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 13 | `0x0` | `0x0` (0 B) | `0x200000000`–`0x200000000` |
| 14 | `0x105040000` | `0x4000` (16,384 B) | `0x305040000`–`0x305043fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`201, 161, 121, 1280`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `spi0_sclk_config` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x16 0x10001` |
| `spi0_mosi_config` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x15 0x10001` |

## Firmware with a matching name [FW]

- [`Firmware/ansf.t8160.release.im4p`](../firmware/Firmware__ansf.t8160.release.im4p.md) (1,396,223 B) Tag: IM4P  Type: ansf  Version: AppleStorageFirmware-3975.40.15~303

## All properties (32) [DT]

- **`AAPL,phandle`**: `154` (`0x9a`) → phandle of [`/arm-io/ans`](root__arm-io__ans.md)
- **`clock-gates`**: (present, empty)
- **`clock-ids`**: 12 bytes
  - u32: `0x14d 0x14c 0x14e`
  ```
  000000  4d 01 00 00 4c 01 00 00 4e 01 00 00              M...L...N...
  ```
- **`compatible`**: `iop,ascwrap-v8`
- **`device_type`**: `ans`
- **`function-spi0_mosi_config`**: 16 bytes
  - u32: `0x35 0x4750494f 0x15 0x10001`
  - text inside: `OIPG`
  ```
  000000  35 00 00 00 4f 49 50 47 15 00 00 00 01 00 01 00  5...OIPG........
  ```
- **`function-spi0_sclk_config`**: 16 bytes
  - u32: `0x35 0x4750494f 0x16 0x10001`
  - text inside: `OIPG`
  ```
  000000  35 00 00 00 4f 49 50 47 16 00 00 00 01 00 01 00  5...OIPG........
  ```
- **`ignore-gating`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 16 bytes
  - u32: `0xc9 0xa1 0x79 0x500`
  ```
  000000  c9 00 00 00 a1 00 00 00 79 00 00 00 00 05 00 00  ........y.......
  ```
- **`iommu-parent`**: `156` (`0x9c`) → phandle of [`/arm-io/sart-ans`](root__arm-io__sart-ans.md)
- **`iop-version`**: `1` (`0x1`)
- **`msgbox-mailbox-num`**: `7` (`0x7`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`msp-bfh-params`**: 60 bytes
  - u32: `0x20001 0xdeadbeef 0x2 0x18 0xffffffff 0xc0003 0x4f5f6f4e 0x72726576 0x73656469 0x40004 0x1 0xdeadbeef 0x5 0x0 0xffffffff`
  - text inside: `No_Overrides`
  ```
  000000  01 00 02 00 ef be ad de 02 00 00 00 18 00 00 00  ................
  000010  ff ff ff ff 03 00 0c 00 4e 6f 5f 4f 76 65 72 72  ........No_Overr
  000020  69 64 65 73 04 00 04 00 01 00 00 00 ef be ad de  ides............
  000030  05 00 00 00 00 00 00 00 ff ff ff ff              ............
  ```
- **`msp-phy-fw-path`**: `t303.aus5`
- **`name`**: `ans`
- **`namespaces`**: 96 bytes
  - u32: `0x1 0x1 0x0 0x2 0xe 0x800 0x3 0x3 0x20 0x4 0x4 0x2 0x5 0x5 0x2 0x6 0x8 0x100 0x7 0xd 0x8000 0x8 0xf 0xff000000`
  ```
  000000  01 00 00 00 01 00 00 00 00 00 00 00 02 00 00 00  ................
  000010  0e 00 00 00 00 08 00 00 03 00 00 00 03 00 00 00  ................
  000020  20 00 00 00 04 00 00 00 04 00 00 00 02 00 00 00   ...............
  000030  05 00 00 00 05 00 00 00 02 00 00 00 06 00 00 00  ................
  000040  08 00 00 00 00 01 00 00 07 00 00 00 0d 00 00 00  ................
  000050  00 80 00 00 08 00 00 00 0f 00 00 00 00 00 00 ff  ................
  ```
- **`nand-debug`**: `0x1` (u64; as two u32: `0x1`, `0x0`)
- **`nvme-ans-ppm-budget`**: `3000` (`0xbb8`)
- **`nvme-ans-selected-hash-type`**: `SHA3-256-4K`
- **`nvme-ans-sha-present`**: (present, empty)
- **`nvme-ans-supported-hash-types`**: `SHA3-256-4K:SHA3-384-4K:SHA3-512-4K`
- **`nvme-interrupt-idx`**: `3` (`0x3`)
- **`nvme-linear-sq`**: (present, empty)
- **`nvme-queue-entries`**: `64` (`0x40`)
- **`nvme-secure-reg-layout`**: (present, empty)
- **`power-gates`**: (present, empty)
- **`reg`**: 240 bytes
  - u32: `0x1600000 0x1 0x74000 0x0 0x1050000 0x1 0x4000 0x0 0x96020000 0x0 0x10000 0x0 0x5cc0000 0x1 0x60000 0x0 0x3000000 0x1 0x1000000 0x0 0x5b90000 0x1 0x10000 0x0 0x5d47c00 0x1 0x4000 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x5040000 0x1 0x4000 0x0`
  ```
  000000  00 00 60 01 01 00 00 00 00 40 07 00 00 00 00 00  ..`......@......
  000010  00 00 05 01 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  000030  00 00 cc 05 01 00 00 00 00 00 06 00 00 00 00 00  ................
  000040  00 00 00 03 01 00 00 00 00 00 00 01 00 00 00 00  ................
  000050  00 00 b9 05 01 00 00 00 00 00 01 00 00 00 00 00  ................
  000060  00 7c d4 05 01 00 00 00 00 40 00 00 00 00 00 00  .|.......@......
  000070  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000080  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000090  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000a0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000b0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000c0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000d0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  0000e0  00 00 04 05 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`role`**: `ANS2`
- **`tunable-table-bundle`**: `qwdbnujv`

# `/arm-io/mcc`

- Name: `mcc`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `54`
- compatible: `mcc,t8160`
- device_type: `mcc`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8160MemCacheController` | `AppleARMIODevice` | [`com.apple.driver.AppleT8160MCC`](../kexts/com.apple.driver.AppleT8160MCC.md) | `mcc,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x80780000` | `0x4000` (16,384 B) | `0x280780000`–`0x280783fff` |
| 1 | `0x20000000` | `0x100000` (1,048,576 B) | `0x220000000`–`0x2200fffff` |
| 2 | `0x4f010000` | `0x8000` (32,768 B) | `0x24f010000`–`0x24f017fff` |
| 3 | `0x50010000` | `0x8000` (32,768 B) | `0x250010000`–`0x250017fff` |
| 4 | `0x51010000` | `0x8000` (32,768 B) | `0x251010000`–`0x251017fff` |
| 5 | `0x52010000` | `0x8000` (32,768 B) | `0x252010000`–`0x252017fff` |
| 6 | `0x803c0000` | `0x4000` (16,384 B) | `0x2803c0000`–`0x2803c3fff` |
| 7 | `0x803d0000` | `0x4000` (16,384 B) | `0x2803d0000`–`0x2803d3fff` |
| 8 | `0x21000000` | `0x10000` (65,536 B) | `0x221000000`–`0x22100ffff` |
| 9 | `0x21200000` | `0x10000` (65,536 B) | `0x221200000`–`0x22120ffff` |
| 10 | `0x21400000` | `0x10000` (65,536 B) | `0x221400000`–`0x22140ffff` |
| 11 | `0x21600000` | `0x10000` (65,536 B) | `0x221600000`–`0x22160ffff` |
| 12 | `0x21800000` | `0x10000` (65,536 B) | `0x221800000`–`0x22180ffff` |
| 13 | `0x21a00000` | `0x10000` (65,536 B) | `0x221a00000`–`0x221a0ffff` |

## Referenced by (9) [DT]

- [`/arm-io/error-handler`](root__arm-io__error-handler.md): function-amcc-sram-eventhandler `M$DS`
- [`/arm-io/disp0`](root__arm-io__disp0.md): function-mcc_dataset `M$DS`
- [`/arm-io/dispsec`](root__arm-io__dispsec.md): function-mcc_dataset `M$DS`
- [`/arm-io/ispRtb`](root__arm-io__ispRtb.md): function-mcc_dataset `M$DS`
- [`/arm-io/ave`](root__arm-io__ave.md): function-mcc_dataset `M$DS`
- [`/arm-io/avd`](root__arm-io__avd.md): function-mcc_dataset `M$DS`
- [`/arm-io/ane0`](root__arm-io__ane0.md): function-mcc_dataset `M$DS`
- [`/arm-io/ane1`](root__arm-io__ane1.md): function-mcc_dataset `M$DS`
- [`/arm-io/sgx`](root__arm-io__sgx.md): function-mcc_dataset `M$DS`

## All properties (22) [DT]

- **`AAPL,phandle`**: `54` (`0x36`) → phandle of [`/arm-io/mcc`](root__arm-io__mcc.md)
- **`amcc-count`**: `1` (`0x1`)
- **`amcc-plane-enable-mask`**: `7` (`0x7`)
- **`amcc-reg-idx`**: `1` (`0x1`)
- **`compatible`**: `mcc,t8160`
- **`dcs-channel-enable-mask`**: `63` (`0x3f`)
- **`dcs-count-per-amcc`**: `6` (`0x6`)
- **`dcs-reg-idx`**: `8` (`0x8`)
- **`device_type`**: `mcc`
- **`dramcfg-data`**: `0x5555534000000133` (u64; as two u32: `0x133`, `0x55555340`)
- **`dsid_mgmt`**: `1` (`0x1`)
- **`flush-cache-on-panic`**: `0` (`0x0`)
- **`name`**: `mcc`
- **`panic-save-reg-idx`**: `0` (`0x0`)
- **`pmp_ptd_db_reg_idx`**: `6` (`0x6`)
- **`pmp_ptd_update_reg_idx`**: `7` (`0x7`)
- **`ptd-range-ctrl2drv`**: `30` (`0x1e`)
- **`ptd-range-drv2ctrl`**: `14` (`0xe`)
- **`reg`**: 224 bytes
  - u32: `0x80780000 0x0 0x4000 0x0 0x20000000 0x0 0x100000 0x0 0x4f010000 0x0 0x8000 0x0 0x50010000 0x0 0x8000 0x0 0x51010000 0x0 0x8000 0x0 0x52010000 0x0 0x8000 0x0 0x803c0000 0x0 0x4000 0x0 0x803d0000 0x0 0x4000 0x0 0x21000000 0x0 0x10000 0x0 0x21200000 0x0 0x10000 0x0 0x21400000 0x0 0x10000 0x0 0x21600000 0x0 0x10000 0x0 0x21800000 0x0 0x10000 0x0 0x21a00000 0x0 0x10000 0x0`
  ```
  000000  00 00 78 80 00 00 00 00 00 40 00 00 00 00 00 00  ..x......@......
  000010  00 00 00 20 00 00 00 00 00 00 10 00 00 00 00 00  ... ............
  000020  00 00 01 4f 00 00 00 00 00 80 00 00 00 00 00 00  ...O............
  000030  00 00 01 50 00 00 00 00 00 80 00 00 00 00 00 00  ...P............
  000040  00 00 01 51 00 00 00 00 00 80 00 00 00 00 00 00  ...Q............
  000050  00 00 01 52 00 00 00 00 00 80 00 00 00 00 00 00  ...R............
  000060  00 00 3c 80 00 00 00 00 00 40 00 00 00 00 00 00  ..<......@......
  000070  00 00 3d 80 00 00 00 00 00 40 00 00 00 00 00 00  ..=......@......
  000080  00 00 00 21 00 00 00 00 00 00 01 00 00 00 00 00  ...!............
  000090  00 00 20 21 00 00 00 00 00 00 01 00 00 00 00 00  .. !............
  0000a0  00 00 40 21 00 00 00 00 00 00 01 00 00 00 00 00  ..@!............
  0000b0  00 00 60 21 00 00 00 00 00 00 01 00 00 00 00 00  ..`!............
  0000c0  00 00 80 21 00 00 00 00 00 00 01 00 00 00 00 00  ...!............
  0000d0  00 00 a0 21 00 00 00 00 00 00 01 00 00 00 00 00  ...!............
  ```
- **`skip-mcc-off-to-s2r`**: `1` (`0x1`)
- **`socni-count`**: `4` (`0x4`)
- **`socni-reg-idx`**: `2` (`0x2`)

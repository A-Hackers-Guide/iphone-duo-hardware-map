# `/arm-io/scaler0`

- Name: `scaler0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `290`
- compatible: `scaler,t8101`, `scaler,s5l8960x`
- device_type: `scaler`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleM2ScalerCSCDriver` | `AppleARMIODevice` | [`com.apple.driver.AppleM2ScalerCSCDriver`](../kexts/com.apple.driver.AppleM2ScalerCSCDriver.md) | `scaler,s5l8960x` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x209000000` | `0x14000` (81,920 B) | `0x409000000`–`0x409013fff` |
| 1 | `0x209210000` | `0x4000` (16,384 B) | `0x409210000`–`0x409213fff` |
| 2 | `0x209204000` | `0x4000` (16,384 B) | `0x409204000`–`0x409207fff` |
| 3 | `0x208000000` | `0x8000` (32,768 B) | `0x408000000`–`0x408007fff` |
| 4 | `0x2092c0000` | `0x40000` (262,144 B) | `0x4092c0000`–`0x4092fffff` |
| 5 | `0x209340000` | `0x23c000` (2,342,912 B) | `0x409340000`–`0x40957bfff` |
| 6 | `0x2092a0000` | `0x4000` (16,384 B) | `0x4092a0000`–`0x4092a3fff` |
| 7 | `0x209208000` | `0x4000` (16,384 B) | `0x409208000`–`0x40920bfff` |
| 8 | `0x80700000` | `0x1c000` (114,688 B) | `0x280700000`–`0x28071bfff` |
| 9 | `0x209210000` | `0x4000` (16,384 B) | `0x409210000`–`0x409213fff` |
| 10 | `0x209220000` | `0x4000` (16,384 B) | `0x409220000`–`0x409223fff` |
| 11 | `0x96020000` | `0x10000` (65,536 B) | `0x296020000`–`0x29602ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1290, 1292, 1293, 1294, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 168, 208, 128`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `get_valid_perf_states` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFG` | `0x2d 0x2` |
| `device_reset` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `ARST` | `0x11` |
| `set_perf_state_floor` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `PRFS` | `0x2d 0x2` |

## All properties (22) [DT]

- **`AAPL,phandle`**: `290` (`0x122`) → phandle of [`/arm-io/scaler0`](root__arm-io__scaler0.md)
- **`clock-gates`**: `45` (`0x2d`)
- **`clock-ids`**: `350` (`0x15e`)
- **`compatible`**: `scaler,t8101`, `scaler,s5l8960x`
- **`coprovider-group`**: `scaler`
- **`device_type`**: `scaler`
- **`function-device_reset`**: 12 bytes
  - u32: `0x30 0x41525354 0x11`
  - text inside: `TSRA`
  ```
  000000  30 00 00 00 54 53 52 41 11 00 00 00              0...TSRA....
  ```
- **`function-get_valid_perf_states`**: 16 bytes
  - u32: `0x30 0x50524647 0x2d 0x2`
  - text inside: `GFRP-`
  ```
  000000  30 00 00 00 47 46 52 50 2d 00 00 00 02 00 00 00  0...GFRP-.......
  ```
- **`function-set_perf_state_floor`**: 16 bytes
  - u32: `0x30 0x50524653 0x2d 0x2`
  - text inside: `SFRP-`
  ```
  000000  30 00 00 00 53 46 52 50 2d 00 00 00 02 00 00 00  0...SFRP-.......
  ```
- **`hardware-version`**: `27` (`0x1b`)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 60 bytes
  - u32: `0x50a 0x50c 0x50d 0x50e 0x512 0x513 0x514 0x515 0x516 0x517 0x518 0x519 0xa8 0xd0 0x80`
  ```
  000000  0a 05 00 00 0c 05 00 00 0d 05 00 00 0e 05 00 00  ................
  000010  12 05 00 00 13 05 00 00 14 05 00 00 15 05 00 00  ................
  000020  16 05 00 00 17 05 00 00 18 05 00 00 19 05 00 00  ................
  000030  a8 00 00 00 d0 00 00 00 80 00 00 00              ............
  ```
- **`iommu-parent`**: `0x12500000124` (u64; as two u32: `0x124`, `0x125`)
- **`msgbox-mailbox-num`**: `14` (`0xe`)
- **`msgbox-using-alias`**: `true`
- **`msgbox-using-postoffice`**: `true`
- **`name`**: `scaler0`
- **`power-gates`**: `45` (`0x2d`)
- **`reg`**: 192 bytes
  - u32: `0x9000000 0x2 0x14000 0x0 0x9210000 0x2 0x4000 0x0 0x9204000 0x2 0x4000 0x0 0x8000000 0x2 0x8000 0x0 0x92c0000 0x2 0x40000 0x0 0x9340000 0x2 0x23c000 0x0 0x92a0000 0x2 0x4000 0x0 0x9208000 0x2 0x4000 0x0 0x80700000 0x0 0x1c000 0x0 0x9210000 0x2 0x4000 0x0 0x9220000 0x2 0x4000 0x0 0x96020000 0x0 0x10000 0x0`
  ```
  000000  00 00 00 09 02 00 00 00 00 40 01 00 00 00 00 00  .........@......
  000010  00 00 21 09 02 00 00 00 00 40 00 00 00 00 00 00  ..!......@......
  000020  00 40 20 09 02 00 00 00 00 40 00 00 00 00 00 00  .@ ......@......
  000030  00 00 00 08 02 00 00 00 00 80 00 00 00 00 00 00  ................
  000040  00 00 2c 09 02 00 00 00 00 00 04 00 00 00 00 00  ..,.............
  000050  00 00 34 09 02 00 00 00 00 c0 23 00 00 00 00 00  ..4.......#.....
  000060  00 00 2a 09 02 00 00 00 00 40 00 00 00 00 00 00  ..*......@......
  000070  00 80 20 09 02 00 00 00 00 40 00 00 00 00 00 00  .. ......@......
  000080  00 00 70 80 00 00 00 00 00 c0 01 00 00 00 00 00  ..p.............
  000090  00 00 21 09 02 00 00 00 00 40 00 00 00 00 00 00  ..!......@......
  0000a0  00 00 22 09 02 00 00 00 00 40 00 00 00 00 00 00  .."......@......
  0000b0  00 00 02 96 00 00 00 00 00 00 01 00 00 00 00 00  ................
  ```
- **`service-gates`**: `45` (`0x2d`)
- **`service-reset`**: `17` (`0x11`)
- **`workload-priority`**: `5` (`0x5`)

# `/arm-io/nub-spmi0/btm`

- Name: `btm`
- Parent: [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)
- phandle: `201`
- compatible: `btm,phone`
- device_type: `btm`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleBTM` | `AppleARMSPMIDevice` | [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md) | `btm,phone` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000e` (12,884,901,902 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)

`1651797296, 1651797297, 1651797298, 1651797299`

## Referenced by (5) [DT]

- [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md): function-btm-start `BMST`
- [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md): function-btm-config-battfw `BMC1`
- [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md): function-btm-stop `BMSP`
- [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md): function-btm-config `BMCO`
- [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md): function-btm-vthr `BMVT`

## All properties (17) [DT]

- **`AAPL,phandle`**: `201` (`0xc9`) → phandle of [`/arm-io/nub-spmi0/btm`](root__arm-io__nub-spmi0__btm.md)
- **`battery-data-clients`**: `1` (`0x1`)
- **`battery-data-collection`**: `1` (`0x1`)
- **`btm-pmu-type`**: `15` (`0xf`)
- **`compatible`**: `btm,phone`
- **`config-auto-rate-change-flag`**: `1` (`0x1`)
- **`config-duty-cycle-data-read`**: `1` (`0x1`)
- **`config-vddmain-data-read`**: `1` (`0x1`)
- **`device_type`**: `btm`
- **`function_ptd_read_mult`**: `0x70744d52000000a6` (u64; as two u32: `0xa6`, `0x70744d52`)
- **`interrupt-parent`**: `166` (`0xa6`) → phandle of [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md)
- **`interrupts`**: 16 bytes
  - u32: `0x62746d30 0x62746d31 0x62746d32 0x62746d33`
  - text inside: `0mtb1mtb2mtb3mtb`
  ```
  000000  30 6d 74 62 31 6d 74 62 32 6d 74 62 33 6d 74 62  0mtb1mtb2mtb3mtb
  ```
- **`name`**: `btm`
- **`number-of-PMUs`**: `2` (`0x2`)
- **`number-of-batteries`**: `2` (`0x2`)
- **`pack-format-enabled`**: `1` (`0x1`)
- **`reg`**: 24 bytes
  - u32: `0xe 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0e 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

# `/arm-io/aop-spmi0/hammerfest-spmi`

- Name: `hammerfest-spmi`
- Parent: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- phandle: `212`
- compatible: `nfc,secondary,spmi`
- device_type: `hammerfest-spmi`
- Children (1): [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleStockholmSPMI` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | `nfc,secondary,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000c` (12,884,901,900 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)

`160, 161, 162, 163, 164, 165, 166`

## All properties (12) [DT]

- **`#num-spmi-interrupts`**: `7` (`0x7`)
- **`AAPL,phandle`**: `212` (`0xd4`) → phandle of [`/arm-io/aop-spmi0/hammerfest-spmi`](root__arm-io__aop-spmi0__hammerfest-spmi.md)
- **`compatible`**: `nfc,secondary,spmi`
- **`device_type`**: `hammerfest-spmi`
- **`interrupt-parent`**: `207` (`0xcf`) → phandle of [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- **`interrupts`**: 28 bytes
  - u32: `0xa0 0xa1 0xa2 0xa3 0xa4 0xa5 0xa6`
  ```
  000000  a0 00 00 00 a1 00 00 00 a2 00 00 00 a3 00 00 00  ................
  000010  a4 00 00 00 a5 00 00 00 a6 00 00 00              ............
  ```
- **`name`**: `hammerfest-spmi`
- **`nfccModel`**: `189` (`0xbd`)
- **`nfccModel_A0`**: `188` (`0xbc`)
- **`reg`**: 24 bytes
  - u32: `0xc 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0c 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```
- **`required-functions`**: `support_host_wake_spmi`, `support_data_over_spmi`
- **`skip-spmi-reconfig`**: (present, empty)

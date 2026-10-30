# `/arm-io/aop-spmi0/stockholm-spmi`

- Name: `stockholm-spmi`
- Parent: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- phandle: `210`
- compatible: `nfc,primary,spmi`
- device_type: `stockholm-spmi`
- Children (1): [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleStockholmSPMI` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | `nfc,primary,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x300000008` (12,884,901,896 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)

`176, 177, 178, 179, 180, 181, 182`

## Firmware with a matching name [FW]

- [`Firmware/SE/Stockholm91.RELEASE.sefw`](../firmware/Firmware__SE__Stockholm91.RELEASE.sefw.md) (5,978,021 B) 

## All properties (13) [DT]

- **`#num-spmi-interrupts`**: `7` (`0x7`)
- **`AAPL,phandle`**: `210` (`0xd2`) → phandle of [`/arm-io/aop-spmi0/stockholm-spmi`](root__arm-io__aop-spmi0__stockholm-spmi.md)
- **`compatible`**: `nfc,primary,spmi`
- **`device_type`**: `stockholm-spmi`
- **`interrupt-parent`**: `207` (`0xcf`) → phandle of [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- **`interrupts`**: 28 bytes
  - u32: `0xb0 0xb1 0xb2 0xb3 0xb4 0xb5 0xb6`
  ```
  000000  b0 00 00 00 b1 00 00 00 b2 00 00 00 b3 00 00 00  ................
  000010  b4 00 00 00 b5 00 00 00 b6 00 00 00              ............
  ```
- **`name`**: `stockholm-spmi`
- **`nfccModel`**: `223` (`0xdf`)
- **`nfccModel-A0`**: `218` (`0xda`)
- **`reg`**: 24 bytes
  - u32: `0x8 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  08 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```
- **`required-functions`**: `support_host_wake_spmi`, `support_data_over_spmi`
- **`skip-spmi-reconfig`**: (present, empty)
- **`spmiFollowerReset`**: `1` (`0x1`) → phandle of [`/`](root.md)

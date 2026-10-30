# `/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`

- Name: `hammerfest`
- Parent: [`/arm-io/aop-spmi0/hammerfest-spmi`](root__arm-io__aop-spmi0__hammerfest-spmi.md)
- phandle: `213`
- compatible: `nfc,secondary,gpio`
- device_type: `hammerfest`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleStockholmControl` | `IOService` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | `nfc,secondary,gpio` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `boot_measurements` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x83 0x101` |
| `enable` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x6 0x101` |

## All properties (10) [DT]

- **`AAPL,phandle`**: `213` (`0xd5`) → phandle of [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md)
- **`compatible`**: `nfc,secondary,gpio`
- **`device_type`**: `hammerfest`
- **`function-boot_measurements`**: 16 bytes
  - u32: `0x35 0x4750494f 0x83 0x101`
  - text inside: `OIPG`
  ```
  000000  35 00 00 00 4f 49 50 47 83 00 00 00 01 01 00 00  5...OIPG........
  ```
- **`function-enable`**: 16 bytes
  - u32: `0x72 0x4750494f 0x6 0x101`
  - text inside: `OIPG`
  ```
  000000  72 00 00 00 4f 49 50 47 06 00 00 00 01 01 00 00  r...OIPG........
  ```
- **`name`**: `hammerfest`
- **`nfcWithRadio`**: `1` (`0x1`)
- **`required-gpios`**: `support_venable`, `support_virtual_gpio`, `support_boot_measurements`
- **`rf-antenna-name`**: `RTM8_8S`
- **`supports-nfc-reader-mode`**: (present, empty)

# `/arm-io/aop-spmi0/stockholm-spmi/stockholm`

- Name: `stockholm`
- Parent: [`/arm-io/aop-spmi0/stockholm-spmi`](root__arm-io__aop-spmi0__stockholm-spmi.md)
- phandle: `211`
- compatible: `nfc,primary,gpio`
- device_type: `stockholm`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleStockholmControl` | `IOService` | [`com.apple.driver.AppleStockholmControl`](../kexts/com.apple.driver.AppleStockholmControl.md) | `nfc,primary,gpio` |

## Interrupts [DT]

Controller: [`/arm-io/gpio0`](root__arm-io__gpio0.md)

`142, 2`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `se_boot_measurements` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x80 0x101` |
| `enable` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0x150000` |
| `boot_measurements` | [`/arm-io/gpio0`](root__arm-io__gpio0.md) | `GPIO` | `0x69 0x101` |

## Firmware with a matching name [FW]

- [`Firmware/SE/Stockholm91.RELEASE.sefw`](../firmware/Firmware__SE__Stockholm91.RELEASE.sefw.md) (5,978,021 B) 

## All properties (15) [DT]

- **`AAPL,phandle`**: `211` (`0xd3`) → phandle of [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md)
- **`compatible`**: `nfc,primary,gpio`
- **`device_type`**: `stockholm`
- **`eos-halley-config`**: `1` (`0x1`)
- **`function-boot_measurements`**: 16 bytes
  - u32: `0x35 0x4750494f 0x69 0x101`
  - text inside: `OIPGi`
  ```
  000000  35 00 00 00 4f 49 50 47 69 00 00 00 01 01 00 00  5...OIPGi.......
  ```
- **`function-enable`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x7063494f 0x800000 0x150000`
  - text inside: `8WKpOIcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 4f 49 63 70 00 00 80 00  ....8WKpOIcp....
  000010  00 00 15 00                                      ....
  ```
- **`function-se_boot_measurements`**: 16 bytes
  - u32: `0x35 0x4750494f 0x80 0x101`
  - text inside: `OIPG`
  ```
  000000  35 00 00 00 4f 49 50 47 80 00 00 00 01 01 00 00  5...OIPG........
  ```
- **`interrupt-parent`**: `53` (`0x35`) → phandle of [`/arm-io/gpio0`](root__arm-io__gpio0.md)
- **`interrupts`**: `0x20000008e` (u64; as two u32: `0x8e`, `0x2`)
- **`name`**: `stockholm`
- **`nfcWithRadio`**: `1` (`0x1`)
- **`required-gpios`**: `support_venable`, `support_virtual_gpio`, `support_boot_measurements`, `support_bootstop-interrupts`
- **`rf-antenna-name`**: `RTM8_8`
- **`sn450WithLoadSwitch`**: `1` (`0x1`)
- **`supports-nfc-reader-mode`**: (present, empty)

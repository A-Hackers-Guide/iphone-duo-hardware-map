# `/arm-io/gpio0`

- Name: `gpio0`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `53`
- compatible: `gpio,t8101`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8101GPIOIC` | `AppleARMIODevice` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) | `gpio,t8101` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x9a000000` | `0x100000` (1,048,576 B) | `0x29a000000`–`0x29a0fffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`327, 328, 329, 330, 331, 332, 333`

## Referenced by (15) [DT]

- [`/arm-io/wdt`](root__arm-io__wdt.md): function-panic_notify `GPIO`
- [`/arm-io/ans`](root__arm-io__ans.md): function-spi0_sclk_config `GPIO`
- [`/arm-io/ans`](root__arm-io__ans.md): function-spi0_mosi_config `GPIO`
- [`/arm-io/uart0`](root__arm-io__uart0.md): function-tx `GPIO`
- [`/arm-io/uart0`](root__arm-io__uart0.md): function-rx `GPIO`
- [`/arm-io/i2c2/audio-codec`](root__arm-io__i2c2__audio-codec.md): interrupts 134, 1
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md): function-se_boot_measurements `GPIO`
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md): function-boot_measurements `GPIO`
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md): interrupts 142, 2
- [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md): function-boot_measurements `GPIO`
- [`/arm-io/apcie`](root__arm-io__apcie.md): function-debug_gpio `GPIO`
- [`/arm-io/aod2`](root__arm-io__aod2.md): function-aod_swclk `GPIO`
- [`/arm-io/aod2`](root__arm-io__aod2.md): function-aod_swdio `GPIO`
- [`/arm-io/aod4`](root__arm-io__aod4.md): function-aod_swclk `GPIO`
- [`/arm-io/aod4`](root__arm-io__aod4.md): function-aod_swdio `GPIO`

## All properties (15) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#gpio-int-groups`**: `7` (`0x7`)
- **`#gpio-pins`**: `214` (`0xd6`)
- **`#interrupt-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `53` (`0x35`) → phandle of [`/arm-io/gpio0`](root__arm-io__gpio0.md)
- **`compatible`**: `gpio,t8101`
- **`device_type`**: `interrupt-controller`
- **`glitchless`**: `1` (`0x1`)
- **`ie-fix`**: `1` (`0x1`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 28 bytes
  - u32: `0x147 0x148 0x149 0x14a 0x14b 0x14c 0x14d`
  ```
  000000  47 01 00 00 48 01 00 00 49 01 00 00 4a 01 00 00  G...H...I...J...
  000010  4b 01 00 00 4c 01 00 00 4d 01 00 00              K...L...M...
  ```
- **`name`**: `gpio0`
- **`reg`**: 16 bytes
  - u32: `0x9a000000 0x0 0x100000 0x0`
  ```
  000000  00 00 00 9a 00 00 00 00 00 00 10 00 00 00 00 00  ................
  ```
- **`role`**: `AP`

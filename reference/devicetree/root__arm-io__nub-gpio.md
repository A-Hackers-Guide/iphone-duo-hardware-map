# `/arm-io/nub-gpio`

- Name: `nub-gpio`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `115`
- compatible: `gpio,t8101`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8101GPIOIC` | `AppleARMIODevice` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) | `gpio,t8101` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x881f0000` | `0x4000` (16,384 B) | `0x2881f0000`–`0x2881f3fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`553, 554, 555, 556, 557, 558, 559`

## Referenced by (5) [DT]

- [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md): interrupts 12, 83886083
- [`/arm-io/aod3`](root__arm-io__aod3.md): function-aod_swclk `GPIO`
- [`/arm-io/aod3`](root__arm-io__aod3.md): function-aod_swdio `GPIO`
- [`/centauri`](root__centauri.md): function-error_detect `GPIO`
- [`/centauri`](root__centauri.md): interrupts 22, 100663300

## All properties (20) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#gpio-int-groups`**: `7` (`0x7`)
- **`#gpio-pins`**: `32` (`0x20`)
- **`#interrupt-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `115` (`0x73`) → phandle of [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md)
- **`compatible`**: `gpio,t8101`
- **`device_type`**: `interrupt-controller`
- **`event_name-mask15`**: `dock`
- **`glitchless`**: `1` (`0x1`)
- **`ie-fix`**: `1` (`0x1`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 28 bytes
  - u32: `0x229 0x22a 0x22b 0x22c 0x22d 0x22e 0x22f`
  ```
  000000  29 02 00 00 2a 02 00 00 2b 02 00 00 2c 02 00 00  )...*...+...,...
  000010  2d 02 00 00 2e 02 00 00 2f 02 00 00              -......./...
  ```
- **`name`**: `nub-gpio`
- **`no-resume-restore`**: `1` (`0x1`)
- **`reg`**: 16 bytes
  - u32: `0x881f0000 0x0 0x4000 0x0`
  ```
  000000  00 00 1f 88 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`role`**: `NUB`
- **`supported-int-groups`**: 12 bytes
  - u32: `0x4 0x5 0x6`
  ```
  000000  04 00 00 00 05 00 00 00 06 00 00 00              ............
  ```
- **`wake-events`**: `3846` (`0xf06`)
- **`wake-no-interrupt-group`**: `4` (`0x4`)

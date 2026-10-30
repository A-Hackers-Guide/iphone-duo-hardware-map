# `/arm-io/smc-gpio`

- Name: `smc-gpio`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `116`
- compatible: `gpio,t8101`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleT8101GPIOIC` | `AppleARMIODevice` | [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md) | `gpio,t8101` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x8c820000` | `0x4000` (16,384 B) | `0x28c820000`–`0x28c823fff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`606, 607, 608, 609, 610, 611, 612`

## All properties (18) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#gpio-int-groups`**: `7` (`0x7`)
- **`#gpio-pins`**: `6` (`0x6`)
- **`#interrupt-cells`**: `2` (`0x2`)
- **`AAPL,phandle`**: `116` (`0x74`) → phandle of [`/arm-io/smc-gpio`](root__arm-io__smc-gpio.md)
- **`compatible`**: `gpio,t8101`
- **`device_type`**: `interrupt-controller`
- **`glitchless`**: `1` (`0x1`)
- **`ie-fix`**: `1` (`0x1`)
- **`interrupt-controller`**: (present, empty)
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: 28 bytes
  - u32: `0x25e 0x25f 0x260 0x261 0x262 0x263 0x264`
  ```
  000000  5e 02 00 00 5f 02 00 00 60 02 00 00 61 02 00 00  ^..._...`...a...
  000010  62 02 00 00 63 02 00 00 64 02 00 00              b...c...d...
  ```
- **`name`**: `smc-gpio`
- **`no-resume-restore`**: `1` (`0x1`)
- **`reg`**: 16 bytes
  - u32: `0x8c820000 0x0 0x4000 0x0`
  ```
  000000  00 00 82 8c 00 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`role`**: `SMC`
- **`supported-int-groups`**: `0x600000005` (u64; as two u32: `0x5`, `0x6`)
- **`wake-events`**: (present, empty)

# `/arm-io/aop-spmi0/baseband-heb`

- Name: `baseband-heb`
- Parent: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- phandle: `209`
- compatible: `baseband,heb`
- device_type: `baseband-heb`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleBasebandSPMIHEB` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md) | `baseband,heb` |
| `AppleSARSPMIHEB` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | `baseband,heb` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000d` (12,884,901,901 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)

`0, 71, 65, 75, 29, 76, 78`

## All properties (16) [DT]

- **`#num-spmi-interrupts`**: `7` (`0x7`)
- **`AAPL,phandle`**: `209` (`0xd1`) → phandle of [`/arm-io/aop-spmi0/baseband-heb`](root__arm-io__aop-spmi0__baseband-heb.md)
- **`compatible`**: `baseband,heb`
- **`device_type`**: `baseband-heb`
- **`interrupt-parent`**: `207` (`0xcf`) → phandle of [`/arm-io/aop-spmi0`](root__arm-io__aop-spmi0.md)
- **`interrupts`**: 28 bytes
  - u32: `0x0 0x47 0x41 0x4b 0x1d 0x4c 0x4e`
  ```
  000000  00 00 00 00 47 00 00 00 41 00 00 00 4b 00 00 00  ....G...A...K...
  000010  1d 00 00 00 4c 00 00 00 4e 00 00 00              ....L...N...
  ```
- **`irq-tx-offset-billboard-send0`**: `18` (`0x12`)
- **`irq-tx-offset-billboard-send1`**: `19` (`0x13`)
- **`irq-tx-offset-billboard-send2`**: `31` (`0x1f`)
- **`irq-tx-offset-ocp-read-complete`**: `27` (`0x1b`)
- **`irq-tx-offset-ocp-send`**: `12` (`0xc`)
- **`msg-buffer-address-rx-ocp`**: `160` (`0xa0`)
- **`msg-buffer-address-tx-billboard`**: `32` (`0x20`)
- **`msg-buffer-address-tx-ocp`**: `4224` (`0x1080`)
- **`name`**: `baseband-heb`
- **`reg`**: 24 bytes
  - u32: `0xd 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0d 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

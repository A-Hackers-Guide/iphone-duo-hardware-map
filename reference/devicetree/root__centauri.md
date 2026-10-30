# `/centauri`

- Name: `centauri`
- Parent: [`/`](root.md)
- phandle: `505`
- device_type: `centauri`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleCentauriManagerHelper` | `IOService` | [`com.apple.driver.AppleCentauriManager`](../kexts/com.apple.driver.AppleCentauriManager.md) | `centauri` |

## Interrupts [DT]

Controller: [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md)

`22, 100663300`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `error_detect` | [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md) | `GPIO` | `0x16 0x100` |
| `sac` | [`/sacm-general`](root__sacm-general.md) | `SACC` | `0x6472616d` |

## All properties (10) [DT]

- **`AAPL,phandle`**: `505` (`0x1f9`) → phandle of [`/centauri`](root__centauri.md)
- **`device_type`**: `centauri`
- **`function-error_detect`**: 16 bytes
  - u32: `0x73 0x4750494f 0x16 0x100`
  - text inside: `OIPG`
  ```
  000000  73 00 00 00 4f 49 50 47 16 00 00 00 00 01 00 00  s...OIPG........
  ```
- **`function-sac`**: 12 bytes
  - u32: `0x1d2 0x53414343 0x6472616d`
  - text inside: `CCASmard`
  ```
  000000  d2 01 00 00 43 43 41 53 6d 61 72 64              ....CCASmard
  ```
- **`interrupt-parent`**: `115` (`0x73`) → phandle of [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md)
- **`interrupts`**: `0x600000400000016` (u64; as two u32: `0x16`, `0x6000004`)
- **`name`**: `centauri`
- **`pci-bridge-handle`**: `/arm-io/apcie/pci-bridge0`
- **`wifi-antenna-sku-info`**: `syscfg/WSKU` *(placeholder, filled in by iBoot at boot)*
- **`wifi-rfem-info`**: `syscfg/RFEM` *(placeholder, filled in by iBoot at boot)*

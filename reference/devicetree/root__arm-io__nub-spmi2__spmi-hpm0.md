# `/arm-io/nub-spmi2/spmi-hpm0`

- Name: `spmi-hpm0`
- Parent: [`/arm-io/nub-spmi2`](root__arm-io__nub-spmi2.md)
- phandle: `206`
- compatible: `usbc,cbtl1702,spmi`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleHPMARMSPMI` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md) | `usbc,cbtl1702,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000c` (12,884,901,900 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/nub-spmi2`](root__arm-io__nub-spmi2.md)

`11, 17, 19`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `ignore_vbus_drop` | [`/port-usb-c-1`](root__port-usb-c-1.md) | `igvb` | `` |

## All properties (18) [DT]

- **`AAPL,phandle`**: `206` (`0xce`) → phandle of [`/arm-io/nub-spmi2/spmi-hpm0`](root__arm-io__nub-spmi2__spmi-hpm0.md)
- **`aod`**: `438` (`0x1b6`)
- **`compatible`**: `usbc,cbtl1702,spmi`
- **`dock`**: `453` (`0x1c5`)
- **`feature-ldcm-arch-version`**: `5` (`0x5`)
- **`feature-ldcm-hw-version`**: `4` (`0x4`)
- **`features-supported`**: 12 bytes
  - u32: `0x1 0x2 0x5`
  ```
  000000  01 00 00 00 02 00 00 00 05 00 00 00              ............
  ```
- **`function-ignore_vbus_drop`**: `0x69677662000001c5` (u64; as two u32: `0x1c5`, `0x69677662`)
- **`hpm-class-type`**: `15` (`0xf`)
- **`interrupt-parent`**: `205` (`0xcd`) → phandle of [`/arm-io/nub-spmi2`](root__arm-io__nub-spmi2.md)
- **`interrupt-type`**: 12 bytes
  - u32: `0x0 0x2 0x3`
  ```
  000000  00 00 00 00 02 00 00 00 03 00 00 00              ............
  ```
- **`interrupts`**: 12 bytes
  - u32: `0xb 0x11 0x13`
  ```
  000000  0b 00 00 00 11 00 00 00 13 00 00 00              ............
  ```
- **`name`**: `spmi-hpm0`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`reg`**: 24 bytes
  - u32: `0xc 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0c 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```
- **`rid`**: `0` (`0x0`)
- **`transports-supported`**: 16 bytes
  - u32: `0x1 0x2 0x3 0x5`
  ```
  000000  01 00 00 00 02 00 00 00 03 00 00 00 05 00 00 00  ................
  ```

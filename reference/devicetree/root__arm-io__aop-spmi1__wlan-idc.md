# `/arm-io/aop-spmi1/wlan-idc`

- Name: `wlan-idc`
- Parent: [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)
- phandle: `217`
- compatible: `wlan,idc`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSARSPMIIDCWLAN` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | `wlan,idc` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000e` (12,884,901,902 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)

`28, 26, 29, 32`

## All properties (15) [DT]

- **`#num-spmi-interrupts`**: `4` (`0x4`)
- **`AAPL,phandle`**: `217` (`0xd9`) → phandle of [`/arm-io/aop-spmi1/wlan-idc`](root__arm-io__aop-spmi1__wlan-idc.md)
- **`billboard-addr-rx-antcluster`**: `128` (`0x80`)
- **`billboard-addr-rx-regulatory`**: `96` (`0x60`)
- **`billboard-addr-rx-rev`**: `32` (`0x20`)
- **`billboard-addr-rx-sar-report`**: `72` (`0x48`)
- **`billboard-addr-tx-accessory`**: `160` (`0xa0`)
- **`billboard-addr-tx-sar-budget`**: `40` (`0x28`)
- **`compatible`**: `wlan,idc`
- **`interrupt-parent`**: `215` (`0xd7`) → phandle of [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)
- **`interrupts`**: 16 bytes
  - u32: `0x1c 0x1a 0x1d 0x20`
  ```
  000000  1c 00 00 00 1a 00 00 00 1d 00 00 00 20 00 00 00  ............ ...
  ```
- **`irq-tx-offset-accessory`**: `60` (`0x3c`)
- **`irq-tx-offset-sar-budget`**: `61` (`0x3d`)
- **`name`**: `wlan-idc`
- **`reg`**: 24 bytes
  - u32: `0xe 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0e 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

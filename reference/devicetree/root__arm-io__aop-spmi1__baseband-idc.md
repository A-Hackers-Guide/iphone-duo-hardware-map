# `/arm-io/aop-spmi1/baseband-idc`

- Name: `baseband-idc`
- Parent: [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)
- phandle: `218`
- compatible: `baseband,idc`
- device_type: `baseband-idc`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleBasebandSPMIHEB` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md) | `baseband,idc` |
| `AppleSARSPMIIDC` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md) | `baseband,idc` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000d` (12,884,901,901 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)

`0, 71, 65, 75, 29, 2, 6, 7, 8, 9, 3, 4, 89`

## All properties (43) [DT]

- **`#num-spmi-interrupts`**: `13` (`0xd`)
- **`AAPL,phandle`**: `218` (`0xda`) → phandle of [`/arm-io/aop-spmi1/baseband-idc`](root__arm-io__aop-spmi1__baseband-idc.md)
- **`arbuffer-addr-rx`**: `128` (`0x80`)
- **`billboard-addr-rx-e85mitigation`**: `168` (`0xa8`)
- **`billboard-addr-rx-mpe-report`**: `96` (`0x60`)
- **`billboard-addr-rx-regulatory`**: `112` (`0x70`)
- **`billboard-addr-rx-rev`**: `32` (`0x20`)
- **`billboard-addr-rx-sar-report`**: `72` (`0x48`)
- **`billboard-addr-rx-vswr-report`**: `156` (`0x9c`)
- **`billboard-addr-tx-accessory`**: `64` (`0x40`)
- **`billboard-addr-tx-config-vswr`**: `148` (`0x94`)
- **`billboard-addr-tx-deviceupdate`**: `176` (`0xb0`)
- **`billboard-addr-tx-e85mitigation`**: `160` (`0xa0`)
- **`billboard-addr-tx-sar-budget`**: `48` (`0x30`)
- **`billboard-addr-tx-wait-time`**: `120` (`0x78`)
- **`compatible`**: `baseband,idc`
- **`device_type`**: `baseband-idc`
- **`interrupt-parent`**: `215` (`0xd7`) → phandle of [`/arm-io/aop-spmi1`](root__arm-io__aop-spmi1.md)
- **`interrupts`**: 52 bytes
  - u32: `0x0 0x47 0x41 0x4b 0x1d 0x2 0x6 0x7 0x8 0x9 0x3 0x4 0x59`
  ```
  000000  00 00 00 00 47 00 00 00 41 00 00 00 4b 00 00 00  ....G...A...K...
  000010  1d 00 00 00 02 00 00 00 06 00 00 00 07 00 00 00  ................
  000020  08 00 00 00 09 00 00 00 03 00 00 00 04 00 00 00  ................
  000030  59 00 00 00                                      Y...
  ```
- **`irq-tx-offset-accessory`**: `57` (`0x39`)
- **`irq-tx-offset-billboard-send0`**: `18` (`0x12`)
- **`irq-tx-offset-billboard-send1`**: `19` (`0x13`)
- **`irq-tx-offset-billboard-send2`**: `31` (`0x1f`)
- **`irq-tx-offset-config-vswr`**: `59` (`0x3b`)
- **`irq-tx-offset-deviceupdate`**: `67` (`0x43`)
- **`irq-tx-offset-e85mitigation`**: `26` (`0x1a`)
- **`irq-tx-offset-ocp-read-complete`**: `27` (`0x1b`)
- **`irq-tx-offset-ocp-send`**: `13` (`0xd`)
- **`irq-tx-offset-sar-budget`**: `56` (`0x38`)
- **`irq-tx-offset-wait-time`**: `65` (`0x41`)
- **`msg-buffer-address-rx-ocp`**: `160` (`0xa0`)
- **`msg-buffer-address-tx-billboard`**: `32` (`0x20`)
- **`msg-buffer-address-tx-ocp`**: `4224` (`0x1080`)
- **`name`**: `baseband-idc`
- **`reg`**: 24 bytes
  - u32: `0xd 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0d 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```
- **`sar-mpe-ant-cluster-config`**: `40` (`0x28`)
- **`supported-all-radio-version`**: `518` (`0x206`)
- **`supported-ap-gpr0-version`**: `518` (`0x206`)
- **`supported-ar-buffer-version`**: `518` (`0x206`)
- **`supported-non-radio-version`**: `518` (`0x206`)
- **`supports-cellular-boost`**: `0` (`0x0`)
- **`supports-hsar-cellular`**: `1` (`0x1`)
- **`supports-hsar-wifi-bt`**: `1` (`0x1`)

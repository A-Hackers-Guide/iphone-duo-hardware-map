# `/arm-io/apcie0-plce`

- Name: `apcie0-plce`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `428`
- compatible: `plce,t8160`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `APCIECoreRCGen5PLCE` | `AppleARMIODevice` | [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md) | `plce,t8160` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x1cb0000000` | `0x10000000` (268,435,456 B) | `0x1cb0000000`–`0x1cbfffffff` |
| 1 | `0x108028000` | `0x4000` (16,384 B) | `0x308028000`–`0x30802bfff` |
| 2 | `0x10802c000` | `0x4000` (16,384 B) | `0x30802c000`–`0x30802ffff` |

## Interrupts [DT]

Controller: [`/arm-io/aic`](root__arm-io__aic.md)

`1466, 1467`

## All properties (15) [DT]

- **`AAPL,phandle`**: `428` (`0x1ac`) → phandle of [`/arm-io/apcie0-plce`](root__arm-io__apcie0-plce.md)
- **`apcie-path`**: `/arm-io/apcie`
- **`compatible`**: `plce,t8160`
- **`interrupt-parent`**: `45` (`0x2d`) → phandle of [`/arm-io/aic`](root__arm-io__aic.md)
- **`interrupts`**: `0x5bb000005ba` (u64; as two u32: `0x5ba`, `0x5bb`)
- **`iommu-parent`**: `426` (`0x1aa`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-plce`](root__arm-io__dart-apcie0__mapper-apcie0-plce.md)
- **`name`**: `apcie0-plce`
- **`plce-link-init0-script`**: `0` (`0x0`)
- **`plce-link-init1-script`**: `1` (`0x1`)
- **`plce-link-restore-script`**: `2` (`0x2`)
- **`plce-link-shutdown-script`**: `95` (`0x5f`)
- **`plce-link-teardown-script`**: `94` (`0x5e`)
- **`plce-num-scripts`**: `96` (`0x60`)
- **`port-id`**: `0` (`0x0`)
- **`reg`**: 48 bytes
  - u32: `0xb0000000 0x1c 0x10000000 0x0 0x8028000 0x1 0x4000 0x0 0x802c000 0x1 0x4000 0x0`
  ```
  000000  00 00 00 b0 1c 00 00 00 00 00 00 10 00 00 00 00  ................
  000010  00 80 02 08 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  000020  00 c0 02 08 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```

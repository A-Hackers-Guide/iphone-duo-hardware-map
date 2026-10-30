# `/arm-io/sart-ans`

- Name: `sart-ans`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `156`
- compatible: `sart,coastguard`
- device_type: `sart`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOCoastGuardSARTMapper` | `AppleARMIODevice` | [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md) | `sart,coastguard` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x105c50000` | `0xc000` (49,152 B) | `0x305c50000`–`0x305c5bfff` |
| 1 | `0x105d44000` | `0x4000` (16,384 B) | `0x305d44000`–`0x305d47fff` |
| 2 | `0x105cc0000` | `0x4000` (16,384 B) | `0x305cc0000`–`0x305cc3fff` |

## Referenced by (1) [DT]

- [`/arm-io/ans`](root__arm-io__ans.md): `iommu-parent`

## Firmware with a matching name [FW]

- [`Firmware/ansf.t8160.release.im4p`](../firmware/Firmware__ansf.t8160.release.im4p.md) (1,396,223 B) Tag: IM4P  Type: ansf  Version: AppleStorageFirmware-3975.40.15~303

## All properties (9) [DT]

- **`AAPL,phandle`**: `156` (`0x9c`) → phandle of [`/arm-io/sart-ans`](root__arm-io__sart-ans.md)
- **`compatible`**: `sart,coastguard`
- **`device_type`**: `sart`
- **`name`**: `sart-ans`
- **`power-canary-offset`**: `0` (`0x0`)
- **`reg`**: 48 bytes
  - u32: `0x5c50000 0x1 0xc000 0x0 0x5d44000 0x1 0x4000 0x0 0x5cc0000 0x1 0x4000 0x0`
  ```
  000000  00 00 c5 05 01 00 00 00 00 c0 00 00 00 00 00 00  ................
  000010  00 40 d4 05 01 00 00 00 00 40 00 00 00 00 00 00  .@.......@......
  000020  00 00 cc 05 01 00 00 00 00 40 00 00 00 00 00 00  .........@......
  ```
- **`sart-power-managed`**: (present, empty)
- **`sart-power-reg-offset`**: `5096` (`0x13e8`)
- **`sart-version`**: `4` (`0x4`)

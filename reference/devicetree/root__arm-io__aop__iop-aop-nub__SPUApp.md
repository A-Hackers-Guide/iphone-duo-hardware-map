# `/arm-io/aop/iop-aop-nub/SPUApp`

- Name: `SPUApp`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `96`
- device_type: `SPUApp`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPUAppDriver` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `SPUApp` |

## All properties (6) [DT]

- **`AAPL,phandle`**: `96` (`0x60`) → phandle of [`/arm-io/aop/iop-aop-nub/SPUApp`](root__arm-io__aop__iop-aop-nub__SPUApp.md)
- **`device_type`**: `SPUApp`
- **`name`**: `SPUApp`
- **`spkamp-config_arc`**: 16 bytes
  - u32: `0x20a0302 0xf00800fd 0x10043e8 0x1010130`
  ```
  000000  02 03 0a 02 fd 00 08 f0 e8 43 00 01 30 01 01 01  .........C..0...
  ```
- **`spkamp-config_btmspk`**: 16 bytes
  - u32: `0x2000605 0xf00800fd 0x10040e8 0x100013a`
  ```
  000000  05 06 00 02 fd 00 08 f0 e8 40 00 01 3a 01 00 01  .........@..:...
  ```
- **`spkamp-names`**: `arc`, `btmspk`

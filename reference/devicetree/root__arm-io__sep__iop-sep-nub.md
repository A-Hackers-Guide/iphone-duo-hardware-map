# `/arm-io/sep/iop-sep-nub`

- Name: `iop-sep-nub`
- Parent: [`/arm-io/sep`](root__arm-io__sep.md)
- phandle: `127`
- compatible: `iop-nub,sep`
- Children (3): [`/arm-io/sep/iop-sep-nub/Sandcat`](root__arm-io__sep__iop-sep-nub__Sandcat.md), [`/arm-io/sep/iop-sep-nub/xART`](root__arm-io__sep__iop-sep-nub__xART.md), [`/arm-io/sep/iop-sep-nub/InvalidateHmac`](root__arm-io__sep__iop-sep-nub__InvalidateHmac.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSEPManager` | `AppleA7IOPNub` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) | `iop-nub,sep` |
| `AppleSEPManager` | `AppleSEPIntelIOPNub` | [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md) | `iop-nub,sep` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `wait_for_power_gate` | [`/arm-io/pmgr`](root__arm-io__pmgr.md) | `Wait` | `0xd 0x0 0x0` |

## Firmware with a matching name [FW]

- [`Firmware/all_flash/sep-firmware.v68.RELEASE.im4p`](../firmware/Firmware__all_flash__sep-firmware.v68.RELEASE.im4p.md) (7,216,106 B) Tag: IM4P  Type: sepi  Version: 1
- [`Firmware/all_flash/sep-patches.v68.im4p`](../firmware/Firmware__all_flash__sep-patches.v68.im4p.md) (21,137 B) Tag: IM4P  Type: stg1  Version: AppleSEPROM-1483.0.0.100.14

## All properties (5) [DT]

- **`AAPL,phandle`**: `127` (`0x7f`) → phandle of [`/arm-io/sep/iop-sep-nub`](root__arm-io__sep__iop-sep-nub.md)
- **`compatible`**: `iop-nub,sep`
- **`function-wait_for_power_gate`**: 20 bytes
  - u32: `0x30 0x57616974 0xd 0x0 0x0`
  - text inside: `tiaW`
  ```
  000000  30 00 00 00 74 69 61 57 0d 00 00 00 00 00 00 00  0...tiaW........
  000010  00 00 00 00                                      ....
  ```
- **`name`**: `iop-sep-nub`
- **`rom-panic-bytes`**: `472` (`0x1d8`)

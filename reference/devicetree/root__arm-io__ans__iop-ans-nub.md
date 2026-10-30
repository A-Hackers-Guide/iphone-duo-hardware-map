# `/arm-io/ans/iop-ans-nub`

- Name: `iop-ans-nub`
- Parent: [`/arm-io/ans`](root__arm-io__ans.md)
- phandle: `155`
- compatible: `iop-nub,rtbuddy-v2`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## Firmware with a matching name [FW]

- [`Firmware/ansf.t8160.release.im4p`](../firmware/Firmware__ansf.t8160.release.im4p.md) (1,396,223 B) Tag: IM4P  Type: ansf  Version: AppleStorageFirmware-3975.40.15~303

## All properties (12) [DT]

- **`AAPL,phandle`**: `155` (`0x9b`) → phandle of [`/arm-io/ans/iop-ans-nub`](root__arm-io__ans__iop-ans-nub.md)
- **`cold-boot-after-hibernate`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`continuous-time`**: (present, empty)
- **`crashlog-non-fatal`**: (present, empty)
- **`name`**: `iop-ans-nub`
- **`no-hibernate-sleep`**: (present, empty)
- **`power-managed`**: `1` (`0x1`)
- **`quiesced`**: (present, empty)
- **`region-base`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
- **`region-size`**: `0x0` (u64; as two u32: `0x0`, `0x0`)
- **`shutdown-sleep`**: (present, empty)

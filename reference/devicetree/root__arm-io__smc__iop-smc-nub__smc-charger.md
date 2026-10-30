# `/arm-io/smc/iop-smc-nub/smc-charger`

- Name: `smc-charger`
- Parent: [`/arm-io/smc/iop-smc-nub`](root__arm-io__smc__iop-smc-nub.md)
- phandle: `160`
- device_type: `smc-charger`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSMCCharger` | `AppleSMCInterface` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | `smc-charger` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `dock_parent` | [`/port-usb-c-1`](root__port-usb-c-1.md) | `accP` | `` |

## All properties (10) [DT]

- **`AAPL,phandle`**: `160` (`0xa0`) → phandle of [`/arm-io/smc/iop-smc-nub/smc-charger`](root__arm-io__smc__iop-smc-nub__smc-charger.md)
- **`battery-id`**: 32 bytes
  - u32: `0x0 0x0 0x0 0x0 0x0 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  000010  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`boot-adapter-id`**: `0` (`0x0`)
- **`boot-voltage`**: `0` (`0x0`)
- **`device_type`**: `smc-charger`
- **`dock-num`**: `1` (`0x1`)
- **`function-dock_parent`**: `0x61636350000001c5` (u64; as two u32: `0x1c5`, `0x61636350`)
- **`name`**: `smc-charger`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)

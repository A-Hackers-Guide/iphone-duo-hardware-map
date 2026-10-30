# `/port-magsafe-1`

- Name: `port-magsafe-1`
- Parent: [`/`](root.md)
- phandle: `454`
- compatible: `dock,0pin`
- device_type: `port-magsafe`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `IOAccessoryDock0PinBuiltin` | `IOService` | [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md) | `dock,0pin` |

## Referenced by (1) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](root__arm-io__smc__iop-smc-nub__smc-ext-charger.md): function-dock_parent `accP`

## All properties (9) [DT]

- **`AAPL,phandle`**: `454` (`0x1c6`) → phandle of [`/port-magsafe-1`](root__port-magsafe-1.md)
- **`compatible`**: `dock,0pin`
- **`device_type`**: `port-magsafe`
- **`features-supported`**: `1` (`0x1`)
- **`name`**: `port-magsafe-1`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `9` (`0x9`)
- **`primary-port-id`**: `512` (`0x200`)
- **`transports-supported`**: `15` (`0xf`)

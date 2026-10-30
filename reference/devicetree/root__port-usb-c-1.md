# `/port-usb-c-1`

- Name: `port-usb-c-1`
- Parent: [`/`](root.md)
- phandle: `453`
- compatible: `dock,usb-c`
- device_type: `port-component-usb-c`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## Referenced by (6) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-charger`](root__arm-io__smc__iop-smc-nub__smc-charger.md): function-dock_parent `accP`
- [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](root__arm-io__smc__iop-smc-nub__smc-ext-charger.md): function-dock_wired `accP`
- [`/arm-io/nub-spmi2/spmi-hpm0`](root__arm-io__nub-spmi2__spmi-hpm0.md): function-ignore_vbus_drop `igvb`
- [`/arm-io/atc-phy0`](root__arm-io__atc-phy0.md): function-dock_parent `accP`
- [`/arm-io/usb-drd0`](root__arm-io__usb-drd0.md): function-dock_parent `accP`
- [`/arm-io/usb-drd0`](root__arm-io__usb-drd0.md): function-parrot_srst `prst`

## All properties (7) [DT]

- **`AAPL,phandle`**: `453` (`0x1c5`) → phandle of [`/port-usb-c-1`](root__port-usb-c-1.md)
- **`compatible`**: `dock,usb-c`
- **`device_type`**: `port-component-usb-c`
- **`name`**: `port-usb-c-1`
- **`port-number`**: `1` (`0x1`)
- **`port-type`**: `2` (`0x2`)
- **`primary-port-id`**: `2` (`0x2`)

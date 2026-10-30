# `/arm-io/aop/iop-aop-nub/pressure`

- Name: `pressure`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `93`
- device_type: `pressure`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (9) [DT]

- **`AAPL,phandle`**: `93` (`0x5d`) → phandle of [`/arm-io/aop/iop-aop-nub/pressure`](root__arm-io__aop__iop-aop-nub__pressure.md)
- **`device-usage`**: `49` (`0x31`)
- **`device-usage-page`**: `20` (`0x14`)
- **`device_type`**: `pressure`
- **`name`**: `pressure`
- **`pressure-global-offset-cal`**: `7936` (`0x1f00`)
- **`pressure-heater-resistance`**: `87000` (`0x153d8`)
- **`pressure-offset-calibration`**: `syscfg/SPPO` *(placeholder, filled in by iBoot at boot)*
- **`temp-compensation-table`**: `syscfg/PRTT` *(placeholder, filled in by iBoot at boot)*

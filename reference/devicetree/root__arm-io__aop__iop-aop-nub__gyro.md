# `/arm-io/aop/iop-aop-nub/gyro`

- Name: `gyro`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `90`
- device_type: `gyro`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (13) [DT]

- **`AAPL,phandle`**: `90` (`0x5a`) → phandle of [`/arm-io/aop/iop-aop-nub/gyro`](root__arm-io__aop__iop-aop-nub__gyro.md)
- **`device-usage`**: `9` (`0x9`)
- **`device-usage-page`**: `65280` (`0xff00`)
- **`device_type`**: `gyro`
- **`gyro-interrupt-calibration`**: `syscfg/GICl` *(placeholder, filled in by iBoot at boot)*
- **`gyro-nominal-extr-cal`**: `syscfg/GRXN,hex/02000201464D30692800000001000000000000000000FFFF000000000000FFFF000000000000000000000000000000000000FFFF524D306928000000010000000000FFFF0000000000000000000000000000FFFF00000000000000000000000000000100B023A1BA` *(placeholder, filled in by iBoot at boot)*
- **`gyro-orientation`**: `syscfg/GRot` *(placeholder, filled in by iBoot at boot)*
- **`gyro-range-extr-cal`**: `syscfg/GRXC` *(placeholder, filled in by iBoot at boot)*
- **`gyro-range-intr-cal`**: `syscfg/GRNC,hex/03000101524D30692C00000002000000A00F00000000FA390000000000000000000000000000FA390000000000000000000000000000FA3968D0D2D4` *(placeholder, filled in by iBoot at boot)*
- **`gyro-range-sensitivity-cal`**: `syscfg/GRSC` *(placeholder, filled in by iBoot at boot)*
- **`gyro-sensitivity-calibration`**: `syscfg/GSCl` *(placeholder, filled in by iBoot at boot)*
- **`gyro-temp-table`**: `syscfg/GYTT` *(placeholder, filled in by iBoot at boot)*
- **`name`**: `gyro`

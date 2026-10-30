# `/arm-io/aop/iop-aop-nub/accel`

- Name: `accel`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `88`
- device_type: `accel`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (14) [DT]

- **`AAPL,phandle`**: `88` (`0x58`) → phandle of [`/arm-io/aop/iop-aop-nub/accel`](root__arm-io__aop__iop-aop-nub__accel.md)
- **`accel-interrupt-calibration`**: `syscfg/AICl` *(placeholder, filled in by iBoot at boot)*
- **`accel-nominal-extr-cal`**: `syscfg/ARXN,hex/02000201464D30692800000001000000000000000000010000000000000001000000000000000000000000000000000000000100524D3069280000000100000000000100000000000000000000000000000001000000000000000000000000000000FFFF17AF70D7` *(placeholder, filled in by iBoot at boot)*
- **`accel-offset-cal`**: `syscfg/AROC` *(placeholder, filled in by iBoot at boot)*
- **`accel-orientation`**: `syscfg/ARot` *(placeholder, filled in by iBoot at boot)*
- **`accel-range-extr-cal`**: `syscfg/ARXC` *(placeholder, filled in by iBoot at boot)*
- **`accel-range-intr-cal`**: `syscfg/ARNC,hex/03000101524D30692C000000020000002000000000007A3F00000000000000000000000000007A3F00000000000000000000000000007A3F8D706AAE` *(placeholder, filled in by iBoot at boot)*
- **`accel-range-sensitivity-cal`**: `syscfg/ARSC` *(placeholder, filled in by iBoot at boot)*
- **`accel-sensitivity-calibration`**: `syscfg/ASCl` *(placeholder, filled in by iBoot at boot)*
- **`device-usage`**: `3` (`0x3`)
- **`device-usage-page`**: `65280` (`0xff00`)
- **`device_type`**: `accel`
- **`low-temp-accel-offset`**: `syscfg/LTAO` *(placeholder, filled in by iBoot at boot)*
- **`name`**: `accel`

# `AppleT8101GPIOIC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md)
- Object size: `0x170` (368 bytes)
- Metaclass: `0xfffffe000b946408`; metaclass vtable `0xfffffe00080b4a40`; class vtable `0xfffffe00080b43e8`
- Registration (init): `0xfffffe0008d080a0`
- Superclasses: [`AppleGPIOICController`](AppleGPIOICController.md) → [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8101GPIOIC` in [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `gpio,t8101`

## Device-tree nodes it binds (5) [DT]

- [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) on `gpio,t8101`
- [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) on `gpio,t8101`
- [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) on `gpio,t8101`
- [`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) on `gpio,t8101`
- [`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) on `gpio,t8101`

## Strings in its kext that name it (3)

- `AppleT8101GPIOIC`
- `site.AppleT8101GPIOIC`
- `AppleT8101GPIOIC.cpp`

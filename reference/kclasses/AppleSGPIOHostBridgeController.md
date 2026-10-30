# `AppleSGPIOHostBridgeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSGPIO`](../kexts/com.apple.driver.AppleSGPIO.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b99b130`; metaclass vtable `0xfffffe00081fb1c0`; class vtable `0xfffffe00081fac00`
- Registration (init): `0xfffffe0009663a4c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSGPIOHostBridgeController` in [`com.apple.driver.AppleSGPIO`](../kexts/com.apple.driver.AppleSGPIO.md): `IOProviderClass` = `AppleDialogSPMIPMUNub`, `IONameMatch` = `sgpio-bridge`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md) on `sgpio-bridge`

## Strings in its kext that name it (2)

- `AppleSGPIOHostBridgeController`
- `site.AppleSGPIOHostBridgeController`

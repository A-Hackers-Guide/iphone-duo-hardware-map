# `AppleSPMIController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md)
- Object size: `0x1ac8` (6,856 bytes)
- Metaclass: `0xfffffe000b99bc10`; metaclass vtable `0xfffffe0008209840`; class vtable `0xfffffe0008209130`
- Registration (init): `0xfffffe00096af59c`
- Superclasses: [`AppleARMSPMIController`](AppleARMSPMIController.md) → [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPMIController` in [`com.apple.driver.AppleSPMI`](../kexts/com.apple.driver.AppleSPMI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `aapl,spmi`

## Device-tree nodes it binds (5) [DT]

- [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) on `aapl,spmi`
- [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) on `aapl,spmi`
- [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) on `aapl,spmi`
- [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) on `aapl,spmi`
- [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) on `aapl,spmi`

## Strings in its kext that name it (3)

- `AppleSPMIController`
- `AppleSPMIController.cpp`
- `site.AppleSPMIController`

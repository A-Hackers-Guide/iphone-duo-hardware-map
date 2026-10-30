# `AppleAOPSMCDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xf8` (248 bytes)
- Metaclass: `0xfffffe000b99cb48`; metaclass vtable `0xfffffe000820d9e0`; class vtable `0xfffffe000820d488`
- Registration (init): `0xfffffe00096c31e8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPSMCDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['smc-control']`, `IOMatchCategory` = `AppleAOPSMCDriver`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) on `smc-control`

## Strings in its kext that name it (2)

- `AppleAOPSMCDriver`
- `site.AppleAOPSMCDriver`

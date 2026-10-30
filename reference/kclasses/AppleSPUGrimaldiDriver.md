# `AppleSPUGrimaldiDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b99caf8`; metaclass vtable `0xfffffe000820cc78`; class vtable `0xfffffe000820c720`
- Registration (init): `0xfffffe00096c1210`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUGrimaldiDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['grimaldi-control']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) on `grimaldi-control`

## Strings in its kext that name it (2)

- `site.AppleSPUGrimaldiDriver`
- `AppleSPUGrimaldiDriver`

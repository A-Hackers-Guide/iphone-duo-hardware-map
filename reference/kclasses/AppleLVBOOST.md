# `AppleLVBOOST`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b99d1a0`; metaclass vtable `0xfffffe000821d0c8`; class vtable `0xfffffe000821cb70`
- Registration (init): `0xfffffe00096df678`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleLVBOOST` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleA7IOPNub`, `IONameMatch` = `['iop-spu-nub', 'iop-aop-nub']`, `IOMatchCategory` = `AppleLVBOOST`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) on `iop-aop-nub`

## Strings in its kext that name it (2)

- `site.AppleLVBOOST`
- `AppleLVBOOST`

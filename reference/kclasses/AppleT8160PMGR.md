# `AppleT8160PMGR`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PMGR`](../kexts/com.apple.driver.AppleT8160PMGR.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9d1408`; metaclass vtable `0xfffffe0008275af8`; class vtable `0xfffffe0008275298`
- Registration (init): `0xfffffe00098d4748`
- Superclasses: [`ApplePMGRv2Impl`](ApplePMGRv2Impl.md) → [`AbstractPMGR`](AbstractPMGR.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8160PMGR` in [`com.apple.driver.AppleT8160PMGR`](../kexts/com.apple.driver.AppleT8160PMGR.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `pmgr2,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) on `pmgr2,t8160`

## Strings in its kext that name it (2)

- `site.AppleT8160PMGR`
- `AppleT8160PMGR`

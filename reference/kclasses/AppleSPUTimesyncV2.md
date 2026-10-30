# `AppleSPUTimesyncV2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b99d388`; metaclass vtable `0xfffffe0008221218`; class vtable `0xfffffe0008220cb8`
- Registration (init): `0xfffffe00096e9798`
- Superclasses: [`AppleSPUTimesync`](AppleSPUTimesync.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUTimesyncV2` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleA7IOPNub`, `IONameMatch` = `['iop-aop-nub']`, `IOMatchCategory` = `AppleSPUTimesync`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) on `iop-aop-nub`

## Strings in its kext that name it (2)

- `site.AppleSPUTimesyncV2`
- `AppleSPUTimesyncV2`

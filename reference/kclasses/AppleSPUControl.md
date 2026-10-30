# `AppleSPUControl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b99d1c8`; metaclass vtable `0xfffffe000821d6b8`; class vtable `0xfffffe000821d160`
- Registration (init): `0xfffffe00096df6b0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUControl` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['multi-touch', 'opal']`, `IOMatchCategory` = `AppleSPUControl`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) on `multi-touch`

## Strings in its kext that name it (2)

- `AppleSPUControl`
- `site.AppleSPUControl`

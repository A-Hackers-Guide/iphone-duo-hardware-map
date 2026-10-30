# `AppleAVE2Driver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAVE2`](../kexts/com.apple.driver.AppleAVE2.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b9366f8`; metaclass vtable `0xfffffe0007fe20b0`; class vtable `0xfffffe0007fe1b48`
- Registration (init): `0xfffffe00089773e4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ave2` in [`com.apple.driver.AppleAVE2`](../kexts/com.apple.driver.AppleAVE2.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['ave2']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) on `ave2`

## Strings in its kext that name it (2)

- `AppleAVE2Driver`
- `site.AppleAVE2Driver`

# `AppleBasebandSARPTD`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b994c68`; metaclass vtable `0xfffffe00081d0aa8`; class vtable `0xfffffe00081d0520`
- Registration (init): `0xfffffe0009520ec4`
- Superclasses: [`AppleBasebandPTD`](AppleBasebandPTD.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleBasebandSARPTD` in [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `baseband,ptd`, `IOMatchCategory` = `AppleBasebandSARPTD`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) on `baseband,ptd`

## Strings in its kext that name it (2)

- `AppleBasebandSARPTD`
- `site.AppleBasebandSARPTD`

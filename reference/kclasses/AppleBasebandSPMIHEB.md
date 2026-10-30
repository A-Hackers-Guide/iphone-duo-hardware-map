# `AppleBasebandSPMIHEB`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md)
- Object size: `0x150` (336 bytes)
- Metaclass: `0xfffffe000b937858`; metaclass vtable `0xfffffe0007ff5b80`; class vtable `0xfffffe0007ff55e8`
- Registration (init): `0xfffffe00089c8ec0`
- Superclasses: [`AppleBasebandSPMI`](AppleBasebandSPMI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleBasebandSPMIHEB` in [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `baseband,heb`, `IOMatchCategory` = `AppleBasebandSPMIHEB`
- `AppleBasebandSPMIIDC` in [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `baseband,idc`, `IOMatchCategory` = `AppleBasebandSPMIHEB`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) on `baseband,heb`
- [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) on `baseband,idc`

## Strings in its kext that name it (2)

- `site.AppleBasebandSPMIHEB`
- `AppleBasebandSPMIHEB`

# `AppleSARSPMIHEB`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b994d08`; metaclass vtable `0xfffffe00081d2338`; class vtable `0xfffffe00081d1da0`
- Registration (init): `0xfffffe0009541d24`
- Superclasses: [`AppleSARSPMI`](AppleSARSPMI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSARSPMIHEB` in [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `baseband,heb`, `IOMatchCategory` = `AppleSARSPMI`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop-spmi0/baseband-heb`](../devicetree/root__arm-io__aop-spmi0__baseband-heb.md) on `baseband,heb`

## Strings in its kext that name it (2)

- `AppleSARSPMIHEB`
- `site.AppleSARSPMIHEB`

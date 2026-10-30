# `AppleSARSPMIIDC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b994a98`; metaclass vtable `0xfffffe00081cdaf8`; class vtable `0xfffffe00081cd560`
- Registration (init): `0xfffffe0009509b14`
- Superclasses: [`AppleSARSPMI`](AppleSARSPMI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSARSPMIIDC` in [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `baseband,idc`, `IOMatchCategory` = `AppleSARSPMI`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop-spmi1/baseband-idc`](../devicetree/root__arm-io__aop-spmi1__baseband-idc.md) on `baseband,idc`

## Strings in its kext that name it (4)

- `AppleSARSPMIIDCWLAN`
- `site.AppleSARSPMIIDC`
- `site.AppleSARSPMIIDCWLAN`
- `AppleSARSPMIIDC`

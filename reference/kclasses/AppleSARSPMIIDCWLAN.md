# `AppleSARSPMIIDCWLAN`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b995558`; metaclass vtable `0xfffffe00081d3ef8`; class vtable `0xfffffe00081d3960`
- Registration (init): `0xfffffe0009548314`
- Superclasses: [`AppleSARSPMI`](AppleSARSPMI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSARSPMIIDCWLAN` in [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `wlan,idc`, `IOMatchCategory` = `AppleSARSPMI`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop-spmi1/wlan-idc`](../devicetree/root__arm-io__aop-spmi1__wlan-idc.md) on `wlan,idc`

## Strings in its kext that name it (2)

- `AppleSARSPMIIDCWLAN`
- `site.AppleSARSPMIIDCWLAN`

# `AppleARMPE`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x128` (296 bytes)
- Metaclass: `0xfffffe000b934328`; metaclass vtable `0xfffffe0007fb9080`; class vtable `0xfffffe0007fb89b0`
- Registration (init): `0xfffffe00086fee60`
- Superclasses: [`IODTPlatformExpert`](IODTPlatformExpert.md) → [`IOPlatformExpert`](IOPlatformExpert.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMPE` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `IOPlatformExpertDevice`, `IONameMatch` = `AppleARM`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (1) [DT]

- [``](../devicetree/root.md) on `AppleARM`

## Strings in its kext that name it (7)

- `AppleARMPE::getGMTTimeOfDay can not provide time of day: RTC did not show up\n`
- `AppleARMPERemoveCoprovider`
- `AppleARMPE::setGMTTimeOfDay can not provide time of day RTC did not show up\n`
- `site.AppleARMPE`
- `AppleARMPEFindCoprovider`
- `AppleARMPE::getGMTTimeOfDay can not provide time of day: RTC appeared, but \"getGMTTimeOfDay\" call failed with %x\n`
- `AppleARMPE`

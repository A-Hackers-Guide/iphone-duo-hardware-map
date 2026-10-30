# `AppleBringUpPMGR`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md)
- Object size: `0x738d8` (473,304 bytes)
- Metaclass: `0xfffffe000b987480`; metaclass vtable `0xfffffe0008190138`; class vtable `0xfffffe000818f360`
- Registration (init): `0xfffffe000933e4e4`
- Superclasses: [`ApplePMGR`](ApplePMGR.md) → [`ApplePMGRBase`](ApplePMGRBase.md) → [`IOPMGR`](IOPMGR.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleBringUpPMGR` in [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `pmgr1,bring-up`

## Strings in its kext that name it (4)

- `site.AppleBringUpPMGR`
- `AppleBringUpPMGR.cpp`
- `AppleBringUpPMGR`
- `virtual void AppleBringUpPMGR::initRegGroups()`

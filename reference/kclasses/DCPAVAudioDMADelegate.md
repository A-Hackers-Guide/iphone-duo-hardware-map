# `DCPAVAudioDMADelegate`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000b9df6a0`; metaclass vtable `0xfffffe00082ced98`; class vtable `0xfffffe00082ce7e8`
- Registration (init): `0xfffffe0009c1be50`
- Superclasses: [`IOAVAudioDMADelegate`](IOAVAudioDMADelegate.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DCPAVAudioDMADelegate` in [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['dp-audio', 'dp-audio0', 'dp-audio1', 'dp-audio2', 'dp-audio3', 'dp-audio4', 'd`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/dp-audio0`](../devicetree/root__arm-io__dp-audio0.md) on `dp-audio0`
- [`/arm-io/dp-audio1`](../devicetree/root__arm-io__dp-audio1.md) on `dp-audio1`

## Strings in its kext that name it (2)

- `site.DCPAVAudioDMADelegate`
- `DCPAVAudioDMADelegate`

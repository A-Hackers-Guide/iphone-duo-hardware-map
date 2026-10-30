# `AppleEmbeddedAudioResourceManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudioResourceManager`](../kexts/com.apple.driver.AppleEmbeddedAudioResourceManager.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b942be0`; metaclass vtable `0xfffffe0008080da0`; class vtable `0xfffffe0008080818`
- Registration (init): `0xfffffe0008c2db6c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleEmbeddedAudioResourceManager` in [`com.apple.driver.AppleEmbeddedAudioResourceManager`](../kexts/com.apple.driver.AppleEmbeddedAudioResourceManager.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['audio,embedded-resource-manager']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/audio-resource-manager`](../devicetree/root__arm-io__audio-resource-manager.md) on `audio,embedded-resource-manager`

## Strings in its kext that name it (2)

- `site.AppleEmbeddedAudioResourceManager`
- `AppleEmbeddedAudioResourceManager`

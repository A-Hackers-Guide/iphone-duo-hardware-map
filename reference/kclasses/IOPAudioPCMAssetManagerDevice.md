# `IOPAudioPCMAssetManagerDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioPCMAssetManagerDevice`](../kexts/com.apple.driver.IOPAudioPCMAssetManagerDevice.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000ba18870`; metaclass vtable `0xfffffe00083d2b30`; class vtable `0xfffffe00083d2580`
- Registration (init): `0xfffffe000a3091cc`
- Superclasses: [`IOPAudioAssetManagerDevice`](IOPAudioAssetManagerDevice.md) → [`IOPAudioDevice`](IOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `PCMAssetManagerDevice` in [`com.apple.driver.IOPAudioPCMAssetManagerDevice`](../kexts/com.apple.driver.IOPAudioPCMAssetManagerDevice.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-audio,pcm-asset-manager-device']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) on `iop-audio,pcm-asset-manager-device`

## Strings in its kext that name it (4)

- `IOPAudioPCMAssetManagerDeviceUserClient`
- `site.IOPAudioPCMAssetManagerDeviceUserClient`
- `IOPAudioPCMAssetManagerDevice`
- `site.IOPAudioPCMAssetManagerDevice`

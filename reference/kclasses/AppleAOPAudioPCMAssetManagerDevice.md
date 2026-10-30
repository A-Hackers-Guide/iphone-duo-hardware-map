# `AppleAOPAudioPCMAssetManagerDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b932e78`; metaclass vtable `0xfffffe0007fa5d28`; class vtable `0xfffffe0007fa5708`
- Registration (init): `0xfffffe000869cdc4`
- Superclasses: [`AppleAOPAudioAssetManagerDevice`](AppleAOPAudioAssetManagerDevice.md) → [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioPCMAssetManagerDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-pcmaudiomgr', 'audio-pcmaudiomgr', 'audio-hw-pcm-audiomgr']`, `IOResourceMatch` = `IOKit`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-hw-pcm-audiomgr`](../devicetree/root__arm-io__iop-audio-controller__audio-hw-pcm-audiomgr.md) on `audio-hw-pcm-audiomgr`

## Strings in its kext that name it (2)

- `AppleAOPAudioPCMAssetManagerDevice`
- `site.AppleAOPAudioPCMAssetManagerDevice`

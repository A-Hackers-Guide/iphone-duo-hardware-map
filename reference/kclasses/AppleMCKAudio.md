# `AppleMCKAudio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b941f90`; metaclass vtable `0xfffffe0008070348`; class vtable `0xfffffe000806fdf0`
- Registration (init): `0xfffffe0008be5510`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMCKAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,mck-only`

## Strings in its kext that name it (14)

- `AppleMCKAudioFunction::%s enable parameter (param1) cannot be a null pointer\n`
- `site.AppleMCKAudio`
- `AppleMCKAudioFunction::%s setUpClock failed -> ret = %#x\n`
- `AppleMCKAudio`
- `AppleMCKAudioFunction::%s could not get data\n`
- `AppleMCKAudioFunction`
- `AppleMCKAudioFunction::%s could not get target instance\n`
- `site.AppleMCKAudioFunction`
- `AppleMCKAudioFunction::%s super::initWithTargetDataAndSymbol failed\n`
- `AppleMCKAudioFunction::%s could not get data`
- `AppleMCKAudioFunction::%s super::initWithTargetDataAndSymbol failed`
- `AppleMCKAudioFunction::%s enable parameter (param1) cannot be a null pointer`
- `AppleMCKAudioFunction::%s could not get target instance`
- `AppleMCKAudioFunction::%s setUpClock failed -> ret = %#x`

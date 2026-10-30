# `AppleAOPAudioSpeakerClientManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b932ef0`; metaclass vtable `0xfffffe0007fa71a0`; class vtable `0xfffffe0007fa6bb0`
- Registration (init): `0xfffffe000869ff50`
- Superclasses: [`AppleAOPAudioLEAPClientManager`](AppleAOPAudioLEAPClientManager.md) → [`AppleAOPAudioClientManager`](AppleAOPAudioClientManager.md) → [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioSpeakerClientManager` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-spkrmgr', 'audio-spkrmgr']`, `IOResourceMatch` = `IOKit`

## Strings in its kext that name it (2)

- `site.AppleAOPAudioSpeakerClientManager`
- `AppleAOPAudioSpeakerClientManager`

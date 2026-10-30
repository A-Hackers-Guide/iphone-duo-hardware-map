# `AppleAOPAudioLEAPClientManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b9330a0`; metaclass vtable `0xfffffe0007fa97e0`; class vtable `0xfffffe0007fa91f0`
- Registration (init): `0xfffffe00086ae084`
- Superclasses: [`AppleAOPAudioClientManager`](AppleAOPAudioClientManager.md) → [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleAOPAudioSpeakerClientManager`](AppleAOPAudioSpeakerClientManager.md) — `com.apple.driver.AppleAOPAudio`

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioLEAPClientManager` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-hapticmgr', 'audio-hapticmgr']`, `IOResourceMatch` = `IOKit`

## Strings in its kext that name it (2)

- `AppleAOPAudioLEAPClientManager`
- `site.AppleAOPAudioLEAPClientManager`

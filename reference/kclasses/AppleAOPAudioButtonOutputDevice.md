# `AppleAOPAudioButtonOutputDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b9331d0`; metaclass vtable `0xfffffe0007fac138`; class vtable `0xfffffe0007fabb40`
- Registration (init): `0xfffffe00086b4ab4`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioButtonOutput` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-buttonout', 'audio-buttonout']`, `IOResourceMatch` = `IOKit`

## Strings in its kext that name it (2)

- `site.AppleAOPAudioButtonOutputDevice`
- `AppleAOPAudioButtonOutputDevice`

# `AppleAOPAudioLEAP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b9330f0`; metaclass vtable `0xfffffe0007faa558`; class vtable `0xfffffe0007fa9f40`
- Registration (init): `0xfffffe00086b04c8`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleAOPAudioHapticLEAP`](AppleAOPAudioHapticLEAP.md) — `com.apple.driver.AppleAOPAudio`

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioLEAP` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-leap', 'audio-leap']`, `IOResourceMatch` = `IOKit`

## Strings in its kext that name it (4)

- `AppleAOPAudioLEAPClientManager`
- `site.AppleAOPAudioLEAPClientManager`
- `AppleAOPAudioLEAP`
- `site.AppleAOPAudioLEAP`

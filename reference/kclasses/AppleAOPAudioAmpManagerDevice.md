# `AppleAOPAudioAmpManagerDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b933118`; metaclass vtable `0xfffffe0007faabe0`; class vtable `0xfffffe0007faa5f0`
- Registration (init): `0xfffffe00086b15e4`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioAmpManagerDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-amp']`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleAOPAudioAmpManagerDevice`, `IOProbeScore` = `1000`

## Strings in its kext that name it (2)

- `site.AppleAOPAudioAmpManagerDevice`
- `AppleAOPAudioAmpManagerDevice`

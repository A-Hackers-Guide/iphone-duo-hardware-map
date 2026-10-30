# `AppleAOPAudioMCA2Device`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b932fd8`; metaclass vtable `0xfffffe0007fa7f08`; class vtable `0xfffffe0007fa7918`
- Registration (init): `0xfffffe00086a2444`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioMCA2Device ` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-mca0', 'audio-mca1']`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleAOPAudioMCA2Device`, `IOProbeScore` = `1000`

## Strings in its kext that name it (2)

- `site.AppleAOPAudioMCA2Device`
- `AppleAOPAudioMCA2Device`

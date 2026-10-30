# `AppleActuatorSecondaryAudio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md)
- Object size: `0x300` (768 bytes)
- Metaclass: `0xfffffe000b942120`; metaclass vtable `0xfffffe0008075328`; class vtable `0xfffffe0008074a98`
- Registration (init): `0xfffffe0008bfcf2c`
- Superclasses: [`AppleSecondaryAudio`](AppleSecondaryAudio.md) → [`AppleARMIISAudioDevice`](AppleARMIISAudioDevice.md) → [`AppleARMDMAAudioDevice`](AppleARMDMAAudioDevice.md) → [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleActuatorAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,actuator`, `IOMatchCategory` = `AppleSecondaryAudio`, `IOProbeScore` = `1000`

## Strings in its kext that name it (2)

- `site.AppleActuatorSecondaryAudio`
- `AppleActuatorSecondaryAudio`

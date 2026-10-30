# `AppleHapticsExternalSecondaryAudio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md)
- Object size: `0x338` (824 bytes)
- Metaclass: `0xfffffe000b941d50`; metaclass vtable `0xfffffe000806a080`; class vtable `0xfffffe00080697e0`
- Registration (init): `0xfffffe0008bcfc9c`
- Superclasses: [`AppleExternalSecondaryAudio`](AppleExternalSecondaryAudio.md) → [`AppleSecondaryAudio`](AppleSecondaryAudio.md) → [`AppleARMIISAudioDevice`](AppleARMIISAudioDevice.md) → [`AppleARMDMAAudioDevice`](AppleARMDMAAudioDevice.md) → [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHapticsExternalAudio` in [`com.apple.driver.AppleEmbeddedAudio`](../kexts/com.apple.driver.AppleEmbeddedAudio.md): `IOProviderClass` = `AppleARMIISDevice`, `IONameMatch` = `audio-data,haptics-external`, `IOMatchCategory` = `AppleSecondaryAudio`

## Strings in its kext that name it (6)

- `site.AppleHapticsExternalSecondaryAudio`
- `AppleHapticsExternalSecondaryAudio::start(..) failed.\n\n\n`
- `AppleHapticsExternalSecondaryAudio::start(..) super::start(..) failed\n\n`
- `AppleHapticsExternalSecondaryAudio`
- `AppleHapticsExternalSecondaryAudio::start(..) super::start(..) failed\n`
- `AppleHapticsExternalSecondaryAudio::start(..) failed.\n\n`

# `IOPAudioSpeaker`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md)
- Object size: `0x1f8` (504 bytes)
- Metaclass: `0xfffffe000b9425d0`; metaclass vtable `0xfffffe000807cb30`; class vtable `0xfffffe000807c058`
- Registration (init): `0xfffffe0008c193dc`
- Superclasses: [`AppleEmbeddedAudio`](AppleEmbeddedAudio.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AOPAudioSpeaker` in [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md): `IOProviderClass` = `AppleAOPAudioDeviceProvider`, `IONameMatch` = `['audio-iop-speaker']`
- `IOPAudioSpeaker` in [`com.apple.driver.IOPAudioSpeaker`](../kexts/com.apple.driver.IOPAudioSpeaker.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['audio-iop-speaker']`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) on `audio-iop-speaker`
- [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) on `audio-iop-speaker`

## Strings in its kext that name it (2)

- `site.IOPAudioSpeaker`
- `IOPAudioSpeaker`

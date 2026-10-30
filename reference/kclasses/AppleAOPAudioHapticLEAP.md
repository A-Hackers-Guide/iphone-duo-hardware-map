# `AppleAOPAudioHapticLEAP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b932e20`; metaclass vtable `0xfffffe0007fa4fe8`; class vtable `0xfffffe0007fa49d0`
- Registration (init): `0xfffffe00086999cc`
- Superclasses: [`AppleAOPAudioLEAP`](AppleAOPAudioLEAP.md) → [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioHapticLEAP` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-haptic-leap', 'audio-haptic-leap']`, `IOResourceMatch` = `IOKit`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) on `audio-haptic-leap`

## Strings in its kext that name it (2)

- `AppleAOPAudioHapticLEAP`
- `site.AppleAOPAudioHapticLEAP`

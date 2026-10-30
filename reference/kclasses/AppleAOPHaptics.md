# `AppleAOPHaptics`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPHaptics`](../kexts/com.apple.driver.AppleAOPHaptics.md)
- Object size: `0x230` (560 bytes)
- Metaclass: `0xfffffe000b942298`; metaclass vtable `0xfffffe00080796e0`; class vtable `0xfffffe0008078c00`
- Registration (init): `0xfffffe0008c0473c`
- Superclasses: [`AppleAOPEmbeddedAudio`](AppleAOPEmbeddedAudio.md) → [`AppleEmbeddedAudio`](AppleEmbeddedAudio.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAOPHapticsAudio` in [`com.apple.driver.AppleAOPHaptics`](../kexts/com.apple.driver.AppleAOPHaptics.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IOPropertyMatch` = `{'compatible': 'aop-audio-haptic'}`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleAOPHaptics`

## Strings in its kext that name it (2)

- `site.AppleAOPHaptics`
- `AppleAOPHaptics`

# `IOPHaptics`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md)
- Object size: `0x278` (632 bytes)
- Metaclass: `0xfffffe000b942838`; metaclass vtable `0xfffffe000807e530`; class vtable `0xfffffe000807da38`
- Registration (init): `0xfffffe0008c1d33c`
- Superclasses: [`IOPEmbeddedAudio`](IOPEmbeddedAudio.md) → [`AppleEmbeddedAudio`](AppleEmbeddedAudio.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOPHaptics` in [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['audio-control,audio-iop-haptics']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) on `audio-control,audio-iop-haptics`

## Strings in its kext that name it (4)

- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPHaptics/IOPHaptics.cpp`
- `IOPHaptics`
- `site.IOPHaptics`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPHaptics/IOPHapticDebug.cpp`

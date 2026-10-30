# `IOPHapticDebug`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md)
- Object size: `0x238` (568 bytes)
- Metaclass: `0xfffffe000b942860`; metaclass vtable `0xfffffe000807f0c0`; class vtable `0xfffffe000807e5c8`
- Registration (init): `0xfffffe0008c1deac`
- Superclasses: [`IOPEmbeddedAudio`](IOPEmbeddedAudio.md) → [`AppleEmbeddedAudio`](AppleEmbeddedAudio.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOPHapticDebug` in [`com.apple.driver.IOPHaptics`](../kexts/com.apple.driver.IOPHaptics.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['audio-control,audio-iop-haptic-debug']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) on `audio-control,audio-iop-haptic-debug`

## Strings in its kext that name it (3)

- `site.IOPHapticDebug`
- `IOPHapticDebug`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPHaptics/IOPHapticDebug.cpp`

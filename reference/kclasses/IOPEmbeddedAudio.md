# `IOPEmbeddedAudio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPEmbeddedAudio`](../kexts/com.apple.driver.IOPEmbeddedAudio.md)
- Object size: `0x228` (552 bytes)
- Metaclass: `0xfffffe000b942738`; metaclass vtable `0xfffffe000807d800`; class vtable `0xfffffe000807cd08`
- Registration (init): `0xfffffe0008c1aa30`
- Superclasses: [`AppleEmbeddedAudio`](AppleEmbeddedAudio.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`IOPHapticDebug`](IOPHapticDebug.md) — `com.apple.driver.IOPHaptics`
- [`IOPHaptics`](IOPHaptics.md) — `com.apple.driver.IOPHaptics`

## IOKit personalities that instantiate it (1)

- `IOPEmbeddedAudio` in [`com.apple.driver.IOPEmbeddedAudio`](../kexts/com.apple.driver.IOPEmbeddedAudio.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['audio-control,iop-embeddedaudio']`

## Strings in its kext that name it (6)

- `IOPEmbeddedAudio::Helper`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPEmbeddedAudio/IOPEmbeddedAudioHelpers.h`
- `IOPEmbeddedAudio`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPEmbeddedAudio/IOPEmbeddedAudioHelpers.cpp`
- `site.IOPEmbeddedAudio`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/src/kext/IOPEmbeddedAudio/IOPEmbeddedAudio.cpp`

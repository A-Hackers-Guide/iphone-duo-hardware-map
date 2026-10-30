# `AppleCS42L79Audio`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCS42L79Audio`](../kexts/com.apple.driver.AppleCS42L79Audio.md)
- Object size: `0x498` (1,176 bytes)
- Metaclass: `0xfffffe000b942488`; metaclass vtable `0xfffffe000807b710`; class vtable `0xfffffe000807ac08`
- Registration (init): `0xfffffe0008c114ac`
- Superclasses: [`AppleEmbeddedAudio`](AppleEmbeddedAudio.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleCS42L77Audio` in [`com.apple.driver.AppleCS42L79Audio`](../kexts/com.apple.driver.AppleCS42L79Audio.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `['audio-control,cs42l79']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) on `audio-control,cs42l79`

## Strings in its kext that name it (3)

- `site.AppleCS42L79Audio`
- `AppleCS42L79Audio`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/CS42L79/AppleCS42L79Audio.cpp`

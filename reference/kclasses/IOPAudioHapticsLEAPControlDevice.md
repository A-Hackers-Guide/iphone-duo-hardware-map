# `IOPAudioHapticsLEAPControlDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioHapticsLEAPControlDevice`](../kexts/com.apple.driver.IOPAudioHapticsLEAPControlDevice.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000ba182b8`; metaclass vtable `0xfffffe00083ce728`; class vtable `0xfffffe00083ce178`
- Registration (init): `0xfffffe000a2fcf98`
- Superclasses: [`IOPAudioLEAPControlDevice`](IOPAudioLEAPControlDevice.md) → [`IOPAudioDevice`](IOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOPAudioHapticsLEAPControlDevice` in [`com.apple.driver.IOPAudioHapticsLEAPControlDevice`](../kexts/com.apple.driver.IOPAudioHapticsLEAPControlDevice.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-audio,haptics-leap-control-device']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/audio-haptic-leap`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic-leap.md) on `iop-audio,haptics-leap-control-device`

## Strings in its kext that name it (2)

- `IOPAudioHapticsLEAPControlDevice`
- `site.IOPAudioHapticsLEAPControlDevice`

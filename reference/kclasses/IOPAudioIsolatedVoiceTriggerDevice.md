# `IOPAudioIsolatedVoiceTriggerDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioVoiceTriggerDevice`](../kexts/com.apple.driver.IOPAudioVoiceTriggerDevice.md)
- Object size: `0x1c0` (448 bytes)
- Metaclass: `0xfffffe000ba189f0`; metaclass vtable `0xfffffe00083d42c8`; class vtable `0xfffffe00083d3d18`
- Registration (init): `0xfffffe000a315090`
- Superclasses: [`IOPAudioVoiceTriggerDevice`](IOPAudioVoiceTriggerDevice.md) → [`IOPAudioDevice`](IOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOPAudioIsolatedVoiceTriggerDevice` in [`com.apple.driver.IOPAudioVoiceTriggerDevice`](../kexts/com.apple.driver.IOPAudioVoiceTriggerDevice.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-audio,isolated-vt-device']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-voicetrigger-controller/audio-vt-device`](../devicetree/root__arm-io__iop-voicetrigger-controller__audio-vt-device.md) on `iop-audio,isolated-vt-device`

## Strings in its kext that name it (2)

- `site.IOPAudioIsolatedVoiceTriggerDevice`
- `IOPAudioIsolatedVoiceTriggerDevice`

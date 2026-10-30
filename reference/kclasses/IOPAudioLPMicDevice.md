# `IOPAudioLPMicDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioLPMicDevice`](../kexts/com.apple.driver.IOPAudioLPMicDevice.md)
- Object size: `0x2f0` (752 bytes)
- Metaclass: `0xfffffe000ba18718`; metaclass vtable `0xfffffe00083d14a0`; class vtable `0xfffffe00083d0e70`
- Registration (init): `0xfffffe000a304400`
- Superclasses: [`IOPAudioClientManagerDevice`](IOPAudioClientManagerDevice.md) → [`IOPAudioDevice`](IOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOPAudioLPMicDevice` in [`com.apple.driver.IOPAudioLPMicDevice`](../kexts/com.apple.driver.IOPAudioLPMicDevice.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-audio,lp-mic-device']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) on `iop-audio,lp-mic-device`

## Strings in its kext that name it (4)

- `IOPAudioLPMicDevice`
- `site.IOPAudioLPMicDeviceUserClient`
- `site.IOPAudioLPMicDevice`
- `IOPAudioLPMicDeviceUserClient`

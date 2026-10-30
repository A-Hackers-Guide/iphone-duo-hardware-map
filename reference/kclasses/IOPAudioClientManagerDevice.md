# `IOPAudioClientManagerDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioClientManagerDevice`](../kexts/com.apple.driver.IOPAudioClientManagerDevice.md)
- Object size: `0x2d0` (720 bytes)
- Metaclass: `0xfffffe000ba17d30`; metaclass vtable `0xfffffe00083caa28`; class vtable `0xfffffe00083ca420`
- Registration (init): `0xfffffe000a2e5aac`
- Superclasses: [`IOPAudioDevice`](IOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`IOPAudioLPMicDevice`](IOPAudioLPMicDevice.md) — `com.apple.driver.IOPAudioLPMicDevice`

## IOKit personalities that instantiate it (1)

- `ClientManagerDevice` in [`com.apple.driver.IOPAudioClientManagerDevice`](../kexts/com.apple.driver.IOPAudioClientManagerDevice.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-audio,client-manager-device']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) on `iop-audio,client-manager-device`

## Strings in its kext that name it (4)

- `IOPAudioClientManagerDeviceUserClient`
- `site.IOPAudioClientManagerDeviceUserClient`
- `IOPAudioClientManagerDevice`
- `site.IOPAudioClientManagerDevice`

# `IOPAudioIsolatedIOBufferDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOPAudioIsolatedIOBufferDevice`](../kexts/com.apple.driver.IOPAudioIsolatedIOBufferDevice.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000ba18510`; metaclass vtable `0xfffffe00083d0430`; class vtable `0xfffffe00083cfe60`
- Registration (init): `0xfffffe000a301138`
- Superclasses: [`IOPAudioDevice`](IOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IsolatedIOBufferDevice` in [`com.apple.driver.IOPAudioIsolatedIOBufferDevice`](../kexts/com.apple.driver.IOPAudioIsolatedIOBufferDevice.md): `IOProviderClass` = `IOPAudioNode`, `IONameMatch` = `['iop-audio,isolated-io-buffer-device']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md) on `iop-audio,isolated-io-buffer-device`

## Strings in its kext that name it (4)

- `site.IOPAudioIsolatedIOBufferDeviceUserClient`
- `IOPAudioIsolatedIOBufferDevice`
- `IOPAudioIsolatedIOBufferDeviceUserClient`
- `site.IOPAudioIsolatedIOBufferDevice`

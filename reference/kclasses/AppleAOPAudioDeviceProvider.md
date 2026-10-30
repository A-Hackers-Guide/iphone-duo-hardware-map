# `AppleAOPAudioDeviceProvider`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b9330c8`; metaclass vtable `0xfffffe0007fa9ea8`; class vtable `0xfffffe0007fa98b8`
- Registration (init): `0xfffffe00086aedc8`
- Superclasses: [`AppleAOPAudioDevice`](AppleAOPAudioDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (4)

- `AppleAOPAudioDeviceProvider` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IOPropertyMatch` = `{'compatible': 'aop-audio-control'}`, `IOMatchCategory` = `AppleAOPAudioDeviceProvider`
- `AppleAOPAudioHapticControlDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IOPropertyMatch` = `{'compatible': 'aop-audio-haptic'}`, `IOMatchCategory` = `AppleAOPAudioDeviceProvider`
- `AppleAOPAudioHapticDebugControlDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IOPropertyMatch` = `{'compatible': 'aop-audio-hpdbg'}`, `IOMatchCategory` = `AppleAOPAudioDeviceProvider`
- `AppleAOPAudioSpeakerControlDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IOPropertyMatch` = `{'compatible': 'aop-audio-speaker'}`, `IOMatchCategory` = `AppleAOPAudioDeviceProvider`

## Strings in its kext that name it (6)

- `site.AppleAOPAudioDeviceProvider`
- `+ AppleAOPAudioDeviceProvider::setDevicePowerState('%c%c%c%c', '%c%c%c%c')\n`
- `+ AppleAOPAudioDeviceProvider::setDevicePowerState('%c%c%c%c', %d)\n`
- `AppleAOPAudioDeviceProvider`
- `+-AppleAOPAudioDeviceProvider::start(provider: %p) -> err: 0x%x\n`
- `AppleAOPAudioDeviceProvider::setDevicePowerState() err: 0x%x\n`

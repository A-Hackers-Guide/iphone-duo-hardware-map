# `AppleAOPAudioDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b933028`; metaclass vtable `0xfffffe0007fa8cf0`; class vtable `0xfffffe0007fa8700`
- Registration (init): `0xfffffe00086a9434`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (12; 17 in total)

- [`AppleAOPAudioAmpManagerDevice`](AppleAOPAudioAmpManagerDevice.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioAssetManagerDevice`](AppleAOPAudioAssetManagerDevice.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioButtonHapticDevice`](AppleAOPAudioButtonHapticDevice.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioButtonOutputDevice`](AppleAOPAudioButtonOutputDevice.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioClientManager`](AppleAOPAudioClientManager.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioDeviceProvider`](AppleAOPAudioDeviceProvider.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioHallDevice`](AppleAOPAudioHallDevice.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioLEAP`](AppleAOPAudioLEAP.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioLPMicInDevice`](AppleAOPAudioLPMicInDevice.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioMCA2Device`](AppleAOPAudioMCA2Device.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioPDM2Device`](AppleAOPAudioPDM2Device.md) — `com.apple.driver.AppleAOPAudio`
- [`AppleAOPAudioSawDevice`](AppleAOPAudioSawDevice.md) — `com.apple.driver.AppleAOPAudio`

## IOKit personalities that instantiate it (1)

- `AppleAOPAudioDevice` in [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md): `IOProviderClass` = `AppleAOPAudioDeviceNode`, `IONameMatch` = `['audio-aop-edt-config']`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleAOPAudioDevice`, `IOProbeScore` = `1000`

## Strings in its kext that name it (15)

- `site.AppleAOPAudioDeviceProvider`
- `+ AppleAOPAudioDeviceProvider::setDevicePowerState('%c%c%c%c', '%c%c%c%c')\n`
- `AppleAOPAudioDeviceControllerObject`
- `site.AppleAOPAudioDeviceControllerObject`
- `AppleAOPAudioDevice`
- `AppleAOPAudioDeviceNode`
- `+ AppleAOPAudioDeviceProvider::setDevicePowerState('%c%c%c%c', %d)\n`
- `AppleAOPAudioDeviceNode::_getIdentifersFromDeviceTree() failed to get property '%s' from registry\n`
- `AppleAOPAudioDeviceController`
- `AppleAOPAudioDeviceProvider`
- `site.AppleAOPAudioDeviceController`
- `+-AppleAOPAudioDeviceProvider::start(provider: %p) -> err: 0x%x\n`
- `site.AppleAOPAudioDeviceNode`
- `site.AppleAOPAudioDevice`
- `AppleAOPAudioDeviceProvider::setDevicePowerState() err: 0x%x\n`

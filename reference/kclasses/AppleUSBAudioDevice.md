# `AppleUSBAudioDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBAudio`](../kexts/com.apple.driver.AppleUSBAudio.md)
- Object size: `0x1e8` (488 bytes)
- Metaclass: `0xfffffe000b9d41e8`; metaclass vtable `0xfffffe000829b300`; class vtable `0xfffffe000829a840`
- Registration (init): `0xfffffe0009ac5ad4`
- Superclasses: [`Audio2Device`](Audio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleUSBADCAudioDevice`](AppleUSBADCAudioDevice.md) — `com.apple.driver.AppleUSBAudio`
- [`AppleUSBDeviceAudioDevice`](AppleUSBDeviceAudioDevice.md) — `com.apple.driver.AppleUSBAudio`

## IOKit personalities that instantiate it (1)

- `AppleUSBAudioControl` in [`com.apple.driver.AppleUSBAudio`](../kexts/com.apple.driver.AppleUSBAudio.md): `IOProviderClass` = `IOUSBHostInterface`

## Strings in its kext that name it (6)

- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/KEXT/AppleUSBAudioDevice.cpp`
- `AppleUSBAudioDevice:: initialization failed!`
- `AppleUSBAudioDevice`
- `AppleUSBAudioDevice::setVoiceActivityDetectState on stream %d - need to send %d to the host\n`
- `AppleUSBAudioDevice::doToggleControlChange(uVAD) to %d`
- `site.AppleUSBAudioDevice`

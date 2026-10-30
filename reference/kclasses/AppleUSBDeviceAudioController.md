# `AppleUSBDeviceAudioController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBDeviceAudioController`](../kexts/com.apple.driver.AppleUSBDeviceAudioController.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b9d4be0`; metaclass vtable `0xfffffe00082a75e8`; class vtable `0xfffffe00082a7090`
- Registration (init): `0xfffffe0009b1fb00`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `AppleUSBDeviceAudioControl` in [`com.apple.driver.AppleUSBDeviceAudioController`](../kexts/com.apple.driver.AppleUSBDeviceAudioController.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'USBAudio2Control'}`
- `AppleUSBDeviceAudioStreamIN` in [`com.apple.driver.AppleUSBDeviceAudioController`](../kexts/com.apple.driver.AppleUSBDeviceAudioController.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'USBAudio2StreamIN'}`
- `AppleUSBDeviceAudioStreamOUT` in [`com.apple.driver.AppleUSBDeviceAudioController`](../kexts/com.apple.driver.AppleUSBDeviceAudioController.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'USBAudio2StreamOUT'}`

## Strings in its kext that name it (3)

- `/Library/Caches/com.apple.xbs/B5FDCB36-D853-46D3-9503-186FD0AD7D5C/TemporaryDirectory.BTvKfA/Sources/AppleUSBAudio/IDAM/AppleUSBDeviceAudioController.cpp`
- `AppleUSBDeviceAudioController`
- `site.AppleUSBDeviceAudioController`

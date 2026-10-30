# `AppleUSBMike`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBMike`](../kexts/com.apple.driver.AppleUSBMike.md)
- Object size: `0x820` (2,080 bytes)
- Metaclass: `0xfffffe000b9d59e8`; metaclass vtable `0xfffffe00082b3660`; class vtable `0xfffffe00082b3020`
- Registration (init): `0xfffffe0009b55cf0`
- Superclasses: [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `USB Mike` in [`com.apple.driver.AppleUSBMike`](../kexts/com.apple.driver.AppleUSBMike.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'USBAudioControl'}`
- `USB Mike Streaming` in [`com.apple.driver.AppleUSBMike`](../kexts/com.apple.driver.AppleUSBMike.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'USBAudioStreaming'}`

## Strings in its kext that name it (4)

- `site.AppleUSBMike`
- `AppleUSBMike`
- `AppleUSBMike-buffer-debug`
- `AppleUSBMike-debug`

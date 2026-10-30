# `AppleUSBDeviceNCM11Data`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md)
- Object size: `0x230` (560 bytes)
- Metaclass: `0xfffffe000b9d4eb8`; metaclass vtable `0xfffffe00082aabf8`; class vtable `0xfffffe00082aa3e8`
- Registration (init): `0xfffffe0009b2a3f4`
- Superclasses: [`AppleUSBDeviceNCMData`](AppleUSBDeviceNCMData.md) → [`IOEthernetController`](IOEthernetController.md) → [`IONetworkController`](IONetworkController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `USB Device NCM Data` in [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'AppleUSBNCMData'}`
- `USB Device NCM Data Aux` in [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'AppleUSBNCMDataAux'}`

## Strings in its kext that name it (2)

- `site.AppleUSBDeviceNCM11Data`
- `AppleUSBDeviceNCM11Data`

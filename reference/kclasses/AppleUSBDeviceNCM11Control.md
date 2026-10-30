# `AppleUSBDeviceNCM11Control`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9d4ee0`; metaclass vtable `0xfffffe00082ab248`; class vtable `0xfffffe00082aac90`
- Registration (init): `0xfffffe0009b2ae3c`
- Superclasses: [`AppleUSBDeviceNCMControl`](AppleUSBDeviceNCMControl.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `USB Device NCM Control` in [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'AppleUSBNCMControl'}`
- `USB Device NCM Control Aux` in [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'AppleUSBNCMControlAux'}`
- `USB Device NCM Control Direct` in [`com.apple.driver.AppleUSBDeviceNCM`](../kexts/com.apple.driver.AppleUSBDeviceNCM.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'AppleUSBNCMControlDirect'}`

## Strings in its kext that name it (2)

- `site.AppleUSBDeviceNCM11Control`
- `AppleUSBDeviceNCM11Control`

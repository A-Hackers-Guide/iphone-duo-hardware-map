# `AppleUSBDeviceMux`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBDeviceMux`](../kexts/com.apple.driver.AppleUSBDeviceMux.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b9d4d10`; metaclass vtable `0xfffffe00082a83e0`; class vtable `0xfffffe00082a7e88`
- Registration (init): `0xfffffe0009b25684`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Apple USB Device Multiplexor` in [`com.apple.driver.AppleUSBDeviceMux`](../kexts/com.apple.driver.AppleUSBDeviceMux.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'AppleUSBMux'}`, `IOResourceMatch` = `IOBSD`

## Strings in its kext that name it (16)

- `void AppleUSBDeviceMux::bmsRetain(struct BulkUSBMuxSession *, const char *)`
- `void AppleUSBDeviceMux::vsendMuxRST(struct tcphdr *, bool, const char *, va_list)`
- `void AppleUSBDeviceMux::bmsRelease(struct BulkUSBMuxSession *, const char *)`
- `IOReturn AppleUSBDeviceMux::allocateUSBReadBuffers()`
- `AppleUSBDeviceMux.cpp`
- `void AppleUSBDeviceMux::asyncWriteComplete(struct USBWriteBuffer *, IOReturn, UInt32)`
- `AppleUSBDeviceMux`
- `AppleUSBDeviceMux::%s - kMessageInterfaceWasSuspended\n`
- `site.AppleUSBDeviceMux`
- `AppleUSBDeviceMux::%s - kMessageInterfaceWasDeActivated\n`
- `void AppleUSBDeviceMux::freeBufferList(struct USBWriteBuffer *)`
- `IOReturn AppleUSBDeviceMux::writeToUSBPipe(struct USBWriteBuffer *)`
- `AppleUSBDeviceMux build: %s %s\n`
- `AppleUSBDeviceMux::%s - kMessageInterfaceWasActivated\n`
- `IOReturn AppleUSBDeviceMux::setPropertiesGated(OSObject *)`
- `IOReturn AppleUSBDeviceMux::allocateUSBWriteBuffers()`

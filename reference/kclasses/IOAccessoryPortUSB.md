# `IOAccessoryPortUSB`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryPortUSB`](../kexts/com.apple.iokit.IOAccessoryPortUSB.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b9f2af8`; metaclass vtable `0xfffffe0008350938`; class vtable `0xfffffe0008350390`
- Registration (init): `0xfffffe000a0627fc`
- Superclasses: [`IOAccessoryPort`](IOAccessoryPort.md) → [`IOAccessoryTransport`](IOAccessoryTransport.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IAP USB Port` in [`com.apple.iokit.IOAccessoryPortUSB`](../kexts/com.apple.iokit.IOAccessoryPortUSB.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'IapOverUsbHid'}`

## Strings in its kext that name it (4)

- `IOAccessoryPortUSBRoleSwitchMaskValue`
- `IOAccessoryPortUSBRoleSwitchMaskIndex`
- `site.IOAccessoryPortUSB`
- `IOAccessoryPortUSB`

# `IOAccessoryPortSerialSync`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0x1f8` (504 bytes)
- Metaclass: `0xfffffe000b9f1cc8`; metaclass vtable `0xfffffe0008336b38`; class vtable `0xfffffe0008336558`
- Registration (init): `0xfffffe0009fd5fc0`
- Superclasses: [`IOAccessoryPortSerial`](IOAccessoryPortSerial.md) → [`IOAccessoryPort`](IOAccessoryPort.md) → [`IOAccessoryTransport`](IOAccessoryTransport.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IAP Serial Port` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `AppleOnboardSerialSync`, `IONameMatch` = `iap,uart`, `IOMatchCategory` = `IOAccessoryPort`

## Strings in its kext that name it (2)

- `IOAccessoryPortSerialSync`
- `site.IOAccessoryPortSerialSync`

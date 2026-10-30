# `IOAccessoryPortIDBus`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b9f2668`; metaclass vtable `0xfffffe000834b038`; class vtable `0xfffffe000834aa98`
- Registration (init): `0xfffffe000a01a03c`
- Superclasses: [`IOAccessoryPort`](IOAccessoryPort.md) → [`IOAccessoryTransport`](IOAccessoryTransport.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IAP ID Bus` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOAccessoryBulkDataEndpoint`

## Strings in its kext that name it (5)

- `%s: receieveDataBuff for kIOAccessoryPortIDBusRetDataTransferRead failed\n`
- `IOAccessoryPortIDBus`
- `IOAccessoryPortIDBusSNTP`
- `site.IOAccessoryPortIDBusSNTP`
- `site.IOAccessoryPortIDBus`

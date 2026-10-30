# `IODPService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md)
- Object size: `0x540` (1,344 bytes)
- Metaclass: `0xfffffe000b9f39d8`; metaclass vtable `0xfffffe0008366b50`; class vtable `0xfffffe0008365b80`
- Registration (init): `0xfffffe000a0c53fc`
- Superclasses: [`IOAVService`](IOAVService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`IODP13Service`](IODP13Service.md) — `com.apple.iokit.IODisplayPortFamily`
- [`IODPLegacyDualDVIService`](IODPLegacyDualDVIService.md) — `com.apple.iokit.IODisplayPortFamily`
- [`IODPServiceAUXOnly`](IODPServiceAUXOnly.md) — `com.apple.iokit.IODisplayPortFamily`

## IOKit personalities that instantiate it (1)

- `IODPService` in [`com.apple.iokit.IODisplayPortFamily`](../kexts/com.apple.iokit.IODisplayPortFamily.md): `IOProviderClass` = `IODPDevice`

## Strings in its kext that name it (9)

- `site.IODPServiceUserClient`
- `IODPServiceConcreteUserClient`
- `site.IODPServiceAUXOnly`
- `IODPServiceAUXOnly`
- `site.IODPServiceConcreteUserClient`
- `IODPService`
- `IODPServiceUserClient`
- `IODPServiceUserInterfaceSupported`
- `site.IODPService`

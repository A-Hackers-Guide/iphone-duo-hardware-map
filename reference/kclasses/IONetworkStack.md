# `IONetworkStack`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONetworkingFamily`](../kexts/com.apple.iokit.IONetworkingFamily.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000ba179b8`; metaclass vtable `0xfffffe00083c71e8`; class vtable `0xfffffe00083c6c90`
- Registration (init): `0xfffffe000a2de5bc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IONetworkStack` in [`com.apple.iokit.IONetworkingFamily`](../kexts/com.apple.iokit.IONetworkingFamily.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `IONetworkStack`

## Strings in its kext that name it (7)

- `site.IONetworkStack`
- `IONetworkStackUserClient`
- `site.IONetworkStackUserClient`
- `IONetworkStackUserCommand`
- `IONetworkStack`
- `IONetworkStack::start(%p) %p failed\n`
- `IONetworkStack::free() %p\n`

# `IOCECUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOCECFamily`](../kexts/com.apple.iokit.IOCECFamily.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b9f3268`; metaclass vtable `0xfffffe0008358f50`; class vtable `0xfffffe0008358958`
- Registration (init): `0xfffffe000a086074`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (9)

- `virtual IOReturn IOCECUserClient::open()`
- `virtual IOReturn IOCECUserClient::close()`
- `virtual IOReturn IOCECUserClient::clientClose()`
- `virtual IOReturn IOCECUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- `virtual bool IOCECUserClient::didTerminate(IOService *, IOOptionBits, bool *)`
- `virtual bool IOCECUserClient::start(IOService *)`
- `IOCECUserClient`
- `virtual IOReturn IOCECUserClient::registerNotificationPort(mach_port_t, UInt32, io_user_reference_t)`
- `site.IOCECUserClient`

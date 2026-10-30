# `AFKSharedMemoryUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b9458b8`; metaclass vtable `0xfffffe00080a1888`; class vtable `0xfffffe00080a1298`
- Registration (init): `0xfffffe0008cb8f10`
- Superclasses: [`IOUserClient2022`](IOUserClient2022.md) → [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (7)

- `virtual bool AFKSharedMemoryUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `IOReturn AFKSharedMemoryUserClient::clientMemoryForTypeGated(UInt32 *, IOOptionBits *, IOMemoryDescriptor **)`
- `IOReturn AFKSharedMemoryUserClient::testMethodGated(void *, IOExternalMethodArguments *)`
- `virtual void AFKSharedMemoryUserClient::stop(IOService *)`
- `virtual bool AFKSharedMemoryUserClient::start(IOService *)`
- `site.AFKSharedMemoryUserClient`
- `AFKSharedMemoryUserClient`

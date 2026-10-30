# `AFKSharedMemoryMapServer`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b945818`; metaclass vtable `0xfffffe000809ff40`; class vtable `0xfffffe000809f9e8`
- Registration (init): `0xfffffe0008cb6054`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AFKSharedMemoryMapServer` in [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md): `IOProviderClass` = `AFKEndpointInterface`, `IONameMatch` = `['afk-shmem-registry', 'afk-shmem-test-registry']`

## Strings in its kext that name it (5)

- `AFKSharedMemoryMapServer`
- `site.AFKSharedMemoryMapServer`
- `virtual void AFKSharedMemoryMapServer::stop(IOService *)`
- `AFKSharedMemoryMapServer.cpp`
- `virtual bool AFKSharedMemoryMapServer::start(IOService *)`

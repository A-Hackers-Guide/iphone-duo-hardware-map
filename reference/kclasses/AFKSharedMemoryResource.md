# `AFKSharedMemoryResource`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b945890`; metaclass vtable `0xfffffe00080a11d0`; class vtable `0xfffffe00080a0c78`
- Registration (init): `0xfffffe0008cb830c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AFKSharedMemoryResource` in [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `AFKSharedMemoryResource`

## Strings in its kext that name it (3)

- `virtual bool AFKSharedMemoryResource::start(IOService *)`
- `AFKSharedMemoryResource`
- `site.AFKSharedMemoryResource`

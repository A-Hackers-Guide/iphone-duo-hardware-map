# `AFKLocalMemoryDescriptorManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b945df0`; metaclass vtable `0xfffffe00080acb30`; class vtable `0xfffffe00080ac5a8`
- Registration (init): `0xfffffe0008cdbe64`
- Superclasses: [`AFKMemoryDescriptorManagerBase`](AFKMemoryDescriptorManagerBase.md) → [`AFKMemoryDescriptorManager`](AFKMemoryDescriptorManager.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AFKLocalMemoryDescriptorManager` in [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md): `IOProviderClass` = `AFKEndpointInterface`, `IOPropertyMatch` = `{'md-allocator': 'md-al-remote'}`

## Strings in its kext that name it (3)

- `AFKLocalMemoryDescriptorManager`
- `site.AFKLocalMemoryDescriptorManager`
- `AFKLocalMemoryDescriptorManager.cpp`

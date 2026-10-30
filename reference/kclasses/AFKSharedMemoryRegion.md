# `AFKSharedMemoryRegion`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b945840`; metaclass vtable `0xfffffe00080a05d0`; class vtable `0xfffffe00080a0058`
- Registration (init): `0xfffffe0008cb6d0c`
- Superclasses: [`AFKSharedMemoryRegionBase`](AFKSharedMemoryRegionBase.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (11)

- `AFKSharedMemoryRegion`
- `site.AFKSharedMemoryRegionBase`
- `virtual IOReturn AFKSharedMemoryRegionBase::newUserClient(task_t, void *, UInt32, IOUserClient **)`
- `virtual bool AFKSharedMemoryRegion::start(IOService *)`
- `AFKSharedMemoryRegion.cpp`
- `site.AFKSharedMemoryRegion`
- `AFKSharedMemoryRegionBase`
- `static OSSharedPtr<AFKSharedMemoryRegion> AFKSharedMemoryRegion::create(const OSSymbol *, size_t, uint8_t, OSString *, bool, IOPhysicalAddress)`
- `%s(%s:%#llx): AFKSharedMemoryRegion::create failed (%s)\n`
- `%s(%s:%#llx): AFKSharedMemoryRegion::attach failed (%s)\n`
- `%s(%s:%#llx): AFKSharedMemoryRegion::start failed (%s)\n`

# `AFKSharedMemoryRegionBase`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleFirmwareKit`](../kexts/com.apple.driver.AppleFirmwareKit.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b945868`; metaclass vtable `0xfffffe00080a0be0`; class vtable `0xfffffe00080a0668`
- Registration (init): `0xfffffe0008cb7410`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`AFKSharedMemoryRegion`](AFKSharedMemoryRegion.md) — `com.apple.driver.AppleFirmwareKit`
- [`AFKTestSharedMemoryRegion`](AFKTestSharedMemoryRegion.md) — `com.apple.driver.AppleFirmwareKit`
- [`AFKiBootSharedMemoryRegion`](AFKiBootSharedMemoryRegion.md) — `com.apple.driver.AppleFirmwareKit`

## Strings in its kext that name it (3)

- `site.AFKSharedMemoryRegionBase`
- `virtual IOReturn AFKSharedMemoryRegionBase::newUserClient(task_t, void *, UInt32, IOUserClient **)`
- `AFKSharedMemoryRegionBase`

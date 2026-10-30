# `KDIBackingStore`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DiskImages.KernelBacked`](../kexts/com.apple.driver.DiskImages.KernelBacked.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b9f54d0`; metaclass vtable `0xfffffe00083887f0`; class vtable `0xfffffe0008388210`
- Registration (init): `0xfffffe000a17175c`
- Superclasses: [`KDIObject`](KDIObject.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 5 in total)

- [`KDIEncoding`](KDIEncoding.md) — `com.apple.driver.DiskImages.KernelBacked`
- [`KDIFileBackingStore`](KDIFileBackingStore.md) — `com.apple.driver.DiskImages.FileBackingStore`
- [`KDIRAMBackingStore`](KDIRAMBackingStore.md) — `com.apple.driver.DiskImages.RAMBackingStore`

## Strings in its kext that name it (4)

- `KDIBackingStore::readBytes: returning kIOReturnUnsupported\n`
- `KDIBackingStore`
- `site.KDIBackingStore`
- `KDIBackingStore::writeBytes: returning kIOReturnUnsupported\n`

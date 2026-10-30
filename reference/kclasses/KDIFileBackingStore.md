# `KDIFileBackingStore`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DiskImages.FileBackingStore`](../kexts/com.apple.driver.DiskImages.FileBackingStore.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000b9f5358`; metaclass vtable `0xfffffe0008386bc8`; class vtable `0xfffffe00083865e8`
- Registration (init): `0xfffffe000a16f004`
- Superclasses: [`KDIBackingStore`](KDIBackingStore.md) → [`KDIObject`](KDIObject.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `KDIFileBackingStore` in [`com.apple.driver.DiskImages.FileBackingStore`](../kexts/com.apple.driver.DiskImages.FileBackingStore.md): `IOProviderClass` = `KDIURL`, `IOProbeScore` = `100`

## Strings in its kext that name it (6)

- `KDIFileBackingStore`
- `KDIFileBackingStore::_handleStart: initial R/W vn_open returned %d\n`
- `KDIFileBackingStore::_handleStart: res = %d\n`
- `KDIFileBackingStore::_handleStart: vnode_getattr() returned %d\n`
- `site.KDIFileBackingStore`
- `KDIFileBackingStore::_handleStart: vn_open() returned %d\n`

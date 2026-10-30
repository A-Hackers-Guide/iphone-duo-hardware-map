# `IONVMeBlockStorageDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x1d8` (472 bytes)
- Metaclass: `0xfffffe000ba174d8`; metaclass vtable `0xfffffe00083c1510`; class vtable `0xfffffe00083c0ee0`
- Registration (init): `0xfffffe000a2ac5f8`
- Superclasses: [`IOBlockStorageDevice`](IOBlockStorageDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`IOEmbeddedNVMeBlockDevice`](IOEmbeddedNVMeBlockDevice.md) — `com.apple.iokit.IONVMeFamily`

## Strings in its kext that name it (9)

- `virtual bool IONVMeBlockStorageDevice::start(IOService *)`
- `site.IONVMeBlockStorageDevice`
- `IONVMeBlockStorageDevice`
- `IONVMeBlockStorageDevice.cpp`
- `IOReturn IONVMeBlockStorageDevice::ScheduleBGRefresh()`
- `IOReturn IONVMeBlockStorageDevice::PowerDownHandler(void *, uint32_t, IOService *, void *, vm_size_t)`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/IONVMeBlockStorageDevice.cpp`
- `virtual IOReturn IONVMeBlockStorageDevice::doEjectMedia()`
- `bool IONVMeBlockStorageDevice::ValidateEntitlement(const char *)`

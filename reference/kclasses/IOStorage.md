# `IOStorage`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOStorageFamily`](../kexts/com.apple.iokit.IOStorageFamily.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000ba1adf0`; metaclass vtable `0xfffffe00083f7328`; class vtable `0xfffffe00083f6d70`
- Registration (init): `0xfffffe000a3e8ab0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (5; 12 in total)

- [`AppleAPFSContainerScheme`](AppleAPFSContainerScheme.md) — `com.apple.filesystems.apfs`
- [`IOBlockStorageDriver`](IOBlockStorageDriver.md) — `com.apple.iokit.IOStorageFamily`
- [`IOFilterScheme`](IOFilterScheme.md) — `com.apple.iokit.IOStorageFamily`
- [`IOMedia`](IOMedia.md) — `com.apple.iokit.IOStorageFamily`
- [`IOPartitionScheme`](IOPartitionScheme.md) — `com.apple.iokit.IOStorageFamily`

## Strings in its kext that name it (7)

- `virtual IOReturn IOUserBlockStorageDevice::doSynchronize(UInt64, UInt64, IOStorageSynchronizeOptions)`
- `virtual IOReturn IOUserBlockStorageDevice::doUnmap(IOBlockStorageDeviceExtent *, UInt32, IOStorageUnmapOptions)`
- `IOStorage`
- `virtual IOReturn IOUserBlockStorageDevice::doAsyncReadWrite(IOMemoryDescriptor *, uint64_t, uint64_t, IOStorageAttributes *, IOStorageCompletion *)`
- `com.apple.iokit.IOStorageFamily`
- `site.IOStorage`
- `IOStorageFeatures`

# `IOGPUMemoryMap`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x48` (72 bytes)
- Metaclass: `0xfffffe000b9f4a28`; metaclass vtable `0xfffffe00083783e8`; class vtable `0xfffffe00083782d0`
- Registration (init): `0xfffffe000a135af4`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 2 in total)

- [`AGXMemoryMap`](AGXMemoryMap.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (5)

- `virtual OSPtr<IOGPUMemoryMap> IOGPUMemory::createGPUMappingInTaskAtAddressLengthAlignment(IOGPUTask *, uint64_t, uint64_t, uint64_t, uint32_t)`
- `site.IOGPUMemoryMap *`
- `IOGPUMemoryMap`
- `bool IOGPUMemoryMap::update_pte(uint32_t, IOMemoryDescriptor *, IOMemoryDescriptor *)`
- `site.IOGPUMemoryMap`

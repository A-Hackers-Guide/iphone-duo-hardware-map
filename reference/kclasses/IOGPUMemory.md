# `IOGPUMemory`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x80` (128 bytes)
- Metaclass: `0xfffffe000b9f4268`; metaclass vtable `0xfffffe0008371be0`; class vtable `0xfffffe0008371ab8`
- Registration (init): `0xfffffe000a0fb318`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (4; 6 in total)

- [`AGXParameterMemoryVirtual`](AGXParameterMemoryVirtual.md) — `com.apple.AGXG19P`
- [`IOGPUGroupMemory`](IOGPUGroupMemory.md) — `com.apple.iokit.IOGPUFamily`
- [`IOGPUSysMemory`](IOGPUSysMemory.md) — `com.apple.iokit.IOGPUFamily`
- [`IOGPUVirtualMemory`](IOGPUVirtualMemory.md) — `com.apple.iokit.IOGPUFamily`

## Strings in its kext that name it (21)

- `IOReturn IOGPUScheduler::freeToWireMemory(IOGPUMemory *)`
- `virtual OSPtr<IOGPUMemoryMap> IOGPUMemory::createGPUMappingInTaskAtAddressLengthAlignment(IOGPUTask *, uint64_t, uint64_t, uint64_t, uint32_t)`
- `\"IOGPUMemory::detach() memory still prepared\\n\" @%s:%d`
- `IOGPUMemoryDecriptor.cpp`
- `\"IOGPUMemory::dealloc() memory still prepared\\n\" @%s:%d`
- `site.IOGPUMemoryMap *`
- `IOGPUMemory`
- `site.IOGPUMemoryInfoUserClient`
- `site.IOGPUMemory`
- `site.IOGPUMemory *`
- `IOGPUMemoryMap`
- `bool IOGPUCommandDescriptor::addMemory(IOGPUMemory *)`
- `IOReturn IOGPUMemory::detach()`
- `IOReturn IOGPUMemoryInfoUserClient::gather_memory_data(uint32_t, uint32_t *, uint32_t *, void *)`
- `bool IOGPUMemoryMap::update_pte(uint32_t, IOMemoryDescriptor *, IOMemoryDescriptor *)`
- `IOGPUMemory.cpp`
- `IOGPUMemoryInfoUserClient`
- `\"IOGPUMemory::dealloc() eviction failed\\n\" @%s:%d`
- `IOReturn IOGPUMemory::prepare_memory_slow(uint32_t, bool, uint64_t)`
- `site.IOGPUMemoryMap`
- `Can't upgrade IOGPUMemory.protectionOptions while still wired (0x%x->0x%x)\n`

# `IOGPUVirtualMemory`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b9f4240`; metaclass vtable `0xfffffe0008371a20`; class vtable `0xfffffe00083718d8`
- Registration (init): `0xfffffe000a0f9ce8`
- Superclasses: [`IOGPUMemory`](IOGPUMemory.md) → [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXVirtualMemory`](AGXVirtualMemory.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (11)

- `virtual IOReturn IOGPUVirtualMemory::updateMemoryAtIndexLocked(uint32_t, IOMemoryDescriptor *)`
- `virtual IOReturn IOGPUVirtualMemory::wire()`
- `virtual void IOGPUVirtualMemory::updateResidencyData(uint32_t, uint8_t)`
- `IOGPUVirtualMemory`
- `virtual void IOGPUVirtualMemory::unwire()`
- `virtual bool IOGPUVirtualMemory::init(IOGPU *, uint64_t, uint32_t, bool, uint64_t, uint64_t, task_t)`
- `virtual void IOGPUVirtualMemory::describeAllocation(OSDictionary *)`
- `IOReturn IOGPUVirtualMemory::copyMemoryAtIndexAndLength(IOGPUVirtualMemory *, uint32_t, uint32_t, uint32_t)`
- `IOGPUVirtualMemory.cpp`
- `site.IOGPUVirtualMemory`
- `%s: Failed to allocate IOGPUVirtualMemory object\n`

# `IOGPUSysMemory`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b9f4a78`; metaclass vtable `0xfffffe00083786e0`; class vtable `0xfffffe00083785b8`
- Registration (init): `0xfffffe000a138bb4`
- Superclasses: [`IOGPUMemory`](IOGPUMemory.md) → [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXAllocation`](AGXAllocation.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (19)

- `static OSSharedPtr<IOMemoryDescriptor> IOGPUSysMemory::memoryDescriptorWithClientBuffer(task_t, mach_vm_address_t, uint64_t)`
- `IOGPUSysMemory.cpp`
- `IOReturn IOGPUSysMemory::replace_backing_bytes_locked(task_t, mach_vm_address_t, uint64_t)`
- `IOReturn IOGPUSysMemory::replace_backing_ranges_locked(task_t, IOAddressRange *, uint32_t, bool)`
- `IOGPUSysMemory *IOGPUResource::owns_replaceable_backing() const`
- `IOGPUSysMemory`
- `static OSSharedPtr<IOMemoryDescriptor> IOGPUSysMemory::memoryDescriptorWithClientRanges(task_t, IOAddressRange *, uint32_t, bool)`
- `site.IOGPUSysMemory`
- `virtual IOMemoryDescriptor **IOGPUSysMemory::get_memory_descriptors(uint32_t, IOOptionBits, uint32_t *)`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withOptions(IOGPU *, task_t, IOGPUDevice *, IOGPUResource *, IOOptionBits, uint64_t, uint64_t, task_t)`
- `virtual IOReturn IOGPUSysMemory::wire()`
- `virtual void IOGPUSysMemory::describeAllocation(OSDictionary *)`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withClientBuffer(IOGPU *, task_t, IOGPUDevice *, mach_vm_address_t, uint64_t)`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withClientRanges(IOGPU *, task_t, IOAddressRange *, uint32_t, bool)`
- `OSPtr<IOMemoryMap> IOGPUSysMemory::retainCPUWireMapping(IOOptionBits)`
- `\"IOGPUSysMemory::makeUntracked() called while resident\\n\" @%s:%d`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withMemoryDescriptor(IOGPU *, IOGPUResource *, IOMemoryDescriptor *)`
- `virtual void IOGPUSysMemory::unwire()`
- `%s: IOGPUSysMemory::withOptions failed\n`

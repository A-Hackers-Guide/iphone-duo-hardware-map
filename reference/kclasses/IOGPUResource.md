# `IOGPUResource`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b9f45b0`; metaclass vtable `0xfffffe0008375040`; class vtable `0xfffffe0008374f20`
- Registration (init): `0xfffffe000a10f580`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXResource`](AGXResource.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (35)

- `\"IOGPUResource::free called for resource still owned by an IOGPUDevice\" @%s:%d`
- `IOReturn IOGPUResource::replace_backing_ranges(task_t, mach_vm_address_t, uint64_t, bool, bool, uint64_t *)`
- `virtual bool IOGPUResource::init(IOGPU *, IOGPUDevice *, uint32_t)`
- `IOGPUResource`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithIOSurfaceDeviceCache(IOGPU *, IOSurfaceDeviceCache *)`
- `IOGPUSysMemory *IOGPUResource::owns_replaceable_backing() const`
- `bool IOGPUResourceSet::add_resource_slow(IOGPUResource *)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithIOSurface(IOGPU *, IOGPUDevice *, IOSurface *, uint32_t, uint32_t)`
- `IOReturn IOGPUResource::updateMappings(OSSharedPtr<IOGPUResource>, sIOGPUMappingOp *, uint32_t, IOOptionBits)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithClientAddressRanges(IOGPU *, IOGPUDevice *, mach_vm_address_t *, IOGPUNewResourceArgs *)`
- `IOGPUResource.cpp`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withOptions(IOGPU *, task_t, IOGPUDevice *, IOGPUResource *, IOOptionBits, uint64_t, uint64_t, task_t)`
- `site.IOGPUResourceSet`
- `const sIOGPUEvent *IOGPUResource::gartEvent() const`
- `site.IOGPUResource *`
- `IOReturn IOGPUResource::copyMappings(OSSharedPtr<IOGPUResource>, sIOGPUMappingOp *, uint32_t, IOOptionBits)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceGroup(IOGPU *, IOGPUDevice *, uint32_t)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithOptions(IOGPU *, IOGPUDevice *, enum eIOGPUResType, uint64_t, IOByteCount, IOOptionBits, mach_vm_address_t *, IOGPUNewResourceArgs *, uint64_t &, uint64_t &)`
- `virtual bool IOGPUResource::mapAtAddressLength(uint64_t, uint64_t, uint64_t)`
- `static OSPtr<IOGPUResource> IOGPUResource::newVirtualResource(IOGPU *, IOGPUDevice *, IOGPUNewResourceArgs *)`
- `void IOGPUResource::setPurgeable(IOOptionBits, IOOptionBits)`
- `IOReturn IOGPUDevice::set_resource_purgeable(const uint32_t, eIOGPUResourcePurgeable, eIOGPUResourcePurgeable *)`
- `IOReturn IOGPUGroupMemory::addMemoryFromResources(IOGPUResource **const, const unsigned int)`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withMemoryDescriptor(IOGPU *, IOGPUResource *, IOMemoryDescriptor *)`
- `IOGPUResourceSet`
- `virtual bool IOGPUResource::map(uint64_t, uint32_t)`
- `IOReturn IOGPUResource::replace_backing_bytes(task_t, mach_vm_address_t, uint64_t)`
- `site.IOGPUResource`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithClientBuffer(IOGPU *, IOGPUDevice *, enum eIOGPUResType, IOByteCount, mach_vm_address_t, mach_vm_address_t, mach_vm_address_t *)`
- `IOReturn IOGPUResource::detach_backing()`
- `void *IOGPUResource::getKernelData()`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithParentResourceID(IOGPU *, IOGPUDevice *, enum eIOGPUResType, uint64_t, IOByteCount, mach_vm_address_t, mach_vm_address_t, mach_vm_address_t *, uint32_t)`
- `const sIOGPUEvent *IOGPUResource::gartWriteEvent() const`
- `%s: allocIOGPUResource failed to alloc texture object\n`
- `%s: PID %d may be leaking IOGPUResource (count=%d)\n`

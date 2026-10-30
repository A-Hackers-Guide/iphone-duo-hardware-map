# `IOGPUDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9f4740`; metaclass vtable `0xfffffe0008375e28`; class vtable `0xfffffe0008375d28`
- Registration (init): `0xfffffe000a11f058`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXShared`](AGXShared.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (55)

- `IOGPUDeviceAssertion`
- `IOReturn IOGPUDevice::resource_replace_backing_bytes(sIOGPUReplaceBackingBytesData *)`
- `\"IOGPUResource::free called for resource still owned by an IOGPUDevice\" @%s:%d`
- `virtual bool IOGPUResource::init(IOGPU *, IOGPUDevice *, uint32_t)`
- `IOReturn IOGPUDevice::resource_replace_backing_ranges(sIOGPUReplaceBackingRangesData *, uint64_t *)`
- `IOReturn IOGPUDeviceUserClient::t_signal_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOReturn IOGPUDeviceUserClient::t_signal_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `static IOReturn IOGPUDeviceUserClient::s_submit_command_buffers(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `virtual int32_t IOGPUEventMachine::requestStampIndexForChannel(IOGPUChannel *, IOGPUDevice *)`
- `virtual bool IOGPUIOCommandQueue::init(IOGPUDevice *, uint32_t, uint32_t)`
- `IOGPUDevice`
- `static IOReturn IOGPUDeviceUserClient::s_create_vniodesc(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.IOGPUDevice`
- `site.struct IOGPUDeviceUserClientPrivate`
- `IOReturn IOGPUDevice::resource_detach_backing(uint32_t)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithIOSurface(IOGPU *, IOGPUDevice *, IOSurface *, uint32_t, uint32_t)`
- `IOReturn IOGPUDeviceUserClient::t_wait_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOGPUDeviceAssertion.cpp`
- `static IOReturn IOGPUDeviceUserClient::s_destroy_io_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `IOGPUDevice.cpp`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithClientAddressRanges(IOGPU *, IOGPUDevice *, mach_vm_address_t *, IOGPUNewResourceArgs *)`
- `\"IOGPUDeviceAssertion::initWithAccelerator Unsupported assertionType %lld\" @%s:%d`
- `static IOReturn IOGPUDeviceUserClient::s_group_add_resources(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_set_io_notification_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withOptions(IOGPU *, task_t, IOGPUDevice *, IOGPUResource *, IOOptionBits, uint64_t, uint64_t, task_t)`
- `IOReturn IOGPUDeviceUserClient::t_wait_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceGroup(IOGPU *, IOGPUDevice *, uint32_t)`
- `static OSPtr<IOGPUSysMemory> IOGPUSysMemory::withClientBuffer(IOGPU *, task_t, IOGPUDevice *, mach_vm_address_t, uint64_t)`
- `IOGPUDeviceUserClient`
- `virtual bool IOGPUDeviceUserClient::deviceUserClientStart()`
- `static IOReturn IOGPUDeviceUserClient::s_create_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithOptions(IOGPU *, IOGPUDevice *, enum eIOGPUResType, uint64_t, IOByteCount, IOOptionBits, mach_vm_address_t *, IOGPUNewResourceArgs *, uint64_t &, uint64_t &)`
- `IOReturn IOGPUDevice::new_resource(IOGPUNewResourceArgs *, struct IOGPUNewResourceReturnData *, IOByteCount, uint32_t *)`
- `static IOReturn IOGPUDeviceUserClient::s_perform_io(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_async_signal_mtlLateEvalevent(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static OSPtr<IOGPUResource> IOGPUResource::newVirtualResource(IOGPU *, IOGPUDevice *, IOGPUNewResourceArgs *)`
- `static IOReturn IOGPUDeviceUserClient::s_create_io_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `IOReturn IOGPUDevice::set_resource_purgeable(const uint32_t, eIOGPUResourcePurgeable, eIOGPUResourcePurgeable *)`
- `static IOReturn IOGPUDeviceUserClient::s_destroy_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `site.IOGPUDeviceAssertion`
- `static IOReturn IOGPUDeviceUserClient::s_group_remove_resources(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_query_mtlLateEvalevent(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_new_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `IOReturn IOGPUDevice::create_notificationqueue(uint32_t, uint32_t, sIOGPUDeviceNotificationQueueData *)`
- `site.IOGPUDeviceShmem`
- `static IOReturn IOGPUDeviceUserClient::s_submit_io_commands(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_try_cancel_io_command_buffer(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_delete_command_queue(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_io_command_buffer_barrier_complete(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `IOGPUDeviceShmem`
- `site.IOGPUDeviceUserClient`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithClientBuffer(IOGPU *, IOGPUDevice *, enum eIOGPUResType, IOByteCount, mach_vm_address_t, mach_vm_address_t, mach_vm_address_t *)`
- `static IOReturn IOGPUDeviceUserClient::s_new_resource(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn IOGPUDeviceUserClient::s_io_command_buffer_complete(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithParentResourceID(IOGPU *, IOGPUDevice *, enum eIOGPUResType, uint64_t, IOByteCount, mach_vm_address_t, mach_vm_address_t, mach_vm_address_t *, uint32_t)`

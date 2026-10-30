# `IOGPU`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x2f0` (752 bytes)
- Metaclass: `0xfffffe000b9f48f8`; metaclass vtable `0xfffffe0008377848`; class vtable `0xfffffe0008377168`
- Registration (init): `0xfffffe000a12c68c`
- Superclasses: [`IOAcceleratorES`](IOAcceleratorES.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 5 in total)

- [`AGXAccelerator`](AGXAccelerator.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (60)

- `IOGPUDeviceAssertion`
- `IOReturn IOGPUDevice::resource_replace_backing_bytes(sIOGPUReplaceBackingBytesData *)`
- `IOGPUStatistics`
- `IOGPUFamily Parameters`
- `IOGPU Completion`
- `virtual void IOGPUCommandQueue::submitCommandBuffer(const sIOGPUCommandQueueCommandBufferArgs *)`
- `static OSSharedPtr<IOMemoryDescriptor> IOGPUSysMemory::memoryDescriptorWithClientBuffer(task_t, mach_vm_address_t, uint64_t)`
- `IOGPUKernelMappedMemory`
- `\"IOGPUResource::free called for resource still owned by an IOGPUDevice\" @%s:%d`
- `IOReturn IOGPUResource::replace_backing_ranges(task_t, mach_vm_address_t, uint64_t, bool, bool, uint64_t *)`
- `IOGPU Submission`
- `IOGPU`
- `site.IOGPUFenceMachine`
- `virtual bool IOGPUResource::init(IOGPU *, IOGPUDevice *, uint32_t)`
- `virtual void IOGPUCommandQueue::processCommandBuffer(const sIOGPUCommandQueueCommandBufferArgs *)`
- `virtual void IOGPUCommandQueue::processKernelCommand(const sIOGPUKernelCommand *, const sIOGPUKernelCommand *)`
- `IOGPUCommandQueue.cpp`
- `bool IOGPUIOCommandBuffer::getIOCommands(sIOGPUIOCommandListHead *)`
- `IOGPUCommandDescriptor`
- `IOReturn IOGPUScheduler::freeToWireMemory(IOGPUMemory *)`
- `IOGPUVnioDesc`
- `void IOGPUIOCommandBuffer::processKernelCommands(uint32_t)`
- `site.IOGPUTask`
- `IOGPUObject.cpp`
- `IOGPUResource`
- `site.IOGPUWorkQueueState`
- `IOReturn IOGPUDevice::resource_replace_backing_ranges(sIOGPUReplaceBackingRangesData *, uint64_t *)`
- `\"IOGPU::systemPagingOff() timeout. %d threads still stuck. addCommandToTail_slow %u, waitForAllSubmitted %u, workQueuesDisabled %u, waitingOnResources %u, waitForStamp %u, wireMemory %u\\n\" @%s:%d`
- `IOReturn IOGPUDeviceUserClient::t_signal_shared_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `IOGPUBlockFence`
- `site.IOGPUSegmentResourceList`
- `com.apple.iokit.IOGPUFamily.API`
- `IOReturn IOGPUDeviceUserClient::t_signal_mtl_event(uintptr_t, uintptr_t, uintptr_t, uintptr_t)`
- `site.IOGPUKernelMappedMemory`
- `IOGPUSysMemory.cpp`
- `static IOReturn IOGPUDeviceUserClient::s_submit_command_buffers(IOGPUDeviceUserClient *, void *, IOExternalMethodArguments *)`
- `virtual int32_t IOGPUEventMachine::requestStampIndexForChannel(IOGPUChannel *, IOGPUDevice *)`
- `site.IOGPUChannel`
- `site.IOGPUEventMachine`
- `IOGPUIOCommandQueue`
- `virtual OSPtr<IOGPUMemoryMap> IOGPUMemory::createGPUMappingInTaskAtAddressLengthAlignment(IOGPUTask *, uint64_t, uint64_t, uint64_t, uint32_t)`
- `\"IOGPUMemory::detach() memory still prepared\\n\" @%s:%d`
- `IOGPUMemoryDecriptor.cpp`
- `IOGPUMetalEvent.cpp`
- `static OSPtr<IOGPUResource> IOGPUResource::newResourceWithIOSurfaceDeviceCache(IOGPU *, IOSurfaceDeviceCache *)`
- `IOGPUScheduler.cpp`
- `\"IOGPUMemory::dealloc() memory still prepared\\n\" @%s:%d`
- `IOReturn IOGPUIOCommandQueue::performIO()`
- `IOReturn IOGPUCommandQueue::schedule_shared_event(mach_port_name_t, uint64_t, bool, uint32_t)`
- `\"IOGPUResidentMemorySet unable to expand\" @%s:%d`
- `virtual IOReturn IOGPUVirtualMemory::updateMemoryAtIndexLocked(uint32_t, IOMemoryDescriptor *)`
- `IOGPUSharedEventFence`
- `IOReturn IOGPUIOCommandQueue::destroyIOCommandBuffer(uint32_t)`
- `IOGPUWorkQueue`
- `IOGPUWorkQueueState`
- `IOGPUClientSharedMachine`
- `IOGPUSegmentResourceList`
- `IOReturn IOGPUSysMemory::replace_backing_bytes_locked(task_t, mach_vm_address_t, uint64_t)`
- `virtual bool IOGPUIOCommandBuffer::init(IOGPUIOCommandQueue *)`
- `virtual bool IOGPUIOCommandQueue::init(IOGPUDevice *, uint32_t, uint32_t)`

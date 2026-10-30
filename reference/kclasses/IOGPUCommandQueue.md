# `IOGPUCommandQueue`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x5d0` (1,488 bytes)
- Metaclass: `0xfffffe000b9f49b0`; metaclass vtable `0xfffffe0008377a40`; class vtable `0xfffffe00083778e0`
- Registration (init): `0xfffffe000a1314f4`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXCommandQueue`](AGXCommandQueue.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (19)

- `virtual void IOGPUCommandQueue::submitCommandBuffer(const sIOGPUCommandQueueCommandBufferArgs *)`
- `virtual void IOGPUCommandQueue::processCommandBuffer(const sIOGPUCommandQueueCommandBufferArgs *)`
- `virtual void IOGPUCommandQueue::processKernelCommand(const sIOGPUKernelCommand *, const sIOGPUKernelCommand *)`
- `IOGPUCommandQueue.cpp`
- `IOReturn IOGPUCommandQueue::schedule_shared_event(mach_port_name_t, uint64_t, bool, uint32_t)`
- `site.IOGPUCommandQueuePrivate`
- `virtual void IOGPUCommandQueue::signalSharedEvent(IOSurfaceSharedEvent *, uint64_t)`
- `virtual void IOGPUCommandQueue::waitSharedEvent(IOSurfaceSharedEvent *, uint64_t, uint32_t)`
- `IOGPUCommandQueue`
- `IOReturn IOGPUCommandQueue::setNotificationQueue(IOGPUNotificationQueue *)`
- `virtual void IOGPUCommandQueue::processSegmentKernelCommand(IOGPUSegmentResourceList *, const sIOGPUKernelCommand *, const sIOGPUKernelCommand *, const uint8_t *, const uint8_t *, const sIOGPUCommandQueueCommandBufferArgs *)`
- `int32_t IOGPUScheduler::registerCommandQueue(const IOGPUCommandQueue *)`
- `virtual void IOGPUCommandQueue::processSegmentKernelCommands(IOGPUSegmentResourceList *, const sIOGPUKernelCommand *, const sIOGPUKernelCommand *, const uint8_t *, const uint8_t *, const sIOGPUCommandQueueCommandBufferArgs *)`
- `void IOGPU::reportGPURestart(const IOGPUCommandQueue *, const char *, uint32_t, uint64_t)`
- `site.IOGPUCommandQueue`
- `virtual IOReturn IOGPUCommandQueue::schedulePostMappingWaitEvent(IOSurfaceSharedEvent *, uint64_t, uint32_t)`
- `void IOGPUCommandQueue::retireCommandBuffer(IOGPUEventFence *)`
- `virtual void IOGPUCommandQueue::processKernelCommands(const sIOGPUKernelCommand *, const sIOGPUKernelCommand *)`
- `%s: The number of queues (%d) exceeding limit (%d), failing IOGPUCommandQueue creation\n`

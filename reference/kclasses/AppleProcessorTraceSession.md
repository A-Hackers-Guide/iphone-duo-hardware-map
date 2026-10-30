# `AppleProcessorTraceSession`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0x160` (352 bytes)
- Metaclass: `0xfffffe000b9937f8`; metaclass vtable `0xfffffe00081bbb88`; class vtable `0xfffffe00081bbaf8`
- Registration (init): `0xfffffe00094579e8`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (44)

- `AppleProcessorTraceSession::enableTracingForTask()\n`
- `AppleProcessorTraceSession::initChunk(%u / %lu, 0x%llX, 0x%llX)\n`
- `AppleProcessorTraceSession::sendThrottleAdvisory(%{public}X)\n`
- `AppleProcessorTraceSession::configured\n`
- `AppleProcessorTraceSession::withConfig\n`
- `AppleProcessorTraceSession::init\n`
- `AppleProcessorTraceSession::sendThrottleAdvisory failed %{public}X\n`
- `AppleProcessorTraceSession::drainDirtyChunk(idx=%u, id=%llu, offset=0x%llX, size=0x%llX, checksum=0x%llX, fill_size=0x%llX, fill_wrap=%u, cluster_id=%u)\n`
- `AppleProcessorTraceSession::free\n`
- `AppleProcessorTraceSession::init: minFreeChunks = %zu (for throttling)\n`
- `IOReturn AppleProcessorTrace::attachToSessionGated(MethodAttachArgs, OSSharedPtr<AppleProcessorTraceSession> &, AppleProcessorTraceUserClient *)`
- `void AppleProcessorTraceSession::sendThrottleAdvisory(TaskState)`
- `IOReturn AppleProcessorTrace::reset(OSSharedPtr<AppleProcessorTraceSession>)_block_invoke`
- `IOReturn AppleProcessorTrace::configureGated(MethodConfigArgs, OSSharedPtr<AppleProcessorTraceSession> &, AppleProcessorTraceUserClient *)`
- `bool AppleProcessorTraceSession::init(const MethodConfigArgs, OSSharedPtr<AppleProcessorTraceEventSource>)`
- `AppleProcessorTraceSession`
- `void AppleProcessorTraceSession::unmapBufferVA()`
- `void AppleProcessorTraceSession::enqueueDirtyChunk(Chunk *)`
- `IOReturn AppleProcessorTrace::pauseTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `IOReturn AppleProcessorTrace::stopTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `IOReturn AppleProcessorTrace::unconfigureGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `virtual void AppleProcessorTraceSession::free()`
- `IOReturn AppleProcessorTrace::releaseChunkGated(OSSharedPtr<AppleProcessorTraceSession>, ChunkData)`
- `void AppleProcessorTraceSession::unlockBufferVA()`
- `void AppleProcessorTraceSession::transferFilledFreeChunksToDirtyQueue()`
- `site.AppleProcessorTraceSession`
- `OSSharedPtr<IOMemoryDescriptor> AppleProcessorTraceSession::getBufferVA()`
- `void AppleProcessorTraceSession::setChunkForCluster(ml_topology_cluster_t, unsigned int, Chunk *)`
- `OSSharedPtr<IOMemoryDescriptor> AppleProcessorTraceSession::getBufferPA()`
- `bool AppleProcessorTraceSession::mapBufferPA()`
- `IOReturn AppleProcessorTrace::reset(OSSharedPtr<AppleProcessorTraceSession>)`
- `IOReturn AppleProcessorTrace::resumeTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `Chunk *AppleProcessorTraceSession::getChunkForCluster(ml_topology_cluster_t, unsigned int)`
- `void AppleProcessorTraceSession::enqueueFreeChunk(Chunk *)`
- `Chunk *AppleProcessorTraceSession::getFreeChunk()`
- `IOReturn AppleProcessorTrace::addTaskGated(OSSharedPtr<AppleProcessorTraceSession>, MethodAddTaskArgs)`
- `AppleProcessorTraceSession.cpp`
- `void AppleProcessorTraceSession::resetBufferVA()`
- `bool AppleProcessorTraceSession::enableTracingForTask(mach_port_name_t)`
- `bool AppleProcessorTraceSession::mapBufferVA()`
- `IOReturn AppleProcessorTrace::startTracingGated(OSSharedPtr<AppleProcessorTraceSession>)`
- `void AppleProcessorTraceSession::drainDirtyChunksAndAdviseThrottle()`
- `void AppleProcessorTraceSession::unmapBufferPA()`
- `void AppleProcessorTraceSession::lockBufferVA()`

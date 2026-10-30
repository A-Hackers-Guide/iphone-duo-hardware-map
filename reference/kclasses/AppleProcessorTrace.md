# `AppleProcessorTrace`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProcessorTrace`](../kexts/com.apple.driver.AppleProcessorTrace.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b9936b8`; metaclass vtable `0xfffffe00081b98d0`; class vtable `0xfffffe00081b92c0`
- Registration (init): `0xfffffe000944bb14`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (22; 22 in total)

- [`AppleProcessorTraceBringUp`](AppleProcessorTraceBringUp.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT6000`](AppleProcessorTraceT6000.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT6020`](AppleProcessorTraceT6020.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT6030`](AppleProcessorTraceT6030.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT6031`](AppleProcessorTraceT6031.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT6040`](AppleProcessorTraceT6040.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT6050`](AppleProcessorTraceT6050.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8101`](AppleProcessorTraceT8101.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8103`](AppleProcessorTraceT8103.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8110`](AppleProcessorTraceT8110.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8112`](AppleProcessorTraceT8112.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8120`](AppleProcessorTraceT8120.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8122`](AppleProcessorTraceT8122.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8130`](AppleProcessorTraceT8130.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8132`](AppleProcessorTraceT8132.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8140`](AppleProcessorTraceT8140.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8142`](AppleProcessorTraceT8142.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8150`](AppleProcessorTraceT8150.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8152`](AppleProcessorTraceT8152.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8160`](AppleProcessorTraceT8160.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8310`](AppleProcessorTraceT8310.md) — `com.apple.driver.AppleProcessorTrace`
- [`AppleProcessorTraceT8320`](AppleProcessorTraceT8320.md) — `com.apple.driver.AppleProcessorTrace`

## Strings in its kext that name it (60)

- `AppleProcessorTrace::unmapBufferVA unlock\n`
- `AppleProcessorTraceSession::enableTracingForTask()\n`
- `AppleProcessorTraceUserClient::externalMethodConfigure\n`
- `AppleProcessorTrace::resumeTracingGated\n`
- `AppleProcessorTrace::validateConfig(buffer_phys=0x%llX, buffer_size=0x%llX)\n`
- `AppleProcessorTrace::start\n`
- `AppleProcessorTrace::enterSleep\n`
- `AppleProcessorTraceSession::initChunk(%u / %lu, 0x%llX, 0x%llX)\n`
- `AppleProcessorTrace::mapBufferPA\n`
- `AppleProcessorTraceUserClient::clientClose\n`
- `AppleProcessorTraceUserClient::externalMethodAttach\n`
- `AppleProcessorTrace::publishNubs\n`
- `AppleProcessorTrace::mapBufferVA\n`
- `AppleProcessorTrace::mapBufferVA : mapping failed.\n`
- `AppleProcessorTrace::VATraceBufferMap unwire\n`
- `AppleProcessorTraceUserClient::start\n`
- `AppleProcessorTrace::allocateTraceBuffers\n`
- `AppleProcessorTrace::allocateDevTraceBuffer(reuseProdTraceBuffer=%u)\n`
- `AppleProcessorTrace::releaseChunkGated(idx=%u, id=%llu, offset=0x%llX, size=0x%llX, checksum=%llX, fill_size=0x%llX, fill_wrap=%u, cluster_id=%u)\n`
- `AppleProcessorTrace::validateConfig(stream_chunk_size=0x%llX, advisory_min_free_chunks=%u)\n`
- `AppleProcessorTrace::mapBufferVA : allocation failed.\n`
- `AppleProcessorTrace::getBufferVA\n`
- `AppleProcessorTraceUserClient::registerNotificationPort(%u)\n`
- `AppleProcessorTraceUserClient::interruptSession\n`
- `AppleProcessorTrace::buffer size %lx\n`
- `AppleProcessorTraceSession::sendThrottleAdvisory(%{public}X)\n`
- `AppleProcessorTraceUserClient::externalMethodRequestBuffer\n`
- `AppleProcessorTrace::pauseTracingGated\n`
- `AppleProcessorTrace::prepareForPanicTrace\n`
- `AppleProcessorTrace::unmapBufferPA\n`
- `AppleProcessorTrace::mapBufferVA : reset.\n`
- `AppleProcessorTraceUserClient::externalMethodPause\n`
- `AppleProcessorTraceUserClient::externalMethodUnconfigure\n`
- `AppleProcessorTraceSession::configured\n`
- `AppleProcessorTrace::sptm init\n`
- `AppleProcessorTrace::cores config\n`
- `AppleProcessorTraceUserClient::externalMethodAddTask\n`
- `AppleProcessorTrace::validateConfig:%u: fail condition '{public}%s' met.\n`
- `AppleProcessorTrace::allocateProdTraceBuffer\n`
- `AppleProcessorTrace::configureGated\n`
- `AppleProcessorTrace::startTracingOnClustersGated(%p)\n`
- `AppleProcessorTrace::apt_unregister_callback\n`
- `AppleProcessorTrace::unconfigureGated\n`
- `AppleProcessorTrace::validateConfig(panic_trace=%u)\n`
- `AppleProcessorTrace::mapBufferVA : mapped.\n`
- `AppleProcessorTraceSession::withConfig\n`
- `AppleProcessorTrace::stopTracingOnClustersGated\n`
- `AppleProcessorTrace::mapBufferVA : wire.\n`
- `AppleProcessorTrace::VATraceBufferMap del\n`
- `AppleProcessorTraceSession::init\n`
- `AppleProcessorTraceSession::sendThrottleAdvisory failed %{public}X\n`
- `AppleProcessorTraceUserClient::externalMethodResume\n`
- `AppleProcessorTrace::reset\n`
- `AppleProcessorTrace::attachGated\n`
- `AppleProcessorTraceSession::drainDirtyChunk(idx=%u, id=%llu, offset=0x%llX, size=0x%llX, checksum=0x%llX, fill_size=0x%llX, fill_wrap=%u, cluster_id=%u)\n`
- `AppleProcessorTraceUserClient::externalMethodGetSystemMetadata\n`
- `AppleProcessorTrace::stop\n`
- `AppleProcessorTrace::clusters config\n`
- `AppleProcessorTrace::done\n`
- `AppleProcessorTrace::validateConfig(disabled_exception_levels=[%llu, %llu, %llu, %llu, %llu, %llu]\n`

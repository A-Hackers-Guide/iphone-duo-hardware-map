# `IOGPUScheduler`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x250` (592 bytes)
- Metaclass: `0xfffffe000b9f46c8`; metaclass vtable `0xfffffe0008375970`; class vtable `0xfffffe00083758a0`
- Registration (init): `0xfffffe000a11a264`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (1; 1 in total)

- [`AGXScheduler`](AGXScheduler.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (12)

- `IOReturn IOGPUScheduler::freeToWireMemory(IOGPUMemory *)`
- `IOGPUScheduler.cpp`
- `virtual void IOGPUScheduler::progressTimerCheckInterrupt()`
- `bool IOGPUScheduler::init(IOGPU *)`
- `void IOGPUScheduler::hardware_error_interrupt(IOInterruptEventSource *, int)`
- `int32_t IOGPUScheduler::registerCommandQueue(const IOGPUCommandQueue *)`
- `void IOGPUScheduler::signalHardwareError(eRestartRequest, int32_t)`
- `IOGPUScheduler`
- `site.IOGPUScheduler`
- `IOGPUScheduler: increment_gart_collector_disable_count -> %d`
- `%s: IOGPUScheduler alloc or init failed\n`
- `IOGPUScheduler: decrement_gart_collector_disable_count -> %d`

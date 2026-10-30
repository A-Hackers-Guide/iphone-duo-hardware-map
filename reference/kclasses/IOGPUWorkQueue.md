# `IOGPUWorkQueue`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b9f4678`; metaclass vtable `0xfffffe00083756b0`; class vtable `0xfffffe00083755c8`
- Registration (init): `0xfffffe000a1154b8`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 3 in total)

- [`AGXWorkQueue`](AGXWorkQueue.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (9)

- `site.IOGPUWorkQueueState`
- `IOGPUWorkQueue`
- `IOGPUWorkQueueState`
- `site.IOGPUWorkQueue`
- `IOGPUWorkQueue.cpp`
- `\"Excessive time stalled (>%ds) in IOGPUWorkQueue::waitForAllSubmitted()\" @%s:%d`
- `\"Excessive time stalled (>%ds) in IOGPUWorkQueue::addCommandToTail_slow()\" @%s:%d`
- `virtual void IOGPUWorkQueue::logRingBuffer()`
- `virtual void IOGPUWorkQueue::restart()`

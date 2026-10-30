# `IOGPUEventFence`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b9f4498`; metaclass vtable `0xfffffe00083746d8`; class vtable `0xfffffe0008374630`
- Registration (init): `0xfffffe000a108190`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (4; 5 in total)

- [`AGXLateEvalEventFence`](AGXLateEvalEventFence.md) — `com.apple.AGXG19P`
- [`IOGPUBlockFence`](IOGPUBlockFence.md) — `com.apple.iokit.IOGPUFamily`
- [`IOGPUMappingFence`](IOGPUMappingFence.md) — `com.apple.iokit.IOGPUFamily`
- [`IOGPUSharedEventFence`](IOGPUSharedEventFence.md) — `com.apple.iokit.IOGPUFamily`

## Strings in its kext that name it (3)

- `IOGPUEventFence`
- `site.IOGPUEventFence`
- `void IOGPUCommandQueue::retireCommandBuffer(IOGPUEventFence *)`

# `IOGPUTask`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOGPUFamily`](../kexts/com.apple.iokit.IOGPUFamily.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b9f48a8`; metaclass vtable `0xfffffe0008376ae0`; class vtable `0xfffffe0008376a20`
- Registration (init): `0xfffffe000a1277e4`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 4 in total)

- [`AGXGart`](AGXGart.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (6)

- `site.IOGPUTask`
- `virtual OSPtr<IOGPUMemoryMap> IOGPUMemory::createGPUMappingInTaskAtAddressLengthAlignment(IOGPUTask *, uint64_t, uint64_t, uint64_t, uint32_t)`
- `\"%s: IOGPUTask unexpectedly freed\\n\" @%s:%d`
- `IOGPUTask`
- `IOGPUTask.cpp`
- `virtual void IOGPUTask::free()`

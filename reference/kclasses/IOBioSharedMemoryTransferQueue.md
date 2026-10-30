# `IOBioSharedMemoryTransferQueue`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOBiometricFamily`](../kexts/com.apple.iokit.IOBiometricFamily.md)
- Object size: `0x40` (64 bytes)
- Metaclass: `0xfffffe000b9f30a8`; metaclass vtable `0xfffffe0008356df8`; class vtable `0xfffffe0008356d00`
- Registration (init): `0xfffffe000a08109c`
- Superclasses: [`IOBioArrayQueue`](IOBioArrayQueue.md) → [`IOBioQueue`](IOBioQueue.md)

## Direct subclasses (1; 1 in total)

- [`IOPearlSharedMemoryTransferQueue`](IOPearlSharedMemoryTransferQueue.md) — `com.apple.driver.ApplePearlSEPDriver`

## Strings in its kext that name it (8)

- `IOBioSharedMemoryTransferQueue::%s: <%d:%s> [QUEUED] obj:%d:%p\n`
- `IOBioSharedMemoryTransferQueue::%s -> obj:%d:%p -(%d)-> <%d:%s> (queued:%d)\n`
- `IOBioSharedMemoryTransferQueue::%s -> <%d:%s> -X-> obj:%d:%p (queued:%d)\n`
- `IOBioSharedMemoryTransferQueue::%s <- <%d:%s> count:%u, type:%u\n`
- `IOBioSharedMemoryTransferQueue::%s: <%d:%s> -X-> obj:%d:%p\n`
- `IOBioSharedMemoryTransferQueue::%s: <%d:%s> [STATE] type:%u, capacity:%u, count:%u/%u\n`
- `IOBioSharedMemoryTransferQueue`
- `site.IOBioSharedMemoryTransferQueue`

# `IOBioArrayQueue`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOBiometricFamily`](../kexts/com.apple.iokit.IOBiometricFamily.md)
- Object size: `0x40` (64 bytes)
- Metaclass: `0xfffffe000b9f30f8`; metaclass vtable `0xfffffe0008357160`; class vtable `0xfffffe0008357088`
- Registration (init): `0xfffffe000a082980`
- Superclasses: [`IOBioQueue`](IOBioQueue.md)

## Direct subclasses (3; 4 in total)

- [`IOBioSharedMemoryTransferQueue`](IOBioSharedMemoryTransferQueue.md) — `com.apple.iokit.IOBiometricFamily`
- [`IOMesaCaptureDataQueue`](IOMesaCaptureDataQueue.md) — `com.apple.driver.AppleMesaSEPDriver`
- [`IOPearlFrameQueue`](IOPearlFrameQueue.md) — `com.apple.driver.ApplePearlSEPDriver`

## Strings in its kext that name it (11)

- `IOBioArrayQueue::%s <- <%u:%s>\n`
- `IOBioArrayQueue::%s: <%u:%s> -X-> obj:%s:%p\n`
- `IOBioArrayQueue::%s: <%u:%s> [STATE] capacity:%u, count:%u, releaseWhenFull:%d\n`
- `IOBioArrayQueue::%s <- <%u:%s> count:%u\n`
- `IOBioArrayQueue::%s: <%u:%s> [QUEUED] obj:%s:%p\n`
- `IOBioArrayQueue::%s -> obj:%s:%p -(%d)-> <%u:%s> (queued:%d)\n`
- `IOBioArrayQueue::%s -> <%u:%s> -X-> obj:%s:%p (queued:%d)\n`
- `IOBioArrayQueue::%s <- <%u:%s> -X-X (count:%u)\n`
- `IOBioArrayQueue::%s -> <%u:%s>: result:%d (_capacity:%u, _releaseWhenFull:%d)\n`
- `IOBioArrayQueue`
- `site.IOBioArrayQueue`

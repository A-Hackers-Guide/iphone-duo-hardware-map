# `AppleNVMeRequestPool`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x60` (96 bytes)
- Metaclass: `0xfffffe000ba17348`; metaclass vtable `0xfffffe00083bdfa8`; class vtable `0xfffffe00083bdec0`
- Registration (init): `0xfffffe000a28f570`
- Superclasses: [`IOCommandPool`](IOCommandPool.md)

## Direct subclasses (1; 1 in total)

- [`AppleNVMeRequestPoolTagReserve`](AppleNVMeRequestPoolTagReserve.md) — `com.apple.iokit.IONVMeFamily`

## Strings in its kext that name it (11)

- `AppleNVMeRequestPool.cpp`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp`
- `virtual IOReturn AppleNVMeRequestPoolTagReserve::Rebuild(uint8_t, uint32_t, bool, NVMeCGType_t, IOMapper *)`
- `static AppleNVMeRequestPoolTagReserve *AppleNVMeRequestPoolTagReserve::Create(AppleNVMeWorkLoop *, uint8_t, uint16_t, uint32_t, bool, NVMeBufferAllocator *, lck_mtx_t *, NVMeCGType_t, IOMapper *)`
- `site.AppleNVMeRequestPool`
- `AppleNVMeRequestPoolTagReserve.cpp`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp`
- `AppleNVMeRequestPoolTagReserve`
- `site.AppleNVMeRequestPoolTagReserve`
- `AppleNVMeRequestPool`
- `static AppleNVMeRequestPool *AppleNVMeRequestPool::Create(AppleNVMeWorkLoop *, uint8_t, uint16_t, uint32_t, bool, NVMeBufferAllocator *, lck_mtx_t *, NVMeCGType_t, IOMapper *)`

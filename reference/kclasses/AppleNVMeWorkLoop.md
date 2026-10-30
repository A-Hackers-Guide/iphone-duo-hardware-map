# `AppleNVMeWorkLoop`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x50` (80 bytes)
- Metaclass: `0xfffffe000ba17398`; metaclass vtable `0xfffffe00083be7f0`; class vtable `0xfffffe00083be6c0`
- Registration (init): `0xfffffe000a290c2c`
- Superclasses: [`IOWorkLoop`](IOWorkLoop.md)

## Strings in its kext that name it (5)

- `static AppleNVMeRequestPoolTagReserve *AppleNVMeRequestPoolTagReserve::Create(AppleNVMeWorkLoop *, uint8_t, uint16_t, uint32_t, bool, NVMeBufferAllocator *, lck_mtx_t *, NVMeCGType_t, IOMapper *)`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeWorkLoop.cpp`
- `site.AppleNVMeWorkLoop`
- `AppleNVMeWorkLoop`
- `static AppleNVMeRequestPool *AppleNVMeRequestPool::Create(AppleNVMeWorkLoop *, uint8_t, uint16_t, uint32_t, bool, NVMeBufferAllocator *, lck_mtx_t *, NVMeCGType_t, IOMapper *)`

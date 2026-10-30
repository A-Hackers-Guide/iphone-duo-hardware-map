# `DIDeviceRequestPool`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDiskImages2`](../kexts/com.apple.driver.AppleDiskImages2.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b941068`; metaclass vtable `0xfffffe0008052610`; class vtable `0xfffffe0008052510`
- Registration (init): `0xfffffe0008b83584`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (12)

- `site.DIDeviceRequestPool`
- `DIDeviceRequestPool`
- `virtual void DIDeviceRequestPool::free()`
- `DIDeviceRequestPool.h`
- `bool DIDeviceRequestPool::AllocateRequests(size_t, user_addr_t, size_t, unsigned int)`
- `static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &, Mode) [TElem = DIDeviceRequest]`
- `IOReturn DIDeviceRequestPool::AllocateBuffersForRequest(DIDeviceRequest *, size_t, bool, abort_request_allocation_fn_t, void *)`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/DIDeviceRequestPool.cpp`
- `size_t DIDeviceRequestPool::AddBuffersForReconnection(user_addr_t, size_t, unsigned int)`
- `DIDeviceRequest *DIDeviceRequestPool::GetReservedRequest()`
- `void DIDeviceRequestPool::ReleaseReservedRequest()`
- `static void DIDeviceRequestPool::ReleasePoolElements(uint32_t &, ::IOLWPool<TElem> &, Mode) [TElem = DISharedBuffer]`

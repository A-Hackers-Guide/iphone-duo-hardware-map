# `AppleSEPCoreBuffer`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x78` (120 bytes)
- Metaclass: `0xfffffe000b99afe0`; metaclass vtable `0xfffffe00081f7ed0`; class vtable `0xfffffe00081f7e18`
- Registration (init): `0xfffffe000964c9a8`
- Superclasses: [`IOSlaveMemoryBuffer`](IOSlaveMemoryBuffer.md) → [`IOSlaveMemory`](IOSlaveMemory.md)

## Strings in its kext that name it (11)

- `kern_return_t AppleSEPCoreBuffer::coredump_save_thread_state(void *, core_save_thread_state_cb, void *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp`
- `AppleSEPCoreBuffer::AppleSEPCoreBuffer(AppleSEPSharedMemoryBuffer *, bool)`
- `kern_return_t AppleSEPCoreBuffer::coredump_init(void *)`
- `site.AppleSEPCoreBuffer`
- `AppleSEPCoreBuffer.cpp`
- `kern_return_t AppleSEPCoreBuffer::coredump_save_segment_descriptions(core_save_segment_descriptions_cb, void *)`
- `kern_return_t AppleSEPCoreBuffer::coredump_save_summary(core_save_summary_cb, void *)`
- `kern_return_t AppleSEPCoreBuffer::coredump_save_segment_data(core_save_segment_data_cb, void *)`
- `AppleSEPCoreBuffer`
- `void AppleSEPCoreBuffer::attachOwner(AppleSEPSharedMemoryBuffer *)`

# `AppleSEPControl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b99a818`; metaclass vtable `0xfffffe00081f4cb8`; class vtable `0xfffffe00081f4b78`
- Registration (init): `0xfffffe0009636298`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (14)

- `AppleSEPControl`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPControl.cpp`
- `site.AppleSEPControl`
- `IOReturn AppleSEPControl::cmsgGET_ENTROPY_FOR_XNU_PRNG(uint32_t *, UInt32)`
- `IOReturn AppleSEPControl::cmsgSET_OOL_OUT(UInt8, IOSlaveMemory *, UInt32)`
- `static void AppleSEPControl::_notifyActiveAsync(thread_call_param_t, thread_call_param_t)`
- `IOReturn AppleSEPControl::_cmsgSend(AppleSEPMessage *, UInt32 *, bool *)`
- `void AppleSEPControl::_cmsgAction(void *, void *)`
- `IOReturn AppleSEPControl::cmsgSET_DMA_OUT(UInt8, IOSlaveMemory *, UInt32)`
- `IOReturn AppleSEPControl::cmsgSET_OOL_IN(UInt8, IOSlaveMemory *, UInt32)`
- `void AppleSEPControl::_callActiveAsync()`
- `IOReturn AppleSEPControl::cmsgSET_DMA_IN(UInt8, IOSlaveMemory *, UInt32)`
- `IOReturn AppleSEPControl::_cmsgSET_DMA_CMD(UInt32 *)`
- `AppleSEPControl.cpp`

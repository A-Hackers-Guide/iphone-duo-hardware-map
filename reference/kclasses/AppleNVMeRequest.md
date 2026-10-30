# `AppleNVMeRequest`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x258` (600 bytes)
- Metaclass: `0xfffffe000ba174b0`; metaclass vtable `0xfffffe00083c0e48`; class vtable `0xfffffe00083c0d38`
- Registration (init): `0xfffffe000a2a5114`
- Superclasses: [`IODMACommand`](IODMACommand.md) → [`IOCommand`](IOCommand.md)

## Strings in its kext that name it (30)

- `AppleNVMeRequestPool.cpp`
- `site.AppleNVMeRequestTimer`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeRequestPool.cpp`
- `AppleNVMeRequest`
- `void IONVMeController::HandleCompletionErrors(AppleNVMeRequest *, uint32_t)`
- `site.AppleNVMeRequest *`
- `void AppleNVMeRequest::PrintRequest()`
- `AppleNVMeRequestTimer.cpp`
- `void AppleANS2CGNVMeController::NVMeCoastGuardSetTCBEntry(tcb_queue_entry *, AppleNVMeRequest *)`
- `virtual IOReturn AppleNVMeRequestPoolTagReserve::Rebuild(uint8_t, uint32_t, bool, NVMeCGType_t, IOMapper *)`
- `static AppleNVMeRequestPoolTagReserve *AppleNVMeRequestPoolTagReserve::Create(AppleNVMeWorkLoop *, uint8_t, uint16_t, uint32_t, bool, NVMeBufferAllocator *, lck_mtx_t *, NVMeCGType_t, IOMapper *)`
- `bool IONVMeController::RequestFoundInCompletionQueue(AppleNVMeRequest *)`
- `void AppleANS2CGv2Controller::NVMeCoastGuardSetTCBEntry(tcb_queue_entry *, AppleNVMeRequest *)`
- `site.AppleNVMeRequestPool`
- `AppleNVMeRequestPoolTagReserve.cpp`
- `virtual void IONVMeController::CommandTimeout(AppleNVMeRequest *)`
- `IOReturn AppleNVMeController::ProcessTunnelCommand(AppleNVMeRequest *, AppleNVMeBuffer *, AppleNVMeBuffer *)`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeRequestPoolTagReserve.cpp`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeRequestTimer.cpp`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/AppleNVMeRequest.cpp`
- `site.AppleNVMeRequest`
- `virtual void IOEmbeddedNVMeBlockDevice::HandleANS2SHA(AppleNVMeRequest *)`
- `virtual void IONVMeController::ReturnRequest(AppleNVMeRequest *)`
- `IOReturn AppleNVMeRequest::BuildCommandReadWriteStruct(NVMeRWCommand *, IODirection)`
- `void IONVMeController::PrintCompletionErrorDetail(AppleNVMeRequest *, uint32_t)`
- `AppleNVMeRequestPoolTagReserve`
- `AppleNVMeRequestTimer`
- `site.AppleNVMeRequestPoolTagReserve`
- `AppleNVMeRequestPool`
- `static AppleNVMeRequestPool *AppleNVMeRequestPool::Create(AppleNVMeWorkLoop *, uint8_t, uint16_t, uint32_t, bool, NVMeBufferAllocator *, lck_mtx_t *, NVMeCGType_t, IOMapper *)`

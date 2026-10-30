# `IONVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x2e0` (736 bytes)
- Metaclass: `0xfffffe000ba173c0`; metaclass vtable `0xfffffe00083bf190`; class vtable `0xfffffe00083be888`
- Registration (init): `0xfffffe000a29ceb4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 8 in total)

- [`AppleNVMeController`](AppleNVMeController.md) — `com.apple.iokit.IONVMeFamily`

## IOKit personalities that instantiate it (1)

- `GenericNVMeSSD` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `IOPCIDevice`, `IOProbeScore` = `100`

## Strings in its kext that name it (43)

- `%s::%d:IONVMeController::HandleControllerPowerOff, ShutdownNVMe() completed with status = 0x%08x\n`
- `virtual bool IONVMeController::handleIsOpen(const IOService *) const`
- `virtual IOReturn IONVMeController::setPowerState(unsigned long, IOService *)`
- `bool IONVMeController::CreateBlockStorageDevice(uint32_t)`
- `virtual IOReturn IONVMeController::EnableController()`
- `IOReturn IONVMeController::PollRegister(uint32_t, uint32_t, uint32_t, uint32_t, uint32_t, uint32_t, uint32_t *)`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/IONVMeControllerPolledAdapter.cpp`
- `virtual void IONVMeController::HandleControllerPowerOff()`
- `virtual bool IONVMeController::handleOpen(IOService *, IOOptionBits, void *)`
- `void IONVMeController::DoANSTagFifoWorkaround(uint16_t)`
- `void IONVMeController::HandleCompletionErrors(AppleNVMeRequest *, uint32_t)`
- `virtual void IONVMeController::ThreadEntry()`
- `virtual IOReturn IONVMeController::CheckWriteProtection()`
- `virtual bool IONVMeController::start(IOService *)`
- `bool IONVMeController::CheckCFS()`
- `site.IONVMeControllerPolledAdapter`
- `virtual IOReturn IONVMeController::SendShutdownNotification(bool)`
- `virtual bool IONVMeController::didTerminate(IOService *, IOOptionBits, bool *)`
- `virtual void IONVMeController::systemWillShutdown(IOOptionBits)`
- `IOReturn IONVMeController::PollCSTS(uint32_t, uint32_t, uint32_t, uint32_t)`
- `bool IONVMeController::RequestFoundInCompletionQueue(AppleNVMeRequest *)`
- `void IONVMeController::FatalHandling()`
- `virtual IOReturn IONVMeController::ShutdownNVMe(bool, bool)`
- `virtual IOReturn IONVMeController::CreateSubmissionQueue(uint16_t, uint8_t)`
- `virtual void IONVMeController::CommandTimeout(AppleNVMeRequest *)`
- `void IONVMeController::CheckANSTagFifoWorkaround()`
- `virtual IOReturn IONVMeController::performNVMeShutdownTasks()`
- `virtual IOReturn IONVMeController::newUserClient(task_t, void *, UInt32, OSDictionary *, IOUserClient **)`
- `virtual void IONVMeController::handleClose(IOService *, IOOptionBits)`
- `IOReturn IONVMeController::PerformSanitizeOperation()`
- `site.IONVMeController`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Common/IONVMeController.cpp`
- `virtual void IONVMeController::ReturnRequest(AppleNVMeRequest *)`
- `virtual IOFilterInterruptEventSource *IONVMeController::CreateDeviceInterrupt(IOInterruptEventSource::Action, IOFilterInterruptEventSource::Filter, IOService *)`
- `IONVMeControllerPolledAdapter`
- `virtual uint32_t IONVMeController::GetSaturationByteCountKey()`
- `void IONVMeController::PrintCompletionErrorDetail(AppleNVMeRequest *, uint32_t)`
- `virtual bool IONVMeController::InitializeController()`
- `IONVMeControllerPolledAdapter.cpp`
- `virtual uint32_t IONVMeController::GetDefaultRequestTimeout()`
- `bool IONVMeController::ProcessCompletionQueue(AppleNVMeCompletionQueue *)`
- `IONVMeController`
- `IONVMeController.cpp`

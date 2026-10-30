# `AppleANS2NVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0xa90` (2,704 bytes)
- Metaclass: `0xfffffe000ba170f0`; metaclass vtable `0xfffffe00083b7d88`; class vtable `0xfffffe00083b7270`
- Registration (init): `0xfffffe000a27d540`
- Superclasses: [`AppleEmbeddedNVMeController`](AppleEmbeddedNVMeController.md) → [`AppleNVMeController`](AppleNVMeController.md) → [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 5 in total)

- [`AppleANS2CGNVMeController`](AppleANS2CGNVMeController.md) — `com.apple.iokit.IONVMeFamily`
- [`AppleANS2CGv2Controller`](AppleANS2CGv2Controller.md) — `com.apple.iokit.IONVMeFamily`
- [`AppleANS2DARTNVMeController`](AppleANS2DARTNVMeController.md) — `com.apple.iokit.IONVMeFamily`

## IOKit personalities that instantiate it (1)

- `AppleANS2NVMeController` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANS2'}`

## Strings in its kext that name it (40)

- `virtual bool AppleANS2NVMeController::IsFWNamespaceTypeMismatch()`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleANS2NVMeController.cpp`
- `IOReturn AppleANS2NVMeController::SendSleepNotificationToANS(uint32_t, bool *)`
- `AppleANS2NVMeController`
- `virtual void AppleANS2NVMeController::SetModeselRegister(uint32_t)`
- `virtual IOReturn AppleANS2NVMeController::ConfigFWUpdateRetry(IOReturn)`
- `IOReturn AppleANS2NVMeController::PowerStateAction(unsigned long, unsigned long)`
- `IOReturn AppleANS2NVMeController::EnableLifeboatMode()`
- `virtual IOReturn AppleANS2NVMeController::EnableSubmissionQueue(uint16_t)`
- `IOReturn AppleANS2NVMeController::WaitDeviceActive()`
- `virtual IOReturn AppleANS2NVMeController::setProperties(OSObject *)`
- `virtual bool AppleANS2NVMeController::CheckNameSpaceSizeMismatch()`
- `virtual IOReturn AppleANS2NVMeController::systemPowerChange(void *, UInt32, IOService *, void *, vm_size_t)`
- `virtual void AppleANS2NVMeController::SetRuntimeProperties()`
- `virtual bool AppleANS2NVMeController::IsClogMismatch()`
- `IOReturn AppleANS2NVMeController::SetNANDMode()`
- `IOReturn AppleANS2NVMeController::SetNANDPECycles()`
- `IOReturn AppleANS2NVMeController::PublishPCIUpDARTMapping()`
- `IOReturn AppleANS2NVMeController::ConfigPcieSTGLanes(bool)`
- `IOReturn AppleANS2NVMeController::CreatePCIeUPDARTMapping()`
- `virtual IOReturn AppleANS2NVMeController::GetVirtualCardSize(OSDictionary *, uint64_t *)`
- `virtual IOReturn AppleANS2NVMeController::AllocateResources()`
- `virtual void AppleANS2NVMeController::ParseSanitizeCounters(uint8_t *)`
- `site.AppleANS2NVMeController`
- `virtual IOReturn AppleANS2NVMeController::PerformBFH(void *, uint32_t, void *, uint32_t, void *, uint32_t, task_t)`
- `virtual IOFilterInterruptEventSource *AppleANS2NVMeController::CreateDeviceInterrupt(IOInterruptEventSource::Action, IOFilterInterruptEventSource::Filter, IOService *)`
- `virtual IOReturn AppleANS2NVMeController::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)`
- `bool AppleANS2NVMeController::SetNANDGeomPropertiesV2(OSDictionary *)`
- `virtual IOReturn AppleANS2NVMeController::EnableSHA()`
- `virtual bool AppleANS2NVMeController::SetNANDGeomProperties(OSDictionary *)`
- `bool AppleANS2NVMeController::CreateLifeboatBlockDevice(uint32_t, uint8_t)`
- `virtual bool AppleANS2NVMeController::start(IOService *)`
- `virtual IOService *AppleANS2NVMeController::probe(IOService *, SInt32 *)`
- `virtual IOReturn AppleANS2NVMeController::FirmwareVersionCheck(void *)`
- `virtual IOReturn AppleANS2NVMeController::EnableCompletionQueue(uint16_t)`
- `virtual bool AppleANS2NVMeController::CheckNameSpaceSizeGreater()`
- `AppleANS2NVMeController.cpp`
- `void AppleANS2NVMeController::RegisterPPM()`
- `virtual IOReturn AppleANS2NVMeController::SetNANDDebug()`
- `virtual IOReturn AppleANS2NVMeController::GetSanitizeCounters()`

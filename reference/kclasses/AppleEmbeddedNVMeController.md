# `AppleEmbeddedNVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x830` (2,096 bytes)
- Metaclass: `0xfffffe000ba17028`; metaclass vtable `0xfffffe00083b4988`; class vtable `0xfffffe00083b3eb8`
- Registration (init): `0xfffffe000a2737b4`
- Superclasses: [`AppleNVMeController`](AppleNVMeController.md) → [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 6 in total)

- [`AppleANS2NVMeController`](AppleANS2NVMeController.md) — `com.apple.iokit.IONVMeFamily`

## IOKit personalities that instantiate it (1)

- `AppleEmbeddedNVMeController` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `IOPCIDevice`, `IOPCIMatch` = `0x2002106b`

## Strings in its kext that name it (50)

- `nvme: \"AppleEmbeddedNVMeController::enablePCIPort failed !\\n\" @%s:%d`
- `virtual void AppleEmbeddedNVMeController::DoHousekeeping()`
- `bool AppleEmbeddedNVMeController::DetermineNamespaces()`
- `bool AppleEmbeddedNVMeController::IdentifyNamespaces()`
- `virtual IOReturn AppleEmbeddedNVMeController::SetPowerGatingTimeout(uint32_t)`
- `virtual IOReturn AppleEmbeddedNVMeController::ValidateNamespaceSize(uint8_t)`
- `site.AppleEmbeddedNVMeController`
- `virtual IOReturn AppleEmbeddedNVMeController::newUserClient(task_t, void *, UInt32, OSDictionary *, IOUserClient **)`
- `bool AppleEmbeddedNVMeController::SetSwapWriteLimit(uint32_t)`
- `AppleEmbeddedNVMeTemperatureSensor *AppleEmbeddedNVMeController::CreateTemperatureSensor()`
- `nvme: \"nvme: AppleEmbeddedNVMeController::ThreadEntry, ShutdownNVMe() completed with status = 0x%08x\\n\" @%s:%d`
- `virtual bool AppleEmbeddedNVMeController::IsFullInit()`
- `bool AppleEmbeddedNVMeController::SetNANDIDProperties(OSDictionary *)`
- `virtual bool AppleEmbeddedNVMeController::disablePCIPort(bool)`
- `IOReturn AppleEmbeddedNVMeController::IssueFlush(uint32_t)`
- `bool AppleEmbeddedNVMeController::CheckClogVersionMismatch()`
- `virtual IOReturn AppleEmbeddedNVMeController::FirmwareVersionCheck(void *)`
- `AppleEmbeddedNVMeController.cpp`
- `void AppleEmbeddedNVMeController::SetNumBurninBlks(int64_t)`
- `virtual bool AppleEmbeddedNVMeController::SetNANDQual()`
- `virtual void AppleEmbeddedNVMeController::ThreadEntry()`
- `virtual void AppleEmbeddedNVMeController::InitializeWallTime()`
- `virtual bool AppleEmbeddedNVMeController::SetQoSParameters()`
- `virtual bool AppleEmbeddedNVMeController::StartController()`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleEmbeddedNVMeController.cpp`
- `virtual bool AppleEmbeddedNVMeController::GetProviderFunctions()`
- `virtual void AppleEmbeddedNVMeController::SetRuntimeProperties()`
- `virtual IOReturn AppleEmbeddedNVMeController::SetNVMeProperties()`
- `void AppleEmbeddedNVMeController::GetRestoreEnvironment()`
- `IOReturn AppleEmbeddedNVMeController::SetATVMode()`
- `virtual IOReturn AppleEmbeddedNVMeController::CreateIOReporter()`
- `virtual bool AppleEmbeddedNVMeController::AllocateNodes(bool)`
- `virtual IOReturn AppleEmbeddedNVMeController::SendTimeToDevice()`
- `virtual bool AppleEmbeddedNVMeController::enablePCIPort(bool)`
- `virtual IOReturn AppleEmbeddedNVMeController::PreCCEnableHook()`
- `AppleEmbeddedNVMeController`
- `bool AppleEmbeddedNVMeController::IsRootDeviceRamdisk()`
- `bool AppleEmbeddedNVMeController::DetermineBlankPart()`
- `bool AppleEmbeddedNVMeController::AreNamespacesPresent()`
- `virtual bool AppleEmbeddedNVMeController::InitializeController()`
- `virtual IOReturn AppleEmbeddedNVMeController::setProperties(OSObject *)`
- `virtual bool AppleEmbeddedNVMeController::SetBDRFactor()`
- `bool AppleEmbeddedNVMeController::CreateEmbeddedBlockDevice(uint8_t, uint8_t)`
- `bool AppleEmbeddedNVMeController::CreateNamespaces(uint64_t, uint32_t)`
- `nvme: \"AppleEmbeddedNVMeController::disablePCIPort failed !\\n\" @%s:%d`
- `virtual bool AppleEmbeddedNVMeController::SetNANDGeomProperties(OSDictionary *)`
- `virtual IOReturn AppleEmbeddedNVMeController::SetClockGatingTimeout(uint32_t)`
- `bool AppleEmbeddedNVMeController::SetNamespacesStruct()`
- `virtual IOReturn AppleEmbeddedNVMeController::AllocateResources()`
- `bool AppleEmbeddedNVMeController::IsBootModeiBEC()`

# `AppleANS2CGNVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0xaa0` (2,720 bytes)
- Metaclass: `0xfffffe000ba17140`; metaclass vtable `0xfffffe00083b9018`; class vtable `0xfffffe00083b84f0`
- Registration (init): `0xfffffe000a27f584`
- Superclasses: [`AppleANS2NVMeController`](AppleANS2NVMeController.md) → [`AppleEmbeddedNVMeController`](AppleEmbeddedNVMeController.md) → [`AppleNVMeController`](AppleNVMeController.md) → [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleANS3NVMeController`](AppleANS3NVMeController.md) — `com.apple.iokit.IONVMeFamily`

## IOKit personalities that instantiate it (1)

- `AppleANS2CGNVMeController` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANS2'}`

## Strings in its kext that name it (14)

- `virtual void AppleANS2CGNVMeController::SetupAdminQueue()`
- `virtual uint32_t AppleANS2CGNVMeController::GetNVMePPLQueueEntries()`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleANS2CGNVMeController.cpp`
- `virtual IOReturn AppleANS2CGNVMeController::PolledEnableCompletionQueue(uint16_t)`
- `AppleANS2CGNVMeController`
- `virtual IOReturn AppleANS2CGNVMeController::PolledEnableSubmissionQueue(uint16_t)`
- `void AppleANS2CGNVMeController::NVMeCoastGuardSetTCBEntry(tcb_queue_entry *, AppleNVMeRequest *)`
- `virtual IOReturn AppleANS2CGNVMeController::EnableSubmissionQueue(uint16_t)`
- `virtual bool AppleANS2CGNVMeController::InitializePCI()`
- `virtual IOService *AppleANS2CGNVMeController::probe(IOService *, SInt32 *)`
- `virtual IOReturn AppleANS2CGNVMeController::EnableCompletionQueue(uint16_t)`
- `IOReturn AppleANS2CGNVMeController::SendOSBuildStrToDevice()`
- `site.AppleANS2CGNVMeController`
- `AppleANS2CGNVMeController.cpp`

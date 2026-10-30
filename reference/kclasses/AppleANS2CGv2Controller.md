# `AppleANS2CGv2Controller`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0xaa0` (2,720 bytes)
- Metaclass: `0xfffffe000ba173e8`; metaclass vtable `0xfffffe00083bfde8`; class vtable `0xfffffe00083bf2c0`
- Registration (init): `0xfffffe000a29e63c`
- Superclasses: [`AppleANS2NVMeController`](AppleANS2NVMeController.md) → [`AppleEmbeddedNVMeController`](AppleEmbeddedNVMeController.md) → [`AppleNVMeController`](AppleNVMeController.md) → [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleANS3CGv2Controller`](AppleANS3CGv2Controller.md) — `com.apple.iokit.IONVMeFamily`

## IOKit personalities that instantiate it (1)

- `AppleANS2CGv2Controller` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANS2'}`

## Strings in its kext that name it (13)

- `virtual void AppleANS2CGv2Controller::SetupAdminQueue()`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleANS2CGv2Controller.cpp`
- `site.AppleANS2CGv2Controller`
- `virtual IOReturn AppleANS2CGv2Controller::PolledEnableCompletionQueue(uint16_t)`
- `virtual IOReturn AppleANS2CGv2Controller::EnableCompletionQueue(uint16_t)`
- `virtual uint32_t AppleANS2CGv2Controller::GetNVMeSPTMQueueEntries()`
- `IOReturn AppleANS2CGv2Controller::SendOSBuildStrToDevice()`
- `virtual IOService *AppleANS2CGv2Controller::probe(IOService *, SInt32 *)`
- `void AppleANS2CGv2Controller::NVMeCoastGuardSetTCBEntry(tcb_queue_entry *, AppleNVMeRequest *)`
- `virtual IOReturn AppleANS2CGv2Controller::PolledEnableSubmissionQueue(uint16_t)`
- `virtual IOReturn AppleANS2CGv2Controller::EnableSubmissionQueue(uint16_t)`
- `AppleANS2CGv2Controller.cpp`
- `AppleANS2CGv2Controller`

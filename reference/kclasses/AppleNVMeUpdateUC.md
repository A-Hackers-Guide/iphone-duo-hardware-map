# `AppleNVMeUpdateUC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000ba17208`; metaclass vtable `0xfffffe00083bb0a8`; class vtable `0xfffffe00083baac0`
- Registration (init): `0xfffffe000a285490`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (12)

- `virtual bool AppleNVMeUpdateUC::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `\"nvme: AppleNVMeUpdateUC::FirmwareActivate, ShutdownNVMe() completed with status = 0x%08x\\n\" @%s:%d`
- `AppleNVMeUpdateUC.cpp`
- `static IOReturn AppleNVMeUpdateUC::UpdateMspBfhParams(OSObject *, void *, IOExternalMethodArguments *)`
- `site.AppleNVMeUpdateUC`
- `static IOReturn AppleNVMeUpdateUC::FirmwareDownload(OSObject *, void *, IOExternalMethodArguments *)`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleNVMeUpdateUC.cpp`
- `AppleNVMeUpdateUC`
- `virtual bool AppleNVMeUpdateUC::start(IOService *)`
- `static bool AppleNVMeUpdateUC::IsTunnelPermitted(AppleNVMeUpdateUC *, uint32_t)`
- `static IOReturn AppleNVMeUpdateUC::FirmwareActivate(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleNVMeUpdateUC::FinalizeFWUpdate(OSObject *, void *, IOExternalMethodArguments *)`

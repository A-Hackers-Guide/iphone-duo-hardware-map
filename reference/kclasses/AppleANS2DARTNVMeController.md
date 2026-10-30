# `AppleANS2DARTNVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0xab8` (2,744 bytes)
- Metaclass: `0xfffffe000ba16fd8`; metaclass vtable `0xfffffe00083b3ca0`; class vtable `0xfffffe00083b3188`
- Registration (init): `0xfffffe000a26c100`
- Superclasses: [`AppleANS2NVMeController`](AppleANS2NVMeController.md) → [`AppleEmbeddedNVMeController`](AppleEmbeddedNVMeController.md) → [`AppleNVMeController`](AppleNVMeController.md) → [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleANS2DARTNVMeController` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANS2'}`

## Strings in its kext that name it (9)

- `virtual IOReturn AppleANS2DARTNVMeController::InitializeNVMe(bool)`
- `virtual IOReturn AppleANS2DARTNVMeController::EnableSHA()`
- `virtual void AppleANS2DARTNVMeController::EnableLinearSQ()`
- `site.AppleANS2DARTNVMeController`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleANS2DARTNVMeController.cpp`
- `virtual IOReturn AppleANS2DARTNVMeController::ShutdownNVMe(bool, bool)`
- `AppleANS2DARTNVMeController`
- `virtual IOService *AppleANS2DARTNVMeController::probe(IOService *, SInt32 *)`
- `IOReturn AppleANS2DARTNVMeController::SendOSBuildStrToDevice()`

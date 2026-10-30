# `AppleANS3NVMeController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0xaa0` (2,720 bytes)
- Metaclass: `0xfffffe000ba170c8`; metaclass vtable `0xfffffe00083b71d8`; class vtable `0xfffffe00083b66b0`
- Registration (init): `0xfffffe000a2758f8`
- Superclasses: [`AppleANS2CGNVMeController`](AppleANS2CGNVMeController.md) → [`AppleANS2NVMeController`](AppleANS2NVMeController.md) → [`AppleEmbeddedNVMeController`](AppleEmbeddedNVMeController.md) → [`AppleNVMeController`](AppleNVMeController.md) → [`IONVMeController`](IONVMeController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleANS3NVMeController` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ANS2'}`

## Strings in its kext that name it (5)

- `site.AppleANS3NVMeController`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleANS3NVMeController.cpp`
- `virtual IOService *AppleANS3NVMeController::probe(IOService *, SInt32 *)`
- `AppleANS3NVMeController`
- `virtual void AppleANS3NVMeController::EnableLinearSQ()`

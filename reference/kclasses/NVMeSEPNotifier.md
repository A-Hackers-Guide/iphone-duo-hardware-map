# `NVMeSEPNotifier`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000ba171b8`; metaclass vtable `0xfffffe00083ba418`; class vtable `0xfffffe00083b9ec0`
- Registration (init): `0xfffffe000a281d00`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `NVMeSEPNotifier` in [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md): `IOProviderClass` = `AppleSEPManager`, `IOMatchCategory` = `NVMeSEPNotifier`

## Strings in its kext that name it (4)

- `site.NVMeSEPNotifier`
- `virtual bool NVMeSEPNotifier::start(IOService *)`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/NVMeSEPNotifier.cpp`
- `NVMeSEPNotifier`

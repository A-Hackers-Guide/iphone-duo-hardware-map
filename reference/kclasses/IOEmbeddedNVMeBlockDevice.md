# `IOEmbeddedNVMeBlockDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0x238` (568 bytes)
- Metaclass: `0xfffffe000ba17168`; metaclass vtable `0xfffffe00083b96e0`; class vtable `0xfffffe00083b90b0`
- Registration (init): `0xfffffe000a281244`
- Superclasses: [`IONVMeBlockStorageDevice`](IONVMeBlockStorageDevice.md) → [`IOBlockStorageDevice`](IOBlockStorageDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`IONVMeEffaceableDevice`](IONVMeEffaceableDevice.md) — `com.apple.iokit.IONVMeFamily`

## Strings in its kext that name it (9)

- `virtual bool IOEmbeddedNVMeBlockDevice::start(IOService *)`
- `virtual IOReturn IOEmbeddedNVMeBlockDevice::doAsyncReadWrite(IOMemoryDescriptor *, UInt64, UInt64, IOStorageAttributes *, IOStorageCompletion *)`
- `IOEmbeddedNVMeBlockDevice`
- `site.IOEmbeddedNVMeBlockDevice`
- `IOReturn IOEmbeddedNVMeBlockDevice::writeData()`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/IOEmbeddedNVMeBlockDevice.cpp`
- `virtual IOReturn IOEmbeddedNVMeBlockDevice::doFormatMedia(UInt64)`
- `IOEmbeddedNVMeBlockDevice.cpp`
- `virtual void IOEmbeddedNVMeBlockDevice::HandleANS2SHA(AppleNVMeRequest *)`

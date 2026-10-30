# `AppleNVMeNamespaceDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IONVMeFamily`](../kexts/com.apple.iokit.IONVMeFamily.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000ba17320`; metaclass vtable `0xfffffe00083bdda8`; class vtable `0xfffffe00083bd828`
- Registration (init): `0xfffffe000a28e810`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleNVMeEAN`](AppleNVMeEAN.md) — `com.apple.iokit.IONVMeFamily`
- [`AppleNVMeFWNamespaceDevice`](AppleNVMeFWNamespaceDevice.md) — `com.apple.iokit.IONVMeFamily`

## Strings in its kext that name it (8)

- `virtual bool AppleNVMeNamespaceDevice::start(IOService *)`
- `com.apple.AppleNVMeNamespaceDevice.allow`
- `virtual IOReturn AppleNVMeNamespaceDevice::GetDeviceProperties()`
- `selector < kAppleNVMeNamespaceDeviceMethodCount`
- `( inSideBarVersion == 0 ) || ( fOwner->metaCast(\"AppleNVMeNamespaceDevice\") != NULL )`
- `AppleNVMeNamespaceDevice`
- `site.AppleNVMeNamespaceDevice`
- `/Library/Caches/com.apple.xbs/B10A3681-4E24-45D6-AB50-3EE47EE2ABD1/TemporaryDirectory.c1KMK0/Sources/IONVMeFamily/Embedded/AppleNVMeNamespaceDevice.cpp`

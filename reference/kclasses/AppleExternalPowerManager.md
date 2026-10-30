# `AppleExternalPowerManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedAudioLibs`](../kexts/com.apple.driver.AppleEmbeddedAudioLibs.md)
- Object size: `0x20` (32 bytes)
- Metaclass: `0xfffffe000b942a90`; metaclass vtable `0xfffffe000807fb80`; class vtable `0xfffffe000807fae8`
- Registration (init): `0xfffffe0008c245e8`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (9)

- `%s failed to initialize an AppleExternalPowerManager object`
- `%s failed to allocate an AppleExternalPowerManager object`
- `AppleExternalPowerManager.cpp`
- `static OSSharedPtr<AppleExternalPowerManager> AppleExternalPowerManager::withCapacity(IOService *, UInt32)`
- `AppleExternalPowerManager`
- `site.AppleExternalPowerManager`
- `static OSSharedPtr<IOService> AppleExternalPowerManager::getARMFunctionProvider(IORegistryEntry *, const char *)`
- `static OSSharedPtr<OSArray> AppleExternalPowerManager::parsePhandles(OSData *)`
- `virtual bool AppleExternalPowerManager::init(IOService *, UInt32)`

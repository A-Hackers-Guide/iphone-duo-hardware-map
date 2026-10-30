# `AppleMobileFileIntegrity`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMobileFileIntegrity`](../kexts/com.apple.driver.AppleMobileFileIntegrity.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b986240`; metaclass vtable `0xfffffe000817a4d0`; class vtable `0xfffffe0008179f78`
- Registration (init): `0xfffffe00092abf5c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMobileFileIntegrity` in [`com.apple.driver.AppleMobileFileIntegrity`](../kexts/com.apple.driver.AppleMobileFileIntegrity.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `AppleMobileFileIntegrity`

## Strings in its kext that name it (15)

- `kern_return_t _initializeAppleMobileFileIntegrity()`
- `%s: target is not AppleMobileFileIntegrity object\n`
- `AppleMobileFileIntegrity.cpp`
- `virtual IOReturn AppleMobileFileIntegrityUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `static IOReturn AppleMobileFileIntegrityUserClient::isCdhashInTrustCache(OSObject *, void *, IOExternalMethodArguments *)`
- `site.AppleMobileFileIntegrity`
- `static IOReturn AppleMobileFileIntegrityUserClient::loadCompilationServiceCodeDirectoryHash(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleMobileFileIntegrityUserClient::copyBytesFromInputArguments(IOExternalMethodArguments *, void **, IOByteCount *)`
- `AppleMobileFileIntegrityUserClient`
- `virtual bool AppleMobileFileIntegrity::start(IOService *)`
- `site.AppleMobileFileIntegrityUserClient`
- `virtual void AppleMobileFileIntegrity::stop(IOService *)`
- `AppleMobileFileIntegrity`
- `static IOReturn AppleMobileFileIntegrityUserClient::setDenylist(OSObject *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleMobileFileIntegrityUserClient::loadTrustCache(OSObject *, void *, IOExternalMethodArguments *)`

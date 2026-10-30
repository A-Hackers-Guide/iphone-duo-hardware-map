# `AppleSEPARTService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b99af40`; metaclass vtable `0xfffffe00081f7948`; class vtable `0xfffffe00081f73f0`
- Registration (init): `0xfffffe000964a7f4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ARTService` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPManager`

## Strings in its kext that name it (9)

- `OSData *AppleSEPARTService::getART()_block_invoke`
- `OSData *AppleSEPARTService::getART()`
- `void AppleSEPARTService::clearART()`
- `void AppleSEPARTService::_ensure_nvram_readable()`
- `AppleSEPARTService`
- `void AppleSEPARTService::_ensure_nvram_writable()`
- `site.AppleSEPARTService`
- `virtual bool AppleSEPARTService::start(IOService *)`
- `bool AppleSEPARTService::setART(const OSData *)`

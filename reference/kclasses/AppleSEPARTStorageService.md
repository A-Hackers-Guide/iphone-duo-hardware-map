# `AppleSEPARTStorageService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b99af18`; metaclass vtable `0xfffffe00081f7360`; class vtable `0xfffffe00081f6e08`
- Registration (init): `0xfffffe000964a7b8`
- Superclasses: [`AppleSEPEndpointService`](AppleSEPEndpointService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ARTStorageDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,arts`

## Strings in its kext that name it (3)

- `site.AppleSEPARTStorageService`
- `virtual bool AppleSEPARTStorageService::start(IOService *)`
- `AppleSEPARTStorageService`

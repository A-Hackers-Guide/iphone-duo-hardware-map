# `AppleSEPARTRequestsService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b99aec8`; metaclass vtable `0xfffffe00081f6b90`; class vtable `0xfffffe00081f6638`
- Registration (init): `0xfffffe000964a748`
- Superclasses: [`AppleSEPEndpointService`](AppleSEPEndpointService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ARTRequestsDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,artr`

## Strings in its kext that name it (3)

- `virtual bool AppleSEPARTRequestsService::start(IOService *)`
- `site.AppleSEPARTRequestsService`
- `AppleSEPARTRequestsService`

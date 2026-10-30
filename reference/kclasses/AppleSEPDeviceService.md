# `AppleSEPDeviceService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b99a448`; metaclass vtable `0xfffffe00081f0020`; class vtable `0xfffffe00081efac8`
- Registration (init): `0xfffffe000962054c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (11)

- `bool AppleSEPARTRequests::_initForDeviceService(AppleSEPDeviceService *)`
- `bool AppleSEPARTStorage::_initForDeviceService(AppleSEPDeviceService *)`
- `site.AppleSEPDeviceService`
- `bool AppleSEPDeviceService::_init(const discovery_endpoint_info_t *, AppleSEPManager *)`
- `static AppleSEPARTStorage *AppleSEPARTStorage::sepARTStorage(AppleSEPDeviceService *)`
- `void AppleSEPDeviceService::_publish()`
- `bool AppleSEPXART::_initForDeviceService(AppleSEPDeviceService *, bool)`
- `bool AppleSEPHilo::_init(AppleSEPDeviceService *)`
- `AppleSEPEndpoint *AppleSEPDeviceService::getEndpoint(OSObject *, IOSlaveEndpoint::Action, void *)`
- `AppleSEPDeviceService`
- `static void AppleSEPDeviceService::getPropertyForEpName(char *, size_t, uint32_t)`

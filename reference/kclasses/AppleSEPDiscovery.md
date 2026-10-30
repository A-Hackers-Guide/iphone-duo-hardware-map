# `AppleSEPDiscovery`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xa98` (2,712 bytes)
- Metaclass: `0xfffffe000b99a470`; metaclass vtable `0xfffffe00081f01f8`; class vtable `0xfffffe00081f00b8`
- Registration (init): `0xfffffe0009621008`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (10)

- `AppleSEPDiscovery`
- `void AppleSEPDiscovery::_msgReceived(void *, void *)`
- `IOReturn AppleSEPDiscovery::_getEndpointInfoGated(void *, uint32_t *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPDiscovery.cpp`
- `site.AppleSEPDiscovery`
- `void AppleSEPDiscovery::_init(AppleSEPManager *)`
- `IOReturn AppleSEPDiscovery::_endpointIsAdvertisedGated(uint32_t *, bool *)`
- `AppleSEPDiscovery.cpp`
- `bool AppleSEPDiscovery::endpointIsAdvertised(uint32_t)`
- `void AppleSEPDiscovery::_exposeNub(const discovery_endpoint_info_t *)`

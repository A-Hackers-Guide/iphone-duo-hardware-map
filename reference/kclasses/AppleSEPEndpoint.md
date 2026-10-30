# `AppleSEPEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b99a5d8`; metaclass vtable `0xfffffe00081f1f90`; class vtable `0xfffffe00081f1e50`
- Registration (init): `0xfffffe000962cca4`
- Superclasses: [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Direct subclasses (11; 11 in total)

- [`AppleSEPARTRequests`](AppleSEPARTRequests.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPARTStorage`](AppleSEPARTStorage.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPBooter`](AppleSEPBooter.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPControl`](AppleSEPControl.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPDebug`](AppleSEPDebug.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPDiscovery`](AppleSEPDiscovery.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPHDCPEndpoint`](AppleSEPHDCPEndpoint.md) — `com.apple.driver.AppleSEPHDCPManager`
- [`AppleSEPHilo`](AppleSEPHilo.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPLogger`](AppleSEPLogger.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPTesting`](AppleSEPTesting.md) — `com.apple.driver.AppleSEPManager`
- [`AppleSEPXART`](AppleSEPXART.md) — `com.apple.driver.AppleSEPManager`

## Strings in its kext that name it (27)

- `AppleSEPEndpoint::endpointWithIndex(handle) == nullptr`
- `virtual IOReturn AppleSEPEndpoint::setReceiveOOLBuffer(IOSlaveMemory *)`
- `AppleSEPEndpoint.cpp`
- `virtual void AppleSEPEndpoint::enable()`
- `virtual IOReturn AppleSEPEndpoint::setSendOOLBuffer(IOSlaveMemory *)`
- `void AppleSEPEndpoint::startOperation()`
- `void AppleSEPEndpoint::_unholdAfterSleep()`
- `virtual IOCommandGate *AppleSEPEndpoint::getCommandGate()`
- `AppleSEPEndpoint::initWithOptions(forSEP, this, action, nullptr, EP_DISCOVERY)`
- `void AppleSEPEndpoint::_holdForSleep()`
- `(*endpointHandle < AppleSEPEndpoint::_max_endpoints) || (*endpointHandle == EP_L4INFO)`
- `AppleSEPEndpoint`
- `site.AppleSEPEndpointService`
- `AppleSEPEndpointService`
- `static IOReturn AppleSEPEndpoint::setReceiveRelayBuffer(IOSlaveProcessor *, uint8_t, IOOptionBits, IOByteCount, IOByteCount, IOSlaveMemory **)`
- `void AppleSEPEndpoint::endOperation()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPEndpoint.cpp`
- `AppleSEPEndpoint *AppleSEPDeviceService::getEndpoint(OSObject *, IOSlaveEndpoint::Action, void *)`
- `site.AppleSEPEndpoint`
- `static IOReturn AppleSEPEndpoint::setSendRelayBuffer(IOSlaveProcessor *, uint8_t, IOOptionBits, IOByteCount, IOByteCount, IOSlaveMemory **)`
- `message.frame.endpoint < AppleSEPEndpoint::_max_endpoints`
- `AppleSEPEndpoint::endpointWithIndex(handle) == endpoint`
- `AppleSEPEndpoint::endpointWithIndex(EP_CONTROL) == endpoint`
- `AppleSEPEndpoint *AppleSEPManager::_getEndpointFromEndpointService(uint32_t, uint32_t)`
- `handle < AppleSEPEndpoint::_max_endpoints`
- `virtual bool AppleSEPEndpoint::initWithOptions(IOSlaveProcessor *, OSObject *, IOSlaveEndpoint::Action, void *, UInt32)`
- `virtual IOReturn AppleSEPEndpoint::sendMessage(void *, void *, bool)`

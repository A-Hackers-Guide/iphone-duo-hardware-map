# `AppleSEPARTRequests`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b99aea0`; metaclass vtable `0xfffffe00081f65a0`; class vtable `0xfffffe00081f6460`
- Registration (init): `0xfffffe000964a708`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (17)

- `IOReturn AppleSEPARTRequests::_msgSendInternal(AppleSEPARTStorage::Opcode *, unsigned int *, AppleSEPMessage *)`
- `void AppleSEPARTRequests::configure_in_buffer()`
- `AppleSEP:WARNING: AppleSEPARTRequests::_msgAction() Unexpected! - Got a message that isn't a response.\n`
- `bool AppleSEPARTRequests::_initForDeviceService(AppleSEPDeviceService *)`
- `AppleSEP:WARNING: AppleSEPARTRequests received message for inactive tag %u\n`
- `virtual bool AppleSEPARTRequestsService::start(IOService *)`
- `site.AppleSEPARTRequestsService`
- `AppleSEPARTRequests`
- `void AppleSEPARTRequests::_msgAction(void *, void *)`
- `IOReturn AppleSEPARTRequests::handle_first_connected()`
- `AppleSEP:WARNING: AppleSEPARTRequests::_msgSendInternal() - result != kIOReturnSuccess - setting active to false\n`
- `site.AppleSEPARTRequests`
- `AppleSEP:WARNING: AppleSEPARTRequests received message for incorrect endpoint %u\n`
- `AppleSEPARTRequestsService`
- `IOReturn AppleSEPARTRequests::_msgSend(AppleSEPARTStorage::Opcode, unsigned int *, AppleSEPMessage *)`
- `void AppleSEPARTRequests::configure_out_buffer()`
- `AppleSEP:WARNING: AppleSEPARTRequests received message for invalid tag %u\n`

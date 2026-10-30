# `AppleSEPARTStorage`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xf8` (248 bytes)
- Metaclass: `0xfffffe000b99aef0`; metaclass vtable `0xfffffe00081f6d68`; class vtable `0xfffffe00081f6c28`
- Registration (init): `0xfffffe000964a780`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (33)

- `IOReturn AppleSEPARTStorage::purgeSystemToken()`
- `IOReturn AppleSEPARTRequests::_msgSendInternal(AppleSEPARTStorage::Opcode *, unsigned int *, AppleSEPMessage *)`
- `bool AppleSEPARTStorage::_initForDeviceService(AppleSEPDeviceService *)`
- `IOReturn AppleSEPARTStorage::invalidateNonce()`
- `void AppleSEPARTStorage::find_firmware_manifest(AppleSEPFirmware *, void **, vm_size_t *)`
- `bool AppleSEPARTStorage::fetch_persisted_art()`
- `IOReturn AppleSEPARTStorage::getCurrentART(OSData **)`
- `AppleSEPARTStorage`
- `bool AppleSEPARTStorage::save_incoming_art(const uint8_t *, const uint8_t *)`
- `site.AppleSEPARTStorageService`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPARTStorage.cpp`
- `virtual bool AppleSEPARTStorageService::start(IOService *)`
- `static AppleSEPARTStorage *AppleSEPARTStorage::sepARTStorage(AppleSEPDeviceService *)`
- `void AppleSEPARTStorage::configure_in_buffer()`
- `AppleSEP:WARNING: AppleSEPARTStorage received message for inactive tag %u\n`
- `AppleSEPARTStorageService`
- `site.AppleSEPARTStorage`
- `void AppleSEPARTStorage::_msgAction(void *, void *)`
- `IOReturn AppleSEPARTStorage::commitHash()`
- `IOReturn AppleSEPARTStorage::handle_first_connected()`
- `IOReturn AppleSEPARTStorage::_msgSendInternal(Opcode *, unsigned int *)`
- `AppleSEP:WARNING: AppleSEPARTStorage received message for invalid tag %u\n`
- `IOReturn AppleSEPARTStorage::counterSelfTest(uint16_t *, uint16_t *)`
- `IOReturn AppleSEPARTStorage::getNewNonce(OSData **)`
- `IOReturn AppleSEPARTStorage::setART(const uint8_t *, const uint8_t *)`
- `IOReturn AppleSEPARTStorage::clearART()`
- `bool AppleSEPARTStorage::persist_art(const uint8_t *, const uint8_t *, OSData **)`
- `void AppleSEPARTStorage::configure_out_buffer()`
- `AppleSEPARTStorage.cpp`
- `IOReturn AppleSEPARTStorage::captureSleepART()`
- `IOReturn AppleSEPARTStorage::_msgSend(Opcode, unsigned int *)`
- `AppleSEP:WARNING: AppleSEPARTStorage received message for endpoint %u\n`
- `IOReturn AppleSEPARTRequests::_msgSend(AppleSEPARTStorage::Opcode, unsigned int *, AppleSEPMessage *)`

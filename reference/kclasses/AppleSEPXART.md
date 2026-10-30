# `AppleSEPXART`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b99a8b8`; metaclass vtable `0xfffffe00081f5308`; class vtable `0xfffffe00081f51c8`
- Registration (init): `0xfffffe000963b670`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (42)

- `AppleSEPXART_embedded.cpp`
- `void AppleSEPXART::_initInternals(bool)`
- `IOReturn AppleSEPXART::gl_initialize(const char *)_block_invoke`
- `void AppleSEPManager::checkInMaster(AppleSEPXART *)`
- `IOReturn AppleSEPXART::bncn_generate(uint8_t, uint8_t *, size_t)`
- `AppleSEPXARTService`
- `IOReturn AppleSEPXART::_xmsgSendLocked(XARTMessage *, xart_buffer_config *, uint32_t *)`
- `void AppleSEPXART::_handle_sep_driven_msg(XARTMessage *)`
- `IOReturn AppleSEPXART::lynx_authenticate(const void *, size_t)_block_invoke`
- `virtual void AppleSEPXART::enable()`
- `IOReturn AppleSEPXART::_initOOLBuffers()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp`
- `IOReturn AppleSEPXART::getFullEpochs(SEPEpoch::EpochSlot *, size_t)_block_invoke`
- `bool AppleSEPXART::_shouldHaveBootMessageTimeout()`
- `void AppleSEPXART::format_acks(char *, size_t)`
- `bool AppleSEPXART::_getApManifestHash(uint8_t *, size_t *)`
- `void AppleSEPXART::_xmsgReceived(void *, void *)`
- `site.AppleSEPXART`
- `virtual bool AppleSEPXARTService::start(IOService *)`
- `void AppleSEPXART::format_acks(char *, size_t)_block_invoke`
- `AppleSEPXART.cpp`
- `AppleSEPXART`
- `IOReturn AppleSEPXART::commitEpochs(SEPEpoch::Epoch *, size_t)`
- `IOReturn AppleSEPXART::gl_initialize(const char *)`
- `IOReturn AppleSEPXART::_xmsgSend(XARTMessage *, xart_buffer_config *, uint32_t)`
- `IOReturn AppleSEPXART::commit_hash(uint8_t, const uint8_t *, size_t, bool)_block_invoke`
- `AppleSEP:WARNING: AppleSEPXART (EP: %u) received unknown SEP request op %u\n`
- `IOReturn AppleSEPXART::set_provisional_ap(uint8_t, bool)_block_invoke`
- `bool AppleSEPXART::_initForDeviceService(AppleSEPDeviceService *, bool)`
- `AppleSEP:WARNING: AppleSEPXART (EP: %u) received message for incorrect endpoint %u\n`
- `void AppleSEPXART::_initOOLBuffersAsync()`
- `AppleSEP:WARNING: AppleSEPXART (EP: %u)received message for inactive tag %u opcode %u\n`
- `IOReturn AppleSEPXART::_nonce_action(void *, uint32_t *, uint8_t, uint8_t *)_block_invoke`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/xART/AppleSEPXART.cpp`
- `site.AppleSEPXARTService`
- `IOReturn AppleSEPXART::get_ap_slot_info(uint8_t, uint8_t *, size_t, uint8_t *, size_t, uint8_t *)_block_invoke`
- `IOReturn AppleSEPXART::bncn_generate(uint8_t, uint8_t *, size_t)_block_invoke`
- `AppleSEP:WARNING: AppleSEPXART (EP: %u) received message for invalid tag %u opcode %u\n`
- `void AppleSEPManager::checkInMaster(AppleSEPXART *)_block_invoke`
- `IOReturn AppleSEPXART::getFullEpochs(SEPEpoch::EpochSlot *, size_t)`
- `IOReturn AppleSEPXART::get_ap_slot_info(uint8_t, uint8_t *, size_t, uint8_t *, size_t, uint8_t *)`
- `IOReturn AppleSEPXART::get_provisional_ap(uint8_t, bool *)_block_invoke`

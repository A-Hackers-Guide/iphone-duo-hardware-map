# `AppleSEPTesting`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b99a538`; metaclass vtable `0xfffffe00081f0e00`; class vtable `0xfffffe00081f0cc0`
- Registration (init): `0xfffffe0009629e24`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (18)

- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPTesting.cpp`
- `IOReturn AppleSEPTesting::_set_debug_var_gated(uint32_t, OSBoundedArrayRef<const uint8_t>, uint64_t)`
- `AppleSEPTestingService`
- `void AppleSEPTesting::_initInternals()`
- `site.AppleSEPTesting`
- `IOReturn AppleSEPTesting::_data_set_gated(OSBoundedArrayRef<const uint8_t>, uint32_t, uint32_t)`
- `IOReturn AppleSEPTesting::_initSendOOLBuffer(IOByteCount)`
- `AppleSEPTesting`
- `IOReturn AppleSEPTesting::_data_get_gated(OSBoundedArrayRef<uint8_t>, uint32_t *, uint32_t)`
- `site.AppleSEPTestingService`
- `AppleSEP:WARNING: AppleSEPTesting received message for inactive command (raw msg=%llx)\n`
- `IOReturn AppleSEPTesting::_initOOLs()`
- `void AppleSEPTesting::_testAction(void *, void *)`
- `virtual bool AppleSEPTestingService::start(IOService *)`
- `AppleSEPTesting.cpp`
- `IOReturn AppleSEPTesting::_get_debug_var_gated(uint32_t, OSBoundedArrayRef<const uint8_t>, uint64_t *, uint32_t *, uint8_t *)`
- `IOReturn AppleSEPTesting::_check_msg(TestingMessage *)`
- `IOReturn AppleSEPTesting::_runCommand(uint8_t, TestingMessage::Request::Payload, TestingMessage::Reply::Payload *, int)`

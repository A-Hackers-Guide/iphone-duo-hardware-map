# `AppleSEPBooter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b99a840`; metaclass vtable `0xfffffe00081f4e90`; class vtable `0xfffffe00081f4d50`
- Registration (init): `0xfffffe000963824c`
- Superclasses: [`AppleSEPEndpoint`](AppleSEPEndpoint.md) → [`IOSlaveEndpoint`](IOSlaveEndpoint.md) → [`IOEventSource`](IOEventSource.md)

## Strings in its kext that name it (15)

- `IOReturn AppleSEPBooter::generateROMNonce(uint8_t *, uint32_t *)`
- `void AppleSEPBooter::get_iBIC_KCV(uint8_t *, size_t)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPBooter.cpp`
- `static AppleSEPBooter *AppleSEPBooter::sepBooter(AppleSEPManager *)`
- `AppleSEPBooter.cpp`
- `site.AppleSEPBooter`
- `void AppleSEPBooter::_bootAction(void *, void *)`
- `bool AppleSEPBooter::initForSEP(AppleSEPManager *)`
- `void AppleSEPBooter::_captureiBICKCV()`
- `AppleSEPBooter`
- `static void AppleSEPBooter::triggerRecoveryMode()`
- `bool AppleSEPBooter::_getBootSlotId(uint8_t *)`
- `IOReturn AppleSEPBooter::_sendSEPART(IOMemoryDescriptor *)`
- `IOReturn AppleSEPBooter::romCommand(UInt64 *)`
- `IOReturn AppleSEPBooter::bootSEP(AppleSEPFirmware *, bool, AppleSEPSharedMemoryBuffer *, uint8_t *)`

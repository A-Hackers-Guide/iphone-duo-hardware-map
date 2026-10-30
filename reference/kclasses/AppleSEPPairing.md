# `AppleSEPPairing`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b99a7a0`; metaclass vtable `0xfffffe00081f4318`; class vtable `0xfffffe00081f3dc0`
- Registration (init): `0xfffffe0009633ce4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `PairingDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,pair`

## Strings in its kext that name it (10)

- `IOReturn AppleSEPPairing::_pmsgSendProvLocked(void *, void *, void *)`
- `AppleSEPPairing`
- `void AppleSEPPairing::_prepareOOLBuffers()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPPairing.cpp`
- `AppleSEPPairing.cpp`
- `site.AppleSEPPairing`
- `virtual bool AppleSEPPairing::start(IOService *)`
- `IOReturn AppleSEPPairing::send_4cc_message(uint32_t, const void *, size_t, void *, uint32_t *)`
- `IOReturn AppleSEPPairing::_pmsgSendLocked(void *, void *, void *)`
- `IOReturn AppleSEPPairing::getSTCKPairingInfo(const void *, size_t, void *, uint32_t *)`

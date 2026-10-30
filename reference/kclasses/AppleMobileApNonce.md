# `AppleMobileApNonce`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMobileApNonce`](../kexts/com.apple.driver.AppleMobileApNonce.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b97d760`; metaclass vtable `0xfffffe00081714d0`; class vtable `0xfffffe0008170f78`
- Registration (init): `0xfffffe00092723d8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMobileApNonceNVRAM` in [`com.apple.driver.AppleMobileApNonce`](../kexts/com.apple.driver.AppleMobileApNonce.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `defaults`

## Device-tree nodes it binds (1) [DT]

- [`/defaults`](../devicetree/root__defaults.md) on `defaults`

## Strings in its kext that name it (35)

- `AppleMobileApNonce`
- `static void AppleMobileApNonce::_printNonceAndHash(uint64_t, const void *, size_t)`
- `IOCommandGate *AppleMobileApNonce::_getCommandGate()`
- `IOReturn AppleMobileApNonce::_saveNonceGated(const char *)`
- `IOReturn AppleMobileApNonce::_generateNonceHash(uint64_t, uint8_t *)`
- `IOReturn AppleMobileApNonce::_readNonceGated(OSString **)`
- `IOReturn AppleMobileApNonce::_retrieveNonce(uint64_t *)`
- `site.AppleMobileApNonceUserClient`
- `void AppleMobileApNonce::_readNonceFromNVRAM(OSString **)`
- `virtual IOReturn AppleMobileApNonceUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `IOReturn AppleMobileApNonce::generateNonce(void *, size_t *)`
- `IOReturn AppleMobileApNonce::_readNonce(OSString **)`
- `IOReturn AppleMobileApNonce::getSlotID(uint32_t *)`
- `SEPApNonce *AppleMobileApNonce::_getSEPApNonce()`
- `AppleMobileApNonceUserClient`
- `void AppleMobileApNonce::_cleanupNonceSlots()`
- `void AppleMobileApNonce::_saveNonceInfoInNVRAM(const char *)`
- `void AppleMobileApNonce::_startupTasks()`
- `void AppleMobileApNonce::_waitForNVRAMReadable()`
- `IOReturn AppleMobileApNonce::_saveNonce(const char *)`
- `AppleMobileApNonce.cpp`
- `IOReturn AppleMobileApNonce::_clearNonceGated()`
- `virtual void AppleMobileApNonce::registerService(IOOptionBits)`
- `IOReturn AppleMobileApNonce::retrieveNonce(void *, size_t *)`
- `void AppleMobileApNonce::_waitForSandcatInit()`
- `IOReturn AppleMobileApNonce::_clearNonce()`
- `void AppleMobileApNonce::_waitForNVRAMWritable()`
- `virtual IOReturn AppleMobileApNonceUserClient::clientClose()`
- `bool AppleMobileApNonce::_getBootedSlotAndState(uint8_t *, uint8_t *)`
- `IOReturn AppleMobileApNonce::_generateNonce(void *, size_t *)`
- `virtual bool AppleMobileApNonceUserClient::start(IOService *)`
- `virtual bool AppleMobileApNonce::start(IOService *)`
- `void AppleMobileApNonce::_clearNonceInfoFromNVRAM()`
- `site.AppleMobileApNonce`
- `IOReturn AppleMobileApNonce::_pickNewNonceSlot(uint8_t *)`

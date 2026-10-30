# `AppleMemCacheController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x460` (1,120 bytes)
- Metaclass: `0xfffffe000b934620`; metaclass vtable `0xfffffe0007fbe808`; class vtable `0xfffffe0007fbe198`
- Registration (init): `0xfffffe00087177cc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (10)

- `site.AppleMemCacheController`
- `IOReturn AppleMemCacheController::updateCacheSize(uint32_t, bool)`
- `virtual void AppleMemCacheController::initDCSThermalLoop(IOService *)`
- `virtual bool AppleMemCacheController::start(IOService *)`
- `virtual edt_ptd_range_config *AppleMemCacheController::getPTDRange(const char *, uint32_t)`
- `IOReturn AppleMemCacheController::copyDataStreamInfo(MCDataStreamId, dataStreamInfo *)_block_invoke`
- `IOReturn AppleMemCacheController::ackCommand(unsigned int)`
- `bool AppleMemCacheController::sendCommandToPMP(MCCommand *, MCCommandQueue *)`
- `AppleMemCacheController.cpp`
- `AppleMemCacheController`

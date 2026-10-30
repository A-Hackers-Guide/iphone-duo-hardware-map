# `AppleSmartIODMAController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md)
- Object size: `0x4e0` (1,248 bytes)
- Metaclass: `0xfffffe000b9a4cc0`; metaclass vtable `0xfffffe0008235298`; class vtable `0xfffffe0008234cd8`
- Registration (init): `0xfffffe00097682f0`
- Superclasses: [`IODMAController`](IODMAController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSmartIODMA` in [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md): `IOProviderClass` = `AppleSmartIODMANub`, `IOMatchCategory` = `DMA`

## Strings in its kext that name it (18)

- `bool AppleSmartIODMAController::_enter_channel(UInt32, AppleSmartIODMA *, UInt32 *)`
- `virtual IOReturn AppleSmartIODMAController::initDMAChannel(IOService *, IODMAEventSource *, UInt32 *, UInt32)`
- `void AppleSmartIODMAController::returnBuffer(BufferHandle, unsigned int)`
- `virtual IOReturn AppleSmartIODMAController::queryDMACommand(UInt32, IODMACommand **, IOByteCount *, bool)`
- `IOReturn AppleSmartIODMAController::_initDMAChannelGated(const AppleSmartIODMAConfig *, IODMAEventSource *, UInt32 *)`
- `virtual IOReturn AppleSmartIODMAController::startDMACommand(UInt32, IODMACommand *, IODirection, IOByteCount, IOByteCount)`
- `virtual IOReturn AppleSmartIODMAController::setFrameSize(UInt32, UInt8)`
- `virtual bool AppleSmartIODMAController::start(IOService *)`
- `SmartIOResponseBuffer *AppleSmartIODMAController::responseForEndpointAndTag(UInt32, UInt32)`
- `virtual IOReturn AppleSmartIODMAController::stopDMACommand(UInt32, bool, UInt64)`
- `site.AppleSmartIODMAController`
- `virtual IOReturn AppleSmartIODMAController::setFIFODepth(UInt32, IOByteCount)`
- `SmartIODMABuffer *AppleSmartIODMAController::bufferForHandle(BufferHandle)`
- `AppleSmartIODMAController`
- `SmartIODMASegment *AppleSmartIODMAController::segmentForHandle(BufferHandle)`
- `virtual IOByteCount AppleSmartIODMAController::validFIFODepth(UInt32, IOByteCount, IODirection)`
- `virtual IOByteCount AppleSmartIODMAController::getFIFODepth(UInt32, IODirection)`
- `bool AppleSmartIODMA::_initWithOptions(AppleSmartIO *, AppleSmartIODMAController *, IODMAEventSource *, UInt32)`

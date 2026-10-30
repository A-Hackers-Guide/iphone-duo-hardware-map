# `AppleSmartIODMA`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md)
- Object size: `0x39f0` (14,832 bytes)
- Metaclass: `0xfffffe000b9a4ce8`; metaclass vtable `0xfffffe0008235430`; class vtable `0xfffffe0008235338`
- Registration (init): `0xfffffe000976832c`
- Superclasses: [`AppleSmartIOEndpoint`](AppleSmartIOEndpoint.md)

## Strings in its kext that name it (36)

- `bool AppleSmartIODMAController::_enter_channel(UInt32, AppleSmartIODMA *, UInt32 *)`
- `virtual IOReturn AppleSmartIODMAController::initDMAChannel(IOService *, IODMAEventSource *, UInt32 *, UInt32)`
- `void AppleSmartIODMA::_setConfiguration(AppleSmartIODMAConfig *)`
- `AppleSmartIODMA.cpp`
- `void AppleSmartIODMAController::returnBuffer(BufferHandle, unsigned int)`
- `virtual IOReturn AppleSmartIODMAController::queryDMACommand(UInt32, IODMACommand **, IOByteCount *, bool)`
- `site.AppleSmartIODMA`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIODMA.cpp`
- `IOReturn AppleSmartIODMAController::_initDMAChannelGated(const AppleSmartIODMAConfig *, IODMAEventSource *, UInt32 *)`
- `virtual IOReturn AppleSmartIODMAController::startDMACommand(UInt32, IODMACommand *, IODirection, IOByteCount, IOByteCount)`
- `IOReturn AppleSmartIODMA::_configureDMA()`
- `virtual IOByteCount AppleSmartIODMA::validFIFODepth(IOByteCount, IODirection)`
- `IOReturn AppleSmartIODMA::_queryDMA(IODMACommand **, IOByteCount *, bool *)`
- `virtual void AppleSmartIODMA::_asyncMessage(void *, void *)`
- `void AppleSmartIODMA::_completeCommand(AppleSmartIOCommand *)`
- `AppleSmartIODMA`
- `void AppleSmartIODMA::_notifyCommand(AppleSmartIOCommand *)`
- `virtual IOReturn AppleSmartIODMAController::setFrameSize(UInt32, UInt8)`
- `virtual bool AppleSmartIODMAController::start(IOService *)`
- `IOReturn AppleSmartIODMA::_stopDMA(bool *, void *)`
- `AppleSmartIODMANub`
- `site.AppleSmartIODMANub`
- `IOReturn AppleSmartIODMA::_setFIFODepth(IOByteCount *)`
- `SmartIOResponseBuffer *AppleSmartIODMAController::responseForEndpointAndTag(UInt32, UInt32)`
- `bool AppleSmartIODMANub::initWithRegistryEntry(AppleSmartIO *, IORegistryEntry *)`
- `virtual IOReturn AppleSmartIODMAController::stopDMACommand(UInt32, bool, UInt64)`
- `site.AppleSmartIODMAController`
- `virtual IOReturn AppleSmartIODMAController::setFIFODepth(UInt32, IOByteCount)`
- `SmartIODMABuffer *AppleSmartIODMAController::bufferForHandle(BufferHandle)`
- `AppleSmartIODMAController`
- `SmartIODMASegment *AppleSmartIODMAController::segmentForHandle(BufferHandle)`
- `virtual IOByteCount AppleSmartIODMAController::validFIFODepth(UInt32, IOByteCount, IODirection)`
- `IOReturn AppleSmartIODMA::setParam(SmartIOParameter, UInt32)`
- `virtual IOByteCount AppleSmartIODMAController::getFIFODepth(UInt32, IODirection)`
- `bool AppleSmartIODMA::_initWithOptions(AppleSmartIO *, AppleSmartIODMAController *, IODMAEventSource *, UInt32)`
- `IOReturn AppleSmartIODMA::_startDMACommand(IODMACommand *, IOByteCount *, IOByteCount *)`

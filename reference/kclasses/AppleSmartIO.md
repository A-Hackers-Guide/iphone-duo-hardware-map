# `AppleSmartIO`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md)
- Object size: `0x858` (2,136 bytes)
- Metaclass: `0xfffffe000b9a4ba8`; metaclass vtable `0xfffffe0008233e30`; class vtable `0xfffffe00082338c8`
- Registration (init): `0xfffffe00097607c4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSmartIO` in [`com.apple.driver.AppleSmartIO2`](../kexts/com.apple.driver.AppleSmartIO2.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `['SIOEndpoint1', 'SIO1Endpoint1']`

## Strings in its kext that name it (60)

- `bool AppleSmartIODMAController::_enter_channel(UInt32, AppleSmartIODMA *, UInt32 *)`
- `virtual IOReturn AppleSmartIODMAController::initDMAChannel(IOService *, IODMAEventSource *, UInt32 *, UInt32)`
- `virtual IOReturn AppleSmartIOEndpoint::sendMessage(void *, void *, bool)`
- `bool AppleSmartIOEndpoint::initWithOptions(AppleSmartIO *, OSObject *, UInt32)`
- `void AppleSmartIODMA::_setConfiguration(AppleSmartIODMAConfig *)`
- `AppleSmartIO (RTBuddy-based)::start Could not find valid mapper\n`
- `virtual bool AppleSmartIOCommandPool::returnCommand(AppleSmartIOCommand *)`
- `virtual bool AppleSmartIO::start(IOService *)`
- `site.AppleSmartIOControl`
- `AppleSmartIODMA.cpp`
- `void AppleSmartIODMAController::returnBuffer(BufferHandle, unsigned int)`
- `AppleSmartIO.cpp`
- `virtual IOReturn AppleSmartIOUserClient::externalMethod(uint32_t, IOExternalMethodArgumentsOpaque *)`
- `virtual IOReturn AppleSmartIODMAController::queryDMACommand(UInt32, IODMACommand **, IOByteCount *, bool)`
- `AppleSmartIOUserClient.cpp`
- `void AppleSmartIOControl::sendTunables()`
- `void AppleSmartIOControl::sendPSRegisters()`
- `site.AppleSmartIODMA`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIODMA.cpp`
- `AppleSmartIO`
- `site.AppleSmartIOCommand *`
- `void AppleSmartIOControl::populateShimPowerGateProperties()`
- `void AppleSmartIOControl::setupShims()`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.cpp`
- `site.AppleSmartIOCommand`
- `IOReturn AppleSmartIODMAController::_initDMAChannelGated(const AppleSmartIODMAConfig *, IODMAEventSource *, UInt32 *)`
- `site.AppleSmartIO`
- `AppleSmartIOControl.cpp`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOCommand.cpp`
- `AppleSmartIOCommand.cpp`
- `virtual void AppleSmartIOEndpoint::ep_disable()`
- `void AppleSmartIOControl::setupDevices()`
- `virtual IOReturn AppleSmartIODMAController::startDMACommand(UInt32, IODMACommand *, IODirection, IOByteCount, IOByteCount)`
- `IOReturn AppleSmartIODMA::_configureDMA()`
- `virtual IOByteCount AppleSmartIODMA::validFIFODepth(IOByteCount, IODirection)`
- `virtual IOReturn AppleSmartIO::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)`
- `AppleSmartIOEndpoint`
- `IOReturn AppleSmartIODMA::_queryDMA(IODMACommand **, IOByteCount *, bool *)`
- `site.AppleSmartIOUserClient`
- `virtual void AppleSmartIODMA::_asyncMessage(void *, void *)`
- `void AppleSmartIODMA::_completeCommand(AppleSmartIOCommand *)`
- `UInt32 AppleSmartIO::shimToPSIndex(UInt32)`
- `AppleSmartIODMA`
- `void AppleSmartIODMA::_notifyCommand(AppleSmartIOCommand *)`
- `AppleSmartIOControl`
- `virtual IOReturn AppleSmartIODMAController::setFrameSize(UInt32, UInt8)`
- `AppleSmartIOUserClient`
- `virtual void AppleSmartIOControl::_asyncMessage(void *, void *)`
- `virtual void AppleSmartIOPerf::_asyncMessage(void *, void *)`
- `void AppleSmartIOControl::setupPanicBuffer()`
- `virtual bool AppleSmartIODMAController::start(IOService *)`
- `IOCommandGate *AppleSmartIOEndpoint::getCommandGate()`
- `IOReturn AppleSmartIODMA::_stopDMA(bool *, void *)`
- `AppleSmartIO.h`
- `AppleSmartIOCommand`
- `bool AppleSmartIOCommandPool::_initWithOptions(IOWorkLoop *, unsigned int)`
- `AppleSmartIODMANub`
- `site.AppleSmartIODMANub`
- `void AppleSmartIOPerf::setupPerfBuffer()`
- `AppleSmartIO (RTBuddy-based)::start (%p) - (%s@%s)\n`

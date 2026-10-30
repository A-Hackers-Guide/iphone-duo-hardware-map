# `AppleSEPManager`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xbb8` (3,000 bytes)
- Metaclass: `0xfffffe000b99ad48`; metaclass vtable `0xfffffe00081f6248`; class vtable `0xfffffe00081f5c80`
- Registration (init): `0xfffffe0009646964`
- Superclasses: [`IOSlaveProcessor`](IOSlaveProcessor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `A7IOPNub` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleA7IOPNub`, `IONameMatch` = `iop-nub,sep`
- `IntelIOPNub` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPIntelIOPNub`, `IONameMatch` = `iop-nub,sep`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) on `iop-nub,sep`
- [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) on `iop-nub,sep`

## Strings in its kext that name it (60)

- `void AppleSEPManager::_doorbellAction(void *, UInt32)`
- `AppleSEPManager: Received Paging off notification\n`
- `bool AppleSEPManager::_hasMessageBox()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPControl.cpp`
- `void AppleSEPHilo::_allocateMappedBounceBuffer(AppleSEPManager *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPTesting.cpp`
- `bool AppleSEPManager::_getRsepfirmwareInfo(uint32_t *)`
- `void AppleSEPManager::_requestPanicGated(const char *, const char *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp`
- `IOReturn AppleSEPManager::removeVisibleMemory(IODMACommand *)`
- `AppleSEPManagerARM.cpp`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/FIFO.h`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AllocMPM.cpp`
- `void AppleSEPManager::_updateDeviceTree()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPBooter.cpp`
- `void AppleSEPManager::_report_sandcat_pwn(uint32_t)`
- `bool AppleSEPManager::tryStartReseed()_block_invoke`
- `void AppleSEPManager::checkInMaster(AppleSEPXART *)`
- `void AppleSEPManager::_loadChannelObjectData()`
- `AppleSEPManager`
- `static AppleSEPBooter *AppleSEPBooter::sepBooter(AppleSEPManager *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp`
- `void AppleSEPManager::_sepIdleTimeout(IOTimerEventSource *)`
- `IOReturn AppleSEPManager::addVisibleMemory(IOMemoryDescriptor *, IODMACommand **, UInt64 *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPDiscovery.cpp`
- `virtual IOSlaveEndpoint *AppleSEPManager::endpointForHandle(OSObject *, IOSlaveEndpoint::Action, UInt32, void *)`
- `bool AppleSEPManager::endpointIsAdvertised(uint32_t)`
- `static IOService *AppleSEPManager::getReadableNvram()`
- `void AppleSEPManager::_allocateShm(bool)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPManagerARM.cpp`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPLogger.cpp`
- `void AppleSEPDiscovery::_init(AppleSEPManager *)`
- `void AppleSEPManager::_waitUntilCanSendMessage()`
- `enum AppleSEPManager::SEPSleepMode AppleSEPManager::_getSleepMode()`
- `unsigned int AppleSEPManager::_loadChannelObjectEntries(AppleSEPSharedMemoryBuffer::ChannelEntry *, unsigned int)`
- `virtual IOSlaveMemory *AppleSEPManager::_allocateRelayMemory(IOOptionBits, IOByteCount, IOByteCount)`
- `IOService *AppleSEPManager::_getServiceFromEndpointName(uint32_t, uint32_t)`
- `AppleSEPManager starting trace boot timer\n`
- `void AppleSEPManager::_asyncHoldForSleep(bool)`
- `void AppleSEPManager::_asyncHoldCall()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/SEPApNonce.cpp`
- `void AppleSEPHilo::_getBounceBuffer(AppleSEPManager *)`
- `void AppleSEPManager::_setupEpPower(uint32_t, uint32_t)_block_invoke`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPPairing.cpp`
- `IOReturn AppleSEPManager::_waitOSActiveGated(unsigned int *)`
- `bool AppleSEPDeviceService::_init(const discovery_endpoint_info_t *, AppleSEPManager *)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPCommon.h`
- `bool AppleSEPBooter::initForSEP(AppleSEPManager *)`
- `bool AppleSEPManager::_getTzInfo(unsigned int, bool *, uint32_t *)`
- `IOReturn AppleSEPManager::readDynamicObjectProperties(const char *, uint32_t *, uint32_t *)`
- `void AppleSEPManager::_setMapperState(IOMapper *, bool)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/SEPEpoch.cpp`
- `IOReturn AppleSEPManager::_sendMessageGated(UInt32 *, void *, void *, int *)`
- `bool AppleSEPManager::reseedXNUPRNG()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPARTStorage.cpp`
- `void AppleSEPManager::_setupEpPower(uint32_t, uint32_t)`
- `AppleSEPManager panic for %s: %s\n%s\n%s`
- `IOReturn AppleSEPManager::mapDynamicObject(const char *, IOBufferMemoryDescriptor **, uint32_t *, uint32_t *)`
- `static bool AppleSEPManager::_propToUint32(const OSObject *, uint32_t *)`

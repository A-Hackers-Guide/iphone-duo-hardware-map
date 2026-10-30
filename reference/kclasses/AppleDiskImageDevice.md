# `AppleDiskImageDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDiskImages2`](../kexts/com.apple.driver.AppleDiskImages2.md)
- Object size: `0x7238` (29,240 bytes)
- Metaclass: `0xfffffe000b941018`; metaclass vtable `0xfffffe0008052350`; class vtable `0xfffffe0008051d48`
- Registration (init): `0xfffffe0008b80208`
- Superclasses: [`IOBlockStorageDevice`](IOBlockStorageDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (47)

- `uint32_t AppleDiskImageDevice::getCreatorUCPID() const`
- `site.AppleDiskImageDevice`
- `virtual void AppleDiskImageDevice::free()`
- `IOReturn AppleDiskImageDevice::SetDeviceParams(const DICreateDeviceParams *)`
- `void AppleDiskImageDevice::CompleteCommand(uint32_t, int)`
- `bool AppleDiskImageDevice::sendDaemonRespawnMessage()`
- `IOReturn AppleDiskImageDevice::HandleUnmappedDIORequest(DIDeviceRequest *)`
- `bool AppleDiskImageDevice::AddStorageFeaturesDict(bool, bool)`
- `void AppleDiskImageDevice::cleanupDormantState()`
- `void AppleDiskImageDevice::AbortAllCommands()`
- `void AppleDiskImageDevice::CompleteRequest(DIDeviceRequest *, int, bool)`
- `bool AppleDiskImageDevice::setCreatorUC(DIDeviceCreatorUserClient *)`
- `bool AppleDiskImageDevice::requestGracefulShutdown(bool)`
- `void AppleDiskImageDevice::TerminateMightFaultThread(MightFaultCopier_t &)`
- `IOReturn AppleDiskImageDevice::boostAnyRequest(uint8_t)`
- `IOReturn AppleDiskImageDevice::PrepareMappedBuffersForIO(DIDeviceRequest *, bool)`
- `AppleDiskImageDevice`
- `IOReturn AppleDiskImageDevice::PrepareRequest(DIDeviceRequest *, enum kDIIO, KernelInflightGuard, bool, IOStorageAttributes *, bool)`
- `IOReturn AppleDiskImageDevice::SetupDormantRequestBuffers(DIDeviceRequest *)`
- `IOReturn AppleDiskImagesController::CreateDevice(DICreateDeviceParams *, DICreateDeviceReply *, OSSharedPtr<AppleDiskImageDevice> &)`
- `IOReturn AppleDiskImageDevice::executeBarrierQueueElement(DIDeviceRequest *, bool)`
- `virtual void AppleDiskImageDevice::stop(IOService *)`
- `bool AppleDiskImageDevice::onIOClientClose(DIDeviceIOUserClient *)`
- `/Library/Caches/com.apple.xbs/CE15835D-198B-471A-8C88-40746A5CDBDD/TemporaryDirectory.jeIxpv/Sources/DiskImages2/AppleDiskImages2/AppleDiskImageDevice.cpp`
- `void AppleDiskImageDevice::dormantIOTimeoutOccurred(OSObject *, IOTimerEventSource *)`
- `bool AppleDiskImageDevice::onCreatorClientClose()`
- `virtual IOReturn AppleDiskImageDevice::doEjectMedia()`
- `IOReturn AppleDiskImageDevice::ValidateAndSetupCommonParams(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `bool AppleDiskImageDevice::flushDeviceWithTimeout(uint32_t)`
- `IOReturn AppleDiskImageDevice::enqueueRequest(DIDeviceRequest *, bool)`
- `void AppleDiskImageDevice::mightFaultThread()`
- `void AppleDiskImageDevice::respawnRetryTimerFired(OSObject *, IOTimerEventSource *)`
- `bool AppleDiskImageDevice::triggerDaemonRespawn()`
- `virtual bool AppleDiskImageDevice::willTerminate(IOService *, IOOptionBits)`
- `IOReturn AppleDiskImageDevice::prepareUnmapCommand(DIDeviceRequest *, bool)`
- `void AppleDiskImageDevice::DIOThread()`
- `bool AppleDiskImageDevice::drainDormantIOQueue()`
- `virtual bool AppleDiskImageDevice::terminate(IOOptionBits)`
- `void AppleDiskImageDevice::cleanupForDaemonRespawn()`
- `IOReturn AppleDiskImageDevice::ReconnectForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`
- `bool AppleDiskImageDevice::setIOProvider(DIDeviceIOUserClient *)`
- `IOReturn AppleDiskImageDevice::CopyFromSharedBuffers(DIDeviceRequest *)`
- `bool AppleDiskImageDevice::AddOwnerCredentials()`
- `IOReturn AppleDiskImageDevice::boostAllPending(uint8_t)`
- `void AppleDiskImageDevice::executeBarrierQueueLocked()`
- `IOReturn AppleDiskImageDevice::claimDormantDevice(uint32_t)`
- `IOReturn AppleDiskImageDevice::InitForIO(DIDeviceIOUserClient *, DIDeviceIOParams *, uint16_t)`

# `AGXAccelerator`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x1d160` (119,136 bytes)
- Metaclass: `0xfffffe000b92a4b0`; metaclass vtable `0xfffffe0007f6ec70`; class vtable `0xfffffe0007f71270`
- Registration (init): `0xfffffe0008547c9c`
- Superclasses: [`IOGPU`](IOGPU.md) → [`IOAcceleratorES`](IOAcceleratorES.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 4 in total)

- [`AGXFamilyAccelerator`](AGXFamilyAccelerator.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (38)

- `bool AGXHWDSIDManager::init(AGXAccelerator *, IOService *)`
- `void AGXAccelerator::populateLinearFrequencyTransferTable(float *, uint32_t)`
- `virtual uint32_t AGXAcceleratorRing<AGFIAcceleratorDeviceControlEntry>::getWriteIndex() const [AGXAcceleratorRingEntry = AGFIAcceleratorDeviceControlEntry]`
- `void AGXArmFirmwareMapper::setAccelerator(AGXAccelerator *const)`
- `virtual uint32_t AGXAcceleratorRing<AGFIAcceleratorDeviceControlEntry>::getReadIndex() const [AGXAcceleratorRingEntry = AGFIAcceleratorDeviceControlEntry]`
- `virtual uint64_t AGXAccelerator::getAgxCrUmaIdealConstantCount()`
- `virtual uint64_t AGXAccelerator::halReadKSMFEReg(uint32_t)`
- `virtual bool AGXAccelerator::configureDevice(IOService *)`
- `bool AGXSecureGart::initInner(AGXAccelerator *, task_t, uint64_t, bool, AGFIFirmwareRole)`
- `bool AGXAccelerator::umaDescIsLoaded(AGXUSCPrivMemFList *) const`
- `virtual void AGXAccelerator::halWriteKSMFEReg(uint32_t, uint64_t)`
- `void AGXAccelerator::allocateMemoryEvent(IOInterruptEventSource *, int)`
- `void AGXAccelerator::validateASCWakeupEvent()`
- `void AGXAccelerator::waitForCommandSubmissionEnabled(const uint32_t, const uint64_t, const eIOGPUCommandQueuePriority)`
- `site.AGXAcceleratorG19P`
- `virtual OSSharedPtr<IOFence> AGXAccelerator::createIOFenceWithTransaction(IOSurface *, uint32_t, IOGPUCommandDescriptor *, IOFenceTransaction *)`
- `virtual FSTPBitArray AGXAccelerator::convertFromGlobalToDmMask(AGXIOFenceDataMasterType, const FSTPBitArray &)`
- `virtual void AGXAccelerator::mcacheApertureBufferSetup(AGXCommandHWDSIDData &, int32_t, AGFICommandKSMBufferInfo &, int32_t)`
- `virtual uint32_t AGXAcceleratorRing<AGFIAcceleratorDataMasterEntry>::getReadIndex() const [AGXAcceleratorRingEntry = AGFIAcceleratorDataMasterEntry]`
- `virtual bool AGXAccelerator::setupCSCAllocation()`
- `AGXAccelerator`
- `virtual void AGXAccelerator::populateMaximumPerformancePower()`
- `virtual void AGXAccelerator::halWaitForFenderPowerGate()`
- `void AGXAccelerator::storeUMADesc(AGXUSCPrivMemFList *)`
- `virtual void AGXAccelerator::halSetEventFlags(const AGFIKSMEventFlagMask &)`
- `virtual uint32_t AGXAcceleratorRing<AGFIAcceleratorDataMasterEntry>::getCFIIndex() const [AGXAcceleratorRingEntry = AGFIAcceleratorDataMasterEntry]`
- `virtual uint32_t AGXAcceleratorRing<AGFIAcceleratorDataMasterEntry>::getWriteIndex() const [AGXAcceleratorRingEntry = AGFIAcceleratorDataMasterEntry]`
- `uint32_t AGXAcceleratorRing<AGFIAcceleratorDeviceControlEntry>::getRingIndexForEntry(AGXAcceleratorRingEntry *) [AGXAcceleratorRingEntry = AGFIAcceleratorDeviceControlEntry]`
- `void KernelCalculatedSMAFinalResults::snapShotEnvironment(const AGXAccelerator &, const AGXUSCPrivMemPoolSMA &, AGXIOFenceDataMasterType)`
- `virtual uint64_t AGXAccelerator::halGetAgxCrUmaDefaultDupmMinCount() const`
- `void AGXAccelerator::populateLinearPowerTransferTable(float *, uint32_t)`
- `void AGXAccelerator::loadUMADesc(AGXUSCPrivMemFList *)`
- `virtual uint32_t AGXAcceleratorRing<AGFIAcceleratorDeviceControlEntry>::getCFIIndex() const [AGXAcceleratorRingEntry = AGFIAcceleratorDeviceControlEntry]`
- `AGXAcceleratorG19P`
- `virtual void AGXAccelerator::halResetEventFlags(const AGFIKSMEventFlagMask &)`
- `virtual void AGXAccelerator::handleSAPTInterrupt()`
- `virtual bool AGXAccelerator::start(IOService *)`
- `site.AGXAccelerator`

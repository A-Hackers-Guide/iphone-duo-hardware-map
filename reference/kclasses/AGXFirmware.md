# `AGXFirmware`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x1848` (6,216 bytes)
- Metaclass: `0xfffffe000b92a6b0`; metaclass vtable `0xfffffe0007f725e8`; class vtable `0xfffffe0007f727f8`
- Registration (init): `0xfffffe000857e704`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (1; 2 in total)

- [`AGXArmFirmware`](AGXArmFirmware.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (41)

- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventProcessExitComplete, FWET1 = kAGFIFirmwareEventTypeProcessExitComplete, FWET2 = kAGFIFirmwareEventNone]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGXSTrace, FWET1 = kAGFIFirmwareEventTypeFWTrace, FWET2 = kAGFIFirmwareEventNone]`
- `virtual void AGXFirmware::setupConfig()`
- `void AGXFirmwareResourceStack<unsigned char, AGXParameterManagement>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = unsigned char, ElementOwner = AGXParameterManagement, kL1WidthBits = 64, kL2WidthBits = 64]`
- `virtual bool AGXFirmware::isFWAwake()`
- `void AGXFirmwareResourceStack<_AGFISchedulerState, AGXCommandQueue, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = _AGFISchedulerState, ElementOwner = AGXCommandQueue, kL1WidthBits = 64, kL2WidthBits = 256]`
- `void AGXFirmwareResourceStack<_AGFIChannelState, AGXChannel, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = _AGFIChannelState, ElementOwner = AGXChannel, kL1WidthBits = 64, kL2WidthBits = 256]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventStampUpdate, FWET1 = kAGFIFirmwareEventTypeStampsUpdated, FWET2 = kAGFIFirmwareEventNone]`
- `virtual void AGXFirmware::decodeAndPrintSchedulerStatus(AGFSubmitList *)`
- `AGFIFirmwareEventType AGXFirmwareRingValidator::peekNextEntry(AGFIFirmwareEventRingEntry *) const`
- `site.AGXFirmwareResourceAllocation`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventMetrologyAging, FWET1 = kAGFIFirmwareEventTypeMtrResult, FWET2 = kAGFIFirmwareEventNone]`
- `void AGXStatistics::recordStatisticsEntryFromFW(AGFIFirmwareEventRingEntry, const AGXFirmwareRingValidator *)`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIChannelErrorEventArgs, FWET1 = kAGFIFirmwareEventTypeChannelError, FWET2 = kAGFIFirmwareEventNone]`
- `AGXFirmware`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventHWRecovery, FWET1 = kAGFIFirmwareEventTypeGPURestart, FWET2 = kAGFIFirmwareEventNone]`
- `void AGXFirmwareResourceStack<AGXCachedFWChannelMem, AGXChannel, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = AGXCachedFWChannelMem, ElementOwner = AGXChannel, kL1WidthBits = 64, kL2WidthBits = 256]`
- `void AGXFirmware::drainFirmwareEventRing(AGFIFirmwareRole)`
- `void AGXFirmware::handleChannelErrorEvent(const AGFIChannelErrorEventArgs &)`
- `void AGXFirmwareResourceStack<AGXUncachedFWChannelMem, AGXChannel, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = AGXUncachedFWChannelMem, ElementOwner = AGXChannel, kL1WidthBits = 64, kL2WidthBits = 256]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventSMAPPDTUpdateIdle, FWET1 = kAGFIFirmwareEventTypeSMAPPDTUpdateIdle, FWET2 = kAGFIFirmwareEventNone]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventRTCompletionInfo, FWET1 = kAGFIFirmwareEventTypeRTCompletionEvent, FWET2 = kAGFIFirmwareEventNone]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventSharedEventSignalComplete, FWET1 = kAGFIFirmwareEventTypeSharedEventSignalComplete, FWET2 = kAGFIFirmwareEventNone]`
- `virtual void AGXFirmware::submitContextIDBaseAddress(int32_t, uint64_t, uint32_t)`
- `AGXFirmwareKextG18RTBuddy`
- `bool AGXFirmwareRingValidator::ringHasOutstandingEntries() const`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventAlive, FWET1 = kAGFIFirmwareEventTypeFirmwareAlive, FWET2 = kAGFIFirmwareEventNone]`
- `void AGXFirmwareRingValidator::snapshotState()`
- `site.AGXFirmwareResourceStackInstType`
- `AGXFirmwareKextRTBuddy - AGXFirmwareKextG18RTBuddy`
- `virtual bool AGXFirmware::isGFXBooted(uint64_t *)`
- `virtual void AGXFirmware::blockForRingEmpty(uint32_t)`
- `virtual bool AGXFirmware::requestGartInval(AGXGart *)`
- `virtual const IOGPUCommandQueue *AGXFirmware::processFirmwareInitiatedRecovery(AGFIRecoveryInfo *, const eRestartReason)`
- `virtual const void AGXFirmware::processFirmwareTACommandsRecovery(AGFIRecoveryInfo *)`
- `void AGXFirmwareResourceStack<unsigned long long, AGXLateEvalEvent, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = unsigned long long, ElementOwner = AGXLateEvalEvent, kL1WidthBits = 64, kL2WidthBits = 256]`
- `static uint32_t AGXFirmware::getFirmwarePriorityForAGXPriority(eAGXContextPriorityType)`
- `AGXGrowableArray<AGXFirmwareResourceAllocation *>::~AGXGrowableArray() [T = AGXFirmwareResourceAllocation *]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventSMAStarvedInterrupt, FWET1 = kAGFIFirmwareEventTypeSMAStarvedInterrupt, FWET2 = kAGFIFirmwareEventNone]`
- `void AGXFirmwareResourceStack<_AGFITimeStampQueue, AGXTimeStampQueue, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = _AGFITimeStampQueue, ElementOwner = AGXTimeStampQueue, kL1WidthBits = 64, kL2WidthBits = 256]`
- `const RET *AGXFirmwareRingValidator::validateType(const AGFIFirmwareEventRingEntry *) const [RET = AGFIFirmwareEventPMRequestMemory, FWET1 = kAGFIFirmwareEventTypeAllocatePMMemory, FWET2 = kAGFIFirmwareEventNone]`

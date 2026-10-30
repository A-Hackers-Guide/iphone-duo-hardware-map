# `ApplePTD`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePTD`](../kexts/com.apple.driver.ApplePTD.md)
- Object size: `0x160` (352 bytes)
- Metaclass: `0xfffffe000b9882c8`; metaclass vtable `0xfffffe000819c5d8`; class vtable `0xfffffe000819bff8`
- Registration (init): `0xfffffe0009375968`
- Superclasses: [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ApplePTD` in [`com.apple.driver.ApplePTD`](../kexts/com.apple.driver.ApplePTD.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `ptd,v1`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) on `ptd,v1`

## Strings in its kext that name it (59)

- `IOReturn ApplePTD::_ptdDoMultiCmdOp(ptd_cmd_t, uintptr_t, uint64_t)`
- `ApplePTDUserClient`
- `virtual IOReturn ApplePTD::unregisterInterrupt(IOService *, int)`
- `ApplePTDAccessorConcrete::ApplePTDAccessorConcrete(ApplePTD *)`
- `ApplePTDFunctionMultiCmd: cmd %d (%d)\n`
- `virtual IOReturn ApplePTD::disableInterrupt(IOService *, int)`
- `site.ApplePTDFunctionMultiCmd`
- `bool ApplePTDCommon::start(IOService *, IOService *)`
- `IOReturn ApplePTDCommon::_ptdLookupMultiple(ptd_data_entry_t *, uint32_t)`
- `IOReturn ApplePTDCommon::ptdDoCmdOp(ptd_cmd_t, uintptr_t, const ApplePTDAccessor &)`
- `IOReturn ApplePTD::_ptdRegisterHwIrqVector(uint32_t)`
- `ApplePTDFunctionCmd`
- `ApplePTDCommon.cpp`
- `virtual IOReturn ApplePTD::causeInterrupt(IOService *, int)`
- `IOReturn ApplePTD::_ptdAllocVectors()`
- `ApplePTDFunctionMultiCmd`
- `IOReturn ApplePTDCommon::_ptdInsertEntry(ptd_data_entry_t *)`
- `virtual void ApplePTD::initVector(IOInterruptVectorNumber, IOInterruptVector *)`
- `bool ApplePTDCommon::init(const char *)`
- `virtual bool ApplePTD::start(IOService *)`
- `IOReturn ApplePTD::_ptdGetConfig()`
- `site.ApplePTDFunctionCmd`
- `IOReturn ApplePTD::_ptdIsUpdated(ptd_data_entry_t *, ptd_function_args_t *)`
- `site.ApplePTDUserClient`
- `ApplePTD`
- `IOReturn ApplePTD::dumpInterrupt(IOService *, int)`
- `IOReturn ApplePTD::_ptdDoCmdOp(ptd_cmd_t, uintptr_t)`
- `IOReturn ApplePTD::_ptdRead(ptd_data_entry_t *, ptd_function_args_t *, bool)`
- `IOReturn ApplePTD::_ptdWrite(ptd_data_entry_t *, ptd_function_args_t *)`
- `ApplePTDCommon`
- `IOReturn ApplePTD::_ptdDoCmdOpISR(ptd_cmd_t, uintptr_t)`
- `IOReturn ApplePTD::_ptdSingleRead(uint64_t, uint64_t *, uint64_t *)`
- `ApplePTD.cpp`
- `site.ApplePTDCommon`
- `virtual IOReturn ApplePTD::enableInterrupt(IOService *, int)`
- `static SInt32 ApplePTDCommon::_ptdSortFunction(const OSMetaClassBase *, const OSMetaClassBase *, void *)`
- `IOReturn ApplePTDCommon::ptdEntryStruct(OSDictionary *, ptd_data_entry_t *)`
- `virtual IOReturn ApplePTDFunctionCmd::callFunction(void *, void *, void *)`
- `IOReturn ApplePTDCommon::_ptdLookupLength(uint32_t, uint32_t *)`
- `IOReturn ApplePTDCommon::_ptdFindAndCheckEntry(ptd_data_entry_t *, ptd_function_args_t *)`
- `site.ApplePTD`
- `void ApplePTD::deleteVector(IOInterruptVectorNumber, IOInterruptVector *)`
- `virtual void ApplePTD::enableVector(IOInterruptVectorNumber, IOInterruptVector *)`
- `virtual bool ApplePTDFunctionCmd::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)`
- `IOReturn ApplePTDCommon::_ptdReadMultiple(ptd_function_args_t *, uint32_t, bool, const ApplePTDAccessor &)`
- `ApplePTDFunctionCmd: data->getLength() %d dwords %lu\n`
- `virtual IOReturn ApplePTDFunctionMultiCmd::callFunction(void *, void *, void *)`
- `ApplePTDFunctionMultiCmd: data->getLength() %d dwords %lu\n`
- `IOReturn ApplePTD::_ptdIrqEnable(ptd_data_entry_t *, bool)`
- `ApplePTDFunctionCmd: cmd %d ptd_id 0x%x (%d)\n`
- `IOReturn ApplePTDCommon::appleARMFunctionNew(void *, void *)`
- `virtual IOReturn ApplePTD::registerInterrupt(IOService *, const int, void *, IOInterruptHandler, void *)`
- `virtual IOReturn ApplePTD::handleInterrupt(void *, IOService *, int)`
- `void ApplePTD::_ptdIrqRestore()`
- `virtual void ApplePTD::disableVectorHard(IOInterruptVectorNumber, IOInterruptVector *)`
- `ApplePTDFunctions.cpp`
- `IOReturn ApplePTDCommon::ptdDoMultiCmdOp(ptd_cmd_t, uintptr_t, uint64_t, const ApplePTDAccessor &)`
- `\"ApplePTD: %s:%u REQUIRE failed: %s\" @%s:%d`
- `virtual bool ApplePTDFunctionMultiCmd::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)`

# `com.apple.driver.ApplePTD`

- Name: ApplePTD
- Version: `1.0.0`
- UUID: `4BA71D8A-EF48-3EBC-991E-DCFF330A814E`
- Source version: `50.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ApplePTD` | `ptd,v1` |

## IOKit personalities (2) [KC]

### ApplePTD
- `CFBundleIdentifier`: `com.apple.driver.ApplePTD`
- `IOClass`: `ApplePTD`
- `IONameMatch`: `ptd,v1`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePTD`
- `IOPlatformActiveAction`: `89000`
- `IOPlatformHaltRestartAction`: `89000`
- `IOPlatformPanicAction`: `89000`
- `IOPlatformQuiesceAction`: `89000`
- `IOPlatformSleepAction`: `300`
- `IOPlatformWakeAction`: `300`
- `IOProviderClass`: `AppleARMIODevice`

### ApplePTDRemote
- `CFBundleIdentifier`: `com.apple.driver.ApplePTD`
- `IOClass`: `ApplePTDRemote`
- `IONameMatch`: `remote-ptd,v1`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePTD`
- `IOPlatformActiveAction`: `89000`
- `IOPlatformHaltRestartAction`: `89000`
- `IOPlatformPanicAction`: `89000`
- `IOPlatformQuiesceAction`: `89000`
- `IOPlatformSleepAction`: `300`
- `IOPlatformWakeAction`: `300`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePTD` | 0x160 | IOInterruptController → IOService → IORegistryEntry |
| `ApplePTDCommon` | 0x40 |  |
| `ApplePTDFunctionCmd` | 0x60 | AppleARMFunction |
| `ApplePTDFunctionMultiCmd` | 0x48 | AppleARMFunction |
| `ApplePTDUserClient` | 0xd8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002420 off=0x0069dde0-0x006a0200 addr=0xfffffe00076a1de0-0xfffffe00076a4200 r--/r--   __TEXT            
	sz=0x00001d85 off=0x0069e458-0x006a01dd addr=0xfffffe00076a2458-0xfffffe00076a41dd               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x006a01e0-0x006a0200 addr=0xfffffe00076a41e0-0xfffffe00076a4200               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00009114 off=0x0236d7a0-0x023768b4 addr=0xfffffe00093717a0-0xfffffe000937a8b4 r-x/r-x   __TEXT_EXEC       
	sz=0x00008e04 off=0x0236d7a0-0x023765a4 addr=0xfffffe00093717a0-0xfffffe000937a5a4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x023765a4-0x023768b4 addr=0xfffffe000937a5a4-0xfffffe000937a8b4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001e8 off=0x049841f0-0x049843d8 addr=0xfffffe000b9881f0-0xfffffe000b9883d8 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049841f0-0x049842b4 addr=0xfffffe000b9881f0-0xfffffe000b9882b4               __DATA.__data             
	sz=0x00000120 off=0x00000000-0x00000120 addr=0xfffffe000b9882b8-0xfffffe000b9883d8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001658 off=0x01197f98-0x011995f0 addr=0xfffffe000819bf98-0xfffffe000819d5f0 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x01197f98-0x01197fb8 addr=0xfffffe000819bf98-0xfffffe000819bfb8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x01197fb8-0x01197fd8 addr=0xfffffe000819bfb8-0xfffffe000819bfd8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000010d0 off=0x01197fd8-0x011990a8 addr=0xfffffe000819bfd8-0xfffffe000819d0a8         __DATA_CONST.__const            
	sz=0x00000140 off=0x011990a8-0x011991e8 addr=0xfffffe000819d0a8-0xfffffe000819d1e8         __DATA_CONST.__kalloc_type      
	sz=0x000001e0 off=0x011991e8-0x011993c8 addr=0xfffffe000819d1e8-0xfffffe000819d3c8         __DATA_CONST.__kalloc_var       
	sz=0x00000188 off=0x011993c8-0x01199550 addr=0xfffffe000819d3c8-0xfffffe000819d550         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a0 off=0x01199550-0x011995f0 addr=0xfffffe000819d550-0xfffffe000819d5f0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 118 at 0x04ae1b44
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4BA71D8A-EF48-3EBC-991E-DCFF330A814E
008: LC_SOURCE_VERSION           50.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004aac9e8 size=0x140
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePTD`
- `CFBundleGetInfoString`: `Copyright © 2026 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.ApplePTD`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePTD`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022 - 2026 Apple. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePTD.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898860576`
- `_PrelinkExecutableRelativePath`: `ApplePTD`
- `_PrelinkExecutableSize`: `52596`
- `_PrelinkExecutableSourceAddr`: `-2198898860576`
- `_PrelinkKmodInfo`: `-2198828711440`

## Strings (219) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.ptd_irq_node_t`
- `IOReturn ApplePTD::_ptdDoMultiCmdOp(ptd_cmd_t, uintptr_t, uint64_t)`
- `ApplePTDUserClient`
- `%s: cmd %d id 0x%x version 0x%x\n`
- `virtual IOReturn ApplePTD::unregisterInterrupt(IOService *, int)`
- `%s:    - source                %d\n`
- `ApplePTDAccessorConcrete::ApplePTDAccessorConcrete(ApplePTD *)`
- `%s: logging at level >= 1\n`
- `%s: PTD Not Found Error id 0x%x version 0x%x\n`
- `dict && ptd`
- `%s:kPtdLookupMultipleCmd (%d)\n`
- `%s:    - nub                   %p\n`
- `ptd_entry_irq < kPtdIrqEntryMax`
- `interrupts`
- `data`
- `ptd-int-enable-clr-offset`
- `ApplePTDFunctionMultiCmd: cmd %d (%d)\n`
- `_name`
- `dict != NULL`
- `virtual IOReturn ApplePTD::disableInterrupt(IOService *, int)`
- `12212`
- `ptd_tmp_node->guard == kPtdGuardPattern && ptd_tmp_node->vector != NULL`
- `%s: cannot alloc array\n`
- `ptd-int-enable-offset`
- `%s: starting\n`
- `super::start(provider)`
- `vector->interruptLock`
- `vectorCount == _ptdHwIrqVectors`
- `site.ApplePTDFunctionMultiCmd`
- `bool ApplePTDCommon::start(IOService *, IOService *)`
- `%s: InsertEntry %x %d %d %d %d %d %d\n`
- `IOReturn ApplePTDCommon::_ptdLookupMultiple(ptd_data_entry_t *, uint32_t)`
- `%s:kPtdIsUpdatedCmd updated %d (%d)\n`
- `_ptdVectorList[vectorNumber].nodes < kPtdNodesPerIrqMax`
- `%s: cannot alloc ic lock\n`
- `%s: waitForMatchingService failed\n`
- `ptd_id && length`
- `IOReturn ApplePTDCommon::ptdDoCmdOp(ptd_cmd_t, uintptr_t, const ApplePTDAccessor &)`
- `args`
- `%s:kPtdWriteCmd msg 0x%llx (%d)\n`
- `%s:    - target                %p\n`
- `%s:  node.id                   [%s]\n`
- `ret == 0`
- `IOReturn ApplePTD::_ptdRegisterHwIrqVector(uint32_t)`
- `%s: found %d interrupts\n`
- `%s: cannot alloc list array\n`
- `ApplePTDFunctionCmd`
- `0`
- `%s: registerInterrupt source %d, id %x, irq %d, irq entry %d\n`
- `%s: cannot alloc irq lock\n`
- `ApplePTDCommon.cpp`
- `%s: stopped\n`
- `ok`
- `virtual IOReturn ApplePTD::causeInterrupt(IOService *, int)`
- `%s:    - refCon                %p\n`
- `IOReturn ApplePTD::_ptdAllocVectors()`
- `ApplePTDFunctionMultiCmd`
- `%s: Found data table with %d rows\n`
- `%s: common start complete\n`
- `IOReturn ApplePTDCommon::_ptdInsertEntry(ptd_data_entry_t *)`
- `%s: cmd %d id 0x%x\n`
- `virtual void ApplePTD::initVector(IOInterruptVectorNumber, IOInterruptVector *)`
- `ptd_new_node`
- `bool ApplePTDCommon::init(const char *)`
- `ptd-data-table-rows`
- `ptdList && ptdListSize`
- `%s:kPtdPeekCmd msg 0x%llx (%d)\n`
- `%s: Args list size Error\n`
- `_registerServiceDone`
- `%s:  node.ref_cnt              %d\n`
- `ptd_prev_node->guard == kPtdGuardPattern && ptd_prev_node->vector != NULL`
- `entry_ptr && ptd && ptd->msg`
- `%s: Invalid data table! Length=%d Rows=%d\n`
- `%s: QuiesceAction\n`
- `!ml_get_interrupts_enabled()`
- `ptd_vers`
- `%s: PTD Not Found Error id 0x%x offset 0x%x entries 0x%x\n`
- `entryList && entryListSize`
- `argsList && argsListParam`
- `%s:kPtdLookupLengthCmd (%d)\n`
- `virtual bool ApplePTD::start(IOService *)`
- `ret == kIOReturnSuccess`
- `vector != NULL`
- `ptd_irq`
- `(mask & rdval) == 0`
- `data_row && _ptdEntries`
- `%s: initVector %x %d %d %p %p\n`
- `irq_num < _ptdHwIrqVectors`
- `IOReturn ApplePTD::_ptdGetConfig()`
- `site.ApplePTDFunctionCmd`
- `%s: terminating\n`
- `Finding ptd_id=0x%x, _ptdTableRows=%u\n`
- `%s: SleepAction\n`
- `IOReturn ApplePTD::_ptdIsUpdated(ptd_data_entry_t *, ptd_function_args_t *)`
- `site.ApplePTDUserClient`
- `ptd-data-table`
- `%s: PTD Table Invalid Error\n`
- `ApplePTD`
- `%s: start complete\n`
- `IOReturn ApplePTD::dumpInterrupt(IOService *, int)`
- `IOReturn ApplePTD::_ptdDoCmdOp(ptd_cmd_t, uintptr_t)`
- `IOReturn ApplePTD::_ptdRead(ptd_data_entry_t *, ptd_function_args_t *, bool)`
- `IOReturn ApplePTD::_ptdWrite(ptd_data_entry_t *, ptd_function_args_t *)`
- `ApplePTDCommon`
- `vector`
- `%s:  node.guard                0x%x\n`
- `IOReturn ApplePTD::_ptdDoCmdOpISR(ptd_cmd_t, uintptr_t)`
- `AppleSMCInterface`
- `ptd_id`
- `ptd_start`
- `ptd-data-table-dict`
- `%s: PTD Invalid Error id 0x%x offset 0x%x entries 0x%x size 0x%x\n`
- `%s: irq pending id 0x%x node %p\n`
- `21121111`
- `%s: deleteVector %d %p\n`
- `112`
- `_provider`
- `ptd-int-enable-set-offset`
- `IOReturn ApplePTD::_ptdSingleRead(uint64_t, uint64_t *, uint64_t *)`
- `121111221122`
- `ApplePTD.cpp`
- `%s: full path is %s\n`
- `_workLoop`
- `%s: InterruptControllerName not found\n`
- `entry.irq_num < _ptdHwIrqVectors`
- `%s:    - interruptRegistered   %d\n`
- `121111121222121211111111111`
- `site.ApplePTDCommon`
- `virtual IOReturn ApplePTD::enableInterrupt(IOService *, int)`
- `site.ptd_irq_list_t`
- `ptd_irq_num`
- `static SInt32 ApplePTDCommon::_ptdSortFunction(const OSMetaClassBase *, const OSMetaClassBase *, void *)`
- `No ptd entries populated!\n`
- `IOReturn ApplePTDCommon::ptdEntryStruct(OSDictionary *, ptd_data_entry_t *)`
- `_ptdDashboardMemoryMap && _ptdUpdateMemoryMap && _ptdConfigMemoryMap && _ptdPeekMemoryMap`
- `%s: WakeAction\n`
- `%s: ActiveAction\n`
- `%s:    - interruptDisabledSoft %d\n`
- `%s:    - handler               %p\n`
- `virtual IOReturn ApplePTDFunctionCmd::callFunction(void *, void *, void *)`
- `IOReturn ApplePTDCommon::_ptdLookupLength(uint32_t, uint32_t *)`
- `12111112122212121111111111111112222222211112`
- `site.IOLock *`
- `ptd-int-status-offset`
- `ptd_size`
- `dict1 && dict2`
- `IOReturn ApplePTDCommon::_ptdFindAndCheckEntry(ptd_data_entry_t *, ptd_function_args_t *)`
- `%s: Entry id 0x%x version 0x%x entry_start 0x%x size 0x%x irq_num 0x%x entry_irq 0x%x features 0x%x\n`
- `site.ApplePTD`
- `site.IOInterruptVector`
- `%s: causeInterrupt %x %d %p %p\n`
- `void ApplePTD::deleteVector(IOInterruptVectorNumber, IOInterruptVector *)`
- `virtual void ApplePTD::enableVector(IOInterruptVectorNumber, IOInterruptVector *)`
- `virtual bool ApplePTDFunctionCmd::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)`
- `%s: PTD Not Found Error id 0x%x\n`
- `IOReturn ApplePTDCommon::_ptdReadMultiple(ptd_function_args_t *, uint32_t, bool, const ApplePTDAccessor &)`
- `IOHibernateState`
- `%s: HaltRestartAction\n`
- `ml_get_interrupts_enabled()`
- `tmpData`
- `entry_ptr`
- `ApplePTDFunctionCmd: data->getLength() %d dwords %lu\n`
- `%s:kPtdPeekMultipleCmd (%d)\n`
- `%s:  node.vector               %p\n`
- `%s:    - interruptDisabledHard %d\n`
- `%s:  node.next                 %p\n`
- `%s:_ptdGetConfig %d %x %x %x %x\n`
- `virtual IOReturn ApplePTDFunctionMultiCmd::callFunction(void *, void *, void *)`
- `ApplePTDFunctionMultiCmd: data->getLength() %d dwords %lu\n`
- `ptd_data_table`
- `%s:kPtdReadCmd msg 0x%llx (%d)\n`
- `_commandGate`
- `vectorNumber < _ptdHwIrqVectors`
- `ptd-hw-irq-vectors`
- `IOReturn ApplePTD::_ptdIrqEnable(ptd_data_entry_t *, bool)`
- `ApplePTDFunctionCmd: cmd %d ptd_id 0x%x (%d)\n`
- `ptd_entry_irq`
- `%s: Invalid data table! Rows=0\n`
- `IOReturn ApplePTDCommon::appleARMFunctionNew(void *, void *)`
- `%s: getPath failed, len=%d\n`
- `_ptdDashboardBaseAddress && _ptdUpdateBaseAddress && _ptdConfigBaseAddress && _ptdPeekBaseAddress`
- `ptd_node_to_delete`
- `cmd == kPtdReadCmd || cmd == kPtdPeekCmd`
- `12121112`
- `%s: cmd %d id 0x%x entry_offset 0x%x entries 0x%x\n`
- `%s:kPtdReadMultipleCmd (%d)\n`
- `%s:  node ptr                  %p\n`
- `%s:    - interruptActive       %d\n`
- `common->start(provider, this)`
- `InterruptControllerName`
- `virtual IOReturn ApplePTD::registerInterrupt(IOService *, const int, void *, IOInterruptHandler, void *)`
- `local_ptd_irq.guard == kPtdGuardPattern`
- `virtual IOReturn ApplePTD::handleInterrupt(void *, IOService *, int)`
- `void ApplePTD::_ptdIrqRestore()`
- `%s: PanicAction\n`
- `virtual void ApplePTD::disableVectorHard(IOInterruptVectorNumber, IOInterruptVector *)`
- `data->getLength() / sizeof(uint32_t) == 4`
- `121111212`
- `ptd-debug`
- `%s: logging at level >= 2\n`
- `%s: EntriesCount %d\n`
- `IOUserClientClass`
- `ptd_tmp_node`
- `%s: cannot alloc register lock\n`
- `ApplePTDFunctions.cpp`
- `data->getLength() / sizeof(uint32_t) == 2`
- `_ptdDict`
- `%s: NewFunction 0x%x\n`
- `IOReturn ApplePTDCommon::ptdDoMultiCmdOp(ptd_cmd_t, uintptr_t, uint64_t, const ApplePTDAccessor &)`
- `\"ApplePTD: %s:%u REQUIRE failed: %s\" @%s:%d`
- `%s: enable irq %d mask 0x%x\n`
- `%s: serviceMatching failed\n`
- `addr && msg && metadata`
- `p`
- `virtual bool ApplePTDFunctionMultiCmd::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)`
- `ptd_features`
- `data_row`
- `1`
- `_ptdEntries`

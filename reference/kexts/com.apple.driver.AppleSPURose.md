# `com.apple.driver.AppleSPURose`

- Name: AppleSPURose
- Version: `1`
- UUID: `32688717-9888-39FA-BD23-19EA686AE6D0`
- Source version: `1087.40.4.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleGPIOICController`](com.apple.driver.AppleGPIOICController.md) 1.0.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `AppleSPURoseDriver` | `rose` |
| [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `AppleSPURoseDriverV2` | `rose` |

## IOKit personalities (2) [KC]

### AppleSPURoseDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPURose`
- `IOCFPlugInTypes`:
  - `0A3AB317-88E7-40A0-8968-335558146663`: `AppleSPURose.kext/PlugIns/RoseControllerLib.plugin`
- `IOClass`: `AppleSPURoseDriver`
- `IONameMatch`:
  - `rose`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPURose`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOUserClientClass`: `AppleSPURoseDriverUserClient`

### AppleSPURoseDriverV2
- `CFBundleIdentifier`: `com.apple.driver.AppleSPURose`
- `IOCFPlugInTypes`:
  - `0A3AB317-88E7-40A0-8968-335558146663`: `AppleSPURose.kext/PlugIns/RoseControllerLib.plugin`
- `IOClass`: `AppleSPURoseDriverV2`
- `IONameMatch`:
  - `rose`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPURose`
- `IOProviderClass`: `AppleSPUAppInterface`
- `IOUserClientClass`: `AppleSPURoseDriverUserClientV2`


## C++ classes (15) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSPUGPIOOperation` | 0x28 |  |
| `AppleSPUGPIOSequence` | 0x20 |  |
| `AppleSPURTKitOSClientDriver` | 0x348 | IOService → IORegistryEntry |
| `AppleSPURoseDriver` | 0x2f0 | IOService → IORegistryEntry |
| `AppleSPURoseDriverUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPURoseDriverUserClientV2` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `AppleSPURoseDriverV2` | 0x400 | AppleSPURTKitOSClientDriver → IOService → IORegistryEntry |
| `AppleSPUVisibleMemory` | 0x28 | RTBuddyVisibleMemory |
| `CircularBuffer` | 0x50 |  |
| `RTKitOSClientCrashObject` | 0x50 |  |
| `RTKitOSClientCrashSession` | 0x20 |  |
| `RoseCoredump` | 0x558 |  |
| `RoseCrashlog` | 0x60 |  |
| `RoseFirmwareLog` | 0x1060 |  |
| `RoseLogHandlerV2` | 0x28 | RTBuddyBinaryLogEntryHandler |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004840 off=0x0077a180-0x0077e9c0 addr=0xfffffe000777e180-0xfffffe00077829c0 r--/r--   __TEXT            
	sz=0x00000030 off=0x0077a850-0x0077a880 addr=0xfffffe000777e850-0xfffffe000777e880               __TEXT.__const            
	sz=0x000023e8 off=0x0077a880-0x0077cc68 addr=0xfffffe000777e880-0xfffffe0007780c68               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001d58 off=0x0077cc68-0x0077e9c0 addr=0xfffffe0007780c68-0xfffffe00077829c0               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00017d3c off=0x02703cd0-0x0271ba0c addr=0xfffffe0009707cd0-0xfffffe000971fa0c r-x/r-x   __TEXT_EXEC       
	sz=0x0001783c off=0x02703cd0-0x0271b50c addr=0xfffffe0009707cd0-0xfffffe000971f50c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000500 off=0x0271b50c-0x0271ba0c addr=0xfffffe000971f50c-0xfffffe000971fa0c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000004b2 off=0x04999a50-0x04999f02 addr=0xfffffe000b99da50-0xfffffe000b99df02 rw-/rw-   __DATA            
	sz=0x00000248 off=0x04999a50-0x04999c98 addr=0xfffffe000b99da50-0xfffffe000b99dc98               __DATA.__data             
	sz=0x00000268 off=0x00000000-0x00000268 addr=0xfffffe000b99dc98-0xfffffe000b99df00               __DATA.__common           (Zerofill)
	sz=0x00000002 off=0x00000000-0x00000002 addr=0xfffffe000b99df00-0xfffffe000b99df02               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003b08 off=0x01220d78-0x01224880 addr=0xfffffe0008224d78-0xfffffe0008228880 rw-/rw-   __DATA_CONST      
	sz=0x00000078 off=0x01220d78-0x01220df0 addr=0xfffffe0008224d78-0xfffffe0008224df0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000078 off=0x01220df0-0x01220e68 addr=0xfffffe0008224df0-0xfffffe0008224e68         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003308 off=0x01220e68-0x01224170 addr=0xfffffe0008224e68-0xfffffe0008228170         __DATA_CONST.__const            
	sz=0x000003c0 off=0x01224170-0x01224530 addr=0xfffffe0008228170-0xfffffe0008228530         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x01224530-0x012247b0 addr=0xfffffe0008228530-0xfffffe00082287b0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x012247b0-0x01224880 addr=0xfffffe00082287b0-0xfffffe0008228880         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 186 at 0x04ae6678
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     32688717-9888-39FA-BD23-19EA686AE6D0
008: LC_SOURCE_VERSION           1087.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab2890 size=0x368
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSPURose`
- `CFBundleIdentifier`: `com.apple.driver.AppleSPURose`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSPURose`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSPURose.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897958528`
- `_PrelinkExecutableRelativePath`: `AppleSPURose`
- `_PrelinkExecutableSize`: `132406`
- `_PrelinkExecutableSourceAddr`: `-2198897958528`
- `_PrelinkKmodInfo`: `-2198828623280`

## Strings (379) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `default`
- `coredump->getInfo(&desc->info) == true`
- `outputSize`
- `map`
- `_desiredPowerState == kRoseAPDesiredPowerOn`
- `non-fatal`
- `couldn't add log entry handler`
- `_trigger_coredump_sequence`
- `arguments->scalarInputCount == 2`
- `packetType != kSpuPacketTypeClientOpen`
- `_desiredPowerState == kRTKitOSClientAPDesiredPowerOn`
- `AppleSPURoseDriver`
- `size >= (hdr->size + sizeof(RoseRxPacketHeader))`
- `result == 0`
- `OSBoundedPtr.h`
- `RoseCoredump`
- `ret == 0 `
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV2/AppleSPURoseDriverV2.cpp`
- `durant`
- `!_transfer_inprogress`
- `RequireClient`
- `_queue[type]`
- `1211111212221212111112212122122122111111111221222222222222222221222221112111112222222211111212`
- `allocateQueues() == 0 `
- `_fwLogStore == nullptr`
- `AppleSPURoseDriverUserClient`
- `manual-dart`
- `121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211`
- `AppleDialogSPMIPMU`
- `_triggerClientTC`
- `could not get rtb service`
- `function-rose_smc_ds_reset`
- `arguments->structureInputSize == sizeof(RosefirmwareLoadDescriptor)`
- `state`
- `site.RoseLogHandlerV2`
- `_coredumpBuffer`
- `status == 0 `
- `ap`
- `disabled`
- `_cbLog`
- `rose->setProperty(\"ECID\", ecID, 64) == true`
- `sequence-power_off`
- `function-rose_pwr`
- `time`
- `_fwLogStore`
- `1211`
- `size == 0`
- `mmap != nullptr`
- `RoseLogHandlerV2`
- `CircularBuffer`
- `selector < (uint32_t) kAppleSPURoseDriverNumberOfMethods`
- `manifestIOMD`
- `\"%s\" @%s:%d`
- `bounded_ptr<T>::operator->: Accessing a member through this pointer would access memory outside of the bounds set originally`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Kext/GPIOSequencer/AppleSPUGPIOSequence.cpp`
- `RoseHwResetOk`
- `_queueFirmwareLogs == false`
- `qspi-device`
- `len > 0`
- `_queueRef[type]`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/RoseCoredump.cpp`
- `_queueLock[type] != nullptr`
- `status == true`
- `preprocessFirmware(apFwIOMD, &_fw_desc[ROSE_AP_PAYLOAD]) == 0 `
- `preprocessFirmware(dspFwIOMD, &_fw_desc[ROSE_DSP_PAYLOAD]) == 0 `
- `payloadSize <= 64`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Kext/RTKitOSCrashSession.cpp`
- `_crashlogSize >= sizeof(RTKitCrashlogInfo)`
- `\"%s: magic check failed - observed %04x,expected %04x\" @%s:%d`
- `aop-strict-entitlements`
- `_notifyClientStateTC`
- `sequence-power_on`
- `site.AppleSPURTKitOSClientDriver`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Controller/CircularBuffer.cpp`
- `Success`
- `md`
- `fwIOMD`
- `size <= RoseFirmwareLog::kLogMaxCapacity`
- `_reset_sequence`
- `service_name`
- `1212222112`
- `coredump size too large`
- `_commandGate`
- `core < RoseCoreCount`
- `size <= kCoredumpMaxSize`
- `site.RoseFirmwareLog`
- `function-rd_rose_pwr`
- `rose`
- `site.AppleSPURoseDriverV2`
- `!_fwDownloadInProgress`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Kext/GPIOSequencer/AppleSPUGPIOOperation.cpp`
- `_endpoint`
- `%02x`
- `RoseFirmwareLog.cpp`
- `internal_data`
- `role`
- `entry`
- `capacity`
- `AssertMacros: %s, %s file: %s, line: %d error: %#08x\n`
- `121222222111`
- `\"ringbuffer abort at %s:%d\" @%s:%d`
- `AppleSPUGPIOOperation`
- `RoseFirmwareState`
- `RTKitOSClientCrashSession`
- `\"%s: _rdptr=%u, _endptr=%u\" @%s:%d`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPUVisibleMemory/AppleSPUVisibleMemory.cpp`
- `AppleSPURTKitOSClientDriver`
- `sequence-reset`
- `rose->setProperty(\"ChipID\", chipID, 16) == true`
- `num`
- `RoseFirmwareLog`
- `arguments->scalarInputCount == 1`
- `ResetSequenceOk`
- `ECID`
- `_slaveMemory`
- `would fail`
- `size >= (hdr->size + sizeof(RoseErrorReportHeader))`
- `size != nullptr`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/RoseFirmwareLog.cpp`
- `12112`
- `size <= kBufferMaxSize`
- `_queue`
- `1211122221`
- `hdr != nullptr`
- `_clientAttachedStateLock`
- `sequence-trigger_coredump`
- `setActive`
- `RTKitOSClientCrashObject`
- `service`
- `!_queueEnable`
- `dict`
- `coredump != nullptr`
- `<null>`
- `SPI`
- `info`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV2/RoseLogHandlerV2.cpp`
- `spu_time`
- `lpmCtrlDictionary`
- `AppleSPUVisibleMemory`
- `RTKitROMState`
- `ChipID`
- `roleKey != nullptr`
- `size == sizeof(chipID)`
- `desc`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/AppleSPURoseDriverUCV1.cpp`
- `_name`
- `count != 0`
- `could not allocate log handler`
- `_slaveMemoryMap`
- `offset <= buffer_len`
- `_power_off_sequence`
- `*responseParams->responsePayloadSize >= _responseCache.responsePayloadSize`
- `_coredumpFunction`
- `_rtbService`
- `status == 0`
- `success`
- `matching`
- `RoseCrashlog`
- `funcNameLength != 0 && funcNameLength < lengthIn + sizeof(AppleSPUGPIOOperation::Description)`
- `AppleSPURoseDriverUserClientV2`
- `_powerFunction`
- `%s`
- `size == sizeof(boardID)`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV2/AppleSPURoseDriverUCV2.cpp`
- `cnfgFwIOMD`
- `coredump buffer allocation failed`
- `site.AppleSPUGPIOOperation`
- `operation != nullptr`
- `function-rose_coredump`
- `_crashSession._lock`
- `\"%s: queueRef:%p and queue:%p should be NULL\" @%s:%d`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/RoseCrashlog.cpp`
- `_crashlogBuffer`
- `ret == 0`
- `_buffer`
- `%llu`
- `AppleSPURoseDriver.cpp`
- `(OSCompareAndSwap(0, 1, ((volatile UInt32*)(&_fwDownloadInProgress))))`
- `fatal`
- `site.RoseCrashlog`
- `_crashlogSize <= _crashlogBufferSize`
- `dspFwIOMD`
- `site.AppleSPUVisibleMemory`
- `powerOffHw`
- `result == 0 `
- `lpm1`
- `%s | `
- `Initiated SLog log handler with provider: %s\n`
- `durant->setProperty(\"ECID\", ecID, 64) == true`
- `apFwIOMD`
- `count != 0 && count <= 16`
- `buffer`
- `121111121222121212222222222222222211111111212121221221221221221221221221221221221221221221221221221222211`
- `com.apple.drivers.AppleSPURose`
- `122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `QSPI`
- `site.RoseCoredump`
- `_operationFunction`
- `_logHandler`
- `function-rose_reset`
- `com.apple.aop.rose.controller.admin`
- `<unknown>`
- `_queueRef`
- `chipID == kRoseChipID`
- `enabled`
- `12111112122212121222222222222222221111111121212122122122122122122122122122122122122122122122122122122221111211222222221111212121`
- `triggerCoredump`
- `PowerOnSequenceOk`
- `powerOnHw`
- `continuous_time`
- `size == sizeof(ecID)`
- `site.RTKitOSClientCrashSession`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Kext/RTKitOSCrashObject.cpp`
- `inputBuffer`
- `_fwLogStoreLock`
- `dsp`
- `_bmd`
- `\"%s: size=%lu, capacity=%u\" @%s:%d`
- `iop_ringbuffer.h`
- `source_info`
- `_bufferLock`
- `outputBuffer`
- `(%s) : not entitled for administrating rose\n`
- `failed`
- `_crashobjects`
- `_provider`
- `RoseFirmwareDownloadState`
- `TX`
- `rose_time`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `preprocessFirmware(manifestIOMD, &_fw_desc[ROSE_MANIFEST]) == 0 `
- `site.AppleSPURoseDriverUserClientV2`
- `ok`
- `site.AppleSPURoseDriverUserClient`
- `packetType < 0x100`
- `result`
- `0 == getWorkLoop()->addEventSource(_crashSessionProgressTimer)`
- `RX`
- `_pmuService`
- `RoseRTKReady`
- `Failed`
- `_slaveProcessor`
- `_crashSessionProgressTimer`
- `IOPMUBootLPMCtrl`
- `size >= (hdrSize + sizeof(RTKitOSRxPacketHeader))`
- `AppleSPUGPIOSequence`
- `_resetFunction`
- `iomem`
- `AppleSPURoseDriverV2`
- `_crashSession`
- `RTBuddyService`
- `site.CircularBuffer`
- `12111112122212121111111111111210`
- `site.RTKitOSClientCrashObject`
- `matchingService`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/Rose/AppleSPURose/RoseV1/AppleSPURoseDriver.cpp`
- `fwMap`
- `packetType != kSpuPacketTypeClientClose`
- `workloop`
- `site.AppleSPUGPIOSequence`
- `ok == true`
- `durant->setProperty(\"ChipID\", chipID, 16) == true`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPU/AppleSPUEntitlementCheck.cpp`
- `_power_on_sequence`
- `site.AppleSPURoseDriver`
- `epService`
- `aop_rose-monitor-mask`
- `absolute_time`
- `/Library/Caches/com.apple.xbs/F60BBB0E-3581-4BB1-9823-1856F610155E/TemporaryDirectory.lVqE39/Sources/AppleSPUKext/AppleSPURTKitOSClientDrivers/common/Kext/AppleSPURTKitOSClientDriver.cpp`
- `_bufferVoid`

**[__TEXT.__os_log]**

- `crash data receive timeout`
- `failed to enable rose packet monitoring (0x%x)`
- `eid:%d, cmd:0x%04x, mt:%d, mp:%d, mpt:%d, size %d`
- `corrupted crashlog: packet size too small`
- `(core:%d) Section size error.  Signature %#0x, version %#0x, section (%u bytes) larger than remaining buffer (%u bytes)`
- `received malformed RTKitOSFTABDownloadReport (size %lu, expected %lu)`
- `rom nonce generation wakeup`
- `coredump size %lu, accumulated size %u`
- `rose boot complete event received`
- `passing unhandled endpoint %d event to controller`
- `%s crashlog collection started (sz %u)`
- `coredump chunk size is too small`
- `AppleSPURoseDriver::handleClose`
- `core (%d) crashobject (%d) payload received (size %lu)`
- `crashlog size %lu`
- `crashlog chunk size %lu, accumulated size %lu tot size %lu`
- `seq mismatch, expected: %llu`
- `new %s crash while a crash session already in progress`
- `%s crashlog packet received (size %lu)`
- `%s coredump object already exists`
- `AppleSPURoseDriver::handleOpen ret=%d`
- `(core:%d) crashlog already flushed to the queue`
- `Loading Rose Firmware`
- `coredump/crashlog size %lu, accumulated size %u`
- `unsupported packetType 0x%x\n`
- `%s crash data collection complete`
- `%s coredump collection completed`
- `_notifyUserClientState failed %x`
- `Client \"%s\" attempts to execute internal command %s:%s:%s on %s`
- `%s: AssertMacros: %s, %s file: %s, line: %d value:%x\n`
- `resetHW is called`
- `RTKitROM firmware download status %s`
- `crashlog object already exists, new crash for core %s`
- `%s`
- `corrupted crashlog: header/usupported version(%04x)`
- `reset sequence not found`
- `power sequencing failed`
- `(%d)add span offset %u, size %u`
- `%s(&%u)`
- `RTKitOS firmware download status %s`
- `unhandled crashlog cmd 0x%x`
- `failed to allocate coredump object`
- `%s coredump packet received (size %lu)`
- `Reset error while waiting %d`
- `rom nonce generation commandgate sleep`
- `%s call returned 0x%08X`
- `run sequence %s`
- `unhandled cmd 0x%x`
- `%s crash data collection started`
- `%s crashlog collection completed`
- `%s coredump size: %u`
- `trigger coredump sequence not found`
- `coredump session is closed, accumulated size %u`
- `(%d)add section vbase %llu, pbase %llu, size %u`
- `initializing sequence %s`
- `firmware download in progress, defer sleep`
- `changing power state 0x%x`
- `firmware logs are not handled in the driver`
- `Entitlement check %s for \"%s\" for operation %s:%s:%s on %s`
- `rtkitos command failed %d`
- `mangled timesync packet\n`
- `rx error packet size not supported %d`
- `unhandled cmd(0x%x) on rose crashlog endpoint`
- `failed to create %s crashlog object`
- `%s coredump collection started`
- `failed to send log buffer to aop`
- `rose command failed %d`
- `flush crashlog buffer size %lu`
- `rom nonce generation command failed %d`
- `firmware download completed, allow sleep`
- `triggerClient: %d`
- `unhandled packetType 0x%02x`
- `rtkitos client firmware state set to %d`
- `allocating buffer of size %lu for coredump`
- `create Operation %s: (type: %u, delay: %u ms)`
- `%s not available`
- `crashlog chunk size is too small`
- `error reading crashobject data 0x%x`
- `crashlog will be incomplete: allocated/received(%u/%u)`
- `(core:%d) coredump section found`
- `power off sequence not found`
- `core (%d) crashobject type %d, size %d collection started`
- `(core:%d) Section size too small.  Signature %#0x, version %#0x, section (%u bytes) should be at least %lu bytes`
- `allocating buffer of size %lu for coredump/crashlog`
- `Nonce generation wakeup: Response Packet Received`
- `Unknown function type for %s: %u`
- `unsupported interface %d\n`
- `driver error packet size not supported %lu`
- `RTKitOS firmware download error while waiting %d`
- `powerFunction is not present for this target`
- `Reading power-state from the provided power-read-function`
- `firmware download failed`
- `rx packet size not supported %d`
- `Reading power-state from the provided GPIO power-write-function`
- `lpm1 is %u`
- `rose firmare log queueing %s`
- `failed to add crashobject to session`
- `core (%d) crashobject (%d) collection completed`
- `failed to allocate crash session`
- `power on sequence not found`
- `crashlog queue is full`
- `rose firmware state set to %d`
- `unhandled cmd(0x%x) on durant crashlog endpoint`
- `%s failed with error %x`
- `received kSpuPacketTypeRTKitROMStateReport state %d`
- `sequence %s initialization %s`
- `Device bus type: %s\n`
- `received RTKitOSFTABDownloadReport. succcess=%u`
- `RTKitROM firmware download error while waiting %d`

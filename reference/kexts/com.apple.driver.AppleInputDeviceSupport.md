# `com.apple.driver.AppleInputDeviceSupport`

- Name: AppleInputDeviceSupport
- Version: `1010.1`
- UUID: `CDA60AB0-1FEE-3175-AA06-B4B3054E087B`
- Source version: `10110.1.0.0.0`
- Depends on: [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 11.0, [`com.apple.security.AppleImage4`](com.apple.security.AppleImage4.md) 3.0.0, [`com.apple.security.Image4`](com.apple.security.Image4.md) 1.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (23) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AIDCircularBuffer` | 0x20 |  |
| `AIDCircularBufferShared` | 0xc38 |  |
| `AIDCircularReadBufferShared` | 0xc48 | AIDCircularBufferShared |
| `AIDCircularWriteBufferShared` | 0xc40 | AIDCircularBufferShared |
| `AIDEventLogger` | 0x70 |  |
| `AIDFirmwareUpdateService` | 0x148 | IOService → IORegistryEntry |
| `AIDFirmwareUpdateUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `AIDImageDownloader` | 0x188 | AIDFirmwareUpdateService → IOService → IORegistryEntry |
| `AIDInterface` | 0xa8 | AIDService → IOService → IORegistryEntry |
| `AIDLogger` | 0x10 |  |
| `AIDLoggerUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `AIDQueueEventSource` | 0x70 | IOEventSource |
| `AIDQueueEventSourceWorkItem` | 0x40 |  |
| `AIDReporter` | 0x78 |  |
| `AIDReporterSimple` | 0x98 | AIDReporter |
| `AIDReporterState` | 0xb0 | AIDReporter |
| `AIDReporters` | 0x28 |  |
| `AIDSerialLogger` | 0x10 | AIDLogger |
| `AIDService` | 0xa0 | IOService → IORegistryEntry |
| `AIDSharedMemoryManager` | 0x40 |  |
| `AIDUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |
| `AIDUserClientLogger` | 0x38 | AIDLogger |
| `AppleHIDTransportIODataQueue` | 0x30 | IOSharedDataQueue → IODataQueue |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000042ff off=0x00538f60-0x0053d25f addr=0xfffffe000753cf60-0xfffffe000754125f r--/r--   __TEXT            
	sz=0x00002e4a off=0x00539628-0x0053c472 addr=0xfffffe000753d628-0xfffffe0007540472               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000070 off=0x0053c480-0x0053c4f0 addr=0xfffffe0007540480-0xfffffe00075404f0               __TEXT.__const            
	sz=0x00000d6f off=0x0053c4f0-0x0053d25f addr=0xfffffe00075404f0-0xfffffe000754125f               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001c16c off=0x02047d50-0x02063ebc addr=0xfffffe000904bd50-0xfffffe0009067ebc r-x/r-x   __TEXT_EXEC       
	sz=0x0001b9cc off=0x02047d50-0x0206371c addr=0xfffffe000904bd50-0xfffffe000906771c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000007a0 off=0x0206371c-0x02063ebc addr=0xfffffe000906771c-0xfffffe0009067ebc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000470 off=0x0494e310-0x0494e780 addr=0xfffffe000b952310-0xfffffe000b952780 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0494e310-0x0494e3d8 addr=0xfffffe000b952310-0xfffffe000b9523d8               __DATA.__data             
	sz=0x000003a8 off=0x00000000-0x000003a8 addr=0xfffffe000b9523d8-0xfffffe000b952780               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00005158 off=0x01121f68-0x011270c0 addr=0xfffffe0008125f68-0xfffffe000812b0c0 rw-/rw-   __DATA_CONST      
	sz=0x00000090 off=0x01121f68-0x01121ff8 addr=0xfffffe0008125f68-0xfffffe0008125ff8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000090 off=0x01121ff8-0x01122088 addr=0xfffffe0008125ff8-0xfffffe0008126088         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000041f0 off=0x01122088-0x01126278 addr=0xfffffe0008126088-0xfffffe000812a278         __DATA_CONST.__const            
	sz=0x000006c0 off=0x01126278-0x01126938 addr=0xfffffe000812a278-0xfffffe000812a938         __DATA_CONST.__kalloc_type      
	sz=0x000002d0 off=0x01126938-0x01126c08 addr=0xfffffe000812a938-0xfffffe000812ac08         __DATA_CONST.__kalloc_var       
	sz=0x000003d0 off=0x01126c08-0x01126fd8 addr=0xfffffe000812ac08-0xfffffe000812afd8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e8 off=0x01126fd8-0x011270c0 addr=0xfffffe000812afd8-0xfffffe000812b0c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 273 at 0x04add9cc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CDA60AB0-1FEE-3175-AA06-B4B3054E087B
008: LC_SOURCE_VERSION           10110.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa5bc0 size=0x4b0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleInputDeviceSupport`
- `CFBundleIdentifier`: `com.apple.driver.AppleInputDeviceSupport`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleInputDeviceSupport`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `"Copyright © 2016 Apple Inc. All rights reserved. [AppleInputDeviceSupport_kexts-10110.1]"`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleInputDeviceSupport.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900322464`
- `_PrelinkExecutableRelativePath`: `AppleInputDeviceSupport`
- `_PrelinkExecutableSize`: `154163`
- `_PrelinkExecutableSourceAddr`: `-2198900322464`
- `_PrelinkKmodInfo`: `-2198828932336`

## Strings (426) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/Logger/AIDLoggerUserClient.cpp`
- `212221111122`
- `Write`
- `12111111111112`
- `AIDLoadMs`
- `_canClearImage`
- `_formattedName`
- `121111121222121211111111111112`
- `12111112122212121111111111111111122222222`
- `Performance`
- `downloaders`
- `dataIdentifierMap->getCount() > 0`
- `States`
- `[%s::%s]: Sending event %s to CA kernel service.`
- `1211111112122111221`
- `FDR Classes`
- `image4Ret == kImage4ReturnSuccess`
- `verified == true`
- `Traffic`
- `[%s::%s]: group: '%s' subgroup: '%s' categories: 0x%04X`
- `_fieldReporters->time`
- `[%s::%s]: Added state %s[%c%c%c%c%c%c%c%c]`
- `data`
- `updateReportersGroupData`
- `clearReporterData`
- `\n`
- `AIDFirmwareUpdateService`
- `%s::%s() Total Time Taken For Kernel Client's to complete: %llu ms\n`
- `roleObj`
- `writeSharedMemoryFifo`
- `site.AIDEventLogger`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/Reporter/AIDReporters.cpp`
- `%s[%p]::%s() Boot-arg present, skipping firmware validation\n`
- `%s[%p]::%s() kFWValidationFailed: %u\n`
- `%s[%p]::%s() No loadFDRDataComplete callback registered\n`
- `site.AIDImageDownloader`
- `_workloop`
- `[%s::%s]: Created shared memory buffer: slaveAddr=0x%08llX, size=%llu, optionBits=0x%04X`
- `Created`
- `map`
- `FDR Data Identifiers`
- `roleKey`
- `Mask`
- `site.AIDLogger`
- `%s[%p]::%s() Exiting with status = 0x%x \n`
- `Peripheral`
- `12111211112211`
- `AIDReporterState::Channel`
- `_stateIds`
- `Re-used`
- `AIDReporterSimple`
- `unknown error`
- `_ucLogger`
- `%s_%s_time`
- `AIDCircularWriteBufferShared`
- `size`
- `_afuLock`
- `ClearReportID`
- `Ns`
- `TicksPerSecond`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/AIDSharedMemoryManager.cpp`
- `iommuParents`
- `sharedMemoryFifoSlaveAddress`
- `%s[%p]::%s() status = 0x%x, Disabling event source\n`
- `_loadFDRDataCompleteCallback`
- `[%s::%s]: ERROR!! Unknown category: %s`
- `channels`
- `statesData`
- `_logger`
- `[%s::%s]: %s shared memory %s FIFO: slaveAddress=0x%08llX, totalCapacity=%u, fifoId=%d`
- `fdrClass`
- `%s::%s() Total Time Taken For User Space Request to complete: %llu ms\n`
- `_clearReportPayload`
- `12111112122212121111111111111`
- `createSharedMemory`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/Reporter/AIDReporterSimple.cpp`
- `BitMask`
- `AIDSerialLogger`
- `_firmwareMap`
- `AbsoluteValues`
- `initReporter`
- `channelInfo`
- `_stateNames`
- `_readMemoryFifos`
- `nameValue`
- `signatureType == kNoSignature`
- `registerNotificationPort`
- `iter`
- `nameKey`
- `Simple`
- `site.AppleHIDTransportIODataQueue`
- `AIDEventLogger`
- `FWValidated`
- `rkosftab`
- `AIDLoggerUserClient`
- `matching`
- `ValidationTimeMs`
- `1`
- `site.AIDSharedMemoryManager`
- `_mappers`
- `site.AIDQueueEventSourceWorkItem`
- `12111111`
- `returnValue == kIOReturnSuccess`
- `_reporterDataMD`
- `_firmwareDescriptor`
- `initWithTask`
- `[%s::%s]: ERROR!! Unknown memory type %u`
- `[%s::%s]: Setting up matching notifier for %s`
- `12`
- `AIDLog: `
- `_reportOffset`
- `_numChannels > 0`
- `_reporterSet`
- `slaveMemoryBuffer`
- `_workLoop`
- `_cachedEventNames`
- `aid-cache-logs-size`
- `SubgroupName`
- `fwBuffer`
- `start`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/Reporter/AIDReporterState.cpp`
- `genericMapperIdx < _mappers->getCount()`
- `inputMD`
- `incrementKey`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `AIDFirmwareDecodeImage4(_firmwareBuffer, tag, this)`
- `Field`
- `_reporter`
- `b`
- `%s_totalTime`
- `12111211`
- `type`
- `_beginFDRDataDownloadCallback`
- `ReportID`
- `image-tag`
- `site.AIDLoggerUserClient`
- `[%s::%s]: ERROR!! Unknown unit '%s'`
- `site.AIDCircularWriteBufferShared`
- `data->getLength() >= _dataLength`
- `_beginFirmwareDownloadCallback`
- `it`
- `AHTLoaderName`
- `site.OSObject*`
- `_channels`
- `Offset`
- `initWithService`
- `_coreAnalyticsService`
- `%s[%p]::%s() Invalid map\n`
- `Type`
- `Unit`
- `com.apple.afu.userclientaccess`
- `AIDLogger`
- `AIDLog (%s): `
- `Image Tag`
- `loadFirmware`
- `createSharedMemoryFifo`
- `validateFirmwareGated`
- `tag`
- `addDefaultProxyConfig`
- `aid-next-load-options`
- `1211111112122111122121`
- `virtual IOReturn AIDFirmwareUpdateUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `1221`
- `%s::%s() Performing img4 validation outside of workloop\n`
- `%s[%p]::%s() commandSleep interrupted, validateImage4Completed = %s\n`
- `%s[%p]::%s() No FDR data received\n`
- `ClearReportPayload`
- `AIDStartMs`
- `ret == 0 `
- `sharedMemory`
- `readSharedMemoryFifo`
- `fdrClassBuffer`
- `init()`
- `%s.%s.%s`
- `channelArray`
- `fdr-data-identifier`
- `AIDQueueEventSourceWorkItem`
- `com.apple.hid.firmware.userclientaccess`
- `TX`
- `performCustomValidation`
- `fdrDataIdentifier`
- `AIDNextLoadOptions`
- `sharedMemoryFifo`
- `circularBuffer`
- `_subgroup`
- `12111112122212121111`
- `Name`
- `loadFDRData`
- `_cachedEvents`
- `site.AIDCircularBuffer`
- `site.AIDSerialLogger`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/Reporter/AIDReporter.cpp`
- `classesOnly`
- `[%s::%s]: Added field channel %s with id %llu`
- `sharedMemoryFifoBufferSize`
- `boolRet`
- `[%s::%s]: Added channel %s with id %llu size %u and offset %u`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `%s[%p]::%s() commandSleep waitResult = %d, validateImage4Completed = %s\n`
- `reporterInfo`
- `ioRet == 0 `
- `fifoMapperIdx < _mappers->getCount()`
- `[%s::%s]: Failed to cast CoreAnalyticsHub`
- `site.AIDReporters`
- `payloadReturn`
- `AIDImageDownloadersCreated`
- `Ms`
- `init`
- `mapper`
- `site.AIDCircularBufferShared`
- `%s[%p]::%s() Invalid _firmwareBuffer\n`
- `status == kIOReturnSuccess`
- `loadFDRDataComplete`
- `GroupName`
- `createLogQueue`
- `updateReportWithData`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateUserClient.cpp`
- `matchingDict`
- `OSBoundedPtr.h`
- `_firmwareBuffer`
- `%s::%s() Time Taken For IMG4 Validation: %llu ms\n`
- `%s[%p]::%s() kFWValidationSuccess \n`
- `site.FieldReporters`
- `[%s::%s]: Found CoreAnalyticsHub`
- `getValue`
- `updateReportersData`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareUpdateService.cpp`
- `%s[%p]::%s() commandSleep awakened, validateImage4Completed = %s\n`
- `_customTagValidationCallbackContext`
- `ProxyInterface`
- `AIDInterface`
- `_writeMemoryFifos`
- `AIDCircularBufferShared`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `%s::%s(): Calling external handler for manifest tag 0x%08x\n`
- `1211111212221212111111111111111112222222221111212`
- `iokt`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `%s_totalTransitions`
- `set`
- `findSlaveProcessorWithRole`
- `121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `Size`
- `_group`
- `AIDImageDownloader`
- `downloader`
- `[%s::%s]: ERROR!! Invalid type %u`
- `%s[%p]::%s() Return value from inputMD->prepare(): %d\n`
- `!_reporter`
- `incrementValue`
- `skip-image-loading`
- `imageTag || fdrClasses`
- `unitStr`
- `initWithIommuParentProvider`
- `fdrData`
- `true`
- `%s::%s(): Unhandled manifest tag 0x%08x\n`
- `%s[%p]::%s() No FDR callback registered\n`
- `categoriesArray`
- `name`
- `[%s::%s]: Added channel %s with id %llu offset %u ticks %llu and lastStateIncluded %u`
- `_coreAnalyticsMatchNotifer`
- `eventName`
- `AIDCircularBuffer`
- `AIDReporters`
- `%s[%p]::%s() Invalid _firmwareDescriptor\n`
- `%s[%p]::%s() Only non signed FDR data supported\n`
- `[%s::%s]: ERROR!! %s, %s file: %s, line: %d, value: 0x%08X`
- `121111121222121211111`
- `1211121`
- `UserSpaceRequestTimeMs`
- `AIDFirmwareDecodeImage4`
- `result`
- `site.AIDService`
- `AppleHIDTransportIODataQueue`
- `site.Channel*`
- `site.AIDInterface`
- `site.AIDFirmwareUpdateUserClient`
- `success`
- `_commandGate`
- `ticks`
- `addIOReporter`
- `com.apple`
- `AIDUserClientLogger`
- `false`
- `validateImage4`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/FirmwareUpdate/AIDFirmwareImage4.cpp`
- `addChannel`
- `_slaveProcessor`
- `121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `_customTagValidationCallback`
- `_reportID`
- `clientMemoryForType`
- `stateName`
- `_fieldChannelIds`
- `logEvent`
- `site.AIDReporterSimple`
- `interface`
- `createReporterData`
- `B16@?0^{OSObject=^^?i}8`
- `%s_%s_transitions`
- `mask`
- `groupIter`
- `site.AIDUserClientLogger`
- `RX`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `validationComplete`
- `ReportOffset`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/AIDService.cpp`
- `coreAnalyticsNotificationHandlerGated`
- `eventPayload`
- `validateFirmware`
- `Counter`
- `%s() Validation Successful for payload:%p with length:%u\n`
- `fdr-classes`
- `LoadingGroup`
- `AIDFirmwareUpdateUserClient`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/Reporter/AIDEventLogger.cpp`
- `mt-strings`
- `%s[%p]::%s() No FDR class received\n`
- `121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `_userAccess`
- `bufferLengthIn > classLengthIn`
- `CoreAnalyticsHub`
- `site.AIDFirmwareUpdateService`
- `KernelClientRequestTimeMs`
- `121111111212211`
- `SetReportPayload`
- `_numStates > 0`
- `site.Channel`
- `%s[%p]::%s() Entering \n`
- `_isCustomValidationNeeded`
- `setMapperConfig`
- `%s \n`
- `updateReport`
- `%s[%p]::%s() %s is working asynchronously\n`
- `service`
- `AIDLastLoadOptions`
- `owningTask`
- `LastStateIncluded`
- `AIDSharedMemoryManager`
- `offset`
- `ret`
- `mt-bytes`
- `Need FUD Download`
- `IOUserClientClass`
- `1211111212221212111111111111111`
- `Read`
- `Power`
- `AIDQueueEventSource`
- `Increment`
- `[%s::%s]: ERROR!! Could not create a driver logging queue`
- `AIDReporterState`
- `Channels`
- `AIDReporter`
- `peekSharedMemoryFifo`
- `site.AIDCircularReadBufferShared`
- `AIDLog: %s\n`
- `AIDUserClient`
- `sharedMemoryFifoTotalSize`
- `skipFWValidation`
- `%s[%p]::%s() commandSleep timed out, validateImage4Completed = %s\n`
- `site.AIDReporter`
- `Categories`
- `ReportLength`
- `kids`
- `AIDCircularReadBufferShared`
- `%s[%p]::%s() Cannot create fdrClassBuffer\n`
- `121112`
- `fifo`
- `12111`
- `FWValidationNotRequired == false`
- `site.AIDQueueEventSource`
- `%s[%p]::%s() Cannot create fdrData\n`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleInputDeviceSupport/AIDImageDownloader.cpp`
- `_image`
- `AIDService`
- `11`
- `%s Task not privileged \n`
- `_service`
- `%s[%p]::%s() Invalid _firmwareMap\n`
- `_clearReportID`
- `_fieldReporters`
- `site.AIDUserClient`
- `reporter`
- `logEventWithFullName`
- `_setReportPayload`
- `site.AIDReporterState`
- `Us`
- `_mappers->getCount() > 0`
- `domainName`
- `channel->type != kChannelTypeUnknown`
- `aid-cache-logs`
- `\"%s\" @%s:%d`
- `_validateImage4TES`
- `_fieldReporters->transitions`
- `%s[%p]::%s() bufferLength must be > classLength (%u > %u)\n`
- `%s[%p]::%s() Cannot create fdrClass\n`
- `fullEventName`
- `configureReport`
- `reporters`
- `State`
- `ClearReportZeroPad`

**[__TEXT.__os_log]**

- `Using non-FTAB FW`
- `Unknown validation status %u. Image loading not permitted`
- `%s, %s file: %s, line: %d, value: 0x%08X`
- `Using FTAB tag 0x%08X`
- `Skipping validation on image loading`
- `FDR data validation failed`
- `FDR class '%s' not associated to any property. Ignoring data.`
- `[HID] %s`
- `AIDImageDownloaders already created. Reusing them.`
- `FDR class '%s' assigned to property '%s'`
- `Tag: '%c%c%c%c' Options: 0x%08X`
- `FDR class is null`
- `[%s][%s] %s`
- `Invalid property in FDR classes`
- `Skipping FTAB tag 0x%08X`
- `Trying to load an image that couldn't be validated`
- `Unserializing payload with %u bytes`
- `FDR data is null`
- `Cannot assign FDR class: '%s' (%u bytes) to property '%s'`
- `FDR data for class '%s' (%u bytes) assigned to property '%s'`
- `Cannot add FDR class '%s' to array`
- `Parsing FTAB with %u file entries`
- `Extracting FTAB offset 0x%X size 0x%X`

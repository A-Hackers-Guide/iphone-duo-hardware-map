# `com.apple.driver.AppleMultitouchDriver`

- Name: AppleMultitouchDriver
- Version: `1010.4`
- UUID: `CDA12802-62D4-3FFD-B669-1B05BB4CED72`
- Source version: `10110.4.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 12.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) | `AppleMultitouchTimestampSync` | `timestamp-sync` |

## IOKit personalities (5) [KC]

### AppleMultitouchHIDService (0x0D,0x00)
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchDriver`
- `DefaultMultitouchProperties`:
  - `MT Built-In`: `True`
  - `parser-options`: `16`
  - `parser-type`: `1`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `0`
    - `DeviceUsagePage`: `13`
- `IOClass`: `AppleMultitouchHIDService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMultitouchDriver`
- `IOProbeScore`: `1500`
- `IOProviderClass`: `IOHIDInterface`
- `Manufacturer`: `Apple`

### AppleMultitouchHIDService (0x0D,0x04)
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchDriver`
- `DefaultMultitouchProperties`:
  - `HIDServiceSupport`: `True`
  - `IOCFPlugInTypes`:
    - `0516B563-B15B-11DA-96EB-0014519758EF`: `AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin`
  - `MT Built-In`: `True`
  - `parser-options`: `16`
  - `parser-type`: `1`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `13`
- `IOClass`: `AppleMultitouchHIDService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMultitouchDriver`
- `IOProviderClass`: `IOHIDInterface`
- `Manufacturer`: `Apple`

### AppleMultitouchHIDService (0x0D,0x20)
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchDriver`
- `DefaultMultitouchProperties`:
  - `HIDServiceSupport`: `True`
  - `IOCFPlugInTypes`:
    - `0516B563-B15B-11DA-96EB-0014519758EF`: `AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin`
  - `MT Built-In`: `True`
  - `Timestamp Sync`: `True`
  - `parser-options`: `16`
  - `parser-type`: `4`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `32`
    - `DeviceUsagePage`: `13`
- `IOClass`: `AppleMultitouchHIDService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMultitouchDriver`
- `IOProbeScore`: `1500`
- `IOProviderClass`: `IOHIDInterface`
- `Manufacturer`: `Apple`

### AppleMultitouchTimestampSync
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchDriver`
- `IOClass`: `AppleMultitouchTimestampSync`
- `IONameMatch`:
  - `timestamp-sync`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMultitouchDriver`
- `IOProviderClass`: `IOService`

### MTUserDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `7`
    - `DeviceUsagePage`: `65376`
- `IOClass`: `AppleMultitouchHIDService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleMultitouchDriver`
- `IOProviderClass`: `IOHIDInterface`


## C++ classes (14) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AMDTimestampSyncMgr` | 0x40 |  |
| `AppleMultitouchDevice` | 0xe8 | IOService → IORegistryEntry |
| `AppleMultitouchDeviceUserClient` | 0x178 | IOUserClient → IOService → IORegistryEntry |
| `AppleMultitouchEventDriverV2Wrapper` | 0x20 | AppleMultitouchEventDriverWrapper |
| `AppleMultitouchEventDriverWrapper` | 0x18 |  |
| `AppleMultitouchEventServiceWrapper` | 0x20 | AppleMultitouchEventDriverWrapper |
| `AppleMultitouchHIDEventDriver` | 0x110 | IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleMultitouchHIDEventDriverV2` | 0x148 | IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleMultitouchHIDEventService` | 0xc8 | IOHIDEventService → IOService → IORegistryEntry |
| `AppleMultitouchHIDService` | 0xd8 | IOService → IORegistryEntry |
| `AppleMultitouchTimestampSync` | 0xd8 | IOService → IORegistryEntry |
| `AppleMultitouchTimestampSyncLock` | 0x30 | AppleARMFunction |
| `AppleMultitouchTimestampSyncUC` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `HIDAlwaysNotifyingIODataQueue` | 0x30 | IOSharedDataQueue → IODataQueue |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000666b off=0x0067e8c0-0x00684f2b addr=0xfffffe00076828c0-0xfffffe0007688f2b r--/r--   __TEXT            
	sz=0x000001a8 off=0x0067efe0-0x0067f188 addr=0xfffffe0007682fe0-0xfffffe0007683188               __TEXT.__const            
	sz=0x000022d4 off=0x0067f188-0x0068145c addr=0xfffffe0007683188-0xfffffe000768545c               __TEXT.__cstring          (CstringLiterals)
	sz=0x00003acf off=0x0068145c-0x00684f2b addr=0xfffffe000768545c-0xfffffe0007688f2b               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001c734 off=0x022c0960-0x022dd094 addr=0xfffffe00092c4960-0xfffffe00092e1094 r-x/r-x   __TEXT_EXEC       
	sz=0x0001c0b4 off=0x022c0960-0x022dca14 addr=0xfffffe00092c4960-0xfffffe00092e0a14          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000680 off=0x022dca14-0x022dd094 addr=0xfffffe00092e0a14-0xfffffe00092e1094          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000351 off=0x049823a8-0x049826f9 addr=0xfffffe000b9863a8-0xfffffe000b9866f9 rw-/rw-   __DATA            
	sz=0x000000ca off=0x049823a8-0x04982472 addr=0xfffffe000b9863a8-0xfffffe000b986472               __DATA.__data             
	sz=0x00000270 off=0x00000000-0x00000270 addr=0xfffffe000b986478-0xfffffe000b9866e8               __DATA.__common           (Zerofill)
	sz=0x00000011 off=0x00000000-0x00000011 addr=0xfffffe000b9866e8-0xfffffe000b9866f9               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00005438 off=0x0117a770-0x0117fba8 addr=0xfffffe000817e770-0xfffffe0008183ba8 rw-/rw-   __DATA_CONST      
	sz=0x00000058 off=0x0117a770-0x0117a7c8 addr=0xfffffe000817e770-0xfffffe000817e7c8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000058 off=0x0117a7c8-0x0117a820 addr=0xfffffe000817e7c8-0xfffffe000817e820         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000043d8 off=0x0117a820-0x0117ebf8 addr=0xfffffe000817e820-0xfffffe0008182bf8         __DATA_CONST.__const            
	sz=0x00000280 off=0x0117ebf8-0x0117ee78 addr=0xfffffe0008182bf8-0xfffffe0008182e78         __DATA_CONST.__kalloc_var       
	sz=0x000008c0 off=0x0117ee78-0x0117f738 addr=0xfffffe0008182e78-0xfffffe0008183738         __DATA_CONST.__kalloc_type      
	sz=0x00000340 off=0x0117f738-0x0117fa78 addr=0xfffffe0008183738-0xfffffe0008183a78         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000130 off=0x0117fa78-0x0117fba8 addr=0xfffffe0008183a78-0xfffffe0008183ba8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 246 at 0x04ae0760
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CDA12802-62D4-3FFD-B669-1B05BB4CED72
008: LC_SOURCE_VERSION           10110.4.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aab3d0 size=0x2e8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleMultitouchDriver`
- `CFBundleGetInfoString`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleMultitouchDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.4`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `193.8`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleMultitouchDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898988864`
- `_PrelinkExecutableRelativePath`: `AppleMultitouchDriver`
- `_PrelinkExecutableSize`: `165160`
- `_PrelinkExecutableSourceAddr`: `-2198898988864`
- `_PrelinkKmodInfo`: `-2198828719192`

## Strings (543) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `PowerControlSupported`
- `removeFramesClient`
- `[0x%llx][%llx][%s::%s]: [AppleMultitouchDevice::_initializeCachedReportInfo] Re-initializing report cache`
- `mt-bytes`
- `Multitouch CPU stats`
- `createLogQueue`
- `[0x%llx][%llx][%s::%s]: Getting Parser enabled/disabled state`
- `WirelessChargingNotificationSupported`
- `setPowerState`
- `Critical Errors Timestamp`
- `setPowerStateGated`
- `AppleMultitouchTimestampSyncLock`
- `AMDReporter`
- `site.AppleMultitouchEventDriverV2Wrapper`
- `createReporters`
- `[AMDTimestampSyncMgr::%s]: Timestamp sync %u (host %u) received (version: %u) with timestamp %ums (offset: %lldms)`
- `[0x%llx][%llx][%s::%s]: Timed out enqueuing frame after %u ms`
- `SPI`
- `RX`
- `112111122`
- `Category`
- `site.AppleMultitouchHIDEventService`
- `Error: length received %llu is greater than request %d\n`
- `12111112122212121111111111112`
- `Frames dropped`
- `clientMemoryForType`
- `StatePacketOrder`
- `AnimationThresholds`
- `DeviceUsagePairs`
- `DisableIOReporting`
- `site.AppleMultitouchDevice`
- `AppleMultitouchDriver.kext/Contents/PlugIns/MultitouchHID.plugin`
- `Timestamp Sync Pulse Width`
- `initWithTargetDataAndSymbol`
- `[0x%llx][%llx][%s::%s]: Re-initializing report cache`
- `ChannelName`
- `getPowerState`
- `_setMaxInjectionSize`
- `AdapterDetails`
- `site.AMDReporterManager`
- `site.AMDHandlersStruct`
- `createDataQueue`
- `AMDNonOpaqueReporter`
- `_registerUserClient`
- `VersionNumber`
- `parseDescriptorCommon`
- `AppleMultitouchHIDService::notifyClientsAction(%d)`
- `AppleMultitouchHIDService::simpleSetReport() for reportID 0x%02x, length %d`
- `buildMTDevice`
- `ForceSupported`
- `AppleMultitouchHIDEventDriverV2`
- `Endianness`
- `unknown`
- `Sensor Surface Width`
- `AppleMultitouchTimestampSync`
- `12111112122212121111111111111222222222111111122`
- `Invalid Reason`
- `_handleCriticalErrorsFrame`
- `Multitouch high level stats`
- `MTPowerStatsDescriptor`
- `[0x%llx][%llx][%s::%s]: %s Parser`
- `SerialNumber`
- `Drop packets`
- `site.uint64_t`
- `Multitouch`
- `MT`
- `[AMDTimestampSyncMgr::%s]: Timestamp sync driver found`
- `Timestamp Sync`
- `willTerminate`
- `[0x%llx][%llx][%s::%s]: %u bytes`
- `site.AppleMultitouchTimestampSync`
- `issueDriverRequest`
- `LocationID`
- `site.ExpansionData`
- `injectFrame`
- `121111121222121211111121111`
- `AppleMultitouchHIDService::getMultitouchReportInfo() reportID 0x%02x`
- `AppleMultitouchHIDEventDriverV2::setMultitouchReport() reportID 0x%02x, length %d`
- `121221`
- `_sendNotificationToUserClients`
- `cache-critical-errors`
- `checkBridgeStatusMessage`
- `mt-strings`
- `AppleMultitouchPowerStats`
- `registerNotificationPort`
- `[0x%llx][%llx][%s::%s]: Send : %u`
- `decodeDeviceProperty`
- `VendorID`
- `Multitouch Subdevice ID`
- `IOPMPowerSource`
- `AppleMultitouchHIDEventDriverV2::simpleGetReport() for reportID 0x%02x, length %d completed`
- `_resetDevice`
- `sendNotificationToUserClients`
- `initWithTask`
- `PacketFormat`
- `SendSleepMessage`
- `EnumerationReasonString`
- `IOCFPlugInTypes`
- `newMultitouchProperties`
- `Ready at start`
- `IOUserClientClass`
- `ProductID`
- `Critical Errors Accumulator`
- `1211`
- `AppleMultitouchEventServiceWrapper`
- `AppleMultitouchHIDService::simpleGetReport() for reportID 0x%02x, length %d completed`
- `AppleMultitouchHIDEventDriverV2::simpleGetReport() for reportID 0x%02x, length %d`
- `site.AMDTimestampSyncMgr`
- `[0x%llx][%llx][%s::%s]: %s`
- `[0x%llx][%llx][%s::%s]: Injection max packet size already equal or bigger (%u >= %u)`
- `Sensor Surface Height`
- `filteredClientsAvailable`
- `LastStateIncluded`
- `Multitouch Serial Number`
- `_deviceGetReportWithLookUp`
- `wireless-charging-notfication`
- `Sensor Rows`
- `site.AppleMultitouchEventDriverWrapper`
- `121`
- `MultitouchCriticalErrorBit%lu`
- `site.AppleMultitouchCriticalErrorsReporter`
- `12111`
- `111112`
- `sleep`
- `[0x%llx][%llx][%s::%s]: id:0x%llx %s %s(%d)`
- `function-reset`
- `AppleMultitouchHIDEventDriverV2::getMultitouchReport() reportID 0x%02x, length %d`
- `Timestamp Sync Count`
- `AppleMultitouchEventDriverWrapper`
- `HIDAlwaysNotifyingIODataQueue`
- `DummyID`
- `_parseDescriptor`
- `AutoSuspend`
- `AppleMultitouchHIDService::getMultitouchReport() reportID 0x%02x, length %d`
- `Error: setReport() returned 0x%08X for reportID 0x%02X\n`
- `touch-size-id`
- `[0x%llx][%llx][%s::%s]: Error: In AppleMultitouchDevice::_deviceGetReportWithLookUp, mtReportID %d is invalid.`
- `Sensor Region Param`
- `site.AppleMultitouchPowerStats`
- `site.AppleMultitouchTimestampSyncUC`
- `121111`
- `State`
- `_createReporter`
- `matchingNotificationGated`
- ` %02X`
- `Ns`
- `AppleMultitouchHIDService`
- `[AppleMultitouchHIDEventDriverV2::handleInterruptReport reportID:%d (%d bytes)]`
- `Unknown`
- `AMDReporterManager`
- `ResetCount`
- `registerUserClient`
- `Product`
- `11211121`
- `[0x%llx][%llx][%s::%s]: Setting System Force Response%s`
- `site.AppleMultitouchEventServiceWrapper`
- `[AppleMultitouchHIDService::handleInterruptReport reportID:%d (%d bytes)]`
- `Build at start`
- `12111222`
- `off`
- `Sensor Columns`
- `UseProviderWorkLoop`
- `_readDescriptor`
- `enqueueLog`
- `TicksPerSecond`
- `site.AMDOpaqueReporter`
- `getReport`
- `_deviceSetReportWithLookUp`
- `ReportInterval`
- `BluetoothLowEnergy`
- `[0x%llx][%llx][%s::%s]: Sending notification to all user clients`
- `GroupName`
- `notifyClients`
- `MaintainPowerInUILock`
- `matchingNotification`
- `Transport`
- `setPreferences`
- `function-timestamp_sync`
- `enqueueData`
- `States`
- `ActivationThresholds`
- `FamilyCode`
- `processReport`
- `11111111111111`
- `SPU`
- `FirstPowerOffSuppressed`
- `Type`
- `charger-state-interested`
- `BuildAMDWithMTInit`
- `Unrecognized reportID 0x%02X\n`
- `mt-device-id`
- `Max Packet Size`
- `\n`
- `FilterEnabled`
- `Enable`
- `maintain-power`
- `BuildAMDAtStart`
- `AMDTimestampSyncMgr`
- `AppleUSBMultitouch.kext/Contents/PlugIns/MultitouchHID.plugin`
- `addFramesClient`
- `ParserDisabled`
- `Opaque`
- `site.AppleMultitouchDeviceUserClient`
- `SupportReportInfo`
- ` filtered`
- `_cacheDeviceProperties`
- `callPlatformFunction`
- `site.AMDNonOpaqueReporter`
- `[0x%llx][%llx][%s::%s]: Dropping frame because the queue is full`
- `AppleMultitouchDevice`
- `start`
- `[0x%llx][%llx][%s::%s]: WARNING!! User client array size %u is larger than kMaxUserClientsCount %u, touch frame packets will get dropped for exceeding clients`
- `Sensor Region Descriptor`
- `lock`
- `[AMDTimestampSyncMgr::%s]: ERROR: Unsupported timestamp version %u and/or size %u`
- `[0x%llx][%llx][%s::%s]: id:0x%llx %s(%d)`
- `DefaultMultitouchProperties`
- `AppleMultitouchHIDEventDriverV2::getMultitouchReportInfo() reportID 0x%02x`
- `Input Report`
- `ApplePreferencesDefaultPreferences`
- `VendorIDSource`
- `Dummy`
- `updateReport`
- `Ms`
- `Multitouch ID`
- `[0x%llx][%llx][%s::%s]: mtReportID 0x%02x has status 0x%02x. Report not valid`
- `_initializeCachedReportInfo`
- `1`
- `[0x%llx][%llx][%s::%s]: size %d`
- `AppleMultitouchHIDService::enableMultitouchEvents(%s)`
- `AppleMultitouchHIDService::simpleGetReport() for reportID 0x%02x, length %d`
- `simpleSetReport`
- `Max Injection Packet Size`
- `Error: getReport() returned 0x%08X for reportID 0x%02X\n`
- `site.AMDReporter*`
- `Sensor Surface Descriptor`
- `[0x%llx][%llx][%s::%s]: Set device power`
- `[0x%llx][%llx][%s::%s]: Setting a max packet size of %u for injection`
- `FrameEnqueueTimeout`
- `0516B563-B15B-11DA-96EB-0014519758EF`
- `1211111212221212111111121`
- `12111112122212121111111211111122111111211`
- `[AMDTimestampSyncMgr::%s]: ERROR: Cannot create ts matching dictionary`
- `1211111212221212111111111111`
- `Disable`
- `[0x%llx][%llx][%s::%s]: Get device power`
- `com.apple.hid.multitouch.user-access`
- `stop`
- `resetDevice`
- `bInterfaceID`
- `mtlog (%s): `
- `Power`
- `[AMDTimestampSyncMgr::%s]: ERROR: super::init failed`
- `[0x%llx][%llx][%s::%s]: (%d, %d, 0x%08X)`
- `Family ID`
- `ForceResponse`
- `getMultitouchReportInfo`
- `TouchType`
- `[AMDTimestampSyncMgr::%s]: ERROR: Cannot add ts matching notification`
- `[0x%llx][%llx][%s::%s]: `
- `_getFeatureReportInfo`
- `setSendsFrames`
- `Unit`
- `AMDOpaqueReporter`
- `should-sleep`
- `Z2Init`
- `mtlog: %s\n`
- `site.AppleMultitouchHIDService`
- `site.HIDAlwaysNotifyingIODataQueue`
- `setReport`
- `TX`
- `Field`
- `on`
- `simpleGetReport`
- `ExtendedFeatures`
- `callFunction`
- `[0x%llx][%llx][%s::%s]: Unsupported request %d`
- `1211111212221212111111121111112211`
- `orb-activation-thresholds`
- `AppleMultitouchHIDEventDriverV2::simpleSetReport() for reportID 0x%02x, length %d`
- `Enabling`
- `TransitionCountLengthBytes`
- `1212221122`
- `112`
- `IOClass`
- `_sendLogToUserClients`
- `site.const ReporterDescriptor*`
- `configureReport`
- `site.CommonDescriptor`
- `checkMTDeviceAvailable`
- `unregisterUserClient`
- `timerAction`
- `[0x%llx][%llx][%s::%s]: Resetting device`
- `asyncTaskAction`
- `121112`
- `Manufacturer`
- `DisablerPresent`
- `121111121222121212221112122`
- `unlock`
- `Traffic`
- `createPowerSource`
- `site.AMDEventDriverState`
- `AppleMultitouchDeviceUserClient`
- `AppleMultitouchHIDEventService`
- `Reporters`
- `Bluetooth`
- `true`
- `parseDescriptor`
- `AppleMultitouchHIDService::setMultitouchReport() reportID 0x%02x, length %d`
- `MultitouchPreferences`
- `Critical Errors`
- `AppleMultitouchTimestampSyncUC`
- `Last Timestamp Sync`
- `Us`
- `1112`
- `terminateMTDevice`
- `AppleMultitouchHIDEventDriver`
- `CountryCode`
- `force-supported`
- `site.AMDUserClientState`
- `MTPowerStatsDisable`
- `Timestamp Sync Period`
- `Performance`
- `orb-animation-thresholds`
- `CriticalErrors`
- `handlePointerEventFromDevice`
- `SubgroupName`
- `site.AppleMultitouchHIDEventDriver`
- `IsFake`
- `USB`
- `TrackpadMomentumScroll`
- `false`
- `AppleMultitouchEventDriverV2Wrapper`
- `12122212221`
- `SendChargerNotifications`
- `Disabling`
- `site.AppleMultitouchHIDEventDriverV2`
- `AppleMultitouchHIDEventDriverV2::enableMultitouchEvents(%s)`
- `EnumerationReason`
- `_handleTouchFrame`
- `MouseMomentumScroll`
- `resetGated`
- `[0x%llx][%llx][%s::%s]: Setting auto suspend`
- `NonOpaque`
- `initWithAMDAndEndianness`
- `FIFO`
- `bcdVersion`
- `site.AppleMultitouchTimestampSyncLock`
- `Peripheral`
- `PreferenceFilter`
- `[AppleMultitouchHIDService] Start succeeded\n`
- `_createReporters`
- `DurationCountLengthBytes`

**[__TEXT.__os_log]**

- `[HID] [%s] [Error] %s Invalid signature 0x%08X\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] %s is not entitled\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - packet parsing only supports 8 bytes per data point for transitions into a state\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't start multitouch handler\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Can't add event source to work loop\n`
- `[HID] [%s] [Error] %s Failed to add reporter legend for group <%s> and subgroup <%s>\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not get the memory descriptor for the data queue\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] IOHIDInterface::open() returned false\n`
- `[HID] [%s] %s::%s [0x%llx] Status: External Reset and InitDone\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Cannot create iterator for clients\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not create new MT handler\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Unknown async task: %u\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _getFeatureReportInfo returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Cannot create notification queue\n`
- `[HID] [%s] [Error] %s::%s Cannot create _reportersArray\n`
- `[HID] [%s] %s GPIO asserted when system is trying to sleep. Waiting to finish the pulse.\n`
- `[HID] [%s] %s::%s [0x%llx] Setting System Force Response : %s [%s:%d]\n`
- `[HID] [%s] [Error] %s::%s Failed to increment state (%lld) for channel (%lld) (ret=0x%X)\n\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ERROR - OVERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: wrong subgroup index %u in reporter %u\n`
- `[HID] [%s] %s GPIO asserted when trying to lock. Sleeping...\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing subgroup name in the descriptor\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Not hid interface: %p\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to run multitouchDeviceWillTerminate\n`
- `[HID] [%s] %s Timestamp sync %u (host %u) received (version: %u) with timestamp %ums (offset: %lldms)\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate userClientIterator\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Report length for reportID 0x%02x is 0\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ***** Multitouch Status: value=0x%08lX *****\n`
- `[HID] [%s] [Error] %s::%s Failed to add channel %llu (ret=0x%X)\n`
- `[HID] [%s] %s::%s [0x%llx] Async task : %u\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ERROR - Invalid length : Report struct [ID:0x%02x] length [%u] is larger than max buffer size [%zu]\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to update IOReporter before power is disabled (err=0x%X)\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing group name in the descriptor\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing packet width per element for transition in power state\n`
- `[HID] [%s] [Error] %s::%s Failed to get 0x%X report (ret=0x%X)\n`
- `[HID] [%s] %s::%s Creating AMD Reporter Manager\n`
- `[HID] [%s] [Error] %s::%s Reporter instance creation returned null\n`
- `[HID] [%s] [Error] %s Failed to add channel for <%s>\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] getPowerEnabled returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] userClient is invalid argument\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Payload for rDEVICE_BASIC_INFO is smaller than expected\n`
- `[HID] [%s] [Error] %s::%s IOReport power stats not available (0x%08x)\n`
- `[HID] [%s] [Error] %s::%s Error 0x%08x getting power stat report\n`
- `[HID] [%s] [Error] %s No params in ARM function\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] failed\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _userClientState->clients\n`
- `[HID] [%s] %s Timestamp sync reset with %ums period, %ums pulse width and %u capture count\n`
- `[HID] [%s] %s setPowerState %u.\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] data length is 0\n`
- `[HID] [%s] [Error] %s::%s AMDReporter Log - Unsupported reporter unit %s\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing ticks per second in the descriptor\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - State reporter creation failed \n`
- `[HID] [%s] [Error] %s::%s Failed to add state <%s> (ret=0x%X)\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not cast our provider into appropriate device class\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _userClientState->wantFramesCountLock\n`
- `[HID] [%s] %s::%s [0x%llx] Status: PSoCWDTFired\n`
- `[HID] [%s] %s stop\n`
- `[HID] [%s] [Error] %s::%s AMDReporter Log - No unit field found in descriptor\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing packet width per element for duration in power state\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter - Failed to get 0x%X report (ret=0x%X)\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Cannot queue notification\n`
- `[HID] [%s] [Error] %s runAction returned 0x%08X\n`
- `[HID] [%s] %s::%s [0x%llx] Successfully started\n`
- `[HID] [%s] %s::%s [0x%llx] [AppleMultitouchDevice::willTerminate]\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] invalid type in registerNotificationPort\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] unknown memory type in clientMemoryForType()\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] data is NULL\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Notification queue not available\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't get default multitouch properties\n`
- `[HID] [%s] [Error] %s Cannot add ts matching notification\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ERROR - UNDERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n`
- `[HID] [%s] %s::%s [0x%llx] ***** Multitouch Status: value=0x%08lX ts=0x%08llX *****\n`
- `[HID] [%s] [Error] %s::%s Cannot allocate power stats descriptor\n`
- `[HID] [%s] %s GPIO locked trying to assert. Retrying in %ums\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing states - index dictionary in the descriptor\n`
- `AppleMultitouchHIDService::updateNoiseAvoidanceGated failed to set noise avoidance state: 0x%08x`
- `[HID] [%s] [Error] %s Failed to create IOSimpleReporter\n`
- `[HID] [%s] [Error] %s Invalid timestampsync matched\n`
- `[HID] [%s] %s::%s [0x%llx] Status: GoodByeWorld\n`
- `[HID] [%s] [Error] %s Invalid power state %llu\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] createDataQueue returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - packet parsing only supports 8 bytes per data point for duration in a state\n`
- `[HID] [%s] [Error] %s::%s Failed to add report legend (ret=0x%X)\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to find default preferences\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _getFeatureReportInfo returned result 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _provider is NULL\n`
- `[HID] [%s] [Error] %s::%s Invalid power stats report size\n`
- `[HID] [%s] %s Unlocking timestamp sync GPIO\n`
- `[HID] [%s] [Error] %s Cannot allocate ARM function\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing channel name in the descriptor\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] IOPMPowerSource::registerInterest() returned NULL\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't attach multitouch handler\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] setPowerEnabled returned error 0x%x\n`
- `[HID] [%s] %s::%s [0x%llx] Status: Power on Reset and InitDone\n`
- `[HID] [%s] [Error] %s::%s Unknown descriptor version %u\n`
- `[HID] [%s] [Error] %s::%s Cannot create IOStateReporter\n`
- `[HID] [%s] %s Locking timestamp sync GPIO\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] could not create a driver logging queue\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Error - missing reporter type in descriptor. Look into modifying Reporters in plist\n`
- `thread_call_allocate returned NULL`
- `[HID] [%s] [Error] %s Unsupported timestamp version %u and/or size %u\n`
- `[HID] [%s] %s::%s [0x%llx] Status: Reset\n`
- `[HID] [%s] %s::%s [0x%llx] Status: Watchdog Reset and InitDone\n`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: invalid size\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] registerUserClient returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't copy default multitouch properties\n`
- `[HID] [%s] [Error] %s Timestamp sync already matched\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failing start\n`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: 0 states in reporter %u\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] failed to get hid interface\n`
- `[HID] [%s] [Error] %s::%s No reporters found in descriptor\n`
- `[HID] [%s] [Error] %s super::init failed\n`
- `[HID] [%s] %s start\n`
- `[HID] [%s] [Error] %s Sleep pending but gpio not asserted!!!\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _dataQueue does not exist\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not initialize MT properties dictionary\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X for reportID 0x%02X\n\n`
- `[HID] [%s] %s::%s [0x%llx] Enumerate MT\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] mtReportID 0x%x is invalid\n`
- `[HID] [%s] %s::%s [0x%llx] Entered\n`
- `[HID] [%s] [Error] %s::%s Cannot create _reportersSet\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter - Type parsed is %d, this is unsupported - only type state reporter is supported at the moment\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - enter counts set report failed\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] super::start failed\n`
- `Host operational state : TouchOnAndNormal`
- `Host operational state : Sleeping`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: wrong channel id index %u in reporter %u\n`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: wrong ticks per second index %u in reporter %u\n`
- `[HID] [%s] [Error] %s data length %u\n`
- `[HID] [%s] %s::%s [0x%llx] Setting Parser : %s [%s:%d]\n`
- `[HID] [%s] %s::%s AMD Reporter - generic updateReport called\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to get device initialized state. Result = 0x%08x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _userClientState->filters\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] resetDevice returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Error: reportID 0x%02X is %ld bytes long\n`
- `[HID] [%s] %s Woken up after GPIO deasserted\n`
- `[HID] [%s] [Error] %s::%s Failed to create state reporter\n`
- `[HID] [%s] [Error] %s::%s Missing states array in the descriptor\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X\n`
- `AppleMultitouchHIDService::_systemPowerChangeHandler: Failed with error 0x%08x`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not get notifiers\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't add user client to list of clients\n`
- `[HID] [%s] [Error] %s::%s Error 0x%08x adding channel 0x%016llx to reporter\n`
- `[HID] [%s] [Error] %s target is not a TimestampSync object\n`
- `[HID] [%s] [Error] %s::%s Failed to get IOPMPowerSource after 2 seconds, this should never happen!\n`
- `[HID] [%s] %s::%s [0x%llx] Init received, terminating the current instance of AMD.\n`
- `[HID] [%s] %s::%s [0x%llx] Nothing to do\n`
- `[HID] [%s] [Error] %s Cannot create ts matching dictionary\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _appleMultitouchDeviceExpansionData->_cachedReportInfoLock\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to set extended features property to 0x%lX\n`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: wrong state id index %u in state %u of reporter %u\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _logQueue does not exist\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to run multitouchDeviceDidStart\n`
- `[HID] [%s] [Error] %s::%s Invalid descriptor: 0 reporters\n`
- `[HID] [%s] [Error] %s calling to super failed\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Failed to add report legend (ret=0x%X)\n`
- `[HID] [%s] %s Timestamp sync driver found\n`
- `AppleMultitouchHIDService::updateNoiseAvoidanceGated ignoring unchanged noise avoidance state (existing state: %x)`
- `[HID] [%s] [Error] %s::%s [0x%llx] Failed to create default Multitouch properties\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _injectionMemory in clientMemoryForType\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Missing packet format dictionary in the descriptor\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Failed to add channel %llu (ret=0x%X)\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _userClientState->logBufferLock\n`
- `[HID] [%s] %s Pulse finished. Acknowledging setPowerState\n`
- `[HID] [%s] [Error] %s No functionOut\n`
- `[HID] [%s] [Error] %s::%s Reporter type %d is not supported\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] start failed\n`
- `[HID] [%s] %s::%s entered\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] createPowerSource() returned NULL\n`
- `[HID] [%s] [Error] %s::%s Empty descriptor\n`
- `[HID] [%s] [Error] %s::%s Error 0x%08x incrementing channel 0x%0llx state 0x%0llx\n\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _dataQueue in createDataQueue\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] could not get the memory descriptor for the data queue\n`
- `[HID] [%s] %s::%s AMD Reporter - generic configureReport called\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - duration set report failed\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not allocate _userClientState->clientsLock\n`
- `[HID] [%s] [Error] %s::%s Error 0x%08x setting state id 0x%016llx in channel 0x%016llx\n`
- `[HID] [%s] [Error] %s::%s Cannot add reporter legend\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Log - Failed to increment state (%lld) for channel (%lld) (ret=0x%X)\n\n`
- `AppleMultitouchHIDService::noiseAvoidanceChangeNotification battery status changed`
- `[HID] [%s] [Error] %s::%s Reporter Plist is missing Touch Type field in the descriptor\n`
- `[HID] [%s] %s::%s [0x%llx] Entered stop\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Can't decode unknown reportID 0x%02x\n`
- `[HID] [%s] %s::%s [0x%llx] Status: Firmware Reset and InitDone\n`
- `[HID] [%s] [Error] %s param3 is not OSData\n`
- `[HID] [%s] [Error] %s::%s AMD Reporter Error - Currently AMDReporters of type %s are not supported, only state reporters are supported\n`
- `AppleMultitouchHIDService::updateNoiseAvoidanceGated setting noise avoidance state: %x`
- `[HID] [%s] [Error] %s::%s [0x%llx] getMultitouchReport returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] getMultitouchReportInfo returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Error: reportID 0x%02X is %ld bytes long, %ld bytes remaining\n`

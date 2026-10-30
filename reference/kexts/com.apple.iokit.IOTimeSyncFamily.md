# `com.apple.iokit.IOTimeSyncFamily`

- Name: IOTimeSyncFamily
- Version: `1510.9`
- UUID: `C123A368-6C4C-3AC0-A7DC-17C0512BCAC6`
- Source version: `1510.9.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 2.0, [`com.apple.iokit.IOSkywalkFamily`](com.apple.iokit.IOSkywalkFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 10.0.0d1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 10.0.0d1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 10.0.0d1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 10.0.0d1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 20.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### IOTimeSyncClockManager
- `CFBundleIdentifier`: `com.apple.iokit.IOTimeSyncFamily`
- `IOClass`: `IOTimeSyncClockManager`
- `IOMatchCategory`: `IOTimeSyncClockManager`
- `IOPersonalityPublisher`: `com.apple.iokit.IOTimeSyncFamily`
- `IOProbeScore`: `0`
- `IOProviderClass`: `IOTimeSyncRootService`
- `IOUserClientClass`: `IOTimeSyncClockManagerUserClient`

### IOTimeSyncRootService
- `CFBundleIdentifier`: `com.apple.iokit.IOTimeSyncFamily`
- `IOClass`: `IOTimeSyncRootService`
- `IOMatchCategory`: `IOTimeSyncRootService`
- `IOPersonalityPublisher`: `com.apple.iokit.IOTimeSyncFamily`
- `IOProbeScore`: `0`
- `IOProviderClass`: `IOResources`


## C++ classes (41) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOTimeSyncClockManager` | 0x148 | IOService → IORegistryEntry |
| `IOTimeSyncClockManagerUserClient` | 0x140 | IOUserClient → IOService → IORegistryEntry |
| `IOTimeSyncClockMapping` | 0x20 |  |
| `IOTimeSyncClockTestUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |
| `IOTimeSyncDaemonClientBase` | 0xb0 | IOService → IORegistryEntry |
| `IOTimeSyncDaemonServiceBase` | 0x98 | IOService → IORegistryEntry |
| `IOTimeSyncEdgeTimeCapture` | 0x1b8 | IOService → IORegistryEntry |
| `IOTimeSyncEdgeTimeCaptureUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `IOTimeSyncFilteredService` | 0x138 | IOTimeSyncService → IOService → IORegistryEntry |
| `IOTimeSyncIntervalFilter` | 0xd0 |  |
| `IOTimeSyncIntervalFilter128` | 0xd0 |  |
| `IOTimeSyncIntervalFilterIIR` | 0xf8 | IOTimeSyncIntervalFilter |
| `IOTimeSyncIntervalFilterIIR128` | 0x118 | IOTimeSyncIntervalFilter128 |
| `IOTimeSyncNanosecondSnapshotService` | 0x188 | IOTimeSyncFilteredService → IOTimeSyncService → IOService → IORegistryEntry |
| `IOTimeSyncPersistentUserClockMapping` | 0x28 |  |
| `IOTimeSyncRootService` | 0x88 | IOService → IORegistryEntry |
| `IOTimeSyncService` | 0x100 | IOService → IORegistryEntry |
| `IOTimeSyncServiceDaemonClient` | 0xb8 | IOTimeSyncDaemonClientBase → IOService → IORegistryEntry |
| `IOTimeSyncSyncDaemonClient` | 0xb8 | IOTimeSyncDaemonClientBase → IOService → IORegistryEntry |
| `IOTimeSyncSyncUserClient` | 0x148 | IOUserClient → IOService → IORegistryEntry |
| `IOTimeSyncTimeLineFilter` | 0x128 |  |
| `IOTimeSyncTimeLineFilter128` | 0x1a8 |  |
| `IOTimeSyncTimeLineFilterIIR` | 0x130 | IOTimeSyncTimeLineFilter |
| `IOTimeSyncTimeLineFilterIIR128` | 0x1b0 | IOTimeSyncTimeLineFilter128 |
| `IOTimeSyncTimedEdgeGenerator` | 0xc0 | IOService → IORegistryEntry |
| `IOTimeSyncTimedEdgeGeneratorUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `IOTimeSyncTranslationMach` | 0x100 | IOTimeSyncService → IOService → IORegistryEntry |
| `IOTimeSyncTranslationPMGR` | 0x180 | IOTimeSyncFilteredService → IOTimeSyncService → IOService → IORegistryEntry |
| `IOTimeSyncUserClient` | 0x148 | IOUserClient → IOService → IORegistryEntry |
| `IOTimeSyncUserFilteredService` | 0x138 | IOTimeSyncFilteredService → IOTimeSyncService → IOService → IORegistryEntry |
| `IOTimeSyncUserFilteredServiceUserClient` | 0x150 | IOTimeSyncUserClient → IOUserClient → IOService → IORegistryEntry |
| `TSNAssistedInterface` | 0x1d0 | TSNInterface → IOService → IORegistryEntry |
| `TSNBSDInterface` | 0x238 | TSNAssistedInterface → TSNInterface → IOService → IORegistryEntry |
| `TSNBSDStackInterface` | 0x238 | TSNBSDInterface → TSNAssistedInterface → TSNInterface → IOService → IORegistryEntry |
| `TSNBSDTestInterface` | 0x258 | TSNBSDStackInterface → TSNBSDInterface → TSNAssistedInterface → TSNInterface → IOService → IORegistryEntry |
| `TSNITimeSyncHandler` | 0x28 |  |
| `TSNInterface` | 0x1c8 | IOService → IORegistryEntry |
| `TSNPacketPool` | 0xf8 |  |
| `TSNUserWiFiControlInterface` | 0xc8 | TSNWiFiControlInterface → IOService → IORegistryEntry |
| `TSNWiFiControlInterface` | 0xa0 | IOService → IORegistryEntry |
| `TSNWiFiInterface` | 0x248 | TSNBSDInterface → TSNAssistedInterface → TSNInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000d418 off=0x00aef7f0-0x00afcc08 addr=0xfffffe0007af37f0-0xfffffe0007b00c08 r--/r--   __TEXT            
	sz=0x00003eb8 off=0x00aeff58-0x00af3e10 addr=0xfffffe0007af3f58-0xfffffe0007af7e10               __TEXT.__cstring          (CstringLiterals)
	sz=0x00008c04 off=0x00af3e10-0x00afca14 addr=0xfffffe0007af7e10-0xfffffe0007b00a14               __TEXT.__os_log           
	sz=0x000001e8 off=0x00afca20-0x00afcc08 addr=0xfffffe0007b00a20-0xfffffe0007b00c08               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00031460 off=0x035e2190-0x036135f0 addr=0xfffffe000a5e6190-0xfffffe000a6175f0 r-x/r-x   __TEXT_EXEC       
	sz=0x00030c50 off=0x035e2190-0x03612de0 addr=0xfffffe000a5e6190-0xfffffe000a616de0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000810 off=0x03612de0-0x036135f0 addr=0xfffffe000a616de0-0xfffffe000a6175f0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000791 off=0x04a199b0-0x04a1a141 addr=0xfffffe000ba1d9b0-0xfffffe000ba1e141 rw-/rw-   __DATA            
	sz=0x000000d0 off=0x04a199b0-0x04a19a80 addr=0xfffffe000ba1d9b0-0xfffffe000ba1da80               __DATA.__data             
	sz=0x00000688 off=0x00000000-0x00000688 addr=0xfffffe000ba1da80-0xfffffe000ba1e108               __DATA.__common           (Zerofill)
	sz=0x00000039 off=0x00000000-0x00000039 addr=0xfffffe000ba1e108-0xfffffe000ba1e141               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x0000dba0 off=0x01425b08-0x014336a8 addr=0xfffffe0008429b08-0xfffffe00084376a8 rw-/rw-   __DATA_CONST      
	sz=0x00000100 off=0x01425b08-0x01425c08 addr=0xfffffe0008429b08-0xfffffe0008429c08         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000100 off=0x01425c08-0x01425d08 addr=0xfffffe0008429c08-0xfffffe0008429d08         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000c510 off=0x01425d08-0x01432218 addr=0xfffffe0008429d08-0xfffffe0008436218         __DATA_CONST.__const            
	sz=0x00000d40 off=0x01432218-0x01432f58 addr=0xfffffe0008436218-0xfffffe0008436f58         __DATA_CONST.__kalloc_type      
	sz=0x00000280 off=0x01432f58-0x014331d8 addr=0xfffffe0008436f58-0xfffffe00084371d8         __DATA_CONST.__kalloc_var       
	sz=0x00000408 off=0x014331d8-0x014335e0 addr=0xfffffe00084371d8-0xfffffe00084375e0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000c0 off=0x014335e0-0x014336a0 addr=0xfffffe00084375e0-0xfffffe00084376a0         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x014336a0-0x014336a8 addr=0xfffffe00084376a0-0xfffffe00084376a8         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 282 at 0x04af8fc8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C123A368-6C4C-3AC0-A7DC-17C0512BCAC6
008: LC_SOURCE_VERSION           1510.9.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac7f90 size=0x728
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOTimeSyncFamily`
- `CFBundleGetInfoString`: `IOTimeSyncFamily 1510.9, Copyright © 2010-2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.iokit.IOTimeSyncFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOTimeSyncFamily`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1510.9`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1510.9`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `IOTimeSyncFamily 1510.9, Copyright © 2010-2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `500.10`
- `OSBundleLibraries_x86_64`:
  - `com.apple.iokit.IONetworkingFamily`: `2.0`
  - `com.apple.iokit.IOSkywalkFamily`: `1.0`
  - `com.apple.kpi.bsd`: `10.0.0d1`
  - `com.apple.kpi.iokit`: `10.0.0d1`
  - `com.apple.kpi.libkern`: `10.0.0d1`
  - `com.apple.kpi.mach`: `10.0.0d1`
  - `com.apple.kpi.private`: `20.0`
- `OSBundleRequired`: `Network-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOTimeSyncFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894331920`
- `_PrelinkExecutableRelativePath`: `IOTimeSyncFamily`
- `_PrelinkExecutableSize`: `314281`
- `_PrelinkExecutableSourceAddr`: `-2198894331920`
- `_PrelinkKmodInfo`: `-2198828099152`

## Strings (731) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `handler != nullptr`
- `NULL == mapping`
- `121111121222121211111111111111111111211111`
- `function-perf_cycle_count`
- `orderedLookup->getCount() > 0`
- `com.apple.DriverKit-AppleBCMWLAN`
- `link layer`
- `packet->_packetIndex < _numberOfPacketsInPool`
- `matchDict != nullptr`
- `_ifnet != nullptr`
- `site.IOTimeSyncClockManagerUserClient`
- `1222`
- `ClockIdentifier`
- `ClockLockState`
- `1211112122222111111111122111112`
- `_availablePacketList != nullptr`
- `com.apple.private.timesync.clocksync`
- `NULL == fUserFilteredClocks`
- `clockManager->nextAvailableDynamicClockID(&fClockIdentifier) != 0`
- `12122`
- `unknown`
- `status`
- `MaximumPulseActiveTime`
- `com.apple.TimeSync.outstanding-packets`
- `result`
- `macAddress != nullptr`
- `numberOfRanges > 0`
- `timesync_rx_delay_threshold_ms`
- `announce`
- `count < (UINT32_MAX - 1)`
- `NULL == fIOTimeSyncServiceLock`
- `121111121222121211122111`
- `site.TSNInterface`
- `superResult == true`
- `1211122222222222222222222222221211222`
- `_timeSyncPacketPool != nullptr`
- `fSyncClients`
- `WARNING: `
- `TSNBSDTestInterface`
- `site.IOTimeSyncIntervalFilterIIR`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncService.cpp`
- `local-clock`
- `FilterShift`
- `packetData != nullptr`
- `site.IOTimeSyncEdgeTimeCapture`
- `IOTimeSyncTime`
- `_callbackThreadLock != nullptr`
- `_timeSyncTransmitHandlers != nullptr`
- `fPersistentUserFilteredClocks->getObject(userID)`
- `1212212212222222222222222222222`
- `12111112122212121111111111111121`
- `_stateLock != nullptr`
- `site.TSNLinkStateContext`
- `fProvider`
- `com.apple.private.timesync.clock-testing`
- `setInterfaceState`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncNanosecondSnapshotService.cpp`
- `InterfaceName`
- `1211111212221212111111111111111122111111`
- `!superStarted`
- `TSNWiFiControlInterface`
- `_translationService`
- `site.TSNWiFiControlInterface`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncServiceDaemonClient.cpp`
- `_availablePacketListHead != nullptr`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncFilteredService.cpp`
- `fTSNInterfaceMatchedNotifier != nullptr`
- `com.apple.AppleSunriseWLAN`
- `IOTimeSyncIntervalFilter`
- `0x%016llx`
- `TSNPacketPool.cpp`
- `numberOfPacketsInPool >= MIN_PACKET_COUNT`
- `superStarted == true`
- `timesync_untimestamped_general`
- `timesync_tsnotifytest`
- `121111121222121212112221211222221211112111121111222222211`
- `site.IOTimeSyncUserFilteredService`
- `BSD Name`
- `fAsyncCallbackSetLock != nullptr`
- `NULL == fTimeSyncWorkLoop`
- `LinkActive`
- `112`
- `tsnPacket->packetLength() >= packetLength`
- `[%04lu]:`
- `%u.%u.%u.%u @ %02x:%02x:%02x:%02x:%02x:%02x`
- `followup`
- `NULL == fUserClients`
- `site.TSNPacketPool`
- `numberOfSegments >= 1`
- `site.IOTimeSyncDaemonServiceBase`
- `121111121222121211112111111221112222112`
- `NULL == fTSNCaptureLock`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNAssistedInterface.cpp`
- `NULL == fIOTimeSyncService`
- `NULL == userID`
- `fEthernetController`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncDaemonClient.cpp`
- `getTransmitTimestamp(packet, &timestamp) == kIOReturnSuccess`
- `IOTimeSyncIntervalFilterIIR`
- `super::init() == true`
- `!startDone`
- `sync`
- `12111112122212121111211111122111`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGenerator.cpp`
- `NULL == fDynamicClockIDReferences`
- `IOTimeSyncIntervalFilterIIR128`
- `121111`
- `site.IOTimeSyncUserFilteredServiceUserClient`
- `121111121222121211112111111221112222112111222222`
- `true`
- `timesync_rand_pdelay_range_ms`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManagerUserClient.cpp`
- `com.apple.private.timesync.tsn-capture`
- `MachAbsoluteTimeSnapshot`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimeLineFilter.cpp`
- `site.IOTimeSyncTimedEdgeGeneratorUserClient`
- `packetLength >= sizeof(TSNUDPv4Header)`
- `packetLength >= sizeof(TSNUDPv6Header)`
- `IOTimeSyncNanosecondSnapshotService`
- `IOTimeSyncTimedEdgeGenerator`
- `site.IOTimeSyncSyncDaemonClient`
- `12122122122222222222222222222222222`
- `IOTimeSyncTranslationMach`
- `site.TSNAssistedInterface`
- `SetMACAddress_Impl`
- `timesync_max_jitter`
- `outputMbuf != nullptr`
- `NULL == fTimeDomainSnapshotTimer`
- `rangeCount != nullptr`
- `numberOfSegments <= TSNMaxRangeCount`
- `AppleUSBNCMData`
- `IOBufferCopyController`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacket.cpp`
- `_packets != nullptr`
- `clockManager`
- `clockManagerLoader`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiInterface.cpp`
- `inst != nullptr`
- `12`
- `ClockName`
- `12111222222222222222222222222212112221`
- `NULL == clockID`
- `NULL == newService`
- `NULL == fUserClientsLock`
- `maxSegmentLengths != nullptr`
- `NominalDomainInterval`
- `found == true`
- `packet != nullptr`
- `12111112122212121112211`
- `bsdInterface != nullptr`
- `fLock`
- `IOTimeSyncUserFilteredService`
- `NULL == fIOTimeSyncDaemonServiceBase`
- `resultB != kIOReturnSuccess`
- `MACAddress`
- `NULL == fPersistentUserFilteredClocks`
- `childIterator != nullptr`
- `IOTimeSyncFilteredService`
- `TSNInterface`
- `_timeSyncTransmitHandlersLock != nullptr`
- `TimeSyncTimeCoreAudioClockDomain`
- `site.IOTimeSyncPersistentUserClockMapping`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationMach.cpp`
- `IOTimeSyncSyncDaemonClient`
- `_interface != nullptr`
- `IOTimeSyncTimeLineFilterIIR`
- `site.TSNITimeSyncHandler`
- `IOTimeSyncEdgeTimeCapture`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNPacketPool.cpp`
- `InterfaceState`
- `IOTimeSyncUserClient`
- `AppleBCMWLAN`
- `site.TSNIPacketEntry`
- `NULL == fgPTPLock`
- `12112`
- `12111112122212121111`
- `err == 0`
- `NULL == fIOTimeSyncClockManager`
- `%s%hu`
- `gPTPPresent`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserFilteredService.cpp`
- `IOTimeSyncRootService`
- `com.apple.private.timesync.edge-generate`
- `site.TSNUserWiFiControlInterface`
- `mbuf != nullptr`
- `pdelay response followup`
- `NominalTimeSyncInterval`
- `_controlInterface != nullptr`
- `timesync_rand_pdelay_base_ms`
- `site.IOTimeSyncTimeLineFilter`
- `IOTimeSyncTimeLineFilter128`
- `site.IOTimeSyncEdgeTimeCaptureUserClient`
- `NULL == fUserFilteredClocksLock`
- `_mbufPattern != nullptr`
- `debug`
- `1211111212221212121122212112222212111121111211112222222111111121222222211`
- `IOTimeSyncTime.cpp`
- `site.IOTimeSyncClockMapping`
- `TransmittedEgressUntimestampedCounter`
- `UDPv6`
- `!fPersistentUserFilteredClocks->setObject(userID, mapping)`
- `signal`
- `site.IOTimeSyncService`
- `TimeSyncTime is mach_absolute_time nanoseconds\n`
- `startDone`
- `_startStopLock != nullptr`
- `IOTimeSyncIntervalFilter128`
- `site.IOTimeSyncServiceDaemonClient`
- `site.IOTimeSyncClockTestUserClient`
- `IOTimeSyncDaemonClientBase`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCaptureUserClient.cpp`
- `12111112122212121122222212121111111112111`
- `site.TSNBSDInterface`
- `tsnPacket != nullptr`
- `TSNITimeSyncHandler`
- `IOTimeSyncEdgeTimeCaptureUserClient`
- `0 == nominalMachInterval`
- `IOTimeSyncClockMapping`
- `Unknown`
- `\"INTERNAL PANIC: %s(%s): Received mbuf(%p) with invalid timestamp flag, timestamp %llu\" @%s:%d`
- `firstHostTime`
- `stop`
- `result == kIOReturnSuccess`
- `TSNUserWiFiControlInterface`
- `<unreadable>`
- `1211111212221212111122222222222222222222222222222222212`
- `timesync_log`
- `NULL == fMappingLock`
- `mbufPacket`
- `_metaDataMemoryBuffer != nullptr`
- `IOTimeSyncTranslationPMGR`
- `site.TSNBSDStackInterface`
- `NULL == fIOService`
- `1211111212221212111`
- `AppleThunderboltIPPort`
- `%02x:%02x:%02x:%02x:%02x:%02x`
- `pcieCounterTime`
- `_metaDataMemoryMap != nullptr`
- `12111112122212121111111111111111111111211`
- `pdelay response`
- `superStarted`
- `resultA != kIOReturnSuccess`
- `MinimumPulseActiveTime`
- `IOUserClientClass`
- `IOTimeSyncClockManager`
- `NULL == clockIdentifier`
- `NULL == clockIDNum`
- `AppleCentauriAlpha`
- `UntimestampedGeneralMessageMask`
- `childDone == true`
- `TSNBSDStackInterface`
- `site.TSNPacketPoolListEntry`
- `site.IOTimeSyncRootService`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/DriverKitKernelSupport/TSNUserWiFiControlInterface.cpp`
- `_packetMemoryBuffer[i] != nullptr`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockManager.cpp`
- `NULL == fAsyncCallbackSetLock`
- `%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x @ %02x:%02x:%02x:%02x:%02x:%02x`
- `Locking`
- `NULL == fStartStopLock`
- `NULL == fDaemonClientsLock`
- `KERN_SUCCESS == kern_result`
- `IOBuiltin`
- `IOMACAddress`
- `IOTimeSyncTimeLineFilter`
- `bsdPrefix != nullptr`
- `_timeSyncReceiveHandlers != nullptr`
- `fTimestampLock != NULL`
- `IOTimeSyncServiceDaemonClient`
- `translationStatus == kIOReturnSuccess`
- `NULL == fClockIDMappingReferences`
- `_timeSyncTransmitPacketQueueLock != nullptr`
- `IOEthernetInterface`
- `AppleSunriseWLAN`
- `error == 0 `
- `NULL == fProvider`
- `12111112122212121`
- `free`
- `callback`
- `site.IOTimeSyncTimeLineFilterIIR`
- `timesync_ts_mode`
- `callback != nullptr`
- `0 == nominalClockInterval`
- `TransmittedEgressTimedFailedCounter`
- `NULL == clockManager`
- `com.apple.private.timesync.ppmoffset`
- `status != 0`
- `NULL == fPersistentUserFilteredClocksLock`
- `-timesync_bringup`
- `*rangeCount >= _metaData->numberOfRanges`
- `timesync`
- `site.IOTimeSyncNanosecondSnapshotService`
- `1211111212221212111111111`
- `1211111212221212111111111111112`
- `IOTimeSyncClockTestUserClient`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTranslationPMGR.cpp`
- `NULL == fTimeLineFilter`
- `resources != nullptr`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncUserClient.cpp`
- `site.IOTimeSyncIntervalFilter`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncClockTestUserClient.cpp`
- `site.IOTimeSyncSyncUserClient`
- `IOTimeSyncTimeLineFilterIIR128`
- `client`
- `DOWN`
- `segmentLengths != nullptr`
- `com.apple.private.timesync.direct-userclient`
- `WantsgPTPServices`
- `NULL == fIOTimeSyncClockManagerLock`
- `ranges != nullptr`
- `CFBundleIdentifier`
- `site.IOTS_U128`
- `_availableListLock != nullptr`
- `site.TSNWiFiInterface`
- `childResult == true`
- `fSyncClientsLock`
- `site.IOTimeSyncTranslationMach`
- `1211111212221212121122212112222212111121111211112222222111`
- `UP`
- `thisStatus == kIOReturnSuccess`
- `121111121222121212112221211222221211112111121111222222211111112122222222222`
- `callbackRef != nullptr`
- `121111121222121211111111111111`
- `com.apple.private.timesync.edge-capture`
- `NULL == fFilterLock`
- `121112222222222222222222222222222222222222222212112221`
- `site.IOTimeSyncUserClient`
- `skywalkPacket != nullptr`
- `%lluHz`
- `BSDPrefix`
- `!mapping->init(userID, *clockID)`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonServiceBase.cpp`
- `BSDUnitNumber`
- `found == false`
- `site.IOTimeSyncService::ExpansionData`
- `\"out of packets in pool\" @%s:%d`
- `NULL == fSnapshotWorkLoop`
- `Adaptive`
- `timesync_rand_pdelay_period`
- `result != 0`
- `fIOTimeSyncService != nullptr`
- `IO80211Interface`
- `IOTimeSyncService`
- `provider != nullptr`
- `11`
- `ClockTransportType`
- `!result`
- `packetLength >= sizeof(TSNEthernetHeader)`
- `1211111212221212111221`
- `parsePacketInfo(packet, packetType, messageType, addressString, messageHeader, bufferSize)`
- `NominalMachInterval`
- `orderedLookup != nullptr`
- `numberOfRanges <= TSNMaxRangeCount`
- `com.apple.driver.AppleCentauriAlpha`
- `NULL == fTranslationService`
- `IOTimeSyncDaemonServiceBase`
- `12111222222222222222222222222222222222222222221211222`
- `NULL == properties`
- `timestamp != nullptr`
- `site.IOTimeSyncFilteredService`
- `init`
- `NULL == newValue`
- `\"INTERNAL PANIC: Double complete of TSNPacket at index %lu, num outstanding: %llu\" @%s:%d`
- `TimeSyncTime is ARM PMGR counter\n`
- `fTranslationService != NULL`
- `site.IOTimeSyncIntervalFilterIIR128`
- `IOTimeSyncUserFilteredServiceUserClient`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncSyncUserClient.cpp`
- `_interfaceName != nullptr`
- `instanceIndex >= NUMBER_OF_AVB_INSTANCES`
- `kIOReturnSuccess != removeUserFilteredClock(*clockID)`
- `error != ENOBUFS`
- `TSNBSDInterface.cpp`
- `fSyncClients != nullptr`
- `NULL == fCoreAudioClockDomainMappings`
- `12122122122222222222222222`
- `site.IOTimeSyncDaemonClientBase`
- `site.IOTimeSyncTimeLineFilter128`
- `_infoLock != nullptr`
- `result == true`
- `IOTimeSyncPersistentUserClockMapping`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNBSDInterface.cpp`
- `TransmittedEgressTimedCounter`
- `fSyncClientsLock != nullptr`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncDaemonClientBase.cpp`
- `timesync_local`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNInterface.cpp`
- `_timeSyncPacketPool`
- `NULL == fClockIDLock`
- `site.IOTimeSyncIntervalFilter128`
- `packetentry->inUse == true`
- `TSNAssistedInterface`
- `_packetMemoryMap[i] != nullptr`
- `result != nullptr`
- `IOTimeSyncTimedEdgeGeneratorUserClient`
- `packet->packetLength() >= mbuf_len(mbuf)`
- `TransmittedEgressTimedSuccededCounter`
- `Locked`
- `site.TSNPacket`
- `NULL == fNFInterfaceMatchedNotifier`
- `IOTimeSyncSyncUserClient`
- `TSNWiFiInterface`
- `fExpansionStruct`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncEdgeTimeCapture.cpp`
- `NULL == fDaemonClients`
- `IOTimeSyncClockManagerUserClient`
- `1211111212221212111121111112211122221121112222222`
- `NULL == fAFilter`
- `OutstandingPackets`
- `TranslationClockID`
- `false`
- `TimeSyncTimeClockID`
- `delay request`
- `Failed to get AppleARMFunction\n`
- `_timeSyncReceiveHandlersLock != nullptr`
- `allocatePacketPool`
- `NULL == fDynamicLock`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/TimeSensitiveNetworking/TSNWiFiControlInterface.cpp`
- `delay response`
- `site.IOTimeSyncTranslationPMGR`
- `inst->init(macAddress, bsdPrefix, bsdUnitNumber, interfaceType, timestampingSupport, builtin, nullptr)`
- `%s`
- `pdelay request`
- `site.IOTimeSyncTimeLineFilterIIR128`
- `matching != nullptr`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncTimedEdgeGeneratorUserClient.cpp`
- `UDPv4`
- `SupportsRepeating`
- `_timeSyncPacketPool->init(TIMESYNC_POOL_SIZE, 1, &maxSegmentLength, _packetMapper) == true`
- `\"Failed to get PMGR Counter AppleARMFunction\\n\" @%s:%d`
- `site.TSNBSDTestInterface`
- `WantsTSNCapture`
- `TimeToLock`
- `TSNPacketPool`
- `/Library/Caches/com.apple.xbs/0419396C-BF26-4435-923C-0CDDBDC5B2A6/TemporaryDirectory.UzO7lS/Sources/TimeSync_kext/IOTimeSyncFamily/IOTimeSyncRootService.cpp`
- `_timeSyncReceivePacketQueueLock != nullptr`
- `packetEntry != nullptr`
- `site.IOTimeSyncClockManager`
- `timesync_panic`
- `\"INTERNAL PANIC: %s(%s): Received mbuf(%p) with 0 timestamp, valid flag set\" @%s:%d`
- `secondHostTime`
- `machStatus == kIOReturnSuccess`
- `Not Locking`
- `NULL == matching`
- `err == 0 `
- `fReferenceCount < 0`
- ` %02x`
- `TSNBSDInterface`
- `site.IOTimeSyncTimedEdgeGenerator`
- `Builtin`
- `12111112122212121211222121122222121111211112111122222221111111212222222`
- `NULL == fEntityIDLookupCall`
- `12111112122212121111111111111111111121111`
- `userClient != nullptr`
- `NULL == fBFilter`
- `fClientLock`

**[__TEXT.__os_log]**

- `clockIdentifier argument must be non-NULL\n`
- `Nominal clock period is 0\n`
- `  %s(%s): Removed MBUF callback`
- `  %s(%s): Error: invalid time when trying to convert wake time\n`
- `  %s(%s): ERROR has not overriden transmitTimeSyncPacket() or is incorrectly calling super`
- `failed to allocate persistent user clocks lock\n`
- `Mach average has overflowed 0x%016llx.%016llx\n`
- `  %s(%s): Skip egress timestamp request for general messages, mask 0x%x\n`
- `  %s(%s): reinitializeFilter %u, %llu, %llu\n`
- `+ %s`
- `%s\n`
- `IOTimeSyncUserClient: missing entitlement %s\n`
- `Failed to allocate notification clients lock\n`
- `  %s(%s): Set lock state to %s from %s`
- `Packet pool being freed but has %llu outstanding packets`
- `Failed to allocate stop lock\n`
- `IOTimeSyncClockManager::begin waitQuiet\n`
- `- TSNUserWiFiControlInterface(kernel)::Create\n`
- `failed to allocate persistent user clocks dict\n`
- `No notification clients lock\n`
- `IOTimeSyncService::sendNotification: notification=%u arg0=%llu arg1=%llu`
- `  %s(%s): link down\n`
- `  %s(%s): [Lock state] %sTook %llu milliseconds to lock`
- `failed to start super\n`
- `Packet Timestamp: %llu\n`
- `  %s(%s): mbufTransmitCallback:  packet %p type=%s sequence: %u port %u timestamp %llu status 0x%08x dropped %u`
- `Failed to allocate notification clients array\n`
- `  %s(%s): Max Confidence %llu\n`
- `  %s(%s): takeDomainTime() has not been overriden. Write an implementation of takeDomainTime in your class to take the domain's timestamp\n`
- `failed to allocate identifier\n`
- `  %s(%s): stopped\n`
- `  %s(%s): setLinkActiveAsync: DOWN event (seq=%lld) completed, sent messageClients(DOWN)`
- `IOTimeSyncClockManager::delayedClockIDLookup registered service\n`
- `  %s(%s): link up\n`
- `Failed to get the clock manager\n`
- `failed to allocate lock\n`
- `  %s(%s): addTimestamps %u, 0x%llx.%016llx, 0x%llx.%016llx, 0x%llx.%016llx, 0x%llx.%016llx, %llu, %llu\n`
- `failed to allocate clock manager lock\n`
- `  %s(%s): %s enablePacketTimestamping failed`
- `IOTimeSyncClockTestUserClient: missing entitlement %s\n`
- `Failed to allocate daemon clients array\n`
- `  %s(%s): Mean Confidence %llu\n`
- `failed to cast provider\n`
- `  %s(%s): No provider, cannot identify the Wi-Fi driver`
- `Waiting for packets to flush.  _numberOfOutstandingPackets=%llu`
- `  %s(%s): start registered service\n`
- `  %s(%s): Mach average has overflowed 0x%016llx.%016llx\n`
- `  %s(%s): Starting snapshot.\n`
- `  %s(%s): Reinitialize TimeSync filter interval %llu\n`
- `  %s(%s): %s _timeSyncPacketPool isn't NULL and re-use it`
- `Failed to add interface matching notifier.\n`
- `IOTimeSyncTimedEdgeGeneratorUserClient: missing entitlement %s\n`
- `Boot-arg set PTP packet reception delay threshold to %u ms\n`
- `Unexpected timestamp == nullptr`
- `Unexpected timeout waiting for packets to flush. _numberOfOutstandingPackets=%llu`
- `  %s(%s): snapshot:%llu,%llu,%llu,%llu,%llu,%llu,%s,%s\n`
- `Boot-arg specifying local clock mode %d which is outside supported range of %d to %d\n`
- `- TSNUserWiFiControlInterface(static)::_CreateWithBSDName_Internal\n`
- `IOTimeSyncSyncUserClient: missing entitlement %s\n`
- `  %s(%s): takeSnapshot TimeSync time is not advancing\n`
- `  %s(%s): Thread call allocation failed`
- `failed to allocate user clocks array\n`
- `Packet Length: %lu\n`
- `  %s(%s): Calling enablePacketTimestamping on control interface`
- ` IOTimeSyncFamily assertion FailIfError \"%s\" failed in %s at line %d goto Exit. `
- `  %s(%s): Wi-Fi driver CFBundleIdentifier is \"%s\", chipset %s`
- `failed to allocate gPTP reference lock\n`
- `NULL clockID\n`
- `Persistent user filtered clock already exists: %s\n`
- `  %s(%s): TimeSync average has overflowed 0x%016llx.%016llx\n`
- `IOTimeSyncClockManager::addgPTPServices adding IOTimeSyncgPTPManager\n`
- ` IOTimeSyncFamily assertion FailIfWithAction \"%s\" failed in %s at line %d goto Exit. `
- `  %s(%s): Failed to transmit %s message of type %s sequence %u port %u egress timed packet to %s with error 0x%08x\n`
- `super failed to start\n`
- ` IOTimeSyncFamily assertion FailMessage \"%s\" failed in %s at line %d. `
- `  %s(%s): Transmit TimeSync Completed Count: %u %u`
- `  %s(%s): Transmit TimeSync Added Count: %u`
- `failed to allocate clock ID lock\n`
- `IOTimeSyncClockManager::addTSNCaptureServices requesting matching\n`
- `  %s(%s): Received mbuf(%p) with invalid timestamp flag, timestamp %llu`
- `  %s(%s): Transmitted %s message of type %s sequence %u port %u egress timed packet to %s but the timestamp (%llu) is in the future\n`
- `failed to allocate service lock\n`
- `timeYDelta %llx.%016llx\n`
- `MAC address data length length is smaller (%u) than expected (%u)`
- `  %s(%s): ERROR has not overriden disablePacketTimestamping() or is incorrectly calling super`
- `Failed to get translation service\n`
- `null IOService\n`
- `  %s(%s): Min Confidence %llu\n`
- `  %s(%s): TimeSync range %llu\n`
- `  %s(%s): Callback thread stop semaphore wait returned error %d`
- `IOTimeSyncSyncDaemonClient::clockUpdatedTimeSyncTimeGeneralSyncInfo: kIOTimeSyncSyncNotificationGeneralSyncUpdate rateNumerator=%llu rateDenominator=%llu timeSyncAnchor=%llu domainAnchor=%llu`
- `failed to allocate user clocks lock\n`
- `  %s(%s): Received mbuf(%p) with valid flag, timestamp = %llu. but timestamping mode is %d`
- `Could not allocate timeout thread`
- `- TSNUserWiFiControlInterface(kernel)::CreateWithBSDName\n`
- `  %s(%s): Skipping stale messageClients for link %s (sequence %lld < last processed %lld)`
- `  %s(%s): Failed to transmit message of type %s untimestamped packet with error 0x%08x\n`
- `Injected pdelay %llu for frameType = %u`
- `Failed to remove user filtered clock on cleanup: %llx\n`
- `IOTimeSyncSyncDaemonClient::clockUpdatedTimeSyncTimeGeneralSyncInfo: kIOTimeSyncSyncNotificationPTPSyncUpdate cumulativeScaledRate=%llu inverseCumulativeScaledRate=%llu timeSyncAnchor=%llu domainAnchorHi=%llu domainAnchorLo=%llu grandmasterID=%llu localPortNumber=%u syncFlags=%u syncInfoValid=%u`
- `  %s(%s): Ignoring platform mask 0x%x, boot-arg set mask 0x%x\n`
- `Failed to get AppleARMFunction\n`
- `Negative reference count (%i) for persistent user filtered clock: %s\n`
- `  %s(%s): Egress Timed Failed Packet Count: %u %u\n`
- `  %s(%s): Domain range %llu\n`
- `  %s(%s): Callback thread stopped`
- `Failed to allocate thread call\n`
- `clockID argument is NULL\n`
- `Boot-arg add max random timestamp jitter %u nanoseconds\n`
- `  %s(%s): transmitTimeSyncPacket: packet %p messageType %s sequence %u port %u timestamp %llu`
- `null timeSyncDameonServiceBase\n`
- `  %s(%s): %s MAC %02x:%02x:%02x:%02x:%02x:%02x`
- `IOTimeSyncClockManager::free\n`
- `TSNBSDInterfaceHelper::mbufTXCallback %p %p\n`
- `TimeSyncTime is mach_absolute_time nanoseconds\n`
- `  %s(%s): Transmit TimeSync Ignored Count: %u`
- `  %s(%s): Receive TimeSync Completed Count: %u`
- `instance index unsupported\n`
- `VLAN Tag: 0x%04hx\n`
- `TSNBSDInterfaceHelper::addMbufCallback _mbufCallbackCount=%u`
- `IOTimeSyncClockManager::addTSNCaptureServices adding services\n`
- `Failed to cast provider\n`
- `  %s(%s): Transmit TimeSync Completed Count: %u`
- `  %s(%s): Receive TimeSync Ignored Count: %u`
- `Timeout waiting for timesync node to match, _timesyncNode=%p\n`
- `- %s`
- `Unexpected NULL _timeSyncPacketPool`
- `Failed to re-initialize B filter\n`
- `Failed to create matching dictionary.\n`
- `Failed to create workloop\n`
- `  %s(%s): Domain average has overflowed 0x%016llx.%016llx\n`
- `+ TSNUserWiFiControlInterface(kernel)::Create\n`
- `  %s(%s): linkActiveThreadCall thread call failed`
- `IOTimeSyncClockManager::removegPTPServices removing IOTimeSyncgPTPManager\n`
- `Failed to allocate async callback lock\n`
- `super::start failed\n`
- `IOTimeSyncTimeLineFilter::timeXtoTimeY  timeYDelta128 is ridiculously big!\n`
- `IOTimeSyncClockManager::stop\n`
- `Failed to allocate properties dictionary\n`
- ` IOTimeSyncFamily assertion FailIfNULLWithAction \"%s\" failed in %s at line %d goto Exit. `
- `Failed to allocate work loop\n`
- `Failed to allocate service lock\n`
- `  %s(%s): Egress Timed Succeded Packet Count: %u %u\n`
- `  %s(%s): Egress Timed Packet Count: %u %u\n`
- `No user clients array\n`
- `  %s(%s): Reinitialize domain filter interval %llu\n`
- `- TSNUserWiFiControlInterface(kernel)::Create_Impl\n`
- `- TSNUserWiFiControlInterface(static)::_Create_Internal\n`
- `Boot-arg timesync_ts_mode=%d out of range (%d-%d), ignoring\n`
- `  %s(%s): setLinkActiveAsync: UP event (seq=%lld) completed, sent messageClients(UP)`
- `failed to create coreaudio clock ID mappings array\n`
- `  %s(%s): Dropped %s message of type %s sequence %u port %u egress timed packet to %s with error 0x%08x\n`
- `  %s(%s): MachNanos range %llu\n`
- `  %s(%s): Error: invalid time when trying to convert first wake time\n`
- `Failed to allocate time line filter\n`
- `  %s(%s): Calling disablePacketTimestamping on control interface`
- `null timeSyncService\n`
- `IOTimeSyncSyncDaemonClient::handleExternalMethod selector %u failed result %08x\n`
- `Init user clock map failed\n`
- `IOTimeSyncUserClient::externalMethod called on closed service, selector %u`
- `No user clients lock\n`
- `Failed to allocate dynamic lock\n`
- `IOTimeSyncClockManager::start registered service\n`
- `NULL userID\n`
- `  %s(%s): takeSnapshot mach time is not advancing\n`
- `  %s(%s): Transmit TimeSync Added Count: %u %u`
- `  %s(%s): Transmit TimeSync Ignored Count: %u %u`
- `  %s(%s): TSNInterface: %s%d timestamping support updated to %d`
- `  %s(%s): setLinkActiveAsync: %s event (seq=%lld) starting, lastProcessed=%lld`
- `  %s(%s): *** DISCARDING STALE LINK %s EVENT *** (sequence %lld <= last processed %lld)`
- `failed to create Dynamic Clock ID ref count array\n`
- `  %s(%s): Egress Untimestamped Packet Count: %u, Count since last log entry: %u (timestamping type %u, untimestamped general message mask 0x%x)\n`
- `No notification clients array\n`
- `could not create fTimeDomainSnapshotTimer\n\n`
- `Failed to allocate A domain filter\n`
- `  %s(%s): Receive TimeSync Added Count: %u`
- `IOTimeSyncClockManager::start\n`
- `IOTimeSyncClockManager::matched first IONF interface\n`
- `Failed to get MAC Address from interface: %d\n`
- `IOTimeSyncClockManager:: Generated random clockID %llx\n`
- `TSNBSDInterfaceHelper::removeMbufCallback _mbufCallbackCount=%u`
- `failed to start super class\n`
- `Calculated local clock mode as %d but overriden with %d\n`
- `IOTimeSyncEdgeTimeCaptureUserClient: missing entitlement %s\n`
- `Failed to allocate tsn capture lock\n`
- `  %s(%s): Added MBUF callback`
- `  %s(%s): Dropped %s message of type %s sequence %u port %u egress timed packet to %s\n`
- `TSNBSDInterfaceHelper::removeMbufCallback unregistered err %u`
- `provider is not an IOTimeSyncClockManager\n`
- `- TSNUserWiFiControlInterface(kernel)::CreateWithBSDName_Impl\n`
- `IOTimeSyncClockManager::end waitQuiet\n`
- `Failed to remove user filtered clock: %llx, Error: %d (0x%X)\n`
- `Skip egress timestamp request for general messages, mask 0x%x\n`
- `TSNPacketPool ERROR: Double complete of TSNPacket at index %lu, num outstanding: %llu`
- `  %s(%s): Stopped snapshot.\n`
- ` IOTimeSyncFamily assertion FailIf \"%s\" failed in %s at line %d goto Exit. `
- `+ TSNUserWiFiControlInterface(static)::_Create_Internal\n`
- `  %s(%s): Transmitted %s message of type %s sequence %u port %u egress timed packet to %s but the timestamp (%llu) is invalid\n`
- `  %s(%s): PTP packet reception timing: WiFi HW timestamp: %llu, SW receive time: %llu, Delay: %llu ns (%llu ms)\n`
- `%s::%s %u\n`
- `+ TSNUserWiFiControlInterface(static)::_CreateWithBSDName_Internal\n`
- `IOTimeSyncClockManager::failed delayed clock ID lookup.\n`
- `  %s(%s): Boot-arg timesync_ts_mode overriding %s%d mode from %d to %d`
- `Failed to allocate B domain filter\n`
- `+ TSNUserWiFiControlInterface(kernel)::CreateWithBSDName_Impl\n`
- `  %s(%s): Received mbuf(%p) with 0 timestamp, valid flag set`
- `TSNPacketPool did not flush within %u ms.  outstanding packets: %u`
- `  %s(%s): Dropped %s message of type %s sequence %u port %u egress timed packet to %s and the timestamp was 0\n`
- `  %s(%s): snapshotRaw:%u,%llu,%llu,%llu,%s,0x%016llx\n`
- `  %s(%s): Receive TimeSync Added Count: %u %u`
- `IOTimeSyncRootService::start\n`
- `TimeSyncTime is ARM PMGR counter\n`
- `Matched timesync node but already been initialised\n`
- `Failed clockID num allocation\n`
- `Boot-arg timesync_ts_mode=%d out of range (%d-%d), ignoring`
- `+ TSNUserWiFiControlInterface(kernel)::CreateWithBSDName\n`
- `Failed to allocate user filtered service\n`
- `  %s(%s): Received time sync packet with error status 0x%08x\n`
- `  %s(%s): Callback thread already running, skipping callback thread start`
- `  %s(%s): [Lock state] Kernel notifying kIOTimeSyncNotificationChangeClockLockState to %s`
- `  %s(%s): %s Allocate packetpool successfully`
- `Persistent clock doesn't exist: %s\n`
- `  %s(%s): determineTimestampingSupport: %s%d original timestamping mode from WiFi driver = %d`
- `Couldn't create clock identifier, Error: %d (0x%X)\n`
- `Assert: %s (value 0x%lx %lu), %s file: %s, line: %d\n`
- `IOTimeSyncRootService::probe TimeSyncTime not ready yet\n`
- `  %s(%s): %s disablePacketTimestamping failed`
- `  %s(%s): addTimestamps %u, %llu, %llu, %llu, %llu, %llu, %llu\n`
- `IOTimeSyncClockManager::init\n`
- `Failed to allocate daemon clients lock\n`
- `  %s(%s): Callback thread started`
- `Failed to add user clock, Error: %d (0x%X)\n`
- `  %s(%s): Packet info from mbuf: messageType %s sequence %u port %u now %llu timesynctime %llu`
- `  %s(%s_%s): Number of outstanding packets: %zu %zu\n`
- `  %s(%s): Error: invalid time when trying to schedule wake time\n`
- `  %s(%s): [Lock state] Kernel notifying kIOTimeSyncNotificationChangeClockLockState to %s due to reset`
- `failed to create Clock ID mapping ref count array\n`
- `  %s(%s): Scheduling: %llu\n`
- `  %s(%s): Median Confidence %llu\n`
- `  %s(%s): Link Inactive`
- `Persistent user filtered clock does not exist: %s\n`
- `Launch Timestamp: %llu\n`
- `IOTimeSyncClockManagerUserClient: missing entitlement %s\n`
- `  %s(%s): takeSnapshot domain time is not advancing\n`
- `  %s(%s): Callback thread stop semaphore signal returned error %d`
- `  %s(%s): %s(%u, %u)`
- `  %s(%s): Reinitialize mach filter interval %llu\n`
- `  %s(%s): Snapshots used %u\n`
- `IOTimeSyncClockManager::matched first TSN interface\n`
- `timeXDelta %llu intervalX %llu intervalY %llu\n`
- `  %s(%s): Receive TimeSync Ignored Count: %u %u`
- `  %s(%s): ERROR has not overriden enablePacketTimestamping() or is incorrectly calling super`
- `  %s(%s): WARNING: PTP packet reception delay exceeds %llu ms threshold! WiFi HW timestamp: %llu, SW receive time: %llu, Delay: %llu ns (%llu ms)\n`
- `  %s(%s): Transmitted %s message of type %s sequence %u port %u egress timed packet to %s but the timestamp was 0\n`
- `TSNBSDInterfaceHelper::addMbufCallback registered err %u`
- ` IOTimeSyncFamily assertion FailIfNULL \"%s\" failed in %s at line %d goto Exit. `
- `  %s(%s): Confidence range %llu\n`
- `Failed persistent clock mapping allocation\n`
- `PMGR average has overflowed 0x%016llx.%016llx\n`
- `Failed to start super\n`
- `  %s(%s): freeing\n`
- `Unexpected packet == nullptr`
- `IOTimeSyncService::sendGeneralSyncUpdate unknown sync client\n`
- `Resetting Propagation Delay Injection`
- `Failed to re-initialize A filter\n`
- `+ TSNUserWiFiControlInterface(kernel)::Create_Impl\n`
- `  %s(%s): Receive TimeSync Completed Count: %u %u`
- `failed to allocate mapping lock\n`
- `Failed to add mapping for persistent clock\n`
- `  %s(%s): ERROR has not overriden setInterfaceState() or is incorrectly calling super`
- `  %s(%s): Failed to send CoreAnalytics event %s`
- `IOTimeSyncClockManager::Using interface %s %s%u for identifier\n`
- `  %s(%s): Received time sync packet with timestamp (%llu) in the future of now (%llu)\n`
- `could not add Time Domain Snapshot Timer to workloop\n, Error: %d (0x%X)\n`
- `  %s(%s): Failed to allocate link state context`

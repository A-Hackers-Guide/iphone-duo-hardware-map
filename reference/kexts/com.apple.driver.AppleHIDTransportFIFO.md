# `com.apple.driver.AppleHIDTransportFIFO`

- Name: AppleHIDTransportFIFO
- Version: `1010.1`
- UUID: `A3F5774F-8570-3ABD-8FAA-8F4D8CFFA212`
- Source version: `10110.1.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleDockChannel`](com.apple.driver.AppleDockChannel.md) 1.0, [`com.apple.driver.AppleHIDTransport`](com.apple.driver.AppleHIDTransport.md) 1.0, [`com.apple.driver.AppleHIDTransportSCMCommon`](com.apple.driver.AppleHIDTransportSCMCommon.md) 1.0, [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleHIDTransportDeviceFIFO
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportFIFO`
- `IOClass`: `AppleHIDTransportDeviceFIFO`
- `IONameMatch`:
  - `hid-transport,dc`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDTransportFIFO`
- `IOProviderClass`: `AppleDockChannelDevice`

### AppleHIDTransportHibernator
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportFIFO`
- `IOClass`: `AppleHIDTransportHibernator`
- `IONameMatch`:
  - `aht-hibernator`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDTransportFIFO`
- `IOProviderClass`: `IOService`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleHIDTransportDeviceFIFO` | 0x158 | AppleHIDTransportDevice → AIDService → IOService → IORegistryEntry |
| `AppleHIDTransportProtocolSCMFIFO` | 0x9a0 | AppleHIDTransportProtocol → AIDService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00003267 off=0x004e14c0-0x004e4727 addr=0xfffffe00074e54c0-0xfffffe00074e8727 r--/r--   __TEXT            
	sz=0x00000008 off=0x004e1b38-0x004e1b40 addr=0xfffffe00074e5b38-0xfffffe00074e5b40               __TEXT.__const            
	sz=0x00002be7 off=0x004e1b40-0x004e4727 addr=0xfffffe00074e5b40-0xfffffe00074e8727               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00012cdc off=0x01ef3940-0x01f0661c addr=0xfffffe0008ef7940-0xfffffe0008f0a61c r-x/r-x   __TEXT_EXEC       
	sz=0x000128fc off=0x01ef3940-0x01f0623c addr=0xfffffe0008ef7940-0xfffffe0008f0a23c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003e0 off=0x01f0623c-0x01f0661c addr=0xfffffe0008f0a23c-0xfffffe0008f0a61c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000129 off=0x04949d68-0x04949e91 addr=0xfffffe000b94dd68-0xfffffe000b94de91 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04949d68-0x04949e30 addr=0xfffffe000b94dd68-0xfffffe000b94de30               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b94de30-0xfffffe000b94de90               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b94de90-0xfffffe000b94de91               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000016a8 off=0x010e55b0-0x010e6c58 addr=0xfffffe00080e95b0-0xfffffe00080eac58 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x010e55b0-0x010e55c0 addr=0xfffffe00080e95b0-0xfffffe00080e95c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x010e55c0-0x010e55d0 addr=0xfffffe00080e95c0-0xfffffe00080e95d0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001120 off=0x010e55d0-0x010e66f0 addr=0xfffffe00080e95d0-0xfffffe00080ea6f0         __DATA_CONST.__const            
	sz=0x000002c0 off=0x010e66f0-0x010e69b0 addr=0xfffffe00080ea6f0-0xfffffe00080ea9b0         __DATA_CONST.__kalloc_type      
	sz=0x000001f0 off=0x010e69b0-0x010e6ba0 addr=0xfffffe00080ea9b0-0xfffffe00080eaba0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b8 off=0x010e6ba0-0x010e6c58 addr=0xfffffe00080eaba0-0xfffffe00080eac58         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 147 at 0x04adb9f4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A3F5774F-8570-3ABD-8FAA-8F4D8CFFA212
008: LC_SOURCE_VERSION           10110.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa36b0 size=0x218
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleHIDTransportFIFO`
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportFIFO`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleHIDTransportFIFO`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleHIDTransport.kext/PlugIns/AppleHIDTransportFIFO.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900681536`
- `_PrelinkExecutableRelativePath`: `AppleHIDTransportFIFO`
- `_PrelinkExecutableSize`: `96020`
- `_PrelinkExecutableSourceAddr`: `-2198900681536`
- `_PrelinkKmodInfo`: `-2198828950168`

## Strings (289) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `[0x%llx][%llx][%s::%s]: ERROR!! Creating memory FIFO %d failed`
- `powerState == kAHTPowerStateOn`
- `lockInterfaceGated`
- `_dockChannelDevice`
- `ior == 0 `
- `[0x%llx][%llx][%s::%s]: Handshake not completed, deferring bootload until then.`
- `setInterfacePowerHasChanged`
- `_writeMessage`
- `[0x%llx][%llx][%s::%s]: ERROR!! Requested %llu writes to dcWrite and received %llu bytes written`
- `MemoryFIFOs`
- `setReport`
- `AppleHIDTransportManagement`
- `[0x%llx][%llx][%s::%s]: ERROR!! Report is too small %llu < %lu`
- `handshakeGated`
- `readMessage`
- `On`
- `ReportTimeoutMs`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid interface number - larger than max interfaces: %d >= %d (max)`
- `maxDRAMUsageInLastDay && totalDRAMCapacity`
- `Post-Reset Memory Dump`
- `report->getLength() > 0`
- `[0x%llx][%llx][%s::%s]: Read %llu bytes from HW FIFO`
- `_sharedMemoryManager->setMapperConfig(_genericMemMapperIndex, _swFifoMapperIndex) == 0 `
- `validateInterface`
- `site.AppleHIDTransportProtocolSCMFIFO`
- `handleControlReport`
- `memoryFifoCount && fifoIds && maxDRAMUsageInLastDayArray && totalDRAMCapacityArray`
- `MaxWriteSize`
- `threadLaunched`
- `11`
- `FlatPackBootloaderMsg.version == 1`
- `[0x%llx][%llx][%s::%s]: Handshake done: SW FIFOs registered`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `init`
- `i8@?0`
- `data`
- `[0x%llx][%llx][%s::%s]: ERROR!! Couldn't create input buffer`
- `_myWorkLoop`
- `setReportGated`
- `[0x%llx][%llx][%s::%s]: Driver not started. Read disabled`
- `Unknown`
- `[0x%llx][%llx][%s::%s]: Waiting for interface %u to finish`
- `FIFO`
- `getInterfaceData`
- `[0x%llx][%llx][%s::%s]: Interface %u locked`
- `drainSharedMemoryFifos`
- `maxDRAMUsageInLastDay`
- `ret == 0 `
- `[0x%llx][%llx][%s::%s]: ERROR!! Creating stat array for memory FIFO %d failed`
- `result`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/FIFO/AppleHIDTransportProtocolSCMFIFO.cpp`
- `[0x%llx][%llx][%s::%s]: Invalid interface id %u`
- `[0x%llx][%llx][%s::%s]: Get interface power state: %d`
- `memoryDump`
- `panic-upon-timeout`
- `_dramUsageStat`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unknown power state ordinal: %lu`
- `readNext`
- `reportDescriptor`
- `121111121222121211111112112121111111121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121222121211212222222222222222222222222222222222222222222222222222222222`
- `[0x%llx][%llx][%s::%s]: Interface %u is busy. Sleeping...`
- `reset`
- `_writeBuffer`
- `[0x%llx][%llx][%s::%s]: Using shared memory manager from enumeration cache`
- `[0x%llx][%llx][%s::%s]: Sleeping waiting for response`
- `[0x%llx][%llx][%s::%s]: Cannot allocate control payload`
- `[0x%llx][%llx][%s::%s]: Scheduling SW FIFO report`
- `function-reset`
- `\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u, report ID 0x%02X, transfer ID 0x%02X: invalid checksum (read: 0x%08X, calculated: 0x%08X)\" @%s:%d`
- `[0x%llx][%llx][%s::%s]: ERROR!! %s, %s file: %s, line: %d, value: 0x%08X`
- `handleStop`
- `[0x%llx][%llx][%s::%s]: Report buffer too small: report size %llu, buffer size %llu`
- `[0x%llx][%llx][%s::%s]: Unsupported bootloader, skipping.`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid HID report type %d`
- `iter`
- `[0x%llx][%llx][%s::%s]: Scheduled power toggle on separate thread`
- `[0x%llx][%llx][%s::%s]: %s interface power has changed to %s with status 0x%08X`
- `[0x%llx][%llx][%s::%s]: ERROR!! Coudn't allocate stat arrays`
- `\"%s\" @%s:%d`
- `[0x%llx][%llx][%s::%s]: ERROR!! setSystemAwakeReport(true) failed: 0x%08X`
- `[0x%llx][%llx][%s::%s]: ERROR!! Payload size == 0 - Interface ID [%u]`
- `ioRet == 0 `
- `cacheDeviceConfig`
- `[0x%llx][%llx][%s::%s]: Someone is writing. Sleeping...`
- `\"[%s::%s] Couldn't write into the FIFO: 0x%08X\" @%s:%d`
- `\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: message exceeds capacity %llu bytes\" @%s:%d`
- `[0x%llx][%llx][%s::%s]: ERROR!! No matching memory segment to release: addr 0x%016llX (size %d)`
- `FlatPackBootloader`
- `request.state < kAHTPowerStateCount`
- `111`
- `createInterfacesFromConfig`
- `performCBORBootload`
- `interfaceId < kMaxInterfaces`
- `cacheProtocolConfig`
- `getReport`
- `readCompletionAction`
- `\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: header size too large\" @%s:%d`
- `[0x%llx][%llx][%s::%s]: Read message with %u bytes`
- `handleBootload_block_invoke`
- `122`
- `Generic Mapper Index`
- `handleInputReport`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `disableAccessGated`
- `[0x%llx][%llx][%s::%s]: ERROR!! thread_call_allocate returned NULL`
- `[0x%llx][%llx][%s::%s]: ERROR!! Couldn't create write buffer`
- `[0x%llx][%llx][%s::%s]: Creating memory FIFO with read size %u write size %u`
- `Reset`
- `FlatPackInterface`
- `[0x%llx][%llx][%s::%s]: Get interface power via get report`
- `[0x%llx][%llx][%s::%s]: ordinal: %lu`
- `\"thread_call_free failed on _timeoutThread\" @%s:%d`
- `powerHasChanged`
- `bytesWritten == data->getLength()`
- `[0x%llx][%llx][%s::%s]: Scheduling memory dump complete report`
- `[0x%llx][%llx][%s::%s]: %s interface power will change to %s`
- `\"[%s::%s] Couldn't read from the HW FIFO: 0x%08X\" @%s:%d`
- `memDumpInfo.version == MemoryDumpInfo::Version::Vers1`
- `[0x%llx][%llx][%s::%s]: Interfaces = %u entries`
- `maxDRAMUsageInLastDayCopy && totalDRAMCapacityCopy`
- `configUint8`
- `[0x%llx][%llx][%s::%s]: Interface id %u >= %u`
- `[0x%llx][%llx][%s::%s]: Read %llu bytes from SW FIFO %d`
- `request.interface == interface->getInterfaceId()`
- `[0x%llx][%llx][%s::%s]: Interface set report failed: 0x%08X`
- `site.ReusedSharedMemory`
- `setPower`
- `[0x%llx][%llx][%s::%s]: Claiming wake with reason: %s`
- `MemoryFifos`
- `[0x%llx][%llx][%s::%s]: ERROR!! MemoryFifos[%d] not dictionary`
- `_commandGate`
- `sharedMemMessage.useType != kSharedMemSetReport`
- `interface`
- `getReportWithInterface`
- `MaxSharedMemoryReportLength`
- `ret == kIOReturnSuccess`
- `_management`
- `[0x%llx][%llx][%s::%s]: Resending old table of contents since FlatPack contents has not changed`
- `[0x%llx][%llx][%s::%s]: Found memory dump at addr 0x%016llX (size %d)`
- `interfaceInfo`
- `captureMemoryDump`
- `report`
- `checkControlComplete`
- `configBool`
- `[0x%llx][%llx][%s::%s]: `
- `parseNewBytes`
- `registerSharedMemory`
- `site.MemoryDumpCompleteThreadParam`
- `\"[%s::%s][%p] Control report timeout - Interface ID [%u] %s Report ID 0x%02X\" @%s:%d`
- `boolRet`
- `CachedSharedMemoryManager`
- `[0x%llx][%llx][%s::%s]: Invalid transferId: waiting %u, received %u`
- `interface->setPower(kAIDPowerStateOn) == 0 `
- `response`
- `[0x%llx][%llx][%s::%s]: ERROR!! totalDRAMCapacity is nullptr`
- `_readMessages`
- `_fifoNub`
- `handleBootload`
- `createAndRegisterMemoryDumpSharedMemory`
- `[0x%llx][%llx][%s::%s]: Waiting for ready report.`
- `[0x%llx][%llx][%s::%s]: Releasing memory segment at addr 0x%016llX (size %d)`
- `[0x%llx][%llx][%s::%s]: ERROR!! MemoryFifos[%d] error reading WriteSize`
- `[0x%llx][%llx][%s::%s]: Registering memory FIFO [%d]: slave address = %016llX`
- `_interfacesNeedingBootload`
- `createManagement`
- `type`
- `[0x%llx][%llx][%s::%s]: ERROR!! Memory dump at unknown address: 0x%016llX (size %d)`
- `[0x%llx][%llx][%s::%s]: Set interface power via set report`
- `sharedBuffer`
- `[0x%llx][%llx][%s::%s]: interface %u`
- `1211111212221212111112111221121111112111121`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/FIFO/AppleHIDTransportDeviceFIFO.cpp`
- `getReportGated`
- `[0x%llx][%llx][%s::%s]: Performing set report over shared memory`
- `[0x%llx][%llx][%s::%s]: Interface %d set report 0x%x, size %zu`
- `unlockInterfaceGated`
- `ReadSize`
- `handshake`
- `SW FIFO Mapper Index`
- `[0x%llx][%llx][%s::%s]: Invalid interface`
- `*reportType == kIOHIDReportTypeFeature || *reportType == kIOHIDReportTypeOutput`
- `setInterfacePower`
- `setReportWithInterface`
- `Set`
- `11222`
- `MaxDockFIFOReportLength`
- `performFlatPackBootload`
- `releaseSharedMemory`
- `[0x%llx][%llx][%s::%s]: Requesting reset via set report`
- `AppleHIDTransportDeviceFIFO`
- `site.AppleHIDTransportDeviceFIFO`
- `_timeoutThread`
- `interfaceIdNumber`
- `_maxDRAMUsageInLastDayArray && _totalDRAMCapacityArray`
- `powerWillChange`
- `true`
- `[0x%llx][%llx][%s::%s]: Interface id %u doesn't exist`
- `[0x%llx][%llx][%s::%s]: Reused shared memory expired, releasing...`
- `drainSharedMemoryFifosFromThread_block_invoke`
- `instructions`
- `memDumpData`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unknown FlatPack bootloader message %u`
- `[0x%llx][%llx][%s::%s]: Aborting in-progress report for interface %u`
- `buffer`
- `memDumpBytes`
- `resetDevice`
- `Pre-Reset Memory Dump`
- `configUint32`
- `config`
- `powerState`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid response size from report.`
- `OSBoundedPtr.h`
- `site.DockChannelReadCompletion`
- `AppleHIDTransportProtocolSCMFIFO`
- `[0x%llx][%llx][%s::%s]: ERROR!! Cannot create set report message with %llu bytes`
- `interfaceLocked`
- `_sharedMemorySegments`
- `copyDataToSlaveBuffer`
- `!interfaceData->interface`
- `addReadMessage`
- `readBuffer`
- `Size`
- `[0x%llx][%llx][%s::%s]: Skipping memory dump registration for interface %d (%s): memoryDumpLevel=%d, size=0x%08X`
- `handleFlatPackBootloaderMessageReport`
- `Interfaces`
- `Get`
- `RTP.%s`
- `_sharedMemoryManager`
- `request.version == PowerRequest::Version::Vers1`
- `handleStart`
- `ret`
- `\"[%s::%s] Invalid message read from the FIFO ID %d, interface ID %u: read beyond message boundary\" @%s:%d`
- `handleTogglePowerRequestReport`
- `report->getLength() >= sizeof(FlatPackBootloaderMsg)`
- `[0x%llx][%llx][%s::%s]: %u`
- `[0x%llx][%llx][%s::%s]: ERROR!! Timeout writing %llu bytes: bytesWritten=%llu, now=%llums, timeout=%llums, sleepcount=%u`
- `MaxReadSize`
- `encodedFirmware`
- `_inputReport`
- `WriteSize`
- `Address`
- `[0x%llx][%llx][%s::%s]: ERROR!! Interface %d does not have FlatPack bootloader`
- `[0x%llx][%llx][%s::%s]: ERROR!! Couldn't create write message buffer`
- `[0x%llx][%llx][%s::%s]: ERROR!! Couldn't add read message`
- `[0x%llx][%llx][%s::%s]: ERROR!! maxDRAMUsageInLastDay is nullptr`
- `cborBootloader`
- `handleMemoryDumpReport`
- `write`
- `[0x%llx][%llx][%s::%s]: Registering memory dump for interface %d (%s): memoryDumpLevel=%d, size=0x%08X`
- `site.TogglePowerThreadParam`
- `handlePrioritySystemPowerStateChange`
- `provideAndResetDRAMUsageData`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `AllowReportTimeout`
- `memDesc->getLength() >= dataLength`
- `[0x%llx][%llx][%s::%s]: ERROR!! Failed to create interface %d`
- `[0x%llx][%llx][%s::%s]: interfaceId %u reportId 0x%02x reportType %u`
- `sharedMemMessage.version == kSharedMemVer1`
- `setInterfacePowerWillChange`
- `Off Without Reset`
- `[0x%llx][%llx][%s::%s]: Sending message with %u bytes`
- `memDesc`
- `[0x%llx][%llx][%s::%s]: Shared memory of type %d registered for interface %d (%s) successfully`
- `togglePower`
- `getInterfacePower`
- `false`
- `Sleep`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unpowered`
- `[0x%llx][%llx][%s::%s]: %s = %u`
- `AppleHIDTransportProtocolSCMFIFO.cpp`
- `[0x%llx][%llx][%s::%s]: Unsupported report type : %d`
- `[0x%llx][%llx][%s::%s]: driver not started`
- `leadingPayloadByte == *reportId`
- `Off`
- `result == 0 `
- `[0x%llx][%llx][%s::%s]: Creating new shared memory block for FlatPack contents`
- `param`
- `[0x%llx][%llx][%s::%s]: ERROR!! Report is too small %llu %lu`
- `memoryDumpComplete`
- `[0x%llx][%llx][%s::%s]: ERROR!! MemoryFifos[%d] error reading ReadSize`
- `totalDRAMCapacity`
- `setPowerStateGated`
- `boolResult`
- `[0x%llx][%llx][%s::%s]: ERROR!! setSystemAwakeReport(false) failed: 0x%08X`
- `threadCall`
- `[0x%llx][%llx][%s::%s]: ERROR!! Error sending message`
- `[0x%llx][%llx][%s::%s]: Invalid message type`
- `interface->setPower(kAIDPowerStateOff) == 0 `
- `[0x%llx][%llx][%s::%s]: Creating interfaces from config with managementOnly=%s`

# `com.apple.driver.AppleHIDTransportMailbox`

- Name: AppleHIDTransportMailbox
- Version: `1010.1`
- UUID: `C6F7B08A-7D50-30AD-97AF-7CF1E924DA60`
- Source version: `10110.1.0.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleHIDTransport`](com.apple.driver.AppleHIDTransport.md) 1.0, [`com.apple.driver.AppleHIDTransportSCMCommon`](com.apple.driver.AppleHIDTransportSCMCommon.md) 1.0, [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleHIDTransportDeviceMailbox (MTP)
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportMailbox`
- `IOClass`: `AppleHIDTransportDeviceMailbox`
- `IONameMatch`:
  - `MTPEndpoint1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDTransportMailbox`
- `IOProviderClass`: `RTBuddyEndpointService`

### AppleHIDTransportDeviceMailbox (RTP)
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportMailbox`
- `IOClass`: `AppleHIDTransportDeviceMailbox`
- `IONameMatch`:
  - `RTPEndpoint1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDTransportMailbox`
- `IOProviderClass`: `RTBuddyEndpointService`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleHIDTransportDeviceMailbox` | 0x178 | AppleHIDTransportDevice → AIDService → IOService → IORegistryEntry |
| `AppleHIDTransportProtocolSCMMailbox` | 0x6b0 | AppleHIDTransportProtocol → AIDService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000387d off=0x004e4730-0x004e7fad addr=0xfffffe00074e8730-0xfffffe00074ebfad r--/r--   __TEXT            
	sz=0x00000125 off=0x004e4d58-0x004e4e7d addr=0xfffffe00074e8d58-0xfffffe00074e8e7d               __TEXT.__const            
	sz=0x00003130 off=0x004e4e7d-0x004e7fad addr=0xfffffe00074e8e7d-0xfffffe00074ebfad               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00016d8c off=0x01f06620-0x01f1d3ac addr=0xfffffe0008f0a620-0xfffffe0008f213ac r-x/r-x   __TEXT_EXEC       
	sz=0x0001697c off=0x01f06620-0x01f1cf9c addr=0xfffffe0008f0a620-0xfffffe0008f20f9c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000410 off=0x01f1cf9c-0x01f1d3ac addr=0xfffffe0008f20f9c-0xfffffe0008f213ac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x04949e98-0x04949fc0 addr=0xfffffe000b94de98-0xfffffe000b94dfc0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04949e98-0x04949f60 addr=0xfffffe000b94de98-0xfffffe000b94df60               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b94df60-0xfffffe000b94dfc0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001648 off=0x010e6c58-0x010e82a0 addr=0xfffffe00080eac58-0xfffffe00080ec2a0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x010e6c58-0x010e6c68 addr=0xfffffe00080eac58-0xfffffe00080eac68         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x010e6c68-0x010e6c78 addr=0xfffffe00080eac68-0xfffffe00080eac78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000012e0 off=0x010e6c78-0x010e7f58 addr=0xfffffe00080eac78-0xfffffe00080ebf58         __DATA_CONST.__const            
	sz=0x00000080 off=0x010e7f58-0x010e7fd8 addr=0xfffffe00080ebf58-0xfffffe00080ebfd8         __DATA_CONST.__kalloc_type      
	sz=0x00000208 off=0x010e7fd8-0x010e81e0 addr=0xfffffe00080ebfd8-0xfffffe00080ec1e0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000c0 off=0x010e81e0-0x010e82a0 addr=0xfffffe00080ec1e0-0xfffffe00080ec2a0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 154 at 0x04adbc40
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C6F7B08A-7D50-30AD-97AF-7CF1E924DA60
008: LC_SOURCE_VERSION           10110.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa38c8 size=0x258
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleHIDTransportMailbox`
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportMailbox`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleHIDTransportMailbox`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleHIDTransport.kext/PlugIns/AppleHIDTransportMailbox.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900668624`
- `_PrelinkExecutableRelativePath`: `AppleHIDTransportMailbox`
- `_PrelinkExecutableSize`: `114041`
- `_PrelinkExecutableSourceAddr`: `-2198900668624`
- `_PrelinkKmodInfo`: `-2198828949864`

## Strings (296) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `configUint8`
- `createInterfaces`
- `interface`
- `registerSharedMemory`
- `AppleHIDTransportProtocolSCMMailbox.cpp`
- `wakeReport->getPayloadSize() > 0 && reportPayload != nullptr`
- `[0x%llx][%llx][%s::%s]: Enabling endpoint %s`
- `handleEndpointPowerStateChange_block_invoke`
- `[0x%llx][%llx][%s::%s]: Polling FIFO '%s' configured with blocking consume`
- `powerState`
- `Pre-Reset Memory Dump`
- `_iopToApMessages`
- `Off`
- `[0x%llx][%llx][%s::%s]: Get %s (%d) interface power state: %d`
- `AHT Mailbox Power State`
- `handleStart`
- `[0x%llx][%llx][%s::%s]: Claiming system wake event with reason: %s at %lluus`
- `interfaceIdNumber`
- `[0x%llx][%llx][%s::%s]: endDrainPollingFifo: FIFO %s drain ended`
- `Get`
- `logFIFOUsage`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unsupported power state: %s`
- `memoryDump`
- `interface->setPower(kAIDPowerStateOff) == 0 `
- `AP to IOP Doorbell`
- `armIODevice`
- `[0x%llx][%llx][%s::%s]: Management set report ID 0x%02X returned: 0x%08X`
- `_sharedMemorySegments`
- `iopToApFifosKey`
- `flatPackInterface`
- `peekPollingFifoMessagesNonGated`
- `[0x%llx][%llx][%s::%s]: Interface ID: %d, report ID: 0x%02X, report length: %llu, report type: %u`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid IOHIDReportType report type: %d`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unsupported report type: %d`
- `_setReportBuffer`
- `config`
- `[0x%llx][%llx][%s::%s]: Polling succeeds, wrote %llu bytes to the buffer`
- `\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u: read beyond message boundary\" @%s:%d`
- `\"[%s::%s][%p][0x%08X] Control report timeout - Interface ID [%u] %s Report ID 0x%02X xferID 0x%02X\" @%s:%d`
- `unblockPollingFifo`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `Failed to power on, probably OK for the first power change.`
- `[0x%llx][%llx][%s::%s]: System power state change: %s -> %s`
- `_shouldClaimWake`
- `updateFifoUsage`
- `logWakeReport`
- `getInterfacePower`
- `request.interface == interface->getInterfaceId()`
- `drainPollingFifoNonGated_block_invoke`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `[0x%llx][%llx][%s::%s]: Setting mailbox queue size to %d: %s (0x%08X)`
- `sharedBuffer`
- `[0x%llx][%llx][%s::%s]: Sending set report with %llu bytes`
- `[0x%llx][%llx][%s::%s]: Sending message: messageID=0x%02X (%s), payload=0x%08llX`
- `Reset`
- `[0x%llx][%llx][%s::%s]: ERROR!! Report is too small %llu < %lu`
- `[0x%llx][%llx][%s::%s]: Creating new shared memory block for FlatPack contents`
- `[0x%llx][%llx][%s::%s]: ERROR!! Payload size == 0 - Interface ID [%u]`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid transferId: waiting %u, received %u`
- `[0x%llx][%llx][%s::%s]: drained %u bytes, %u bytes remaining (slow path)`
- `setPowerStateGated`
- `[0x%llx][%llx][%s::%s]: Resending old table of contents since FlatPack contents has not changed`
- `request.state < kAHTPowerStateCount`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid interface`
- `leadingPayloadByte == reportId`
- `%s(%s)`
- `IOP to AP Doorbell`
- `Off Without Reset`
- `fifoConfigs`
- `threadCall`
- `pollingFifoInfo && pollingFifoInfo->fifoCreated`
- `NULL`
- `drainPollingFifoNonGated`
- `Name`
- `_mailbox->claimWake(wakeReason)`
- `\"[%s::%s] Invalid message type received: %d from polling FIFO %s\" @%s:%d`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid interface id %u`
- `i8@?0`
- `fifoName`
- `createSharedMemoryFifo`
- `_sharedMemoryManager->isFifoAcquired(pollingFifoInfo->fifoID)`
- `reportSizeDict`
- `drainInputReportLoggingBufferEntries`
- `power state change failed, probably OK for the first attempt.`
- `!_iopReadyReceived`
- `handleControlReport`
- `writeToInputReportLoggingBuffer`
- `endDrainPollingFifo`
- `_endpointService`
- `iopNub`
- `configUint32`
- `ret`
- `setInterfacePowerHasChanged`
- `getReport_block_invoke`
- `Set`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/Mailbox/AppleHIDTransportDeviceMailbox.cpp`
- `br`
- `_systemPowerState == kSystemPowerOn`
- `[0x%llx][%llx][%s::%s]: Endpoint power state change, new:%lu old%lu`
- `Sleep`
- `performCBORBootload`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unsupported mailbox message ID received: 0x%02X`
- `[0x%llx][%llx][%s::%s]: Read %llu bytes from %s to AP FIFO %d (%s)`
- `[0x%llx][%llx][%s::%s]: Disabling access to mailbox`
- `sharedMemMessage.version == kSharedMemVer1`
- `[0x%llx][%llx][%s::%s]: beginDrainPollingFifo: FIFO %s is empty, skipping drain`
- `[0x%llx][%llx][%s::%s]: Management set report ID 0x%02X, size %zu`
- `[0x%llx][%llx][%s::%s]: watermark reached (readable=%u, watermark=%u), notifying user clients`
- `writePollingMessageToBuffer`
- `_maxRegularReadFifoUsage && _interfaceReportSizePerFifo && _interfaceReportCountPerFifo`
- `AppleHIDTransportManagement`
- `iter`
- `releaseSharedMemory`
- `powerState == kAHTPowerStateSleep`
- `\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u: message exceeds capacity %llu bytes\" @%s:%d`
- `_slaveProcessor`
- `apToIopFifosKey`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid key found in shared memory FIFOs config: %s`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid message type received: %d`
- `result`
- `sharedMemoryFifosConfigArr`
- `createManagement`
- `instructions`
- `memDesc != nullptr`
- `_commandGate`
- `registerMessageReceivedAction`
- `1211111212221212111111121121211111111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211222122212221222122212221222122212221222122212221222122212221222122221111112211121222`
- `createPollingFifo`
- `cborBootloader`
- `[0x%llx][%llx][%s::%s]: Releasing memory segment at addr 0x%016llX (size %d)`
- `[0x%llx][%llx][%s::%s]: Upon wake, FIFO %d (%s) is used %llu bytes, peak value is %llu bytes`
- `[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: polling FIFO %d (%s) is already busy`
- `[0x%llx][%llx][%s::%s]: Logging FIFO usage after AP wakes up`
- `maxUsage != nullptr`
- `IOPlatformSleepAction`
- `[0x%llx][%llx][%s::%s]: Deferring creation of polling FIFO '%s' until the first drainPollingFifoNonGated call`
- `captureMemoryDump`
- `setInterfacePowerWillChange`
- `handleMessageReceived`
- `\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u, report ID 0x%02X, transfer ID 0x%02X: invalid checksum (read: 0x%08X, calculated: 0x%08X)\" @%s:%d`
- `AHT Ready`
- `memDesc->getLength() >= dataLength`
- `[0x%llx][%llx][%s::%s]: Aborting in-progress report for interface %u`
- `setPower`
- `[0x%llx][%llx][%s::%s]: Disabling endpoint %s`
- `\"[%s::%s] Invalid message read from the FIFO ID %u, interface ID %u: header size too large\" @%s:%d`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid response size from report: %llu`
- `reportCount != nullptr`
- `site.AppleHIDTransportDeviceMailbox`
- `maxWriteMessageSize`
- `powerState == kAHTPowerStateOn`
- `handleIopToApSCMMessagesAvailable`
- `reportType == kIOHIDReportTypeFeature || reportType == kIOHIDReportTypeOutput`
- `reportDescriptor`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `validateInterface`
- `[0x%llx][%llx][%s::%s]: Blocking polling FIFO %d (%s)`
- `OSBoundedPtr.h`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `_interfaceReportSizePerFifo && _interfaceReportCountPerFifo`
- `newBootloader`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unknown FlatPack bootloader message %u`
- `powerWillChange`
- `[0x%llx][%llx][%s::%s]: Getting %s (%d) interface power via get report`
- `AP to %s`
- `powerHasChanged`
- `[0x%llx][%llx][%s::%s]: ERROR!! drainPollingFifoNonGated failed with ret=0x%08X (%s), wrote %llu bytes`
- `logFIFOUsage_block_invoke`
- `interfaceIdNumber && interfaceIdNumber->unsigned8BitValue() == kManagementInterfaceId`
- `AppleHIDTransportProtocolSCMMailbox`
- `%s to AP`
- `fifoConfigs->getCount() > 0 && fifoConfigs->getCount() <= kMaxIopToApSharedMemoryFIFOCount`
- `interface->setPower(kAIDPowerStateOn) == 0 `
- `flatPackBootloaderMsg.version == 1`
- `threadLaunched`
- `report->getLength() <= _writeMessage->getCapacity()`
- `_sharedMemoryManager->setMapperConfig(_genericMapperIdx, _sharedMemoryFifoMapperIdx) == 0 `
- `[0x%llx][%llx][%s::%s]: Message received: messageID=0x%02X (%s), payload=0x%08llX`
- `setReportWithManagement`
- `fifoSize`
- `Watermark`
- `init`
- `asyncMessage_block_invoke`
- `fifoConfigs->getCount() == kMaxApToIopSharedMemoryFIFOCount`
- `%s.%s`
- `[0x%llx][%llx][%s::%s]: ERROR!! endDrainPollingFifo: polling FIFO %s not found`
- `report->getLength() > 0`
- `sharedMemoryFifosConfig`
- `encodedFirmware`
- `buffer`
- `disableAccessGated`
- `getReportWithManagement`
- `cacheDeviceConfig`
- `bytesWritten == data->getLength()`
- `[0x%llx][%llx][%s::%s]: %s interface power will change to %s`
- `[0x%llx][%llx][%s::%s]: ERROR!! Sleeping waiting for control response failed with error 0x%08X`
- `reportCountDict`
- `ret == 0 `
- `memoryDescriptor`
- `[0x%llx][%llx][%s::%s]: ERROR!! Report buffer too small: report size %llu, buffer size %llu`
- `!interfaceReportInfo->interface`
- `[0x%llx][%llx][%s::%s]: Device power state change: %s -> %s`
- `type`
- `[0x%llx][%llx][%s::%s]: Running out of space during polling, buffer size is %llu, written size is %llu`
- `beginDrainPollingFifo`
- `[0x%llx][%llx][%s::%s]: Upon wake, interface %s receives %llu reports with total size %llu in FIFO %d (%s)`
- `_sharedMemoryManager`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/Mailbox/AppleHIDTransportProtocolSCMMailbox.cpp`
- `Size`
- `blockPollingFifo`
- `[0x%llx][%llx][%s::%s]: Setting message received action`
- `Unknown`
- `_writeMessage`
- `[0x%llx][%llx][%s::%s]: %d interface configurations found`
- `handleIopReadyMessage`
- `[0x%llx][%llx][%s::%s]: Draining FIFO %d (%s), type=%d, maxDataSize=%llu`
- `[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: Failed to block polling FIFO %d (%s), ret=0x%08X (%s)`
- `[0x%llx][%llx][%s::%s]: ERROR!! No matching memory segment to release: addr 0x%016llX (size %d)`
- `report->getLength() >= sizeof(flatPackBootloaderMsg)`
- `[0x%llx][%llx][%s::%s]: Sending get report with %llu bytes`
- `response`
- `[0x%llx][%llx][%s::%s]: %s interface power has changed to %s with status 0x%08X`
- `[0x%llx][%llx][%s::%s]: Doorbell rang by interface %d (%s)`
- `[0x%llx][%llx][%s::%s]: Peek %llu bytes from %s to AP FIFO %s`
- `[0x%llx][%llx][%s::%s]: ERROR!! Invalid message wakes up AP`
- `IOP to AP Register Shared Memory FIFO`
- `boolRet`
- `bootloader`
- `readMessage`
- `setPower(kAHTPowerStateOn) == 0 `
- `_mailbox`
- `reportTimeoutMs`
- `[0x%llx][%llx][%s::%s]: ERROR!! Failed to handle mailbox message: messageID=0x%02X, payload=0x%08llX`
- `msgBuffer`
- `handleInputReport`
- `_endpoint`
- `interfaceID < kMaxInterfaces`
- `copyDataToSlaveBuffer`
- `sendMailboxMessage`
- `_inputReportBuffer`
- `memDesc`
- `flatPackBootloader`
- `waitForControlResponse`
- `_role`
- `unregisterMessageReceivedAction`
- `createSharedMemoryFifos`
- `parseNewReadBytes`
- `[0x%llx][%llx][%s::%s]: Management get report ID 0x%02X, expected size %zu`
- `IOP Ready`
- `On`
- `maxReadMessageSize`
- `allowReportTimeout`
- `[0x%llx][%llx][%s::%s]: Registered shared memory of type %d, interface %d (%s). Addr 0x%016llX (size %d)`
- `drainIopToApFifos`
- `[0x%llx][%llx][%s::%s]: Polling data buffer full, current write offset %llu, data size %llu, max data size %llu`
- `[0x%llx][%llx][%s::%s]: Creating polling FIFO '%s' on the first drainPollingFifo call`
- `AppleHIDTransportDeviceMailbox`
- `[0x%llx][%llx][%s::%s]: %s = %u`
- `[0x%llx][%llx][%s::%s]: `
- `sharedMemoryFifosConfigArr->getCount() == 1`
- `[0x%llx][%llx][%s::%s]: Unblocking polling FIFO %d (%s)`
- `FIFO`
- `[0x%llx][%llx][%s::%s]: drained %u bytes, 0 bytes remaining`
- `_endpointWorkloop`
- `[0x%llx][%llx][%s::%s]: ERROR!! Unsupported system power state: 0x%08lX`
- `handleFlatPackBootloaderMessageReport`
- `AP to IOP Register Shared Memory FIFO`
- `[0x%llx][%llx][%s::%s]: %s ready message received, registering shared memory FIFOs`
- `Post-Reset Memory Dump`
- `site.AppleHIDTransportProtocolSCMMailbox`
- `_management`
- `handleBootload`
- `[0x%llx][%llx][%s::%s]: Creating interfaces from firmware image config`
- `[0x%llx][%llx][%s::%s]: Waiting for ready report.`
- `[0x%llx][%llx][%s::%s]: ERROR!! beginDrainPollingFifo: polling FIFO %s not found`
- `[0x%llx][%llx][%s::%s]: Read message with %u bytes`
- `_maxRegularReadFifoUsage`
- `[0x%llx][%llx][%s::%s]: ERROR!! %s, %s file: %s, line: %d, value: 0x%08X`
- `role`
- `performFlatPackBootload`
- `request.version == GetPowerRequest::Version::Vers1`
- `drainIopToApFifosFromThread_block_invoke`
- `report`
- `12111112122212121111121112211211111111111111222`
- `setReport_block_invoke`
- `\"%s\" @%s:%d`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `cacheProtocolConfig`
- `reportInfo.interface != nullptr`
- `[0x%llx][%llx][%s::%s]: Interface %u reportID 0x%02X wakes up AP`
- `[0x%llx][%llx][%s::%s]: ERROR!! slow path triggered: %u bytes buffered exceeds %llu bytes available in output buffer. Per-entry drain is suboptimal; increase user-client output buffer to >= logging buffer capacity (%u bytes).`
- `[0x%llx][%llx][%s::%s]: beginDrainPollingFifo: FIFO %s drain started`
- `[0x%llx][%llx][%s::%s]: ERROR!! endDrainPollingFifo: no drain in progress`
- `reportSize != nullptr`
- `[0x%llx][%llx][%s::%s]: interface %u, reportSize=%u, entrySize=%u, readable=%u/%u`
- `claimWake`

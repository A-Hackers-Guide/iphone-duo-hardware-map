# `com.apple.iokit.IOUSBMassStorageDriver`

- Name: IOUSBMassStorageDriver
- Version: `283`
- UUID: `39CCB3BD-FE2F-33AE-B11E-0A5E31755787`
- Source version: `283.0.0.0.0`
- Depends on: [`com.apple.iokit.IOPCIFamily`](com.apple.iokit.IOPCIFamily.md) 1.0.1, [`com.apple.iokit.IOSCSIArchitectureModelFamily`](com.apple.iokit.IOSCSIArchitectureModelFamily.md) 1.0.0, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (10) [KC]

### IOUSBMassStorageDriver
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBMassStorageDriverNub`
- `Read Time Out Duration`: `30000`
- `Write Time Out Duration`: `30000`

### IOUSBMassStorageDriverNub
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageDriverNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBMassStorageInterfaceNub`

### IOUSBMassStorageInterfaceNubMMC
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect`: `USB`
- `Physical Interconnect Location`: `External`
- `bInterfaceClass`: `8`
- `bInterfaceSubClass`: `2`

### IOUSBMassStorageInterfaceNubQIC-157
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect`: `USB`
- `Physical Interconnect Location`: `External`
- `bInterfaceClass`: `8`
- `bInterfaceSubClass`: `3`

### IOUSBMassStorageInterfaceNubRBC
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect`: `USB`
- `Physical Interconnect Location`: `External`
- `bInterfaceClass`: `8`
- `bInterfaceSubClass`: `1`

### IOUSBMassStorageInterfaceNubSCSI
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect`: `USB`
- `Physical Interconnect Location`: `External`
- `bInterfaceClass`: `8`
- `bInterfaceSubClass`: `6`

### IOUSBMassStorageInterfaceNubSFF-8070i
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect`: `USB`
- `Physical Interconnect Location`: `External`
- `bInterfaceClass`: `8`
- `bInterfaceSubClass`: `5`

### IOUSBMassStorageInterfaceNubUFI
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageInterfaceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBHostInterface`
- `Physical Interconnect`: `USB`
- `Physical Interconnect Location`: `External`
- `bInterfaceClass`: `8`
- `bInterfaceSubClass`: `4`

### IOUSBMassStorageResource
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageResource`
- `IOMatchCategory`: `IOUSBMassStorageResource`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`

### IOUSBMassStorageUASDriver
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOClass`: `IOUSBMassStorageUASDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUSBMassStorageDriver`
- `IOProviderClass`: `IOUSBMassStorageDriverNub`
- `Read Time Out Duration`: `30000`
- `Write Time Out Duration`: `30000`
- `bInterfaceProtocol`: `98`


## C++ classes (8) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOUSBMassStorageDriver` | 0x1c8 | IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOUSBMassStorageDriverNub` | 0x688 | IOService → IORegistryEntry |
| `IOUSBMassStorageDriverRequestTimer` | 0x88 | IOTimerEventSource → IOEventSource |
| `IOUSBMassStorageInterfaceNub` | 0x4f8 | IOService → IORegistryEntry |
| `IOUSBMassStorageResource` | 0xa8 | IOService → IORegistryEntry |
| `IOUSBMassStorageResourceUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |
| `IOUSBMassStorageUASDriver` | 0x2a0 | IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOUSBMassStorageUASDriverCommand` | 0x118 | IOCommand |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000031b8 off=0x00b63fa0-0x00b67158 addr=0xfffffe0007b67fa0-0xfffffe0007b6b158 r--/r--   __TEXT            
	sz=0x000028d5 off=0x00b64618-0x00b66eed addr=0xfffffe0007b68618-0xfffffe0007b6aeed               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000268 off=0x00b66ef0-0x00b67158 addr=0xfffffe0007b6aef0-0xfffffe0007b6b158               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0001e97c off=0x038588c0-0x0387723c addr=0xfffffe000a85c8c0-0xfffffe000a87b23c r-x/r-x   __TEXT_EXEC       
	sz=0x0001e22c off=0x038588c0-0x03876aec addr=0xfffffe000a85c8c0-0xfffffe000a87aaec          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000750 off=0x03876aec-0x0387723c addr=0xfffffe000a87aaec-0xfffffe000a87b23c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000309 off=0x04a1ca18-0x04a1cd21 addr=0xfffffe000ba20a18-0xfffffe000ba20d21 rw-/rw-   __DATA            
	sz=0x00000120 off=0x04a1ca18-0x04a1cb38 addr=0xfffffe000ba20a18-0xfffffe000ba20b38               __DATA.__data             
	sz=0x00000190 off=0x00000000-0x00000190 addr=0xfffffe000ba20b38-0xfffffe000ba20cc8               __DATA.__common           (Zerofill)
	sz=0x00000059 off=0x00000000-0x00000059 addr=0xfffffe000ba20cc8-0xfffffe000ba20d21               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003428 off=0x01470860-0x01473c88 addr=0xfffffe0008474860-0xfffffe0008477c88 rw-/rw-   __DATA_CONST      
	sz=0x00000048 off=0x01470860-0x014708a8 addr=0xfffffe0008474860-0xfffffe00084748a8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000048 off=0x014708a8-0x014708f0 addr=0xfffffe00084748a8-0xfffffe00084748f0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002aa0 off=0x014708f0-0x01473390 addr=0xfffffe00084748f0-0xfffffe0008477390         __DATA_CONST.__const            
	sz=0x00000440 off=0x01473390-0x014737d0 addr=0xfffffe0008477390-0xfffffe00084777d0         __DATA_CONST.__kalloc_type      
	sz=0x000003a8 off=0x014737d0-0x01473b78 addr=0xfffffe00084777d0-0xfffffe0008477b78         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000110 off=0x01473b78-0x01473c88 addr=0xfffffe0008477b78-0xfffffe0008477c88         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 268 at 0x04afb7fc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     39CCB3BD-FE2F-33AE-B11E-0A5E31755787
008: LC_SOURCE_VERSION           283.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aca6c8 size=0x388
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOUSBMassStorageDriver`
- `CFBundleGetInfoString`: `283, Copyright © 2016 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.iokit.IOUSBMassStorageDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOUSBMassStorageDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `283`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `283`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUSBMassStorageDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893854816`
- `_PrelinkExecutableRelativePath`: `IOUSBMassStorageDriver`
- `_PrelinkExecutableSize`: `152165`
- `_PrelinkExecutableSourceAddr`: `-2198893854816`
- `_PrelinkKmodInfo`: `-2198828086760`

## Strings (416) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `kIOReturnBadArgument`
- `Ctl>`
- `BulkPhaseError`
- `BulkMaxLunZero`
- `PowerTransToOff`
- `RdBurstLatency8ms`
- `Outstanding Commands Count`
- `AvgTrimLatency`
- `USBProductString`
- `\"%s::%s - !!!!! DEBUG !!!!! - HandleWriteReadyIU() should not be used if the device supports streams!\\n\" @%s:%d`
- `BulkCmdNoTimeout`
- `ResetUSBHostDeviceError`
- `Failed to complete power transition from %lu to %lu\n`
- `UASResponseIUFail`
- `InterimAttachError`
- `WriteIOPS`
- `\"%s::%s - lastEntry (%p)->prev == NULL.\\n\" @%s:%d`
- `PCI-Thunderbolt-Legacy`
- `Do Not Operate`
- `Use Standard USB Reset`
- `USBHostDeviceNotFndTerminate`
- `WrBurstLatency2ms`
- `IOLatency100ms`
- `Supports Streams`
- `kIOReturnIPCError`
- `ReattachDeviceMatchError`
- `DevConn30Min`
- `USB Mass Storage Trace ID`
- `\"%s::%s - !!!!! DEBUG !!!!! - ScheduleRecovery() was called without the lock held!\\n\" @%s:%d`
- `site.IOUSBMassStorageDriverNubExpansionData`
- `BulkDeviceUnresponsive`
- `121111121222121211112211121121111111111111111111111111111111111111111111211222222221`
- `USB device %016llX - Sense IU response received for task management request, taskStatus = %u, SENSE = %u, ASC =0x%02X, ASCQ = 0x%X\n`
- `Requested Speed`
- `Link Re-Train Required`
- `USB device %016llX - %s, %s - re-training\n`
- `Known CSW Tag Issues`
- `Inq:%llu:%08X|`
- `InterimDetachError`
- `TrimBurstLatency4ms`
- `Physical Interconnect Location`
- `12111112122212121121222222222222222222222222222222222222222222222222222222222222222222211121112211111112111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111211222`
- `Tur:%llu:%08X|`
- `IOUSBMassStorageDriver: %016llX-HLEr> %s\n`
- `BulkSendFail`
- `UASRequestForStatusFail`
- `DevConn4H`
- `AbortDataStream`
- `USB device %016llX - %s, %s - re-instantiated during wake up\n`
- `kIOReturnUnderrun`
- `IOMaximumBlockCountWrite`
- `UASReadIUFail`
- `UASWriteIUFail`
- `UASStreamStatusFail`
- `UASCmdNoTimeout`
- `PowerOnTerminate`
- `InterfaceOffTerminate`
- `Connected`
- `IOLatency10s`
- `UAS Debug Data`
- `\"%s::%s - !!!!! DEBUG !!!!! - HandleRequestForStatus should not be used if the device supports streams!\\n\" @%s:%d`
- `device-id`
- `USB Mass Storage Characteristics`
- `USB device %016llX - fConsecutiveResetCount > kIOUSBMassStorageMaxConsecutiveResets ( %u ).\n`
- `USBMassStorageDriver debug interface`
- `kIOReturnNoMemory`
- `Device Stats`
- `BulkDeviceError`
- `BulkClearPipeStallError`
- `RdBurstLatency16ms`
- `SCSI Device Characteristics`
- `Max LUNs reported as %u with 0x%x`
- `kIOReturnBadMedia`
- `BulkTimeout`
- `UASResetNoDevice`
- `CumWriteLatency`
- `WrBurstLatency8ms`
- `IOLatency40ms`
- `USB device %016llX - %s, %s - re-training to 0x%x, status 0x%x\n`
- `kUSBSerialNumberString`
- `kIOReturnNoInterrupt`
- `BulkIOTimeOut`
- `PowerTransToOn`
- `ReadIOPS`
- `PCIThunderboltLegacy`
- `Request Timeout Count`
- `Read Time Out Duration`
- `kIOReturnIsoTooNew`
- `Wak:%llu|`
- `IOMaximumBlockCountRead`
- `CumTrimLatency`
- `InterfaceProtocol`
- `site.IOUSBMassStorageUASDriverExpansionData`
- `Physical Interconnect`
- `kIOReturnLockedWrite`
- `ShL:%u:%llu|`
- `Reattached`
- `Task Reset Count`
- `CompleteCommand`
- `idProduct`
- `Res:%llu|`
- `Shu:%llu|`
- `IOUSBMassStorageDriver: %016llX-Misc> %s\n`
- `\"%s::%s - firstEntry (%p)->prev == NULL.\\n\" @%s:%d`
- `USB device %016llX - Invalid tag in completion! - tag = %d, bytesTransferred = %d status = %s\n`
- `bInterfaceProtocol`
- `bInterfaceClass`
- `kUSBVendorString`
- `kIOReturnNotAttached`
- `kIOReturnUnformattedMedia`
- `LRd:%llu:%08X|`
- `Devices Referenced`
- `kIOReturnPortExists`
- `BulkGetEPStatusError`
- `TaskMgmtErrorResponse`
- `USBVendorString`
- `IOMaximumSegmentByteCountRead`
- `LCm:%llu:%08X|`
- `UASTerminateCmdWait`
- `IOLatency10ms`
- `DevConn15Min`
- `%016llX`
- `\"%s::%s - firstEntry(%p)->next == NULL.\\n\" @%s:%d`
- `\"%s::%s - lastEntry(%p)->next == NULL.\\n\" @%s:%d`
- `Maximum Queue Depth`
- `IOMaximumSegmentCountWrite`
- `DevConnDays`
- `Retry Count`
- `root`
- `Error Count`
- `\"%s::%s - Unknown IU\\n\" @%s:%d`
- `HandleRequestForStatus`
- `site.IOUSBMassStorageDriverNub`
- `locationID`
- `NumInterfaceNubs`
- `USB device %016llX - termination caused by a wake from hibernation or standby!\n`
- `USB device %016llX - BOT reset completed with %s.\n`
- `kIOReturnVMError`
- `kIOReturnAborted`
- `BulkClearPipeStall`
- `\"%s::%s - currentQueueEntry (%p)->prev == NULL.\\n\" @%s:%d`
- `IOMaximumSegmentByteCountWrite`
- `Autonomous Spin Down`
- `kIOReturnBusy`
- `kIOReturnIsoTooOld`
- `kIOReturnInvalid`
- `RwC>`
- `site.IOUSBMassStorageResourceUserClient`
- `ReattachTerminate`
- `DevConnLessThan15Min`
- `UsbSpeed`
- `0x%02X-0x%llX-%s`
- `121111121222121211112211121111112221111211112222221222221`
- `12111112122212121111111111111`
- `RdBurstLatency4ms`
- `IOUSBMassStorageUASDriverCommand`
- `\"%s::%s - !!!!! DEBUG !!!!! - HandleReadReadyIU() should not be used if the device supports streams!\\n\" @%s:%d`
- `\"%s::%s - !!!!! DEBUG !!!!! command %p still in the watch dog fRequestTimer list\\n\" @%s:%d`
- `USB device %016llX - fConsecutiveResetCount = %u.\n`
- `kIOReturnInternalError`
- `kIOReturnNoPower`
- `BulkSendCBWError`
- `BulkSendCSWRecvError`
- `BulkCSWReceive2ndTime`
- `UASTerminateResetWait`
- `PCIDevicePause`
- `TrimCmdCount`
- `DevConn1H`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `free`
- `IOUSBMassStorageDriverNub`
- `121111121222121211212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112221122`
- `Reset Recovery Time`
- `kIOReturnNoDevice`
- `kIOReturnNoMedia`
- `kIOReturnOverrun`
- `DisconnectTag`
- `Preferred Protocol`
- `IOUSBMassStorageDriver: %016llX stop ...\n`
- `UASCmdInvalidTag`
- `ReattachNoResetError`
- `TrimBurstLatency16ms`
- `USB Device Info`
- `kIOReturnNotWritable`
- `BulkCSWTagError`
- `TrimBurstLatency8ms`
- `Rotational`
- `bInterfaceNumber`
- `StS:%llu:%08X|`
- `IOUSBMassStorageUserClient`
- `BulkCheckStallError`
- `ReattachOpenError`
- `ReadCmdCount`
- `CumReadLatency`
- `IOLatency1s`
- `\"%s::%s - currentQueueEntry(%p)->next == NULL.\\n\" @%s:%d`
- `DecrementPendingCommandsCount`
- `GetStreamError`
- `InterfaceClampOnNoDevice`
- `122222222222222222222222112122`
- `IOMaximumByteCountWrite`
- `IOUSBMassStorageInterfaceNub`
- `kIOReturnNoChannels`
- `ReEnumTimeoutTerminate`
- `ResetTimeout`
- `DriverNubStartError`
- `PCIDeviceOn`
- `IOUSBMassStorageUASDriver`
- `IOUSBMassStorageUASDriver.cpp`
- `ExecuteTaskManagementSync`
- `UASResetErrTerminate`
- `WrBurstLatency4ms`
- `IOUnit`
- `Internal`
- `kIOReturnUnsupported`
- `kIOReturnNotPermitted`
- `site.IOUSBMassStorageResource`
- `InterfaceTerminate`
- `WrBurstLatency16ms`
- `EventVersion`
- `*`
- `kIOReturnIOError`
- `LEr:%llu:%08X|`
- `BulkUseStdResetDevice`
- `RdBurstLatency2ms`
- `ReadThroughput`
- `MassStorageEvent`
- `HandleWriteReadyIU`
- `site.IOUSBMassStorageDriver`
- `kIOReturnNoCompletion`
- `BulkMaxLunStall`
- `WriteKBytes`
- `kIOReturnNoResources`
- `Sta:%llu|`
- `BulkPipeStall`
- `MassStorageDriverTerminate`
- `TaskMgmtTaskAbort`
- `USBProductID`
- `UASStatusFail`
- `UASNumOfStreams`
- `TrimBurstLatency2ms`
- `Config for BOT`
- `Preferred Subclass`
- `kIOReturnNotPrivileged`
- `kIOReturnNotAligned`
- `kUSBHostReturnNoPower`
- `PowerOnReEnumWait`
- `site.IOUSBMassStorageUASDriverCommand`
- `Medium Type`
- `kUSBDisconnectInterval`
- `USB device %016llX - %s, %s - detected termination of interfaceNub, currentPowerState %lu, provider is %s\n`
- `site.IOUSBMassStorageInterfaceNub`
- `Force BOT Protocol`
- `USB device %016llX - status = %s, resetting...\n`
- `BulkMassStorageReset`
- `IOUSBMassStorageDriverRequestTimer.cpp`
- `IODeviceTree:/defaults`
- `usb-storage-workaround`
- `HandleReadReadyIU`
- `No INQUIRY VPD Pages`
- `kIOReturnCannotWire`
- `0x%X`
- `121111121222121211212`
- `DeviceDropReEnum`
- `PublishEvent`
- `IOUSBMassStorageDriverRequestTimer`
- `IOUSBMassStorageDriver: %016llX usb reset ...\n`
- `UASDataFail`
- `PowerOnNewInterface`
- `USBVendorID`
- `SetTimeout`
- `Task Reset Success Count`
- `UASStatusCompletion`
- `USB device %016llX - USB Mass Storage stack will be terminated!\n`
- `%08X`
- `BulkCheckStallNoHalt`
- `LinkRetrain`
- `IOLatency30s`
- `DevConn8H`
- `IOMaximumSegmentCountRead`
- `bInterfaceSubClass`
- `kIOReturnDeviceError`
- `BulkCSWReceiveFail`
- `UASResetError`
- `ResetTerminatedDevice`
- `ResetDeviceNotFoundError`
- `InterfaceClampOnTimeout`
- `site.IOUSBMassStorageUASDriver`
- `\"%s::%s - !!!!! DEBUG !!!!! - ScheduleRecovery() command %p is not active!\\n\" @%s:%d`
- `kIOReturnMessageTooLarge`
- `ReattachPipeError`
- `ResetDeviceTerminate`
- `InterfaceOnTerminate`
- `site.IOUSBMassStorageDriverRequestTimer`
- `uasMaxBusStall`
- `Solid State`
- `usbmsDisconnectInterval`
- `kIOReturnRLDError`
- `UASSendFail`
- `WriteThroughput`
- `bConfigurationValue`
- `usbmsdriver`
- `2212222222222222222222222211212`
- `kIOReturnLockedRead`
- `kIOReturnNoSpace`
- `Sle:%llu|`
- `UASCommandFail`
- `TaskMgmtTimeout`
- `%x`
- `USB device %016llX - Device not responding, terminating...\n`
- `Version .02`
- `kIOReturnOffline`
- `kIOReturnUnsupportedMode`
- `kIOReturnNoBandwidth`
- `UASResetOnPowerOn`
- `UASIOTimeOut`
- `UASStartError`
- `ResetDeviceError`
- `USB Reset Count`
- `USB Product Name`
- `Write Time Out Duration`
- `kIOReturnNotFound`
- `BulkMassStorageResetError`
- `DevConn2H`
- `12111211112112112`
- `12112111111111112221111111111112221`
- `Queue Depth`
- `bNumConfigurations`
- `kUSBProductString`
- `kIOReturnNoFrames`
- `IOUserClientClass`
- `InterfaceOffDelayed`
- `StartStopUnitCmdCount`
- `\"%s::%s - fOutstandingCommands = %d, it should always be 0 at free() time.\\n\" @%s:%d`
- `site.AppleUASStatusRequest`
- `ScheduleRecovery`
- `USB Storage Characteristics`
- `USB device %016llX - fIOUSBMassStorageDriverNub->terminate().\n`
- `BulkCSWReceiveFail2ndTime`
- `UASResetSuccess`
- `ResetDeviceSuccess`
- `\"%s::%s - !!!!! DEBUG !!!!! - should run behind the workloop\\n\" @%s:%d`
- `kIOReturnDMAError`
- `kIOReturnTimeout`
- `kUSBHostReturnPipeStalled`
- `LWr:%llu:%08X|`
- `BulkMaxLunNoResp`
- `IOHibernateState`
- `UsbStreamsSupported`
- `Max Logical Unit Number`
- `SyC:%llu:%08X|`
- `IOUSBMassStorageResourceUserClient`
- `BulkStdResetDeviceTerminate`
- `TaskMgmtShutdown`
- `UAS Version`
- `site.IOUSBMassStorageDriverExpansionData`
- `CompleteSCSICommand`
- `Enable Port Suspend-Resume PM`
- `kIOReturnBadMessageID`
- `LUN Reset Success Count`
- `USB device %016llX - failed to re-instantiate!\n`
- `kIOReturnNotResponding`
- `%llu:%08X:%u|`
- `IOUSBMassStorageDriver: %016llX-%s %s\n`
- `BulkXfrDataError`
- `BulkConfigLunError`
- `TaskMgmtError`
- `IOMaximumByteCountRead`
- `AbortCommands`
- `kIOReturnCannotLock`
- `kIOReturnStillOpen`
- `IOUSBMassStorageResource`
- `BulkStdResetDeviceSuccess`
- `RdWrCheckCondition`
- `11111112`
- `USBSpeed`
- `USB device %016llX - will be reset!\n`
- `IOPMSystemSleepType`
- `IOUSBMassStorageDriver.cpp`
- `BulkGetEP0StatusError`
- `ReadKBytes`
- `LUN Reset Count`
- `USB device %016llX - %s, %s - found new interfaceNub\n`
- `kIOReturnNotReady`
- `Cur:%llu|`
- `BulkIOAborted`
- `WriteCmdCount`
- `USBProdRel`
- `\"%s::%s - !!!!! DEBUG !!!!! - ExecuteTaskManagementSync() called from the workloop thread\\n\" @%s:%d`
- `Version .04`
- `kIOReturnNotReadable`
- `Sen:%llu:%08X|`
- `BulkStallCBW`
- `Protocol Characteristics`
- `USB device %016llX - %s, %s - not found during wake up\n`
- `BulkDataOverrun`
- `idVendor`
- `bcdDevice`
- `kIOReturnSuccess`
- `kIOReturnError`
- `kIOReturnExclusiveAccess`
- `USBHostDeviceTerminate`
- `IOLatency20ms`
- `TaskMgmtLUNReset`
- `USB Attached SCSI Characteristics`
- `Reset On Resume`
- `\"%s::%s - !!!!! DEBUG !!!!! - fPendingCommandsCount underflow\\n\" @%s:%d`
- `IOUSBMassStorageDriver`
- `USB device %016llX - ResetBulkOnlyDevice completed with %s.\n`
- `FindPipeError`
- `WakeHibStandby`
- `kIOReturnNotOpen`
- `BulkStdResetDeviceError`
- `\"%s::%s - Unknown abort type\\n\" @%s:%d`
- `\"%s::%s - !!!!! DEBUG !!!!! - data direction should never be %u\\n\" @%s:%d`
- `USBMassStorageDriver`

# `com.apple.iokit.IOSCSIBlockCommandsDevice`

- Name: IOSCSIBlockCommandsDevice
- Version: `565.40.3`
- UUID: `46A5993B-1059-38C2-BC32-936D70456A30`
- Source version: `565.40.3.0.0`
- Depends on: [`com.apple.iokit.IOSCSIArchitectureModelFamily`](com.apple.iokit.IOSCSIArchitectureModelFamily.md) 1.0.0, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.9.9, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.9.9, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.9.9, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.9.9, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.9.9

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### IOSCSIPeripheralDeviceType00
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType00`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `Peripheral Device Type`: `0`

### IOSCSIPeripheralDeviceType07
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOClass`: `IOSCSIPeripheralDeviceType07`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `IOProviderClass`: `IOSCSIPeripheralDeviceNub`
- `Peripheral Device Type`: `7`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOBlockStorageServices` | 0xb8 | IOBlockStorageDevice → IOService → IORegistryEntry |
| `IOSCSIBlockCommandsDevice` | 0x110 | IOSCSIPrimaryCommandsDevice → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSIPeripheralDeviceType00` | 0x118 | IOSCSIBlockCommandsDevice → IOSCSIPrimaryCommandsDevice → IOSCSIProtocolInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000017f2 off=0x00a54070-0x00a55862 addr=0xfffffe0007a58070-0xfffffe0007a59862 r--/r--   __TEXT            
	sz=0x000011ca off=0x00a54698-0x00a55862 addr=0xfffffe0007a58698-0xfffffe0007a59862               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000d5ac off=0x033704b0-0x0337da5c addr=0xfffffe000a3744b0-0xfffffe000a381a5c r-x/r-x   __TEXT_EXEC       
	sz=0x0000cecc off=0x033704b0-0x0337d37c addr=0xfffffe000a3744b0-0xfffffe000a38137c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000006e0 off=0x0337d37c-0x0337da5c addr=0xfffffe000a38137c-0xfffffe000a381a5c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000034c off=0x04a15778-0x04a15ac4 addr=0xfffffe000ba19778-0xfffffe000ba19ac4 rw-/rw-   __DATA            
	sz=0x000002b0 off=0x04a15778-0x04a15a28 addr=0xfffffe000ba19778-0xfffffe000ba19a28               __DATA.__data             
	sz=0x00000098 off=0x00000000-0x00000098 addr=0xfffffe000ba19a28-0xfffffe000ba19ac0               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000ba19ac0-0xfffffe000ba19ac4               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001ff8 off=0x013db3d8-0x013dd3d0 addr=0xfffffe00083df3d8-0xfffffe00083e13d0 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x013db3d8-0x013db3f0 addr=0xfffffe00083df3d8-0xfffffe00083df3f0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x013db3f0-0x013db408 addr=0xfffffe00083df3f0-0xfffffe00083df408         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000018a0 off=0x013db408-0x013dcca8 addr=0xfffffe00083df408-0xfffffe00083e0ca8         __DATA_CONST.__const            
	sz=0x00000340 off=0x013dcca8-0x013dcfe8 addr=0xfffffe00083e0ca8-0xfffffe00083e0fe8         __DATA_CONST.__kalloc_type      
	sz=0x00000370 off=0x013dcfe8-0x013dd358 addr=0xfffffe00083e0fe8-0xfffffe00083e1358         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000078 off=0x013dd358-0x013dd3d0 addr=0xfffffe00083e1358-0xfffffe00083e13d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 235 at 0x04af6b24
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     46A5993B-1059-38C2-BC32-936D70456A30
008: LC_SOURCE_VERSION           565.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac4810 size=0x188
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOSCSIBlockCommandsDevice`
- `CFBundleGetInfoString`: `565.40.3, Copyright © 1999-2016 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIBlockCommandsDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOSCSIBlockCommandsDevice`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `565.40.3`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `565.40.3`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `565.40.3, Copyright © 1999-2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSCSIArchitectureModelFamily.kext/PlugIns/IOSCSIBlockCommandsDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894968720`
- `_PrelinkExecutableRelativePath`: `IOSCSIBlockCommandsDevice`
- `_PrelinkExecutableSize`: `69858`
- `_PrelinkExecutableSourceAddr`: `-2198894968720`
- `_PrelinkKmodInfo`: `-2198828116104`

## Strings (138) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Block Length In Bytes`
- `12111112122212121111221121212122121`
- `MaxPowerOffLatency`
- `[%s:%s] [%s]: Done; CurrentPowerState %d ProposedPowerState %d isPMAborted %d isInactive %d\n`
- `No Additional Device Info`
- `IOSCSIBlockCommandsDevice`
- `[%s:%s] [%s]: START_STOP_UNIT [1] error! serviceResponse 0x%x TaskStatus 0x%x\n`
- `Rotation Rate`
- `Features`
- `Read`
- `[%s:%s] [%s]: serviceResponse 0x%x taskStatus 0x%x START_STOP_UNIT [0] error!`
- `CumUnmapLatency`
- `LinkRetrain`
- `UnmapDescCount`
- `IssueUnmap`
- `Serial Number`
- `Apple TDM Driver`
- `PowerEventLog`
- `WriteCacheState`
- `force-smart`
- `12222221222`
- `[%s:%s] [%s]: ClearNotReadyStatus in progress for %llu sec, service response 0x%x, task status 0x%x, valid Sense %d; sense data 0x%02X/0x%02X/0x%02X ...\n`
- `Medium Type`
- `[%s::AbortPMTransition] [%s] Could not complete power transition %u to %u...terminating\n`
- `AbortPMTransition`
- `12111112122212121121221`
- `site.SCSICmd_INQUIRY_StandardDataAll`
- `Force Unit Access`
- `SBC: READ or WRITE succeeded, but recoverable (soft) error occurred, SENSE_KEY = 0x%01x, ASC = 0x%02x, ASCQ = 0x%02x, LBA = 0x%08x\n`
- `site.BlockServicesClientData`
- `Sector Count per Track`
- `MacModelID`
- `Cylinder Count`
- `[%s:%s] [%s]: serviceResponse 0x%x taskStatus 0x%x START_STOP_UNIT [1] error!`
- `[%s:%s] [%s]: [ %ld => %ld ] Wait time exceeded for outstanding commands, PM aborted %d Exiting ...\n`
- `[%s::AbortPMTransition] [%s] Ack power event\n`
- `site.IOSCSIBlockCommandsDevice`
- `Autonomous Spin Down`
- `Failed%s ReadRetries-%d`
- `PowerEventLatencyLog`
- `MaxPowerVMPLatency`
- `IOBlockStorageDriver`
- `Multiple Initiators`
- `LastWrError`
- `HandlePowerChange`
- `2.00`
- `[%s:%s] [%s]: Verify Medium in progress for %llu sec, service response 0x%x, task status 0x%x, valid Sense %d; sense data 0x%02X/0x%02X/0x%02X ...\n`
- `LastRdError`
- `[%s:%s] [%s]: drive READY, media present, sense data 0x%02X/0x%02X/0x%02X\n`
- `UnmapCapable`
- `MaxUnmapLBACount`
- `UnmapLBACount`
- `IOSCSIPeripheralDeviceType00`
- `[%s::AbortPMTransition] [%s] HandlePowerChange ack-ed power event\n`
- `Invalid Startup Disk`
- `[%s:%s] [%s]: ClearNotReadyStatus error\n`
- `[%s:%s] [%s]: Stop verify media presense check; PM abort %d isInactive %d\n`
- `[%s::AbortPMTransition] [%s] Requesting Close\n`
- `sbc`
- `High Throughput Options`
- `site.IOSCSIPeripheralDeviceType00`
- `scsi-smart`
- `HWError`
- `IOPrimaryDriverTerminateOptions`
- `Physical Interconnect`
- `[%s:%s] [%s]: MODE_SENSE_10 failed after %d retries, last serviceresponse: %x; TaskStatus: %x\n`
- `[%s:%s] [%s]: stop medium capacity checks; PM abort %d isInactive %d\n`
- `1111122222`
- `UnmapCount`
- `Async UNMAP error: ServiceResponse 0x%x TaskStatus 0x%x\n`
- `Open`
- `Manual Eject`
- `SCSIBlockDevice_ReadWriteError`
- `MediumError`
- `site.IOSCSIPeripheralDeviceType00ExpansionData`
- `IOStorageFeatures`
- `site.IOSCSIBlockCommandsDeviceExpansionData`
- `IOMaximumBlockCountRead`
- `MediaOfflineTS`
- `IOBlockStorageServices`
- `Unmap`
- `RdWrXferMismatch`
- `SCSIBusyTaskStatus`
- `DetermineMediumWriteProtectState`
- `[%s:%s] [%s]: ReadTest failed, last serviceresponse: %x; TaskStatus: %x\n`
- `[%s:%s] [%s]: [ %ld => %ld ] : waiting for commands to complete: %llu, %llu\n`
- `PowerEventError`
- `IOMaximumByteCountWrite`
- `[%s:%s] [%s]: drive READY, sense data 0x%02X/0x%02X/0x%02X\n`
- `Target Disk Mode`
- `WriteCacheEnabled`
- `Installed RAM`
- `RdWrErrors`
- `[%s:%s] [%s]: ClearNotReadyStatus failed or took long; result %d, duration %llu sec, status 0x%llx\n`
- `FireWire`
- `1211111212221212111122112121212212`
- `SCSI Device Characteristics`
- `IOMaximumByteCountRead`
- `ClearNotReadyStatus`
- `No INQUIRY VPD Pages`
- `USB`
- `IOPMResetPowerStateOnWake`
- `[%s::AbortPMTransition] [%s] Terminate \n`
- `MaxPowCNRSLatency`
- `MaxUnmapBlkDescCount`
- `Force Write Cache Disable`
- `[%s:%s] [%s]: WriteTest failed: Read retries: %d; last serviceresponse: %x; TaskStatus: %x\n`
- `Write`
- `Device Characteristics`
- `>`
- `Rigid Disk Geometry`
- `MaxPowerIOWaitLatency`
- `[%s::AbortPMTransition] [%s] Media has Changed\n`
- `site.IOBlockStorageServices`
- `DiskNotEjectedProperly`
- `[%s]: I/O error [0x%x] dir 0x%x lba 0x%llx count 0x%llx, retry %d ...\n`
- `[%s:%s] [%s]: Abort PM transition ...\n`
- `Head Count`
- `[%s:%s] [%s]: UNMAP error: ServiceResponse 0x%x TaskStatus 0x%x\n`
- `PowerEventTS`
- `MaxPowerOnLatency`
- `[%s:%s] [%s]: Verify Medium took long or failed; Verify Medium status 0x%llx\n`
- `SBC: Recieved 0x%llx bytes of LBA STATUS, truncating to 0x%llx\n`
- `Rotational`
- `MediaOnlineTS`
- `Bytes per Physical Sector`
- `Force Write Cache Enable`
- `[%s:%s] [%s]: ClearPowerOnReset error\n`
- `Eject Requires START_STOP_UNIT`
- `No Disk Geometry`
- `[%s:%s] [%s]: MODE_SENSE_06 failed after %d retries, last serviceresponse: %x; TaskStatus: %x\n`
- `1`
- `VerifyMediumPresence`
- `Protocol Characteristics`
- `[%s:%s] [%s]: Could not send TEST_UNIT_READY to device; service response 0x%X, task status 0x%X; exiting ClearNotReadyStatus.\n`
- `IOMedia`
- `Solid State`
- `IOMaximumBlockCountWrite`

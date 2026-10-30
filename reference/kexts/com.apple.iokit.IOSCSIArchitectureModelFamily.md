# `com.apple.iokit.IOSCSIArchitectureModelFamily`

- Name: IOSCSIArchitectureModelFamily
- Version: `565.40.3`
- UUID: `A32094CB-72EC-3AF3-A1A0-648CD4911F76`
- Source version: `565.40.3.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.9.9, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.9.9, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.9.9, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.9.9, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.9.9

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleSCSISubsystemGlobals
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIArchitectureModelFamily`
- `IOClass`: `AppleSCSISubsystemGlobals`
- `IOMatchCategory`: `com.apple.iokit.IOSCSIArchitectureModelFamily`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSCSIArchitectureModelFamily`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `com.apple.iokit.SCSISubsystemGlobals`

### IOSCSIPeripheralDeviceNub
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIArchitectureModelFamily`
- `IOClass`: `IOSCSIPeripheralDeviceNub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSCSIArchitectureModelFamily`
- `IOProviderClass`: `IOSCSIProtocolServices`


## C++ classes (10) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOSCSICommandGate` | 0x50 | IOCommandGate → IOEventSource |
| `IOSCSIHierarchicalLogicalUnit` | 0x108 | IOSCSIPeripheralDeviceNub → IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSILogicalUnitNub` | 0xf8 | IOSCSIPeripheralDeviceNub → IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSIMultipathedLogicalUnit` | 0x1c0 | IOSCSIPeripheralDeviceNub → IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSIPeripheralDeviceNub` | 0xf0 | IOSCSIProtocolServices → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSIPrimaryCommandsDevice` | 0xe8 | IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSIProtocolInterface` | 0xb8 | IOService → IORegistryEntry |
| `IOSCSIProtocolServices` | 0xd8 | IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `IOSCSITargetDevice` | 0x130 | IOSCSIPrimaryCommandsDevice → IOSCSIProtocolInterface → IOService → IORegistryEntry |
| `SCSITask` | 0x118 | IOCommand |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001f3d off=0x00a52130-0x00a5406d addr=0xfffffe0007a56130-0xfffffe0007a5806d r--/r--   __TEXT            
	sz=0x00000018 off=0x00a527f8-0x00a52810 addr=0xfffffe0007a567f8-0xfffffe0007a56810               __TEXT.__const            
	sz=0x0000185d off=0x00a52810-0x00a5406d addr=0xfffffe0007a56810-0xfffffe0007a5806d               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00017f18 off=0x03358590-0x033704a8 addr=0xfffffe000a35c590-0xfffffe000a3744a8 r-x/r-x   __TEXT_EXEC       
	sz=0x000178b8 off=0x03358590-0x0336fe48 addr=0xfffffe000a35c590-0xfffffe000a373e48          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000660 off=0x0336fe48-0x033704a8 addr=0xfffffe000a373e48-0xfffffe000a3744a8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000658 off=0x04a15120-0x04a15778 addr=0xfffffe000ba19120-0xfffffe000ba19778 rw-/rw-   __DATA            
	sz=0x00000418 off=0x04a15120-0x04a15538 addr=0xfffffe000ba19120-0xfffffe000ba19538               __DATA.__data             
	sz=0x000001d0 off=0x00000000-0x000001d0 addr=0xfffffe000ba19538-0xfffffe000ba19708               __DATA.__common           (Zerofill)
	sz=0x00000070 off=0x00000000-0x00000070 addr=0xfffffe000ba19708-0xfffffe000ba19778               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00005098 off=0x013d6340-0x013db3d8 addr=0xfffffe00083da340-0xfffffe00083df3d8 rw-/rw-   __DATA_CONST      
	sz=0x00000060 off=0x013d6340-0x013d63a0 addr=0xfffffe00083da340-0xfffffe00083da3a0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000060 off=0x013d63a0-0x013d6400 addr=0xfffffe00083da3a0-0xfffffe00083da400         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003c70 off=0x013d6400-0x013da070 addr=0xfffffe00083da400-0xfffffe00083de070         __DATA_CONST.__const            
	sz=0x000005a0 off=0x013da070-0x013da610 addr=0xfffffe00083de070-0xfffffe00083de610         __DATA_CONST.__kalloc_var       
	sz=0x00000a00 off=0x013da610-0x013db010 addr=0xfffffe00083de610-0xfffffe00083df010         __DATA_CONST.__kalloc_type      
	sz=0x00000330 off=0x013db010-0x013db340 addr=0xfffffe00083df010-0xfffffe00083df340         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000098 off=0x013db340-0x013db3d8 addr=0xfffffe00083df340-0xfffffe00083df3d8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 223 at 0x04af67a8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A32094CB-72EC-3AF3-A1A0-648CD4911F76
008: LC_SOURCE_VERSION           565.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac4468 size=0x3a8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOSCSIArchitectureModelFamily`
- `CFBundleGetInfoString`: `565.40.3, Copyright © 1999-2016 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.iokit.IOSCSIArchitectureModelFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOSCSIArchitectureModelFamily`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSCSIArchitectureModelFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894976720`
- `_PrelinkExecutableRelativePath`: `IOSCSIArchitectureModelFamily`
- `_PrelinkExecutableSize`: `128325`
- `_PrelinkExecutableSourceAddr`: `-2198894976720`
- `_PrelinkKmodInfo`: `-2198828117728`

## Strings (179) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Unsupported`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState - iterating obj %p PS %d ( %s )\n`
- `SCSI Debug Data`
- `IOMaximumByteCountRead`
- `[%s::%s] [%s] ClearPowerOnReset in progress for %llu sec, service response 0x%x, task status 0x%x, valid Sense %d; sense data 0x%02X/0x%02X/0x%02X ...\n`
- `site.IOSCSIProtocolServicesExpansionData`
- `SCSIArchitectureModel debug interface`
- `HLUN %p ::setPowerState - child %p ( %s ) is now asleep\n`
- `IOSCSIMultipathedLogicalUnit: new active path available, checking, loops = %d\n`
- `-IOSCSIMultipathedLogicalUnit %p ::HandlePowerChange curr PS %d\n`
- `IOSCSIProtocolInterface`
- `IOServiceBusyTimeoutExtensions`
- `Association`
- `IOSCSITargetDevice::systemWillShutdown, waiting for commands to complete, fNumCommandsOutstanding = %d\n`
- `1211121111`
- `Explicit`
- `ALUA Support`
- `Active Non-Optimized`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState - Entry curr PS %d doaminState 0x%x\n`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState iter obj %p is OFF ( %s )\n`
- `IOSCSITargetDevice has encountered a device with hierarchical LUNs, yet the HBA does not support it(1).\n`
- `site.IOSCSICommandGate`
- `SCSI Domain Identifier`
- `Physical Interconnect`
- `[%s::%s] [%s] isPMAborted %d elapsedTime %llu s command timeout %u ms\n`
- `[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X, Sense Data 0x%02X, 0x%02X, 0x%02X\n`
- `site.IOSCSIProtocolInterfaceExpansionData`
- `site.__OSHashEntry`
- `HLUN %p ::setPowerState - No multipathing found!\n`
- `root`
- `IOSCSIMultipathedLogicalUnit::setProperties() unable to locate path matching identifier: %s\n`
- `Write Time Out Duration`
- `IOSCSIProtocolServices`
- `HLUN %p ::setPowerState - Entry new PS %lu\n`
- `site.SCSITargetPortGroup`
- `NO_SENSE Debounce Retries`
- `start`
- `INQUIRY Unit Serial Number`
- `SCSI Logical Unit Bytes`
- `%s Assert failed: %s `
- `INQ VPD Change`
- `site.IOSCSIHierarchicalLogicalUnit`
- `Properties`
- `Modified Round Robin`
- `IOSCSIMultipathedLogicalUnit : Timed out waiting for active paths. \n`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState - super returning %lu!\n`
- `IOSCSIPeripheralDeviceNub`
- `121111121222121211112211121112`
- `12111112122212121111221121212`
- `+IOSCSIMultipathedLogicalUnit %p ::HandlePowerChange curr PS %d new PS %d\n`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState - returning %lu!\n`
- `Product Identification`
- `AppleKeyswitch`
- `IOMaximumByteCountWrite`
- `[%s::%s] [%s] drive READY, sense data 0x%02X, 0x%02X, 0x%02X\n`
- `MaxPowerCPORLatency`
- `NULL STRING`
- `1121`
- `site.SCSILogicalUnitPath`
- `Logical Unit Access State`
- `IOSCSIMultipathedLogicalUnit %p ::HandlePowerChange - Enabling Ping\n`
- `[%s::%s] [%s] InitializeDeviceSupport error`
- `site.IOSCSIProtocolInterface`
- `error: %ld `
- `\n`
- `Protocol Characteristics`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState iter obj %p number is NULL\n`
- `SCSITask`
- `%s `
- `SCSICmd_INQUIRY_StandardDataAll`
- `IOUnitLUN`
- `User Disabled`
- `sam`
- `12111112122212121111221121212112211122`
- `IOSCSITargetDevice has encountered a device with hierarchical LUNs, yet the HBA does not support it(2).\n`
- `IOSCSITargetDevice::RetrieveINQUIRYDataPage: Inquiry Failed for page %x\n`
- `site.__OSHashEntryBucket`
- `IOSCSIHierarchicalLogicalUnit`
- `IOUnitLUNBytes`
- `Logical Unit Path Identifier`
- `Unavailable`
- `AddPathToTargetPortGroup : Unknown state %x\n`
- `IOSCSITargetDevice`
- `Read Time Out Duration`
- `Keyswitch`
- `211111`
- `Vendor Name`
- `line: %ld `
- `Physical Interconnect Location`
- `site.IOSCSITargetDevice`
- `Apple TDM Driver`
- `Hierarchical LUN Support`
- `INQUIRY DATA HAS CHANGED\n`
- `SCSI Logical Unit Number`
- `site.SCSICmd_RTPG_Header`
- `Unique SCSI Port Identifier`
- `site.IOSCSIPrimaryCommandsDevice`
- `ATAPI`
- `[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X, happened %d times\n`
- `WaitForTask, taskState = 0x%08X, done = false\n`
- `Load Balancing Algorithm`
- `SCSI Device Characteristics`
- `FireWire`
- `site.SCSITask`
- `Algorithm`
- `Implicit/Explicit`
- `IOSCSIMultipathedLogicalUnit: Failed to Add Path %p\n`
- `122212222222222222222222`
- `Found SAM trace flags = 0x%08x\n`
- `12111112122212121111221112111211121222112112211111111112`
- `IOSCSIMultipathedLogicalUnit: Timed out waiting for paths to become available, loops = %d\n`
- `site.IOSCSILogicalUnitNub`
- `Product Name`
- `Inquiry Length`
- `CheckForSufficientTimeForPMCommand`
- `122`
- `1`
- `Least Bytes`
- `Vendor Identification`
- `121111121222121211112211121`
- `site.SCSICmd_INQUIRY_StandardDataAll`
- `PathState`
- `[%s::%s] [%s] Could not send TEST_UNIT_READY to device; service response 0x%X, task status 0x%X; exiting ClearPowerOnReset \n`
- `12111222222212222111222122221111112`
- `Code Set`
- `Identifier`
- `Retry Count`
- `IOSCSIMultipathedLogicalUnit[%p]: AddPath: Timed out waiting for MultipathedLogicalUnit init completion\n`
- `TPGS Information`
- `Active Optimized`
- `IOSCSIMultipathedLogicalUnit`
- `site.IOSCSIMultipathedLogicalUnit`
- `Logical Unit Unique Identifier`
- `Product Revision Level`
- `Batch Count`
- `IOSCSIMultipathedLogicalUnit[%p]: Timed out waiting for all paths to be removed, fPathsTerminating = %d, fPathCount = %d\n`
- `IOSCSIPrimaryCommandsDevice`
- `12111112122212121111221`
- `file: %s `
- `Device Identifier`
- `CurrentPowerState`
- `IOSCSIMultipathedLogicalUnit : Another path available.\n`
- `[%s::%s] [%s] ClearPowerOnReset either failed or took long; result %d, duration %llu sec, status 0x%llx\n`
- `INQUIRY Device Identification`
- `IOSCSITargetDevice has encountered a device with hierarchical LUNs, yet the HBA does not support it(3).\n`
- `%02x%02x%02x%02x%02x%02x%02x%02x`
- `site.SCSILogicalUnitPath *`
- `Implicit`
- `IOSCSIMultipathedLogicalUnit.cpp`
- `%x`
- `\"IOSCSIMultiPathedLogicalUnit: freeing lunpath before termination\\n\" @%s:%d`
- `1211111212221212111122111211121`
- `site.IOSCSIPeripheralDeviceNub`
- `Found SAM debug flags = 0x%08x\n`
- `site.LogicalUnitEntry`
- `IOSCSILogicalUnitNub`
- `[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X, Sense Data: 0x%02X, 0x%02X, 0x%02X, happened %d times\n`
- `site.IOSCSIProtocolServices`
- `IOSCSICommandGate`
- `Logical Unit Alias`
- `Standby`
- `IOSCSIMultipathedLogicalUnit %p ::HandlePowerChange - Disabling Ping\n`
- `IOSCSIMultipathedLogicalUnit %p ::maxCapabilityForDomainState - Waiting for parents to come up\n`
- `site.IOSCSIPrimaryCommandsDeviceExpansionData`
- `Least Queue Depth`
- `ClearPowerOnReset`
- `samtrace`
- `12`
- `121111121222121211112211121112212`
- `%02X`
- `1111111111112222222`
- `USB`
- `[%s] I/O error! Opcode 0x%02X, Service response 0x%02X, Task status 0x%02X\n`
- `Identifier Type`
- `SCSIArchitectureModel`
- `HLUN %p ::setPowerState - Exit with curr PS %lu\n`
- `Peripheral Device Type`
- `1111122`
- `1112`

# `com.apple.driver.AppleEventLogHandler`

- Name: AppleEventLogHandler
- Version: `1`
- UUID: `6A93F7D9-C36F-39FA-B5AF-2425A1446300`
- Source version: `1976.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/event-log-handler`](../devicetree/root__arm-io__event-log-handler.md) | `AppleEventLogHandler` | `event-log-handler,t8101` |

## IOKit personalities (1) [KC]

### AppleEventLogHandler
- `CFBundleIdentifier`: `com.apple.driver.AppleEventLogHandler`
- `IOClass`: `AppleEventLogHandler`
- `IONameMatch`: `event-log-handler,t8101`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEventLogHandler`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEventLogHandler` | 0x4f0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000cb3 off=0x00463880-0x00464533 addr=0xfffffe0007467880-0xfffffe0007468533 r--/r--   __TEXT            
	sz=0x0000068b off=0x00463ea8-0x00464533 addr=0xfffffe0007467ea8-0xfffffe0007468533               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001588 off=0x01ca13f0-0x01ca2978 addr=0xfffffe0008ca53f0-0xfffffe0008ca6978 r-x/r-x   __TEXT_EXEC       
	sz=0x00001488 off=0x01ca13f0-0x01ca2878 addr=0xfffffe0008ca53f0-0xfffffe0008ca6878          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x01ca2878-0x01ca2978 addr=0xfffffe0008ca6878-0xfffffe0008ca6978          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04940da0-0x04940ea0 addr=0xfffffe000b944da0-0xfffffe000b944ea0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04940da0-0x04940e68 addr=0xfffffe000b944da0-0xfffffe000b944e68               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b944e68-0xfffffe000b944ea0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000778 off=0x010972c0-0x01097a38 addr=0xfffffe000809b2c0-0xfffffe000809ba38 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x010972c0-0x010972c8 addr=0xfffffe000809b2c0-0xfffffe000809b2c8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010972c8-0x010972d0 addr=0xfffffe000809b2c8-0xfffffe000809b2d0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x010972d0-0x010978c0 addr=0xfffffe000809b2d0-0xfffffe000809b8c0         __DATA_CONST.__const            
	sz=0x00000040 off=0x010978c0-0x01097900 addr=0xfffffe000809b8c0-0xfffffe000809b900         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x01097900-0x010979a0 addr=0xfffffe000809b900-0xfffffe000809b9a0         __DATA_CONST.__kalloc_var       
	sz=0x00000080 off=0x010979a0-0x01097a20 addr=0xfffffe000809b9a0-0xfffffe000809ba20         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000018 off=0x01097a20-0x01097a38 addr=0xfffffe000809ba20-0xfffffe000809ba38         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 35 at 0x04ad9824
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     6A93F7D9-C36F-39FA-B5AF-2425A1446300
008: LC_SOURCE_VERSION           1976.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f970 size=0x40
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEventLogHandler`
- `CFBundleGetInfoString`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleEventLogHandler`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEventLogHandler`
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
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEventLogHandler.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901196672`
- `_PrelinkExecutableRelativePath`: `AppleEventLogHandler`
- `_PrelinkExecutableSize`: `10931`
- `_PrelinkExecutableSourceAddr`: `-2198901196672`
- `_PrelinkKmodInfo`: `-2198828986976`

## Strings (46) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"AppleEventLogHandler: %s:%u REQUIRE failed: %s\" @%s:%d`
- `AppleEventLogHandler.cpp`
- `_regMapData[i].virtualAddress`
- `_regMapData[i].physicalAddress`
- `data`
- `event-log-panic-timeout-ms`
- `_eventLogPanicTimer->setTimeoutMS(_eventLogPanicTimeoutMS) == kIOReturnSuccess`
- `112`
- `12111112122212121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222111112111122`
- `interrupts`
- `%s: stopped\n`
- `UInt32 AppleEventLogHandler::_readEventLogReg(EventLogID, UInt32)`
- `Write`
- `True`
- `AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x Deferred=%s\n`
- `1`
- `_interruptFilterEventSource[i]`
- `event-logs`
- `Setting EventLog panic timeout to %u ms\n`
- `_commandGate`
- `void AppleEventLogHandler::_writeEventLogReg(EventLogID, UInt32, UInt32)`
- `_eventCount < kEventCountMax`
- `Read`
- `panic-on-event-log-intr`
- `_eventLogPanicTimer`
- `_workLoop->addEventSource(_eventLogPanicTimer) == kIOReturnSuccess`
- `EventLog %u: AccessType=%s Address=0x%llx\n`
- `\"AppleEventLogHandler: No event log entry found for interrupt %d\" @%s:%d`
- `site.AppleEventLogHandler`
- `virtual bool AppleEventLogHandler::start(IOService *)`
- `result`
- `_workLoop`
- `site.RegMapData`
- `_interruptFilterEventSource`
- `panic-on-missing-event-log`
- `%s: started\n`
- `_regMapData[i].regMap`
- `\"AppleEventLogHandler: Register is locked down! AccessType=%s Address=0x%llx IntrID=%x RegMapID=%x Deferred=%s\" @%s:%d`
- `False`
- `\"AppleEventLogHandler: Received %u unique EventLog entries less than %u ms apart\" @%s:%d`
- `_regMapData`
- `ret == kIOReturnSuccess`
- `site.IOFilterInterruptEventSource *`
- `regOffset <= kEventLogRegOffsetMax`
- `void AppleEventLogHandler::_handleEventLogInterrupt(EventLogID, bool)`
- `AppleEventLogHandler`

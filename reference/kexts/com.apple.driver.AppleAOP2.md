# `com.apple.driver.AppleAOP2`

- Name: AppleAOP2
- Version: `1.0`
- UUID: `FE7BBC07-5148-3903-AAD7-4D74AD5B5A15`
- Source version: `207.40.2.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (5) [KC]

### AOP2AFKTightbeamEndpoints
- `CFBundleIdentifier`: `com.apple.driver.AppleAOP2`
- `IOClass`: `AppleAOP2KextTightbeamEndpoint`
- `IONameMatch`:
  - `aop2.system-iopm-aop2.system-iopm.ap.client-rev`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOP2`
- `IOProviderClass`: `AFKEndpointInterface`

### AOP2Endpoints
- `CFBundleIdentifier`: `com.apple.driver.AppleAOP2`
- `IOClass`: `AFKEPKextV2`
- `IONameMatch`:
  - `AOP2Endpoint1`
  - `AOP2Endpoint2`
  - `AOP2Endpoint3`
  - `AOP2Endpoint4`
  - `AOP2Endpoint5`
  - `AOP2Endpoint6`
  - `AOP2Endpoint7`
  - `AOP2Endpoint8`
  - `AOP2Endpoint9`
  - `AOP2Endpoint10`
  - `AOP2Endpoint11`
  - `AOP2Endpoint12`
  - `AOP2Endpoint13`
  - `AOP2Endpoint14`
  - `AOP2Endpoint15`
  - `AOP2Endpoint16`
  - `AOP2Endpoint17`
  - `AOP2Endpoint18`
  - `AOP2Endpoint19`
  - `AOP2Endpoint20`
  - `AOP2Endpoint21`
  - `AOP2Endpoint22`
  - `AOP2Endpoint23`
  - `AOP2Endpoint24`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOP2`
- `IOProviderClass`: `RTBuddyEndpointService`
- `IdleLowPower`: `False`
- `UseIOPMStateControl`: `True`

### AOP2FirmwareService
- `CFBundleIdentifier`: `com.apple.driver.AppleAOP2`
- `IOClass`: `AFKFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOP2`
- `IOPropertyMatch`:
  - `role`: `AOP2`
- `IOProviderClass`: `RTBuddyService`

### AppleAOP2IOPMService
- `CFBundleIdentifier`: `com.apple.driver.AppleAOP2`
- `IOClass`: `AppleAOP2IOPMService`
- `IONameMatch`:
  - `aop2.system-iopm-aop2.system-iopm.ap.client-rev`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOP2`
- `IOProviderClass`: `AppleAOP2KextTightbeamEndpoint`

### AppleAOP2SystemDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleAOP2`
- `IOClass`: `AppleAOP2SystemDriver`
- `IONameMatch`:
  - `system-manager`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOP2`
- `IOProviderClass`: `AFKMailboxEndpointInterface`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAOP2IOPMService` | 0xb8 | IOService → IORegistryEntry |
| `AppleAOP2KextTightbeamEndpoint` | 0xd0 | AFKTightbeamEndpoint → IOService → IORegistryEntry |
| `AppleAOP2SystemDriver` | 0x98 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001444 off=0x00155280-0x001566c4 addr=0xfffffe0007159280-0xfffffe000715a6c4 r--/r--   __TEXT            
	sz=0x00000b75 off=0x00155948-0x001564bd addr=0xfffffe0007159948-0xfffffe000715a4bd               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000008 off=0x001564c0-0x001564c8 addr=0xfffffe000715a4c0-0xfffffe000715a4c8               __TEXT.__const            
	sz=0x000001fc off=0x001564c8-0x001566c4 addr=0xfffffe000715a4c8-0xfffffe000715a6c4               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000039c8 off=0x0168cc50-0x01690618 addr=0xfffffe0008690c50-0xfffffe0008694618 r-x/r-x   __TEXT_EXEC       
	sz=0x00003618 off=0x0168cc50-0x01690268 addr=0xfffffe0008690c50-0xfffffe0008694268          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003b0 off=0x01690268-0x01690618 addr=0xfffffe0008694268-0xfffffe0008694618          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000002f8 off=0x0492e738-0x0492ea30 addr=0xfffffe000b932738-0xfffffe000b932a30 rw-/rw-   __DATA            
	sz=0x00000248 off=0x0492e738-0x0492e980 addr=0xfffffe000b932738-0xfffffe000b932980               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b932980-0xfffffe000b932a08               __DATA.__common           (Zerofill)
	sz=0x00000028 off=0x00000000-0x00000028 addr=0xfffffe000b932a08-0xfffffe000b932a30               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001698 off=0x00f9cf28-0x00f9e5c0 addr=0xfffffe0007fa0f28-0xfffffe0007fa25c0 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x00f9cf28-0x00f9cf40 addr=0xfffffe0007fa0f28-0xfffffe0007fa0f40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x00f9cf40-0x00f9cf58 addr=0xfffffe0007fa0f40-0xfffffe0007fa0f58         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001308 off=0x00f9cf58-0x00f9e260 addr=0xfffffe0007fa0f58-0xfffffe0007fa2260         __DATA_CONST.__const            
	sz=0x00000140 off=0x00f9e260-0x00f9e3a0 addr=0xfffffe0007fa2260-0xfffffe0007fa23a0         __DATA_CONST.__kalloc_type      
	sz=0x000001d8 off=0x00f9e3a0-0x00f9e578 addr=0xfffffe0007fa23a0-0xfffffe0007fa2578         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x00f9e578-0x00f9e5c0 addr=0xfffffe0007fa2578-0xfffffe0007fa25c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 127 at 0x04ad14b0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     FE7BBC07-5148-3903-AAD7-4D74AD5B5A15
008: LC_SOURCE_VERSION           207.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96a88 size=0xb0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleAOP2`
- `CFBundleIdentifier`: `com.apple.driver.AppleAOP2`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleAOP2`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleAOP2.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904401280`
- `_PrelinkExecutableRelativePath`: `AppleAOP2`
- `_PrelinkExecutableSize`: `26524`
- `_PrelinkExecutableSourceAddr`: `-2198904401280`
- `_PrelinkKmodInfo`: `-2198829062344`

## Strings (55) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"%s: command queueing is not supported\" @%s:%d`
- `I24@?0r^{aop2kext_iopmassertionoptions=[64C]Q{aop2kext_iopmassertionlevel=Q}}8^(aop2kext_iopm_createiopmassertion__result={aop2kext_iopmerror=Q}{aop2kext_iopmassertion=Q})16`
- `I24@?0r^{aop2kext_iopmassertion=Q}8^(aop2kext_iopm_releaseiopmassertion__result={aop2kext_iopmerror=Q})16`
- `\"TB_ASSERT: \" \"(server->deassertlevel != ((void*)0)) && \\\"implementation for deassertLevel is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `AppleAOP2SystemDriver`
- `site.AppleAOP2SystemDriver`
- `1211111212221212111`
- `12111112122212121111112`
- `/Library/Caches/com.apple.xbs/57229649-1242-47A9-A413-4C1C3C39C74A/TemporaryDirectory.JgIlwB/Sources/AppleAOP2/AppleAOP2Kext/src/Services/IOPMService/AppleAOP2IOPMService.cpp`
- `releaseIOPMAssertion`
- `v32@?0^v8*16Q24`
- `site.AppleAOP2IOPMService`
- `status == 0 `
- `_tb_ep_rev`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->releaseiopmassertion != ((void*)0)) && \\\"implementation for releaseIOPMAssertion is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from createIOPMAssertion\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from deassertLevel\" @%s:%d`
- `success`
- `I24@?0r^{aop2kext_iopmassertion=Q}8^(aop2kext_iopm_assertlevel__result={aop2kext_iopmerror=Q})16`
- `\"TB_FATAL: \" \"invalid result returned from releaseIOPMAssertion\" @%s:%d`
- `createIOPMAssertion`
- `deassertLevel`
- `\"Thread call cannot be NULL\" @%s:%d`
- `com.apple.driver.AppleAOP2IOPMService`
- `AOP2Kext_c.c`
- `\"TB_ASSERT: \" \"(aop2kext_iopmassertionoptions__decode(msg, &options) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AOP2Kext.IOPMAssertionOptions\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->createiopmassertion != ((void*)0)) && \\\"implementation for createIOPMAssertion is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AppleAOP2KextTightbeamEndpoint`
- `CFBundleIdentifier`
- `I24@?0r^{aop2kext_iopmassertion=Q}8^(aop2kext_iopm_deassertlevel__result={aop2kext_iopmerror=Q})16`
- `\"%s: wake transition failed\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `assertLevel`
- `AppleAOP2KextTightbeamEndpoint.cpp`
- `\"%s: ctx->cmdBuffer cannot be NULL\" @%s:%d`
- `AppleAOP2IOPMService.cpp`
- `\"TB_ASSERT: \" \"(server->assertlevel != ((void*)0)) && \\\"implementation for assertLevel is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from assertLevel\" @%s:%d`
- `site.AppleAOP2KextTightbeamEndpoint`
- `site.commandHandlerCtx`
- `112`
- `\"%s: ctx cannot be NULL\" @%s:%d`
- `AppleAOP2IOPMService`
- `_provider`
- `_workloop`
- `_commandGate`
- `12111112122212121111111111`

**[__TEXT.__os_log]**

- `aop2kext_iopm__server_start_owned failed: 0x%x`
- `power state change failed %d`
- `%s: AssertMacros: %s, %s file: %s, line: %d value:%x\n`

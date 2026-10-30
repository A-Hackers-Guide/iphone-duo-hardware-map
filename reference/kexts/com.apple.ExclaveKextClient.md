# `com.apple.ExclaveKextClient`

- Name: ExclaveKextClient
- Version: `1.0.0`
- UUID: `5A632DB8-A0AE-33CC-91A1-6DCC1E960218`
- Source version: `509.40.11.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (2) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/exclaves-test`](../devicetree/root__exclaves-test.md) | `AppleExclaveExampleKext` | `exclaves-test` |
| [`/exclaves-test`](../devicetree/root__exclaves-test.md) | `AppleExclaveExampleKext` | `exclaves-test` |

## IOKit personalities (1) [KC]

### DeviceTreeName
- `CFBundleIdentifier`: `com.apple.ExclaveKextClient`
- `IOClass`: `AppleExclaveExampleKext`
- `IOExclaveProxy`: `True`
- `IONameMatch`: `exclaves-test`
- `IOPersonalityPublisher`: `com.apple.ExclaveKextClient`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`
- `IOUserClientClass`: `AppleExclaveExampleKextUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleExclaveExampleKext` | 0xa8 | IOService → IORegistryEntry |
| `AppleExclaveExampleKextUserClient` | 0xd8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000d58 off=0x00922c00-0x00923958 addr=0xfffffe0007926c00-0xfffffe0007927958 r--/r--   __TEXT            
	sz=0x000006d5 off=0x00923278-0x0092394d addr=0xfffffe0007927278-0xfffffe000792794d               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000008 off=0x00923950-0x00923958 addr=0xfffffe0007927950-0xfffffe0007927958               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00001358 off=0x02c5b710-0x02c5ca68 addr=0xfffffe0009c5f710-0xfffffe0009c60a68 r-x/r-x   __TEXT_EXEC       
	sz=0x00001098 off=0x02c5b710-0x02c5c7a8 addr=0xfffffe0009c5f710-0xfffffe0009c607a8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002c0 off=0x02c5c7a8-0x02c5ca68 addr=0xfffffe0009c607a8-0xfffffe0009c60a68          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049dc288-0x049dc3b0 addr=0xfffffe000b9e0288-0xfffffe000b9e03b0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049dc288-0x049dc350 addr=0xfffffe000b9e0288-0xfffffe000b9e0350               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9e0350-0xfffffe000b9e03b0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f88 off=0x012db100-0x012dc088 addr=0xfffffe00082df100-0xfffffe00082e0088 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012db100-0x012db110 addr=0xfffffe00082df100-0xfffffe00082df110         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012db110-0x012db120 addr=0xfffffe00082df110-0xfffffe00082df120         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000d00 off=0x012db120-0x012dbe20 addr=0xfffffe00082df120-0xfffffe00082dfe20         __DATA_CONST.__const            
	sz=0x00000080 off=0x012dbe20-0x012dbea0 addr=0xfffffe00082dfe20-0xfffffe00082dfea0         __DATA_CONST.__kalloc_type      
	sz=0x00000050 off=0x012dbea0-0x012dbef0 addr=0xfffffe00082dfea0-0xfffffe00082dfef0         __DATA_CONST.__assert           
	sz=0x00000160 off=0x012dbef0-0x012dc050 addr=0xfffffe00082dfef0-0xfffffe00082e0050         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x012dc050-0x012dc088 addr=0xfffffe00082e0050-0xfffffe00082e0088         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 95 at 0x04aeee8c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5A632DB8-A0AE-33CC-91A1-6DCC1E960218
008: LC_SOURCE_VERSION           509.40.11.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9ce0 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `ExclaveKextClient`
- `CFBundleGetInfoString`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.ExclaveKextClient`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ExclaveKextClient`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ExclaveKextClient.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896219136`
- `_PrelinkExecutableRelativePath`: `ExclaveKextClient`
- `_PrelinkExecutableSize`: `12640`
- `_PrelinkExecutableSourceAddr`: `-2198896219136`
- `_PrelinkKmodInfo`: `-2198828350840`

## Strings (28) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleExclaveExampleKext`
- `AppleExclaveExampleKext.cpp`
- `AppleExclaveExampleKext received async notification\n`
- `com.apple.private.apple-exclave-example-kext-user-client`
- `\"TB_ASSERT: \" \"(server->doasyncsignal != ((void*)0)) && \\\"implementation for doAsyncSignal is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `121111121222121211111`
- `AppleExclaveExampleKextResult`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->doasyncsignalwithkevent != ((void*)0)) && \\\"implementation for doAsyncSignalWithKevent is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for Start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `AppleExclaveExampleKext`
- `AppleExclaveExampleKext does not have a workloop\n`
- `AppleExclaveExampleKext result:%d\n`
- `site.AppleExclaveExampleKextUserClient`
- `121111121222121211111111111`
- `IOUserClientDefaultLockingSetProperties`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `\"TB_ASSERT: \" \"(server->add != ((void*)0)) && \\\"implementation for add is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `NULL != tb_endpoint`
- `TB_ERROR_SUCCESS == tberr`
- `v20@?0^{IOInterruptEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^{IOService}iIIBB^{ExpansionData}}8i16`
- `AppleExclaveExampleKextUserClient`
- `IOUserClientDefaultLocking`
- `IOUserClientEntitlements`
- `appleexclaveexamplekext_appleexclaveexamplekext_doasyncsignalwithkevent -> %x\n`
- `AppleExclaveExampleKext_tightbeam.c`

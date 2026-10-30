# `com.apple.driver.AudioSharedDARTMapperProxy`

- Name: SharedDARTMapperProxy
- Version: `410.2`
- UUID: `F0782D48-67FD-3AEE-A2F5-CE4743E88054`
- Source version: `410.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0.0, [`com.apple.driver.ExclavesAudioKext`](com.apple.driver.ExclavesAudioKext.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) | `SharedDARTMapperProxy` | `audio-shared-dart-proxy` |

## IOKit personalities (1) [KC]

### DeviceTreeName
- `CFBundleIdentifier`: `com.apple.driver.AudioSharedDARTMapperProxy`
- `IOClass`: `SharedDARTMapperProxy`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `audio-shared-dart-proxy`
- `IOPersonalityPublisher`: `com.apple.driver.AudioSharedDARTMapperProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `SharedDARTMapperProxy` | 0xb0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001079 off=0x00da4440-0x00da54b9 addr=0xfffffe0007da8440-0xfffffe0007da94b9 r--/r--   __TEXT            
	sz=0x00000020 off=0x00da4ab8-0x00da4ad8 addr=0xfffffe0007da8ab8-0xfffffe0007da8ad8               __TEXT.__const            
	sz=0x000008e9 off=0x00da4ad8-0x00da53c1 addr=0xfffffe0007da8ad8-0xfffffe0007da93c1               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000f8 off=0x00da53c1-0x00da54b9 addr=0xfffffe0007da93c1-0xfffffe0007da94b9               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00005e9c off=0x039971a0-0x0399d03c addr=0xfffffe000a99b1a0-0xfffffe000a9a103c r-x/r-x   __TEXT_EXEC       
	sz=0x00005afc off=0x039971a0-0x0399cc9c addr=0xfffffe000a99b1a0-0xfffffe000a9a0c9c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003a0 off=0x0399cc9c-0x0399d03c addr=0xfffffe000a9a0c9c-0xfffffe000a9a103c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001c0 off=0x04a359c0-0x04a35b80 addr=0xfffffe000ba399c0-0xfffffe000ba39b80 rw-/rw-   __DATA            
	sz=0x00000188 off=0x04a359c0-0x04a35b48 addr=0xfffffe000ba399c0-0xfffffe000ba39b48               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000ba39b48-0xfffffe000ba39b80               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000978 off=0x0149f748-0x014a00c0 addr=0xfffffe00084a3748-0xfffffe00084a40c0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0149f748-0x0149f750 addr=0xfffffe00084a3748-0xfffffe00084a3750         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0149f750-0x0149f758 addr=0xfffffe00084a3750-0xfffffe00084a3758         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000730 off=0x0149f758-0x0149fe88 addr=0xfffffe00084a3758-0xfffffe00084a3e88         __DATA_CONST.__const            
	sz=0x00000040 off=0x0149fe88-0x0149fec8 addr=0xfffffe00084a3e88-0xfffffe00084a3ec8         __DATA_CONST.__kalloc_type      
	sz=0x000001d0 off=0x0149fec8-0x014a0098 addr=0xfffffe00084a3ec8-0xfffffe00084a4098         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x014a0098-0x014a00c0 addr=0xfffffe00084a4098-0xfffffe00084a40c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 121 at 0x04afe444
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F0782D48-67FD-3AEE-A2F5-CE4743E88054
008: LC_SOURCE_VERSION           410.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004acca78 size=0xc8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `SharedDARTMapperProxy`
- `CFBundleGetInfoString`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AudioSharedDARTMapperProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `SharedDARTMapperProxy`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `410.2`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `410.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/SharedDARTMapperProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891494336`
- `_PrelinkExecutableRelativePath`: `SharedDARTMapperProxy`
- `_PrelinkExecutableSize`: `31309`
- `_PrelinkExecutableSourceAddr`: `-2198891494336`
- `_PrelinkKmodInfo`: `-2198827984448`

## Strings (33) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"TB_ASSERT: \" \"(server->resume != ((void*)0)) && \\\"implementation for resume is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `setupUseCase`
- `started`
- `!((mExclaveCommsEndpoint) == nullptr)`
- `suspend`
- `\"TB_ASSERT: \" \"(server->setupusecase != ((void*)0)) && \\\"implementation for setupUseCase is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from setupUseCase\" @%s:%d`
- `I24@?0{shareddartmapperservice_shareddartmapperservice_resume__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `SharedDARTMapperService_C.c`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/SharedDARTMapper/Proxy/Source/SharedDARTMapperProxy.cpp`
- `\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d`
- `v24@?0{shareddartmapperservice_shareddartmapperservice_resume__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_ASSERT: \" \"(server->suspend != ((void*)0)) && \\\"implementation for suspend is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from suspend\" @%s:%d`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `resume`
- `!((mWorkLoop) == nullptr)`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from resume\" @%s:%d`
- `I32@?0{shareddartmapperservice_shareddartmapperservice_setupusecase__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_audiodmabufferspectb_s=QQ})}8`
- `I24@?0{shareddartmapperservice_shareddartmapperservice_suspend__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `v24@?0{shareddartmapperservice_shareddartmapperservice_suspend__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `i8@?0`
- `SharedDARTMapperProxy`
- `site.SharedDARTMapperProxy`
- `1211111212221212111112`
- `!((provider) == nullptr)`
- `ret = ret == 0 `
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`

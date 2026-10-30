# `com.apple.driver.ExclavesAudioKext`

- Name: ExclavesAudioKext
- Version: `410.2`
- UUID: `85CFFF3D-5D40-3FB5-9705-C6BB1528B24B`
- Source version: `410.2.0.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (9) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ExclavesAudioProxyDebugInterface` | 0x18 |  |
| `ExclavesAudioProxyDebugTightbeam` | 0x28 | ExclavesAudioProxyDebugInterface |
| `ExclavesAudioProxyEndpoint` | 0x20 |  |
| `ExclavesAudioProxyInputStreamDriverInterface` | 0x20 |  |
| `ExclavesAudioProxyInputStreamDriverTightbeam` | 0x30 | ExclavesAudioProxyInputStreamDriverInterface |
| `ExclavesAudioProxyOutputStreamDebugInterface` | 0x18 |  |
| `ExclavesAudioProxyOutputStreamDebugTightbeam` | 0x28 | ExclavesAudioProxyOutputStreamDebugInterface |
| `ExclavesAudioProxyOutputStreamDriverInterface` | 0x20 |  |
| `ExclavesAudioProxyOutputStreamDriverTightbeam` | 0x30 | ExclavesAudioProxyOutputStreamDriverInterface |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00006312 off=0x00924910-0x0092ac22 addr=0xfffffe0007928910-0xfffffe000792ec22 r--/r--   __TEXT            
	sz=0x00000058 off=0x00924f88-0x00924fe0 addr=0xfffffe0007928f88-0xfffffe0007928fe0               __TEXT.__const            
	sz=0x000052c4 off=0x00924fe0-0x0092a2a4 addr=0xfffffe0007928fe0-0xfffffe000792e2a4               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000097e off=0x0092a2a4-0x0092ac22 addr=0xfffffe000792e2a4-0xfffffe000792ec22               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000173a8 off=0x02c5ea70-0x02c75e18 addr=0xfffffe0009c62a70-0xfffffe0009c79e18 r-x/r-x   __TEXT_EXEC       
	sz=0x00017048 off=0x02c5ea70-0x02c75ab8 addr=0xfffffe0009c62a70-0xfffffe0009c79ab8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000360 off=0x02c75ab8-0x02c75e18 addr=0xfffffe0009c79ab8-0xfffffe0009c79e18          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000240 off=0x049dc4c8-0x049dc708 addr=0xfffffe000b9e04c8-0xfffffe000b9e0708 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049dc4c8-0x049dc590 addr=0xfffffe000b9e04c8-0xfffffe000b9e0590               __DATA.__data             
	sz=0x00000178 off=0x00000000-0x00000178 addr=0xfffffe000b9e0590-0xfffffe000b9e0708               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001c28 off=0x012dc8f8-0x012de520 addr=0xfffffe00082e08f8-0xfffffe00082e2520 rw-/rw-   __DATA_CONST      
	sz=0x00000048 off=0x012dc8f8-0x012dc940 addr=0xfffffe00082e08f8-0xfffffe00082e0940         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000048 off=0x012dc940-0x012dc988 addr=0xfffffe00082e0940-0xfffffe00082e0988         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001778 off=0x012dc988-0x012de100 addr=0xfffffe00082e0988-0xfffffe00082e2100         __DATA_CONST.__const            
	sz=0x00000240 off=0x012de100-0x012de340 addr=0xfffffe00082e2100-0xfffffe00082e2340         __DATA_CONST.__kalloc_type      
	sz=0x000001b0 off=0x012de340-0x012de4f0 addr=0xfffffe00082e2340-0xfffffe00082e24f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x012de4f0-0x012de520 addr=0xfffffe00082e24f0-0xfffffe00082e2520         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 114 at 0x04aef174
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     85CFFF3D-5D40-3FB5-9705-C6BB1528B24B
008: LC_SOURCE_VERSION           410.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9d90 size=0x348
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `ExclavesAudioKext`
- `CFBundleIdentifier`: `com.apple.driver.ExclavesAudioKext`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ExclavesAudioKext`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/ExclavesAudioKext.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896211696`
- `_PrelinkExecutableRelativePath`: `ExclavesAudioKext`
- `_PrelinkExecutableSize`: `128290`
- `_PrelinkExecutableSourceAddr`: `-2198896211696`
- `_PrelinkKmodInfo`: `-2198828350264`

## Strings (175) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
- `Bad physical description index: %hhu`

**[__TEXT.__cstring]**

- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `I24@?0{audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I24@?0{exclavesaudiodrivers_audiodriver_selectphysicalstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `v24@?0{exclavesaudiodrivers_audiodriver_selectphysicalstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = getStreamDescriptionRet == 0 `
- `ret = wakeRet == 0 `
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_mapdmabuffer( &kECDevice, ^(audiostreamdriver_audiostreamdriver_mapdmabuffer__result_s result) { if (!audiostreamdriver_audiostreamdriver_mapdmabuffer__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_mapd`
- `ret = ioReturnFromTBError(audiodriverdebug_audiodebug__init(&client, mTightbeamEndpoint)) == 0 `
- `\"TB_ASSERT: \" \"(exclavesaudiodrivers_exadstreamdescriptionselector__decode(msg, &inSelector) == TB_ERROR_SUCCESS) && \\\"failed to decode type: ExclavesAudioDrivers.ExADStreamDescriptionSelector\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I24@?0{audiostreamdriver_audioinputstreamdriver_readinput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid result returned from wake\" @%s:%d`
- `v24@?0{audiostreamdriver_audiostreamdriver_teardownio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_teardownio( &kECDevice, ^(audiostreamdriver_audiostreamdriver_teardownio__result_s result) { if (!audiostreamdriver_audiostreamdriver_teardownio__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_teardownio`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `readInput`
- `enableInjection`
- `v24@?0{audiostreamdriver_audiostreamdriver_sleep__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `site.ExclavesAudioProxyOutputStreamDebugInterface`
- `inProxy->exclaveStart(inProvider, &mExclaveState)`
- `\"TB_ASSERT: \" \"(server->mapdmabuffer != ((void*)0)) && \\\"implementation for mapDMABuffer is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `v24@?0{audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `!((inEndpoint) == nullptr)`
- `ExclavesAudioProxyInputStreamDriverInterface`
- `v24@?0{exclavesaudiodrivers_audiodriver_teardownclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = readInputRet == 0 `
- `ExclavesAudioProxyOutputStreamDebugInterface`
- `site.ExclavesAudioProxyDebugInterface`
- `I24@?0{audiostreamdriver_audioinputstreamdriver_teardownclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError( audiodriverdebug_audiooutputstreamdebug__init(&client, mTightbeamEndpoint)) == 0 `
- `!((inProvider) == nullptr)`
- `site.ExclavesAudioProxyInputStreamDriverInterface`
- `I24@?0{exclavesaudiodrivers_audiodriver_mapdmabuffer__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I24@?0{exclavesaudiodrivers_audiodriver_wake__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid result returned from setupIO\" @%s:%d`
- `getStreamDescription`
- `mapDMABuffer`
- `ExclavesAudioKext_C.c`
- `I24@?0{audiostreamdriver_audiostreamdriver_teardownio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid result returned from teardownClientIO\" @%s:%d`
- `v24@?0{exclavesaudiodrivers_audiodriver_setupio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `v32@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8`
- `v24@?0{audiodriverdebug_audiodebug_enableinjection__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = enableInjectionIORet == 0 `
- `ExclavesAudioProxyEndpoint`
- `\"TB_ASSERT: \" \"(server->teardownio != ((void*)0)) && \\\"implementation for teardownIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `ret = selectPhysicalStreamDescription(index) == 0 `
- `ret = teardownClientIORet == 0 `
- `v24@?0{exclavesaudiodrivers_audiodriver_sleep__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `numPhysicalDescriptions > 0`
- `\"TB_ASSERT: \" \"(server->sleep != ((void*)0)) && \\\"implementation for sleep is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->teardownclientio != ((void*)0)) && \\\"implementation for teardownClientIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `writeMixOutput`
- `ret = setupClientIORet == 0 `
- `v24@?0{exclavesaudiodrivers_audiodriver_wake__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/OutputStream/ExclavesAudioProxyOutputStreamDriverInterface.cpp`
- `v24@?0{audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ExclavesAudioProxyOutputStreamDebugTightbeam`
- `ExclavesAudioProxyDebugInterface`
- `I32@?0{exclavesaudiodrivers_audiodriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8`
- `\"TB_FATAL: \" \"invalid result returned from writeMixOutput\" @%s:%d`
- `ExclavesAudioProxyOutputStreamDriverInterface`
- `ExclavesAudioProxyDebugTightbeam`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Endpoint/ExclavesAudioProxyEndpoint.cpp`
- `!((outTBEndpoint) == nullptr)`
- `\"TB_FATAL: \" \"invalid result returned from setupClientIO\" @%s:%d`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_setupclientio( &kECDevice, clientIdentifier, ^(exclavesaudiodrivers_audiodriver_setupclientio__result_s result) { if (!exclavesaudiodrivers_audiodriver_setupclientio__result_get_success(&result)) { auto failure = exclavesaudiodrivers_audiodr`
- `!(i == numPhysicalDescriptions)`
- `I24@?0{audiostreamdriver_audiostreamdriver_wake__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `12111`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/OutputStream/ExclavesAudioProxyOutputStreamDebugInterface.cpp`
- `I24@?0{exclavesaudiodrivers_audiodriver_setupio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid result returned from getStreamDescription\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from teardownIO\" @%s:%d`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `teardownClientIO`
- `\"TB_FATAL: \" \"invalid result returned from enableAltSource\" @%s:%d`
- `121`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/InputStream/ExclavesAudioProxyDebugInterface.cpp`
- `\"TB_ASSERT: \" \"(server->getstreamdescription != ((void*)0)) && \\\"implementation for getStreamDescription is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `selectPhysicalStreamDescription`
- `121111`
- `v24@?0{exclavesaudiodrivers_audiodriver_setupclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_readinput( &kECDevice, clientIdentifier, inSampleTime, inFrames, ^(exclavesaudiodrivers_audiodriver_readinput__result_s result) { if (!exclavesaudiodrivers_audiodriver_readinput__result_get_success(&result)) { auto failure = exclavesaudiodri`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/OutputStream/ExclavesAudioProxyOutputStreamDriverTightbeam.cpp`
- `site.ExclavesAudioProxyDebugTightbeam`
- `setupIO`
- `teardownIO`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_teardownclientio( &kECDevice, clientIdentifier, ^(exclavesaudiodrivers_audiodriver_teardownclientio__result_s result) { if (!exclavesaudiodrivers_audiodriver_teardownclientio__result_get_success(&result)) { auto failure = exclavesaudiodriver`
- `v24@?0{audiostreamdriver_audiostreamdriver_setupio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError(audiostreamdriver_audiooutputstreamdriver_writemixoutput( &kECDevice, inSampleTime, inFrames, ^(audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_s result) { if (!audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_get_success( &result)) { auto f`
- `ret = readOutputRet == 0 `
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_wake( &kECDevice, ^(audiostreamdriver_audiostreamdriver_wake__result_s result) { if (!audiostreamdriver_audiostreamdriver_wake__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_wake__result_get_failure(&re`
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_sleep( &kECDevice, ^(audiostreamdriver_audiostreamdriver_sleep__result_s result) { if (!audiostreamdriver_audiostreamdriver_sleep__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_sleep__result_get_failure`
- `I24@?0{audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_selectphysicalstreamdescription( &kECDevice, &selector, ^(exclavesaudiodrivers_audiodriver_selectphysicalstreamdescription__result_s result) { if (!exclavesaudiodrivers_audiodriver_selectphysicalstreamdescription__result_get_success( &result`
- `v24@?0{exclavesaudiodrivers_audiodriver_mapdmabuffer__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = teardownIORet == 0 `
- `I24@?0{audiostreamdriver_audiostreamdriver_sleep__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `enableAltSource`
- `ExclavesAudioProxyInputStreamDriverTightbeam`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverTightbeam.cpp`
- `site.ExclavesAudioProxyOutputStreamDriverTightbeam`
- `setupClientIO`
- `ret = super::initWithEndpoint(inProvider, inEndpoint) == 0 `
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/OutputStream/ExclavesAudioProxyOutputStreamDebugTightbeam.cpp`
- `physical-descriptions`
- `\"TB_ASSERT: \" \"(server->selectphysicalstreamdescription != ((void*)0)) && \\\"implementation for selectPhysicalStreamDescription is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->wake != ((void*)0)) && \\\"implementation for wake is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->enablealtsource != ((void*)0)) && \\\"implementation for enableAltSource is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_setupio( &kECDevice, ^(exclavesaudiodrivers_audiodriver_setupio__result_s result) { if (!exclavesaudiodrivers_audiodriver_setupio__result_get_success(&result)) { auto failure = exclavesaudiodrivers_audiodriver_setupio__result_get_failure(&re`
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Driver/InputStream/ExclavesAudioProxyInputStreamDriverInterface.cpp`
- `I24@?0{audiostreamdriver_audiostreamdriver_mapdmabuffer__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I24@?0{exclavesaudiodrivers_audiodriver_teardownclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I24@?0{exclavesaudiodrivers_audiodriver_readinput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_getstreamdescription( &kECDevice, ^(exclavesaudiodrivers_audiodriver_getstreamdescription__result_s result) { auto success = exclavesaudiodrivers_audiodriver_getstreamdescription__result_get_success(&result); if (success != nullptr) { ecStre`
- `ret = clientIdentifierForID(inClientID, clientIdentifier) == 0 `
- `ExclavesAudioProxyOutputStreamDriverTightbeam`
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_setupio( &kECDevice, ^(audiostreamdriver_audiostreamdriver_setupio__result_s result) { if (!audiostreamdriver_audiostreamdriver_setupio__result_get_success(&result)) { auto failure = audiostreamdriver_audiostreamdriver_setupio__result_get`
- `site.ExclavesAudioProxyOutputStreamDebugTightbeam`
- `ret = enableAltSourceIORet == 0 `
- `!((mProxy) == nullptr)`
- `I24@?0{audiodriverdebug_audiodebug_enableinjection__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `v24@?0{exclavesaudiodrivers_audiodriver_teardownio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_teardownio( &kECDevice, ^(exclavesaudiodrivers_audiodriver_teardownio__result_s result) { if (!exclavesaudiodrivers_audiodriver_teardownio__result_get_success(&result)) { auto failure = exclavesaudiodrivers_audiodriver_teardownio__result_get`
- `I24@?0{audiostreamdriver_audioinputstreamdriver_setupclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_ASSERT: \" \"(server->readinput != ((void*)0)) && \\\"implementation for readInput is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I24@?0{audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `wake`
- `ret = ioReturnFromTBError(audiodriverdebug_audiooutputstreamdebug_enablealtsource( &kECDevice, inEnable, ^(audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_s result) { if (!audiodriverdebug_audiooutputstreamdebug_enablealtsource__result_get_success( &result)) { auto failure = audiodri`
- `!((inStreamDescription.mFormatFlags & kIOAudio2FormatFlagIsBigEndian) != 0)`
- `I24@?0{exclavesaudiodrivers_audiodriver_teardownio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from mapDMABuffer\" @%s:%d`
- `v32@?0{exclavesaudiodrivers_audiodriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8`
- `ret = setupIORet == 0 `
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_sleep( &kECDevice, ^(exclavesaudiodrivers_audiodriver_sleep__result_s result) { if (!exclavesaudiodrivers_audiodriver_sleep__result_get_success(&result)) { auto failure = exclavesaudiodrivers_audiodriver_sleep__result_get_failure(&result); s`
- `v24@?0{audiostreamdriver_audiostreamdriver_wake__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I24@?0{exclavesaudiodrivers_audiodriver_setupclientio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `unknown class?`
- `ret = sleepRet == 0 `
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_wake( &kECDevice, ^(exclavesaudiodrivers_audiodriver_wake__result_s result) { if (!exclavesaudiodrivers_audiodriver_wake__result_get_success(&result)) { auto failure = exclavesaudiodrivers_audiodriver_wake__result_get_failure(&result); wakeR`
- `ret = ioReturnFromTBError(audiodriverdebug_audiodebug_enableinjection( &kECDevice, inEnable, ^(audiodriverdebug_audiodebug_enableinjection__result_s result) { if (!audiodriverdebug_audiodebug_enableinjection__result_get_success(&result)) { auto failure = audiodriverdebug_audiodebug_enableinjection__`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I24@?0{audiostreamdriver_audiostreamdriver_setupio__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_ASSERT: \" \"(server->setupclientio != ((void*)0)) && \\\"implementation for setupClientIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->enableinjection != ((void*)0)) && \\\"implementation for enableInjection is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I24@?0{exclavesaudiodrivers_audiodriver_sleep__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid result returned from sleep\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from enableInjection\" @%s:%d`
- `sleep`
- `\"TB_FATAL: \" \"invalid result returned from readInput\" @%s:%d`
- `ret = selectPhysicalStreamDescriptionRet == 0 `
- `ret = findMatchingStreamDescriptionIndex(inStreamDescription, inStreamBufferFrameSize, index) == 0 `
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver_mapdmabuffer( &kECDevice, ^(exclavesaudiodrivers_audiodriver_mapdmabuffer__result_s result) { if (!exclavesaudiodrivers_audiodriver_mapdmabuffer__result_get_success(&result)) { auto failure = exclavesaudiodrivers_audiodriver_mapdmabuffer__re`
- `ret = mEndpoint->createTightbeamEndpoint(mTightbeamEndpoint) == 0 `
- `/Library/Caches/com.apple.xbs/569F7C41-9BF4-4F05-9823-336262798540/TemporaryDirectory.Teyonp/Sources/ExclavesAudioDrivers/ExclavesAudioKext/ExclavesAudioProxy/Debug/InputStream/ExclavesAudioProxyDebugTightbeam.cpp`
- `site.ExclavesAudioProxyEndpoint`
- `v24@?0{audiostreamdriver_audiostreamdriver_mapdmabuffer__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `1211`
- `\"TB_FATAL: \" \"invalid result returned from selectPhysicalStreamDescription\" @%s:%d`
- `site.ExclavesAudioProxyInputStreamDriverTightbeam`
- `site.ExclavesAudioProxyOutputStreamDriverInterface`
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription( &kECDevice, &selector, ^(audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_s result) { if (!audiostreamdriver_audiostreamdriver_selectphysicalstreamdescription__result_get_success`
- `ret = ioReturnFromTBError(audiostreamdriver_audiostreamdriver_getstreamdescription( &kECDevice, ^(audiostreamdriver_audiostreamdriver_getstreamdescription__result_s result) { auto success = audiostreamdriver_audiostreamdriver_getstreamdescription__result_get_success( &result); if (success != nullptr`
- `\"TB_ASSERT: \" \"(server->setupio != ((void*)0)) && \\\"implementation for setupIO is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `ret = ioReturnFromTBError( audiostreamdriver_audiostreamdriver__init(&client, mTightbeamEndpoint)) == 0 `
- `v24@?0{audiostreamdriver_audiooutputstreamdriver_writemixoutput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_ASSERT: \" \"(server->writemixoutput != ((void*)0)) && \\\"implementation for writeMixOutput is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `ret = ioReturnFromTBError(exclavesaudiodrivers_audiodriver__init(&client, mTightbeamEndpoint)) == 0 `
- `v24@?0{exclavesaudiodrivers_audiodriver_readinput__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `I32@?0{audiostreamdriver_audiostreamdriver_getstreamdescription__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q}{exclavesaudiodrivers_exadstreamdescription_s=IIISCC})}8`

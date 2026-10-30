# `com.apple.driver.IISAudioIsolatedStreamECProxy`

- Name: IISAudioIsolatedStreamECProxy
- Version: `610.2`
- UUID: `CFF3E3E4-B5AD-34D1-9D93-0199A090061A`
- Source version: `610.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.ExclavesAudioKext`](com.apple.driver.ExclavesAudioKext.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/audio-speaker-tx-stream-proxy`](../devicetree/root__arm-io__audio-speaker-tx-stream-proxy.md) | `IISAudioIsolatedOutputStreamECProxy` | `iisaudio,isolated-output-stream-proxy` |
| [`/arm-io/audio-receiver-tx-stream-proxy`](../devicetree/root__arm-io__audio-receiver-tx-stream-proxy.md) | `IISAudioIsolatedOutputStreamECProxy` | `iisaudio,isolated-output-stream-proxy` |
| [`/arm-io/audio-sllb-proxy`](../devicetree/root__arm-io__audio-sllb-proxy.md) | `IISAudioIsolatedStreamECProxy` | `iisaudio,isolated-stream-proxy` |
| [`/arm-io/audio-hp-proxy`](../devicetree/root__arm-io__audio-hp-proxy.md) | `IISAudioIsolatedStreamECProxy` | `iisaudio,isolated-stream-proxy` |

## IOKit personalities (2) [KC]

### IISAudioIsolatedOutputStreamECProxy
- `CFBundleIdentifier`: `com.apple.driver.IISAudioIsolatedStreamECProxy`
- `IOClass`: `IISAudioIsolatedOutputStreamECProxy`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `iisaudio,isolated-output-stream-proxy`
- `IOPersonalityPublisher`: `com.apple.driver.IISAudioIsolatedStreamECProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`

### IISAudioIsolatedStreamECProxy
- `CFBundleIdentifier`: `com.apple.driver.IISAudioIsolatedStreamECProxy`
- `IOClass`: `IISAudioIsolatedStreamECProxy`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `iisaudio,isolated-stream-proxy`
- `IOPersonalityPublisher`: `com.apple.driver.IISAudioIsolatedStreamECProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IISAudioIsolatedOutputStreamECProxy` | 0xa8 | IOService → IORegistryEntry |
| `IISAudioIsolatedStreamECProxy` | 0xa0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000e98 off=0x0096ece0-0x0096fb78 addr=0xfffffe0007972ce0-0xfffffe0007973b78 r--/r--   __TEXT            
	sz=0x000004bc off=0x0096f358-0x0096f814 addr=0xfffffe0007973358-0xfffffe0007973814               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000364 off=0x0096f814-0x0096fb78 addr=0xfffffe0007973814-0xfffffe0007973b78               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000020dc off=0x02eabcd0-0x02eaddac addr=0xfffffe0009eafcd0-0xfffffe0009eb1dac r-x/r-x   __TEXT_EXEC       
	sz=0x00001f8c off=0x02eabcd0-0x02eadc5c addr=0xfffffe0009eafcd0-0xfffffe0009eb1c5c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000150 off=0x02eadc5c-0x02eaddac addr=0xfffffe0009eb1c5c-0xfffffe0009eb1dac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000138 off=0x049eb480-0x049eb5b8 addr=0xfffffe000b9ef480-0xfffffe000b9ef5b8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049eb480-0x049eb548 addr=0xfffffe000b9ef480-0xfffffe000b9ef548               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9ef548-0xfffffe000b9ef5a8               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9ef5a8-0xfffffe000b9ef5b8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000d60 off=0x012f5dd0-0x012f6b30 addr=0xfffffe00082f9dd0-0xfffffe00082fab30 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012f5dd0-0x012f5de0 addr=0xfffffe00082f9dd0-0xfffffe00082f9de0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012f5de0-0x012f5df0 addr=0xfffffe00082f9de0-0xfffffe00082f9df0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000bf0 off=0x012f5df0-0x012f69e0 addr=0xfffffe00082f9df0-0xfffffe00082fa9e0         __DATA_CONST.__const            
	sz=0x00000080 off=0x012f69e0-0x012f6a60 addr=0xfffffe00082fa9e0-0xfffffe00082faa60         __DATA_CONST.__kalloc_type      
	sz=0x000000a8 off=0x012f6a60-0x012f6b08 addr=0xfffffe00082faa60-0xfffffe00082fab08         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x012f6b08-0x012f6b30 addr=0xfffffe00082fab08-0xfffffe00082fab30         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 47 at 0x04aef5e0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CFF3E3E4-B5AD-34D1-9D93-0199A090061A
008: LC_SOURCE_VERSION           610.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aba3d8 size=0x70
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IISAudioIsolatedStreamECProxy`
- `CFBundleIdentifier`: `com.apple.driver.IISAudioIsolatedStreamECProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IISAudioIsolatedStreamECProxy`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `610.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `610.2`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IISAudioIsolatedStreamECProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895907616`
- `_PrelinkExecutableRelativePath`: `IISAudioIsolatedStreamECProxy`
- `_PrelinkExecutableSize`: `15884`
- `_PrelinkExecutableSourceAddr`: `-2198895907616`
- `_PrelinkKmodInfo`: `-2198828288896`

## Strings (26) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`

**[__TEXT.__cstring]**

- `/Library/Caches/com.apple.xbs/5D58D6FB-4B9B-48DB-AF57-4EB20C99A843/TemporaryDirectory.zSX0o6/Sources/AppleARMIISAudio/src/kext/IsolatedStreamECProxy/IOService/IISAudioIsolatedOutputStreamECProxy.cpp`
- `IISAudio,IsolatedStreamHandle`
- `12111112122212121111`
- `!((mDebugInterface) == nullptr)`
- `ret = setIsolatedStreamHandleProperty(inProvider, this) == 0 `
- `!((inProvider) == nullptr)`
- `IISAudioIsolatedOutputStreamECProxy`
- `IISAudio::IsolatedOutputStreamECProxy`
- `IISAudioIsolatedStreamECProxy`
- `site.IISAudioIsolatedStreamECProxy`
- `!((inPhandle) == nullptr)`
- `!((mEndpoint) == nullptr)`
- `ret = mDebugInterface->enableInjection(inEnable) == 0 `
- `!((phandleData) == nullptr)`
- `site.IISAudioIsolatedOutputStreamECProxy`
- `/Library/Caches/com.apple.xbs/5D58D6FB-4B9B-48DB-AF57-4EB20C99A843/TemporaryDirectory.zSX0o6/Sources/AppleARMIISAudio/src/kext/IsolatedStreamECProxy/IOService/IISAudioIsolatedStreamECProxy.cpp`
- `AppleAudioSystemHelper::supportsExclaves()`
- `ret = _configure(inProvider) == 0 `
- `IISAudio,IsolatedOutputStreamHandle`
- `121111121222121211112`
- `ret = mDebugInterface->enableAltSource(inEnable) == 0 `
- `!(AppleAudioSystemHelper::isInRestore())`
- `!(AppleAudioSystemHelper::isInRecovery())`
- `super::start(inProvider)`
- `!((mDriverInterface) == nullptr)`

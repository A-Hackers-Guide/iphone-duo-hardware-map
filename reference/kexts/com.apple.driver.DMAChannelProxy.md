# `com.apple.driver.DMAChannelProxy`

- Name: DMAChannelProxy
- Version: `600.45`
- UUID: `91FCD05F-A6C3-3809-B81A-57697A68B859`
- Source version: `600.45.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.driver.AudioSharedDARTMapperProxy`](com.apple.driver.AudioSharedDARTMapperProxy.md) 1.0, [`com.apple.driver.ExclavesAudioKext`](com.apple.driver.ExclavesAudioKext.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) | `DMAChannelProxy` | `admac-ec-proxy` |
| [`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) | `DMAChannelProxy` | `admac-ec-proxy` |
| [`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) | `DMAChannelProxy` | `admac-ec-proxy` |
| [`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) | `DMAChannelProxy` | `admac-ec-proxy` |

## IOKit personalities (1) [KC]

### DeviceTreeName
- `CFBundleIdentifier`: `com.apple.driver.DMAChannelProxy`
- `IOClass`: `DMAChannelProxy`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `admac-leap-s-proxy`
  - `admac-base-s-proxy`
  - `admac-ec-proxy`
- `IOPersonalityPublisher`: `com.apple.driver.DMAChannelProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `DMAChannelECProxyInterface` | 0x88 | IOService → IORegistryEntry |
| `DMAChannelProxy` | 0xc8 | DMAChannelECProxyInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000c4e off=0x00917790-0x009183de addr=0xfffffe000791b790-0xfffffe000791c3de r--/r--   __TEXT            
	sz=0x00000020 off=0x00917db8-0x00917dd8 addr=0xfffffe000791bdb8-0xfffffe000791bdd8               __TEXT.__const            
	sz=0x00000606 off=0x00917dd8-0x009183de addr=0xfffffe000791bdd8-0xfffffe000791c3de               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00004c00 off=0x02c2fd40-0x02c34940 addr=0xfffffe0009c33d40-0xfffffe0009c38940 r-x/r-x   __TEXT_EXEC       
	sz=0x00004800 off=0x02c2fd40-0x02c34540 addr=0xfffffe0009c33d40-0xfffffe0009c38540          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000400 off=0x02c34540-0x02c34940 addr=0xfffffe0009c38540-0xfffffe0009c38940          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049dbc18-0x049dbd40 addr=0xfffffe000b9dfc18-0xfffffe000b9dfd40 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049dbc18-0x049dbce0 addr=0xfffffe000b9dfc18-0xfffffe000b9dfce0               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9dfce0-0xfffffe000b9dfd40               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f80 off=0x012d5ce0-0x012d6c60 addr=0xfffffe00082d9ce0-0xfffffe00082dac60 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012d5ce0-0x012d5ce8 addr=0xfffffe00082d9ce0-0xfffffe00082d9ce8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012d5ce8-0x012d5cf0 addr=0xfffffe00082d9ce8-0xfffffe00082d9cf0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cd0 off=0x012d5cf0-0x012d69c0 addr=0xfffffe00082d9cf0-0xfffffe00082da9c0         __DATA_CONST.__const            
	sz=0x00000080 off=0x012d69c0-0x012d6a40 addr=0xfffffe00082da9c0-0xfffffe00082daa40         __DATA_CONST.__kalloc_type      
	sz=0x00000200 off=0x012d6a40-0x012d6c40 addr=0xfffffe00082daa40-0xfffffe00082dac40         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x012d6c40-0x012d6c60 addr=0xfffffe00082dac40-0xfffffe00082dac60         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 132 at 0x04aee40c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     91FCD05F-A6C3-3809-B81A-57697A68B859
008: LC_SOURCE_VERSION           600.45.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9720 size=0xb8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `DMAChannelProxy`
- `CFBundleGetInfoString`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.DMAChannelProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `DMAChannelProxy`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.45`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/DMAChannelProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896265328`
- `_PrelinkExecutableRelativePath`: `DMAChannelProxy`
- `_PrelinkExecutableSize`: `26870`
- `_PrelinkExecutableSourceAddr`: `-2198896265328`
- `_PrelinkKmodInfo`: `-2198828352488`

## Strings (30) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `DMAChannelECProxyInterface`
- `start`
- `\"TB_ASSERT: \" \"(server->enqueuedescriptor != ((void*)0)) && \\\"implementation for enqueueDescriptor is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `%s`
- `DMAChannelProxy`
- `proxy-is-development-only`
- `map-word-reg`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `%s: %d: Done with exclaveStart.\n`
- `enqueueDescriptor`
- `%s: %d: About to exclaveStart.\n`
- `@`
- `site.DMAChannelECProxyInterface`
- `v24@?0{audiodmachannel_dmachannel_enqueuedescriptor__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_FATAL: \" \"invalid value: unexpected bits, 0x%llx\" @%s:%d`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `1211111212221212111121112`
- `function-iommu_handler`
- `map-word`
- `AudioDMAChannel_C.c`
- `I24@?0{audiodmachannel_dmachannel_enqueuedescriptor__result_s=C(?={exclavesaudiodrivers_exadresult_s=Q})}8`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->stoptransfer != ((void*)0)) && \\\"implementation for stopTransfer is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `site.DMAChannelProxy`
- `I8@?0`
- `\"TB_FATAL: \" \"invalid result returned from enqueueDescriptor\" @%s:%d`
- `12111112122212121`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`

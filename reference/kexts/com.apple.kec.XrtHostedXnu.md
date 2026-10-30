# `com.apple.kec.XrtHostedXnu`

- Name: XrtHostedXnu
- Version: `1`
- UUID: `E05711EE-2E1C-3769-AE08-ECD775EA20D3`
- Source version: `1490.40.28.0.0`
- Depends on: [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1080)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b80 off=0x00da9750-0x00daa2d0 addr=0xfffffe0007dad750-0xfffffe0007dae2d0 r--/r--   __TEXT            
	sz=0x00000204 off=0x00da9bf0-0x00da9df4 addr=0xfffffe0007dadbf0-0xfffffe0007daddf4               __TEXT.__const            
	sz=0x000004dc off=0x00da9df4-0x00daa2d0 addr=0xfffffe0007daddf4-0xfffffe0007dae2d0               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001b64 off=0x039aab20-0x039ac684 addr=0xfffffe000a9aeb20-0xfffffe000a9b0684 r-x/r-x   __TEXT_EXEC       
	sz=0x00001b44 off=0x039aab20-0x039ac664 addr=0xfffffe000a9aeb20-0xfffffe000a9b0664          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000020 off=0x039ac664-0x039ac684 addr=0xfffffe000a9b0664-0xfffffe000a9b0684          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000220 off=0x04a35e08-0x04a36028 addr=0xfffffe000ba39e08-0xfffffe000ba3a028 rw-/rw-   __DATA            
	sz=0x000000d8 off=0x04a35e08-0x04a35ee0 addr=0xfffffe000ba39e08-0xfffffe000ba39ee0               __DATA.__data             
	sz=0x00000148 off=0x00000000-0x00000148 addr=0xfffffe000ba39ee0-0xfffffe000ba3a028               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000010 off=0x014a2b18-0x014a2b28 addr=0xfffffe00084a6b18-0xfffffe00084a6b28 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x014a2b18-0x014a2b28 addr=0xfffffe00084a6b18-0xfffffe00084a6b28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 4 at 0x04afe9dc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E05711EE-2E1C-3769-AE08-ECD775EA20D3
008: LC_SOURCE_VERSION           1490.40.28.0.0
009: LC_FUNCTION_STARTS          offset=0x004accdb8 size=0x78
```

## Info.plist keys [KC]

- `AppleKernelExternalComponent`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `XrtHostedXnu`
- `CFBundleIdentifier`: `com.apple.kec.XrtHostedXnu`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `XrtHostedXnu`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleAllowUserLoad`: `False`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/XrtHostedXnu.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891473072`
- `_PrelinkExecutableRelativePath`: `XrtHostedXnu`
- `_PrelinkExecutableSize`: `10516`
- `_PrelinkExecutableSourceAddr`: `-2198891473072`
- `_PrelinkKmodInfo`: `-2198827983352`

## Strings (28) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `copy->v1.size.root <= sans_footer`
- `global_size >= sizeof(XrtHosted_Global_t)`
- `copy->v1.size.core.request <= copy->v1.size.core.total`
- `request_size >= sizeof(XrtHosted_Buffer_t)`
- `page_cores_words <= sans_footer`
- `copy->v1.size.global <= sans_footer`
- `/Library/Caches/com.apple.xbs/FB8349A7-73B0-45E8-9D61-A978687BED28/TemporaryDirectory.I3hwn6/Sources/ExclavePlatform_kernel/native-scheduler/XrtHosted/hosted.c`
- `_page_has_index(copy, current)`
- `_hosted_validate`
- `(base & XrtHosted_Page_mask) == 0`
- `footer_size >= sizeof(XrtHosted__Page_t)`
- `core_contents <= copy->v1.size.core.total`
- `core_state_size >= sizeof(XrtHosted_Core_t)`
- `XrtHosted_nextPhys`
- `copy->v1.size.page <= page_words`
- `copy->v1.size.core.total <= sans_footer`
- `copy->v1.size.core.state <= copy->v1.size.core.total`
- `copy->v1.size.core.response <= copy->v1.size.core.total`
- `global_page_offset + copy->v1.size.global <= sans_footer`
- `copy->v1.offset.core.request >= copy->v1.size.core.state`
- `copy->v1.offset.core.response >= request_top`
- `copy->page.sizeLog2 == XrtHosted_Page_sizeLog2`
- `copy->version.xrt >= version`
- `root_size >= sizeof(XrtHosted__Root_t)`
- `response_size >= sizeof(XrtHosted_Buffer_t)`
- `copy->v1.offset.global >= copy->v1.size.root`
- `core_0_offset >= global_top`
- `copy->v1.size.core.total >= response_top`

# `com.apple.driver.usb.AppleUSBCommon`

- Name: AppleUSBCommon
- Version: `1.0`
- UUID: `08094EE1-E375-30D6-AAC9-BCF346BC6904`
- Source version: `1617.40.10.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 23.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 23.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 23.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 23.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 23.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBDescriptor` | 0x20 |  |
| `AppleUSBDescriptorCache` | 0x20 |  |
| `AppleUSBRequest` | 0x38 | IOCommand |
| `AppleUSBRequestCompleter` | 0xb0 | IOEventSource |
| `AppleUSBRequestPool` | 0x60 | IOCommandPool |
| `AppleUSBSparseArray` | 0x28 | OSCollection |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b87 off=0x008cfde0-0x008d0967 addr=0xfffffe00078d3de0-0xfffffe00078d4967 r--/r--   __TEXT            
	sz=0x00000365 off=0x008d04f8-0x008d085d addr=0xfffffe00078d44f8-0xfffffe00078d485d               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000018 off=0x008d0860-0x008d0878 addr=0xfffffe00078d4860-0xfffffe00078d4878               __TEXT.__const            
	sz=0x000000ef off=0x008d0878-0x008d0967 addr=0xfffffe00078d4878-0xfffffe00078d4967               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00005e7c off=0x02b132a0-0x02b1911c addr=0xfffffe0009b172a0-0xfffffe0009b1d11c r-x/r-x   __TEXT_EXEC       
	sz=0x00005adc off=0x02b132a0-0x02b18d7c addr=0xfffffe0009b172a0-0xfffffe0009b1cd7c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003a0 off=0x02b18d7c-0x02b1911c addr=0xfffffe0009b1cd7c-0xfffffe0009b1d11c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001e0 off=0x049d0928-0x049d0b08 addr=0xfffffe000b9d4928-0xfffffe000b9d4b08 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d0928-0x049d09f0 addr=0xfffffe000b9d4928-0xfffffe000b9d49f0               __DATA.__data             
	sz=0x00000110 off=0x00000000-0x00000110 addr=0xfffffe000b9d49f0-0xfffffe000b9d4b00               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000b9d4b00-0xfffffe000b9d4b08               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000010e0 off=0x012a1f70-0x012a3050 addr=0xfffffe00082a5f70-0xfffffe00082a7050 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x012a1f70-0x012a1f98 addr=0xfffffe00082a5f70-0xfffffe00082a5f98         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x012a1f98-0x012a1fc0 addr=0xfffffe00082a5f98-0xfffffe00082a5fc0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000a70 off=0x012a1fc0-0x012a2a30 addr=0xfffffe00082a5fc0-0xfffffe00082a6a30         __DATA_CONST.__const            
	sz=0x00000280 off=0x012a2a30-0x012a2cb0 addr=0xfffffe00082a6a30-0xfffffe00082a6cb0         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x012a2cb0-0x012a2df0 addr=0xfffffe00082a6cb0-0xfffffe00082a6df0         __DATA_CONST.__kalloc_var       
	sz=0x000001d0 off=0x012a2df0-0x012a2fc0 addr=0xfffffe00082a6df0-0xfffffe00082a6fc0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000090 off=0x012a2fc0-0x012a3050 addr=0xfffffe00082a6fc0-0xfffffe00082a7050         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 134 at 0x04aeb594
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     08094EE1-E375-30D6-AAC9-BCF346BC6904
008: LC_SOURCE_VERSION           1617.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7308 size=0x110
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBCommon`
- `CFBundleIdentifier`: `com.apple.driver.usb.AppleUSBCommon`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBCommon`
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
- `NSHumanReadableCopyright`: `Copyright © 2000-2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBCommon.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896558624`
- `_PrelinkExecutableRelativePath`: `AppleUSBCommon`
- `_PrelinkExecutableSize`: `31939`
- `_PrelinkExecutableSourceAddr`: `-2198896558624`
- `_PrelinkKmodInfo`: `-2198828398296`

## Strings (52) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleUSBRequest`
- `AppleUSBRequestCompleter`
- `%s: %s::%s: thread_call failed with 0x%08x`
- `AppleUSBDescriptorCache`
- `debug`
- `1211112`
- `-restore`
- `AppleUSBSparseArray`
- `site.AppleUSBRequestPool`
- `%s: %s::%s: memory descriptor still set\n`
- `returnDMACommand_block_invoke`
- `AppleUSBRequestCompleter.cpp`
- `%s: %s::%s: _queueSnapshot is not empty\n`
- `1221`
- `12221`
- `site.OSMetaClassBase*`
- `AppleUSBRequestPool`
- `i8@?0`
- ` @%s:%d`
- `site.AppleUSBRequest`
- `enqueueRequest`
- `completeRequestQueue`
- `AppleUSBCommonDebug@%s-debug`
- `121121121112`
- `AppleUSBRequest.cpp`
- `1211121111111111111212`
- `usb_bundling_timeout`
- `site.tRequestCompleteData`
- `site.AppleUSBDescriptor`
- `%s-debug`
- `com.apple.usb`
- `1`
- `checkForWork`
- `11`
- `AppleUSBDescriptor`
- `1211`
- `0x%02x`
- `AppleUSBCommon-debug`
- `site.AppleUSBSparseArray`
- `free`
- `%s: %s::%s: thread_call failed with 0x%08x\n`
- `site.AppleUSBDescriptorCache`
- `%s@%s-debug`
- `all`
- `site.AppleUSBRequestCompleter`
- `%s: %s::%s: queues not empty\n`

**[__TEXT.__os_log]**

- `%s: %s::%s: _queueSnapshot is not empty\n`
- `%s: %s::%s: thread_call failed with 0x%08x\n`
- `%s: %s::%s: memory descriptor still set\n`
- `%s: %s::%s: queues not empty\n`
- `%s: %s::%s: request completer mismatch\n`
- `%s: %s::%s: thread_call failed with 0x%08x`

# `com.apple.iokit.IOSlowAdaptiveClockingFamily`

- Name: IOSlowAdaptiveClockingFamily
- Version: `1.0.0`
- UUID: `3DDCB787-4434-37B4-B5B6-B21DF1C159A0`
- Source version: `35.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOSlowAdaptiveClockingDomain` | 0xa0 |  |
| `IOSlowAdaptiveClockingManager` | 0xc0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000ce0 off=0x00a5cad0-0x00a5d7b0 addr=0xfffffe0007a60ad0-0xfffffe0007a617b0 r--/r--   __TEXT            
	sz=0x000003a0 off=0x00a5d148-0x00a5d4e8 addr=0xfffffe0007a61148-0xfffffe0007a614e8               __TEXT.__cstring          (CstringLiterals)
	sz=0x000002c8 off=0x00a5d4e8-0x00a5d7b0 addr=0xfffffe0007a614e8-0xfffffe0007a617b0               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002eac off=0x033c9080-0x033cbf2c addr=0xfffffe000a3cd080-0xfffffe000a3cff2c r-x/r-x   __TEXT_EXEC       
	sz=0x00002cfc off=0x033c9080-0x033cbd7c addr=0xfffffe000a3cd080-0xfffffe000a3cfd7c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001b0 off=0x033cbd7c-0x033cbf2c addr=0xfffffe000a3cfd7c-0xfffffe000a3cff2c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x04a16968-0x04a16a90 addr=0xfffffe000ba1a968-0xfffffe000ba1aa90 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a16968-0x04a16a30 addr=0xfffffe000ba1a968-0xfffffe000ba1aa30               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba1aa30-0xfffffe000ba1aa90               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000ae8 off=0x013edb98-0x013ee680 addr=0xfffffe00083f1b98-0xfffffe00083f2680 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013edb98-0x013edba8 addr=0xfffffe00083f1b98-0xfffffe00083f1ba8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013edba8-0x013edbb8 addr=0xfffffe00083f1ba8-0xfffffe00083f1bb8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007f8 off=0x013edbb8-0x013ee3b0 addr=0xfffffe00083f1bb8-0xfffffe00083f23b0         __DATA_CONST.__const            
	sz=0x00000080 off=0x013ee3b0-0x013ee430 addr=0xfffffe00083f23b0-0xfffffe00083f2430         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x013ee430-0x013ee570 addr=0xfffffe00083f2430-0xfffffe00083f2570         __DATA_CONST.__kalloc_var       
	sz=0x000000d8 off=0x013ee570-0x013ee648 addr=0xfffffe00083f2570-0xfffffe00083f2648         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x013ee648-0x013ee680 addr=0xfffffe00083f2648-0xfffffe00083f2680         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 61 at 0x04af7d90
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3DDCB787-4434-37B4-B5B6-B21DF1C159A0
008: LC_SOURCE_VERSION           35.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac5628 size=0x70
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOSlowAdaptiveClockingFamily`
- `CFBundleGetInfoString`: `Copyright © 2014 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.iokit.IOSlowAdaptiveClockingFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOSlowAdaptiveClockingFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSlowAdaptiveClockingFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894933296`
- `_PrelinkExecutableRelativePath`: `IOSlowAdaptiveClockingFamily`
- `_PrelinkExecutableSize`: `18332`
- `_PrelinkExecutableSourceAddr`: `-2198894933296`
- `_PrelinkKmodInfo`: `-2198828111512`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `(%p) IOSlowAdaptiveClocking::%s: Callback result: %x\n`
- `(%p) IOSlowAdaptiveClocking::%s: SlowAdaptiveClocking Start\n`
- `(%p) IOSlowAdaptiveClocking::%s: aggressor count:%d\n`
- `(%p) IOSlowAdaptiveClocking::%s: frequency: %llu, noisewidth: %u\n`
- `(%p) IOSlowAdaptiveClocking::%s: frequency: %llu, bandwidth: %u, priority: %u\n`
- `(%p) IOSlowAdaptiveClocking::%s: frequency: %llu\n`
- `(%p) IOSlowAdaptiveClocking::%s: found frequency: %llu\n`
- `(%p) IOSlowAdaptiveClocking::%s: not found frequency: %llu\n`
- `(%p) IOSlowAdaptiveClocking::%s: Boot args found: %d\n`
- `(%p) IOSlowAdaptiveClocking::%s: victim count:%d\n`

**[__TEXT.__cstring]**

- `(%p) IOSlowAdaptiveClocking::%s: frequency: %llu, bandwidth: %u, priority: %u\n`
- `_removeVictim`
- `(%p) IOSlowAdaptiveClocking::%s: found frequency: %llu\n`
- `(%p) IOSlowAdaptiveClocking::%s: Callback result: %x\n`
- `(%p) IOSlowAdaptiveClocking::%s: frequency: %llu, noisewidth: %u\n`
- `(%p) IOSlowAdaptiveClocking::%s: SlowAdaptiveClocking Start\n`
- `site.UInt32`
- `initWithAggressor`
- `_addVictim`
- `site.IOSlowAdaptiveClockingManager`
- `removeVictims`
- `12111112121212121112`
- `_findIndexListGated`
- `sac_debug`
- `initAggressor`
- `IOSlowAdaptiveClockingDomain`
- `site.IOSACVictim`
- `2211`
- `121111121222121211111112`
- `site.IOSlowAdaptiveClockingDomain`
- `IOSlowAdaptiveClockingManager`
- `debug`
- `(%p) IOSlowAdaptiveClocking::%s: frequency: %llu\n`
- `(%p) IOSlowAdaptiveClocking::%s: Boot args found: %d\n`
- `start`
- `(%p) IOSlowAdaptiveClocking::%s: victim count:%d\n`
- `_freeVictim`
- `(%p) IOSlowAdaptiveClocking::%s: not found frequency: %llu\n`
- `addVictims`
- `(%p) IOSlowAdaptiveClocking::%s: aggressor count:%d\n`

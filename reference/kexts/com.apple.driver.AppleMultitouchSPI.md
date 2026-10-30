# `com.apple.driver.AppleMultitouchSPI`

- Name: AppleMultitouchSPI
- Version: `1010.4`
- UUID: `231B1336-C59B-3FE5-A02C-0913DC13FA79`
- Source version: `10110.4.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

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
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000007c8 off=0x00684f30-0x006856f8 addr=0xfffffe0007688f30-0xfffffe00076896f8 r--/r--   __TEXT            
	sz=0x00000050 off=0x00685558-0x006855a8 addr=0xfffffe0007689558-0xfffffe00076895a8               __TEXT.__const            
	sz=0x0000008b off=0x006855a8-0x00685633 addr=0xfffffe00076895a8-0xfffffe0007689633               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000c5 off=0x00685633-0x006856f8 addr=0xfffffe0007689633-0xfffffe00076896f8               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000088c off=0x022dd0a0-0x022dd92c addr=0xfffffe00092e10a0-0xfffffe00092e192c r-x/r-x   __TEXT_EXEC       
	sz=0x000007bc off=0x022dd0a0-0x022dd85c addr=0xfffffe00092e10a0-0xfffffe00092e185c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000d0 off=0x022dd85c-0x022dd92c addr=0xfffffe00092e185c-0xfffffe00092e192c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000000d8 off=0x04982700-0x049827d8 addr=0xfffffe000b986700-0xfffffe000b9867d8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04982700-0x049827c8 addr=0xfffffe000b986700-0xfffffe000b9867c8               __DATA.__data             
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9867c8-0xfffffe000b9867d8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000001c0 off=0x0117fba8-0x0117fd68 addr=0xfffffe0008183ba8-0xfffffe0008183d68 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x0117fba8-0x0117fbd0 addr=0xfffffe0008183ba8-0xfffffe0008183bd0         __DATA_CONST.__const            
	sz=0x000000a0 off=0x0117fbd0-0x0117fc70 addr=0xfffffe0008183bd0-0xfffffe0008183c70         __DATA_CONST.__kalloc_var       
	sz=0x00000080 off=0x0117fc70-0x0117fcf0 addr=0xfffffe0008183c70-0xfffffe0008183cf0         __DATA_CONST.__kalloc_type      
	sz=0x00000068 off=0x0117fcf0-0x0117fd58 addr=0xfffffe0008183cf0-0xfffffe0008183d58         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000010 off=0x0117fd58-0x0117fd68 addr=0xfffffe0008183d58-0xfffffe0008183d68         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 28 at 0x04ae0b38
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     231B1336-C59B-3FE5-A02C-0913DC13FA79
008: LC_SOURCE_VERSION           10110.4.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aab6b8 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleMultitouchSPI`
- `CFBundleIdentifier`: `com.apple.driver.AppleMultitouchSPI`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleMultitouchSPI`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.4`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleMultitouchSPI.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898962640`
- `_PrelinkExecutableRelativePath`: `AppleMultitouchSPI`
- `_PrelinkExecutableSize`: `4844`
- `_PrelinkExecutableSourceAddr`: `-2198898962640`
- `_PrelinkKmodInfo`: `-2198828718336`

## Strings (11) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Multitouch`
- `CriticalErrors`
- `site.AppleMultitouchCriticalErrorsReporter`
- `12111`
- `site.uint64_t`
- `MT`
- `_createReporter`
- `MultitouchCriticalErrorBit%lu`

**[__TEXT.__os_log]**

- `[HID] [%s] [Error] %s Failed to create IOSimpleReporter\n`
- `[HID] [%s] [Error] %s Failed to add channel for <%s>\n`
- `[HID] [%s] [Error] %s Failed to add reporter legend for group <%s> and subgroup <%s>\n`

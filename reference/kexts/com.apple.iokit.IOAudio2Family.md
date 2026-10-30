# `com.apple.iokit.IOAudio2Family`

- Name: IOAudio2Family
- Version: `1.0`
- UUID: `65A42983-609E-31E3-B2CD-D34782B2D4F6`
- Source version: `550.1.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOAudio2Device` | 0xe8 | IOService → IORegistryEntry |
| `IOAudio2DeviceUserClient` | 0x110 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000009f0 off=0x009bd070-0x009bda60 addr=0xfffffe00079c1070-0xfffffe00079c1a60 r--/r--   __TEXT            
	sz=0x000003af off=0x009bd698-0x009bda47 addr=0xfffffe00079c1698-0xfffffe00079c1a47               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000018 off=0x009bda48-0x009bda60 addr=0xfffffe00079c1a48-0xfffffe00079c1a60               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00005d5c off=0x0305efb0-0x03064d0c addr=0xfffffe000a062fb0-0xfffffe000a068d0c r-x/r-x   __TEXT_EXEC       
	sz=0x00005b4c off=0x0305efb0-0x03064afc addr=0xfffffe000a062fb0-0xfffffe000a068afc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000210 off=0x03064afc-0x03064d0c addr=0xfffffe000a068afc-0xfffffe000a068d0c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049eeb20-0x049eec48 addr=0xfffffe000b9f2b20-0xfffffe000b9f2c48 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049eeb20-0x049eebe8 addr=0xfffffe000b9f2b20-0xfffffe000b9f2be8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9f2be8-0xfffffe000b9f2c48               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001260 off=0x0134cba0-0x0134de00 addr=0xfffffe0008350ba0-0xfffffe0008351e00 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0134cba0-0x0134cbb0 addr=0xfffffe0008350ba0-0xfffffe0008350bb0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0134cbb0-0x0134cbc0 addr=0xfffffe0008350bb0-0xfffffe0008350bc0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001058 off=0x0134cbc0-0x0134dc18 addr=0xfffffe0008350bc0-0xfffffe0008351c18         __DATA_CONST.__const            
	sz=0x00000080 off=0x0134dc18-0x0134dc98 addr=0xfffffe0008351c18-0xfffffe0008351c98         __DATA_CONST.__kalloc_type      
	sz=0x00000108 off=0x0134dc98-0x0134dda0 addr=0xfffffe0008351c98-0xfffffe0008351da0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x0134dda0-0x0134de00 addr=0xfffffe0008351da0-0xfffffe0008351e00         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 78 at 0x04af09b8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     65A42983-609E-31E3-B2CD-D34782B2D4F6
008: LC_SOURCE_VERSION           550.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004abdc20 size=0x150
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOAudio2Family`
- `CFBundleGetInfoString`: `IOAudio2Family 1.0`
- `CFBundleIdentifier`: `com.apple.iokit.IOAudio2Family`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOAudio2Family`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOAudio2Family.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895587216`
- `_PrelinkExecutableRelativePath`: `IOAudio2Family`
- `_PrelinkExecutableSize`: `31444`
- `_PrelinkExecutableSourceAddr`: `-2198895587216`
- `_PrelinkKmodInfo`: `-2198828274912`

## Strings (63) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `descriptor`
- `db per step`
- `device UID`
- `site.IOAudio2Device`
- `available formats`
- `uses isolated IO`
- `com.apple.private.audio.driver-host`
- `terminal type`
- `is running`
- `site.IOAudio2DeviceUserClient`
- `bytes per frame`
- `base class`
- `kind`
- `Time Stamp Seed`
- `1211111212221212111111111111121121`
- `format ID`
- `element`
- `mapping options`
- `Sample Time`
- `IOAudio2`
- `stream ID`
- `scope`
- `start int value`
- `current format`
- `min sample rate`
- `block ID`
- `right value`
- `exclusive access owner`
- `class`
- `maximum value`
- `Host Time`
- `frames per packet`
- `right channel`
- `sample rate`
- `format flags`
- `control ID`
- `transfer function`
- `center value`
- `12111112122212121212222111221`
- `IOAudio2DeviceUserClient`
- `minimum value`
- `range map`
- `IOAudio2Device`
- `buffer mapping options`
- `bits per channel`
- `read only`
- `channels per frame`
- `max sample rate`
- `bytes per packet`
- `variant`
- `name`
- `left value`
- `Client Output position`
- `Engine Running`
- `starting channel`
- `value`
- `multi-selector`
- `left channel`
- `property selectors`
- `start db value`
- `selectors`
- `integer steps`
- `Client Input position`

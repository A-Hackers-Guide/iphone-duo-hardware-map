# `com.apple.iokit.IOSerialFamily`

- Name: IOKit Serial Port Family
- Version: `11`
- UUID: `30D833CF-002B-3D09-8DE3-DBB6AA31C200`
- Source version: `118.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 10.0.0d2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 10.0.0d2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 10.0.0d2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 10.0.0d2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 10.0.0d2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOSerialBSDClient
- `CFBundleIdentifier`: `com.apple.iokit.IOSerialFamily`
- `IOClass`: `IOSerialBSDClient`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSerialFamily`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOSerialStreamSync`
- `IOResourceMatch`: `IOBSD`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOModemSerialStreamSync` | 0x98 | IOSerialStreamSync → IOService → IORegistryEntry |
| `IORS232SerialStreamSync` | 0x98 | IOSerialStreamSync → IOService → IORegistryEntry |
| `IOSerialBSDClient` | 0x1d0 | IOService → IORegistryEntry |
| `IOSerialDriverSync` | 0x88 | IOService → IORegistryEntry |
| `IOSerialStreamSync` | 0x98 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000d40 off=0x00a55870-0x00a565b0 addr=0xfffffe0007a59870-0xfffffe0007a5a5b0 r--/r--   __TEXT            
	sz=0x00000030 off=0x00a55f40-0x00a55f70 addr=0xfffffe0007a59f40-0xfffffe0007a59f70               __TEXT.__const            
	sz=0x00000640 off=0x00a55f70-0x00a565b0 addr=0xfffffe0007a59f70-0xfffffe0007a5a5b0               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00007c38 off=0x0337da60-0x03385698 addr=0xfffffe000a381a60-0xfffffe000a389698 r-x/r-x   __TEXT_EXEC       
	sz=0x000077a8 off=0x0337da60-0x03385208 addr=0xfffffe000a381a60-0xfffffe000a389208          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000490 off=0x03385208-0x03385698 addr=0xfffffe000a389208-0xfffffe000a389698          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003a9 off=0x04a15ac8-0x04a15e71 addr=0xfffffe000ba19ac8-0xfffffe000ba19e71 rw-/rw-   __DATA            
	sz=0x00000258 off=0x04a15ac8-0x04a15d20 addr=0xfffffe000ba19ac8-0xfffffe000ba19d20               __DATA.__data             
	sz=0x00000130 off=0x00000000-0x00000130 addr=0xfffffe000ba19d20-0xfffffe000ba19e50               __DATA.__common           (Zerofill)
	sz=0x00000021 off=0x00000000-0x00000021 addr=0xfffffe000ba19e50-0xfffffe000ba19e71               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000024d8 off=0x013dd3d0-0x013df8a8 addr=0xfffffe00083e13d0-0xfffffe00083e38a8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013dd3d0-0x013dd3e0 addr=0xfffffe00083e13d0-0xfffffe00083e13e0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013dd3e0-0x013dd3f0 addr=0xfffffe00083e13e0-0xfffffe00083e13f0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001f70 off=0x013dd3f0-0x013df360 addr=0xfffffe00083e13f0-0xfffffe00083e3360         __DATA_CONST.__const            
	sz=0x00000140 off=0x013df360-0x013df4a0 addr=0xfffffe00083e3360-0xfffffe00083e34a0         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x013df4a0-0x013df5e0 addr=0xfffffe00083e34a0-0xfffffe00083e35e0         __DATA_CONST.__kalloc_var       
	sz=0x00000248 off=0x013df5e0-0x013df828 addr=0xfffffe00083e35e0-0xfffffe00083e3828         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x013df828-0x013df8a8 addr=0xfffffe00083e3828-0xfffffe00083e38a8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 162 at 0x04af6ed0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     30D833CF-002B-3D09-8DE3-DBB6AA31C200
008: LC_SOURCE_VERSION           118.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac4998 size=0xd8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOSerialFamily`
- `CFBundleGetInfoString`: `Copyright © 1997-2010 Apple Inc. All rights reserved. IOKit Serial Port Family`
- `CFBundleIdentifier`: `com.apple.iokit.IOSerialFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOKit Serial Port Family`
- `CFBundleNumericVersion`: `285245440`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `11`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `11`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.4`
- `OSBundleRequired`: `Safe Boot`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSerialFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894962576`
- `_PrelinkExecutableRelativePath`: `IOSerialFamily`
- `_PrelinkExecutableSize`: `45561`
- `_PrelinkExecutableSourceAddr`: `-2198894962576`
- `_PrelinkKmodInfo`: `-2198828115256`

## Strings (70) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1`
- `setBaseTypeForDev`
- `start`
- `ttyopn`
- `1211111212221212112222222221121222222222112222211111221221`
- `ttyioss%04x: mctl RS232_S_OUTPUTS failed %x\n`
- `ttyioss%04x: %sware Overflow\n`
- `Hard`
- `IOTTYBaseName`
- `IODialinDevice`
- `IOSerialFamily::%s: end normal\n`
- `createDevNodes`
- `TTY.%s: Failed non type based match\n`
- `site.IOModemSerialStreamSync`
- `IOSerialFamily::%s: begin\n`
- `getUniqueTTYSuffix`
- `IOSerialFamily::%s: finish error\n`
- `IOModemSerialStreamSync`
- `IOSerialBSDClient`
- `IOSerialBSDClientType`
- `IOModemSerialStream`
- `AppleVirtIOAgentDevice`
- `site.IOSerialStreamSync`
- `/dev/cu.`
- `%s`
- `ttyioss%04x: dev node unavailable, wait.\n`
- `ttypre`
- `registerTTY`
- `IOSerialFamily::%s: finish\n`
- `ttyctr`
- `site.IOSerialDriverSync`
- `IOCalloutDevice`
- `IOSerialFamily::%s: no suffix SET\n`
- `IORS232SerialStream`
- `ttyrev`
- `ttyioss%04x: ACTIVE failed (%x)\n`
- `ttydelay`
- `ttyioss%04x: dequeueData ret %x\n`
- `TTY.%s: Failed superclass match\n`
- `IOSerialDriverSync`
- `site.IOSerialBSDClient`
- `IOTTYDevice`
- `IOSerialFamily::%s: no UniqueTTYSuffix\n`
- `TTY.%s: doesn't have a %s interface\n`
- `IOTTYWaitForIdle`
- `releaseUniqueTTYSuffix`
- `IOSerialFamily::%s:  Cleanup Resources\n`
- `/dev/tty.`
- `IOSerialFamily::%s: finish normal\n`
- `ttyioss%04x: enqueueData rtn (%x)\n`
- `IORS232SerialStreamSync`
- `IOSerialStream`
- `IOTTYSuffix`
- `site.IOSerialBSDClient*`
- `assign_dev_t`
- `IOSerialFamily::%s: no suffix\n`
- `Soft`
- `IOSerialStreamSync`
- `1211111212221212111`
- `IOSerialBSDClient didn't initialize`
- `%d`
- `IOSerialFamily::%s:  finished\n`
- `site.IORS232SerialStreamSync`
- `IOSerialFamily::%s: no Nub for basename SET\n`
- `ttyidl`
- `IOSerialFamily::%s: end not normal\n`
- `IOSerialFamily::%s: end\n`
- `IOSerialFamily::%s: no Nub for basename\n`
- `TTY.%s: %s isn't an OSString?\n`
- `12111112122212121`

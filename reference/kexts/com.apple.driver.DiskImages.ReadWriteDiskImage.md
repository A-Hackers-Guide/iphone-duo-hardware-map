# `com.apple.driver.DiskImages.ReadWriteDiskImage`

- Name: AppleDiskImagesReadWriteDiskImage
- Version: `493.0.0`
- UUID: `9CC63A47-6B6D-3DD8-B78B-236AA1801B89`
- Source version: `710.0.0.0.0`
- Depends on: [`com.apple.driver.DiskImages`](com.apple.driver.DiskImages.md) 128, [`com.apple.driver.DiskImages.KernelBacked`](com.apple.driver.DiskImages.KernelBacked.md) 128, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### KDIReadWriteDiskImage
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.ReadWriteDiskImage`
- `IOClass`: `KDIReadWriteDiskImage`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.ReadWriteDiskImage`
- `IOProbeScore`: `100`
- `IOProviderClass`: `KDIBackingStore`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `KDIReadWriteDiskImage` | 0xb0 | KDIDiskImage → KDIObject → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000620 off=0x009f2930-0x009f2f50 addr=0xfffffe00079f6930-0xfffffe00079f6f50 r--/r--   __TEXT            
	sz=0x00000048 off=0x009f2f08-0x009f2f50 addr=0xfffffe00079f6f08-0xfffffe00079f6f50               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000600 off=0x03170480-0x03170a80 addr=0xfffffe000a174480-0xfffffe000a174a80 r-x/r-x   __TEXT_EXEC       
	sz=0x00000580 off=0x03170480-0x03170a00 addr=0xfffffe000a174480-0xfffffe000a174a00          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000080 off=0x03170a00-0x03170a80 addr=0xfffffe000a174a00-0xfffffe000a174a80          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049f1678-0x049f1778 addr=0xfffffe000b9f5678-0xfffffe000b9f5778 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049f1678-0x049f173c addr=0xfffffe000b9f5678-0xfffffe000b9f573c               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9f5740-0xfffffe000b9f5778               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000718 off=0x01386678-0x01386d90 addr=0xfffffe000838a678-0xfffffe000838ad90 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01386678-0x01386680 addr=0xfffffe000838a678-0xfffffe000838a680         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01386680-0x01386688 addr=0xfffffe000838a680-0xfffffe000838a688         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000678 off=0x01386688-0x01386d00 addr=0xfffffe000838a688-0xfffffe000838ad00         __DATA_CONST.__const            
	sz=0x00000040 off=0x01386d00-0x01386d40 addr=0xfffffe000838ad00-0xfffffe000838ad40         __DATA_CONST.__kalloc_type      
	sz=0x00000040 off=0x01386d40-0x01386d80 addr=0xfffffe000838ad40-0xfffffe000838ad80         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000010 off=0x01386d80-0x01386d90 addr=0xfffffe000838ad80-0xfffffe000838ad90         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 18 at 0x04af2bbc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9CC63A47-6B6D-3DD8-B78B-236AA1801B89
008: LC_SOURCE_VERSION           710.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac0420 size=0x20
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiskImagesReadWriteDiskImage`
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.ReadWriteDiskImage`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImagesReadWriteDiskImage`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `493.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `493.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2017 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDIXController.kext/PlugIns/AppleDiskImagesReadWriteDiskImage.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895367888`
- `_PrelinkExecutableRelativePath`: `AppleDiskImagesReadWriteDiskImage`
- `_PrelinkExecutableSize`: `5176`
- `_PrelinkExecutableSourceAddr`: `-2198895367888`
- `_PrelinkKmodInfo`: `-2198828263816`

## Strings (3) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `KDIReadWriteDiskImage`
- `site.KDIReadWriteDiskImage`
- `1211111212221212121221`

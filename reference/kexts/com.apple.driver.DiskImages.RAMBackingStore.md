# `com.apple.driver.DiskImages.RAMBackingStore`

- Name: AppleDiskImagesRAMBackingStore
- Version: `493.0.0`
- UUID: `8CF3440C-B8CA-3E81-BD4A-E32F296EC736`
- Source version: `710.0.0.0.0`
- Depends on: [`com.apple.driver.DiskImages`](com.apple.driver.DiskImages.md) 128, [`com.apple.driver.DiskImages.KernelBacked`](com.apple.driver.DiskImages.KernelBacked.md) 128, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### KDIRAMBackingStore
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.RAMBackingStore`
- `IOClass`: `KDIRAMBackingStore`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.RAMBackingStore`
- `IOProbeScore`: `100`
- `IOProviderClass`: `KDIURL`
- `KDIURLScheme`: `ram`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `KDIRAMBackingStore` | 0xc0 | KDIBackingStore → KDIObject → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000006a0 off=0x009f2290-0x009f2930 addr=0xfffffe00079f6290-0xfffffe00079f6930 r--/r--   __TEXT            
	sz=0x000000c8 off=0x009f2868-0x009f2930 addr=0xfffffe00079f6868-0xfffffe00079f6930               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000bb0 off=0x0316f8d0-0x03170480 addr=0xfffffe000a1738d0-0xfffffe000a174480 r-x/r-x   __TEXT_EXEC       
	sz=0x00000ab0 off=0x0316f8d0-0x03170380 addr=0xfffffe000a1738d0-0xfffffe000a174380          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x03170380-0x03170480 addr=0xfffffe000a174380-0xfffffe000a174480          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049f1578-0x049f1678 addr=0xfffffe000b9f5578-0xfffffe000b9f5678 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049f1578-0x049f163c addr=0xfffffe000b9f5578-0xfffffe000b9f563c               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9f5640-0xfffffe000b9f5678               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000770 off=0x01385f08-0x01386678 addr=0xfffffe0008389f08-0xfffffe000838a678 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01385f08-0x01385f10 addr=0xfffffe0008389f08-0xfffffe0008389f10         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01385f10-0x01385f18 addr=0xfffffe0008389f10-0xfffffe0008389f18         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000678 off=0x01385f18-0x01386590 addr=0xfffffe0008389f18-0xfffffe000838a590         __DATA_CONST.__const            
	sz=0x00000040 off=0x01386590-0x013865d0 addr=0xfffffe000838a590-0xfffffe000838a5d0         __DATA_CONST.__kalloc_type      
	sz=0x00000080 off=0x013865d0-0x01386650 addr=0xfffffe000838a5d0-0xfffffe000838a650         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x01386650-0x01386678 addr=0xfffffe000838a650-0xfffffe000838a678         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 37 at 0x04af2b28
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8CF3440C-B8CA-3E81-BD4A-E32F296EC736
008: LC_SOURCE_VERSION           710.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac03f8 size=0x28
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiskImagesRAMBackingStore`
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.RAMBackingStore`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImagesRAMBackingStore`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDIXController.kext/PlugIns/AppleDiskImagesRAMBackingStore.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895369584`
- `_PrelinkExecutableRelativePath`: `AppleDiskImagesRAMBackingStore`
- `_PrelinkExecutableSize`: `6848`
- `_PrelinkExecutableSourceAddr`: `-2198895369584`
- `_PrelinkKmodInfo`: `-2198828264072`

## Strings (13) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `KDIRAMBackingStore`
- `ram`
- `ramdisk`
- `KDIURLHost`
- `ramfile-memory-descriptor`
- `RAM`
- `Physical Interconnect Location`
- `site.KDIRAMBackingStore`
- `121111121222121212121112`
- `KDIURLScheme`
- `ramfile`
- `KDIURLPath`
- `write-protected`

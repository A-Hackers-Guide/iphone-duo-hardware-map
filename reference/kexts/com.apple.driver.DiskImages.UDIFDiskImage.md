# `com.apple.driver.DiskImages.UDIFDiskImage`

- Name: AppleDiskImagesUDIFDiskImage
- Version: `493.0.0`
- UUID: `6FC520B3-AE2B-3DE5-AC27-DDECF32767E4`
- Source version: `710.0.0.0.0`
- Depends on: [`com.apple.driver.DiskImages`](com.apple.driver.DiskImages.md) 128, [`com.apple.driver.DiskImages.KernelBacked`](com.apple.driver.DiskImages.KernelBacked.md) 128, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### KDIUDIFDiskImage
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.UDIFDiskImage`
- `IOClass`: `KDIUDIFDiskImage`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.UDIFDiskImage`
- `IOProbeScore`: `200`
- `IOProviderClass`: `KDIUDIFEncoding`

### KDIUDIFEncoding
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.UDIFDiskImage`
- `IOClass`: `KDIUDIFEncoding`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.UDIFDiskImage`
- `IOProbeScore`: `200`
- `IOProviderClass`: `KDIBackingStore`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `KDISecondaryEncoding` | 0xb0 | KDIEncoding → KDIBackingStore → KDIObject → IOService → IORegistryEntry |
| `KDIUDIFCacheBuffer` | 0x48 |  |
| `KDIUDIFCacheObject` | 0x40 |  |
| `KDIUDIFDiskImage` | 0xc8 | KDIDiskImage → KDIObject → IOService → IORegistryEntry |
| `KDIUDIFEncoding` | 0x2b8 | KDISecondaryEncoding → KDIEncoding → KDIBackingStore → KDIObject → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000039c0 off=0x009f2f50-0x009f6910 addr=0xfffffe00079f6f50-0xfffffe00079fa910 r--/r--   __TEXT            
	sz=0x00003090 off=0x009f35d0-0x009f6660 addr=0xfffffe00079f75d0-0xfffffe00079fa660               __TEXT.__const            
	sz=0x000002b0 off=0x009f6660-0x009f6910 addr=0xfffffe00079fa660-0xfffffe00079fa910               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000b94c off=0x03170a80-0x0317c3cc addr=0xfffffe000a174a80-0xfffffe000a1803cc r-x/r-x   __TEXT_EXEC       
	sz=0x0000b70c off=0x03170a80-0x0317c18c addr=0xfffffe000a174a80-0xfffffe000a18018c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000240 off=0x0317c18c-0x0317c3cc addr=0xfffffe000a18018c-0xfffffe000a1803cc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x049f1778-0x049f1918 addr=0xfffffe000b9f5778-0xfffffe000b9f5918 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049f1778-0x049f183c addr=0xfffffe000b9f5778-0xfffffe000b9f583c               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b9f5840-0xfffffe000b9f5918               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002a90 off=0x01386d90-0x01389820 addr=0xfffffe000838ad90-0xfffffe000838d820 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x01386d90-0x01386db0 addr=0xfffffe000838ad90-0xfffffe000838adb0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x01386db0-0x01386dd0 addr=0xfffffe000838adb0-0xfffffe000838add0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000025f0 off=0x01386dd0-0x013893c0 addr=0xfffffe000838add0-0xfffffe000838d3c0         __DATA_CONST.__const            
	sz=0x00000140 off=0x013893c0-0x01389500 addr=0xfffffe000838d3c0-0xfffffe000838d500         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x01389500-0x01389690 addr=0xfffffe000838d500-0xfffffe000838d690         __DATA_CONST.__kalloc_var       
	sz=0x00000120 off=0x01389690-0x013897b0 addr=0xfffffe000838d690-0xfffffe000838d7b0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000070 off=0x013897b0-0x01389820 addr=0xfffffe000838d7b0-0xfffffe000838d820         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 86 at 0x04af2c04
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     6FC520B3-AE2B-3DE5-AC27-DDECF32767E4
008: LC_SOURCE_VERSION           710.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac0440 size=0x100
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiskImagesUDIFDiskImage`
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.UDIFDiskImage`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImagesUDIFDiskImage`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDIXController.kext/PlugIns/AppleDiskImagesUDIFDiskImage.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895366320`
- `_PrelinkExecutableRelativePath`: `AppleDiskImagesUDIFDiskImage`
- `_PrelinkExecutableSize`: `73532`
- `_PrelinkExecutableSourceAddr`: `-2198895366320`
- `_PrelinkKmodInfo`: `-2198828263560`

## Strings (31) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `KDIUDIFCacheObject`
- `12121222`
- `site.KDIUDIFEncoding`
- `resource-fork`
- `site.KDIUDIFDiskImage`
- `site.KDIUDIFCacheBuffer *`
- `KDIUDIFCacheObject: low on memory - deleting cache buffers`
- ` `
- `ID`
- `cache-depth`
- `+`
- `KDIUDIFCacheBuffer`
- `KDIUDIFDiskImage`
- `image-format-read-only`
- `1`
- `KDIUDIFCacheObject::cacheData: setLength failed\n`
- `%2d %1.1s %+9qd %9qd %9qd %12qd %12qd\n`
- `KDISecondaryEncoding`
- `1.2.3`
- `site.OSData *`
- `## ? ...score.. ...age... ...use... ...start ... ...length...\n`
- `site.KDIUDIFCacheBuffer`
- `1211111212221212121211`
- `ZBM`
- `1211111212221212121221121`
- `site.KDISecondaryEncoding`
- `site.KDIUDIFCacheObject`
- `122222221`
- `Data`
- `KDIUDIFEncoding`
- `121111121222121212121122222222222222222222222222222222222222222222222222222222222222221`

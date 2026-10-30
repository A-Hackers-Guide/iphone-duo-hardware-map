# `com.apple.driver.DiskImages.FileBackingStore`

- Name: AppleDiskImagesFileBackingStore
- Version: `493.0.0`
- UUID: `ADB66921-E26B-35B1-BC60-8990BF0F37E1`
- Source version: `710.0.0.0.0`
- Depends on: [`com.apple.driver.DiskImages`](com.apple.driver.DiskImages.md) 128, [`com.apple.driver.DiskImages.KernelBacked`](com.apple.driver.DiskImages.KernelBacked.md) 128, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### KDIFileBackingStore
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.FileBackingStore`
- `IOClass`: `KDIFileBackingStore`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.FileBackingStore`
- `IOProbeScore`: `100`
- `IOProviderClass`: `KDIURL`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `KDIFileBackingStore` | 0xc0 | KDIBackingStore → KDIObject → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000877 off=0x009f1060-0x009f18d7 addr=0xfffffe00079f5060-0xfffffe00079f58d7 r--/r--   __TEXT            
	sz=0x00000010 off=0x009f1690-0x009f16a0 addr=0xfffffe00079f5690-0xfffffe00079f56a0               __TEXT.__const            
	sz=0x00000237 off=0x009f16a0-0x009f18d7 addr=0xfffffe00079f56a0-0xfffffe00079f58d7               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001574 off=0x03169d70-0x0316b2e4 addr=0xfffffe000a16dd70-0xfffffe000a16f2e4 r-x/r-x   __TEXT_EXEC       
	sz=0x00001314 off=0x03169d70-0x0316b084 addr=0xfffffe000a16dd70-0xfffffe000a16f084          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000260 off=0x0316b084-0x0316b2e4 addr=0xfffffe000a16f084-0xfffffe000a16f2e4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049f1280-0x049f1380 addr=0xfffffe000b9f5280-0xfffffe000b9f5380 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049f1280-0x049f1344 addr=0xfffffe000b9f5280-0xfffffe000b9f5344               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9f5348-0xfffffe000b9f5380               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000838 off=0x013825b8-0x01382df0 addr=0xfffffe00083865b8-0xfffffe0008386df0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013825b8-0x013825c0 addr=0xfffffe00083865b8-0xfffffe00083865c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013825c0-0x013825c8 addr=0xfffffe00083865c0-0xfffffe00083865c8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000678 off=0x013825c8-0x01382c40 addr=0xfffffe00083865c8-0xfffffe0008386c40         __DATA_CONST.__const            
	sz=0x00000040 off=0x01382c40-0x01382c80 addr=0xfffffe0008386c40-0xfffffe0008386c80         __DATA_CONST.__kalloc_type      
	sz=0x00000130 off=0x01382c80-0x01382db0 addr=0xfffffe0008386c80-0xfffffe0008386db0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x01382db0-0x01382df0 addr=0xfffffe0008386db0-0xfffffe0008386df0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 84 at 0x04af2844
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     ADB66921-E26B-35B1-BC60-8990BF0F37E1
008: LC_SOURCE_VERSION           710.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac02d0 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiskImagesFileBackingStore`
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.FileBackingStore`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImagesFileBackingStore`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDIXController.kext/PlugIns/AppleDiskImagesFileBackingStore.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895374240`
- `_PrelinkExecutableRelativePath`: `AppleDiskImagesFileBackingStore`
- `_PrelinkExecutableSize`: `10019`
- `_PrelinkExecutableSourceAddr`: `-2198895374240`
- `_PrelinkKmodInfo`: `-2198828264832`

## Strings (20) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `KDIFileBackingStore`
- `getUserVnode`
- `KDIURLCreateIfNeeded`
- `KDIFileBackingStore::_handleStart: initial R/W vn_open returned %d\n`
- `Physical Interconnect Location`
- `KDIFileBackingStore::_handleStart: res = %d\n`
- `KDIURLAttachResult`
- `vnode_getwithref(_vnode) failed?`
- `KDIFileBackingStore::_handleStart: vnode_getattr() returned %d\n`
- `site.KDIFileBackingStore`
- `KDIURLPath`
- `KDIFileBackingStore::_handleStart: vn_open() returned %d\n`
- `write-protected`
- `File`
- `file`
- `121111121222121212121122`
- `KDIURLScheme`
- `%s: error: vnode_getfromfd failed. status=%d\n`
- `%s: error: vnode_ref failed. status=%d\n`
- `KDIURLFD`

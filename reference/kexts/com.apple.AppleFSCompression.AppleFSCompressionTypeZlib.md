# `com.apple.AppleFSCompression.AppleFSCompressionTypeZlib`

- Name: AppleFSCompressionTypeZlib
- Version: `1.0.0`
- UUID: `2787E338-59FB-3E08-9CEC-C7638A36B9D7`
- Source version: `182.40.4.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b1, [`com.apple.kpi.dsep`](com.apple.kpi.dsep.md) 8.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 7.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0d0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0b1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### com.apple.AppleFSCompression.AppleFSCompressionTypeZlib
- `CFBundleIdentifier`: `com.apple.AppleFSCompression.AppleFSCompressionTypeZlib`
- `IOClass`: `com_apple_AppleFSCompression_AppleFSCompressionTypeZlib`
- `IOMatchCategory`: `com_apple_AppleFSCompression_AppleFSCompressionTypeZlib`
- `IOPersonalityPublisher`: `com.apple.AppleFSCompression.AppleFSCompressionTypeZlib`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `com.apple.AppleFSCompression.providesType10`: `True`
- `com.apple.AppleFSCompression.providesType11`: `True`
- `com.apple.AppleFSCompression.providesType12`: `True`
- `com.apple.AppleFSCompression.providesType3`: `True`
- `com.apple.AppleFSCompression.providesType4`: `True`
- `com.apple.AppleFSCompression.providesType7`: `True`
- `com.apple.AppleFSCompression.providesType8`: `True`
- `com.apple.AppleFSCompression.providesType9`: `True`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `com_apple_AppleFSCompression_AppleFSCompressionTypeZlib` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000402d off=0x00466190-0x0046a1bd addr=0xfffffe000746a190-0xfffffe000746e1bd r--/r--   __TEXT            
	sz=0x00003180 off=0x00466810-0x00469990 addr=0xfffffe000746a810-0xfffffe000746d990               __TEXT.__const            
	sz=0x0000082d off=0x00469990-0x0046a1bd addr=0xfffffe000746d990-0xfffffe000746e1bd               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00008f08 off=0x01ca4fc0-0x01cadec8 addr=0xfffffe0008ca8fc0-0xfffffe0008cb1ec8 r-x/r-x   __TEXT_EXEC       
	sz=0x00008d58 off=0x01ca4fc0-0x01cadd18 addr=0xfffffe0008ca8fc0-0xfffffe0008cb1d18          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001b0 off=0x01cadd18-0x01cadec8 addr=0xfffffe0008cb1d18-0xfffffe0008cb1ec8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000101 off=0x049410e0-0x049411e1 addr=0xfffffe000b9450e0-0xfffffe000b9451e1 rw-/rw-   __DATA            
	sz=0x000000d8 off=0x049410e0-0x049411b8 addr=0xfffffe000b9450e0-0xfffffe000b9451b8               __DATA.__data             
	sz=0x00000029 off=0x00000000-0x00000029 addr=0xfffffe000b9451b8-0xfffffe000b9451e1               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000019d0 off=0x01098c60-0x0109a630 addr=0xfffffe000809cc60-0xfffffe000809e630 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01098c60-0x01098c68 addr=0xfffffe000809cc60-0xfffffe000809cc68         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01098c68-0x01098c70 addr=0xfffffe000809cc68-0xfffffe000809cc70         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001700 off=0x01098c70-0x0109a370 addr=0xfffffe000809cc70-0xfffffe000809e370         __DATA_CONST.__const            
	sz=0x00000040 off=0x0109a370-0x0109a3b0 addr=0xfffffe000809e370-0xfffffe000809e3b0         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x0109a3b0-0x0109a540 addr=0xfffffe000809e3b0-0xfffffe000809e540         __DATA_CONST.__kalloc_var       
	sz=0x000000d8 off=0x0109a540-0x0109a618 addr=0xfffffe000809e540-0xfffffe000809e618         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000018 off=0x0109a618-0x0109a630 addr=0xfffffe000809e618-0xfffffe000809e630         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 57 at 0x04ad99cc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     2787E338-59FB-3E08-9CEC-C7638A36B9D7
008: LC_SOURCE_VERSION           182.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9fa30 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleFSCompressionTypeZlib`
- `CFBundleIdentifier`: `com.apple.AppleFSCompression.AppleFSCompressionTypeZlib`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleFSCompressionTypeZlib`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `182.40.4`
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
- `NSHumanReadableCopyright`: `Copyright © 2008-2015 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleFSCompressionTypeZlib.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901186160`
- `_PrelinkExecutableRelativePath`: `AppleFSCompressionTypeZlib`
- `_PrelinkExecutableSize`: `59910`
- `_PrelinkExecutableSourceAddr`: `-2198901186160`
- `_PrelinkKmodInfo`: `-2198828986144`

## Strings (40) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ZBM`
- `12111112122212121`
- `com.apple.AppleFSCompressionTypeZlib load again\n`
- `/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Compressors/Zlib/compressorKext.c`
- `%s:%d: %s: allocating buffer of size %u failed\n`
- `%s:%d: %s: allocating buffer of size %llu failed for compression algorithm 0x%x\n`
- `register_decmpfs_decompressor %d: CMP_Type%d failed: %d\n`
- `unknown path`
- `com.apple.ResourceFork`
- `%s:%d: %s: decmpfs xattr size (%u) should be greater than decmpfs disk header size (%zu)\n`
- `%s:%d: Error: unknown compressor %d\n`
- `%s:%d: allocation of %zu bytes failed\n`
- `%s:%d: %s: workbuffer allocation failed\n`
- `/Library/Caches/com.apple.xbs/E3BFA698-622A-4A7D-B585-0B6C2AFD4C16/TemporaryDirectory.UICCsZ/Sources/AppleFSCompression/Common/ChunkCompression.cpp`
- `com_apple_AppleFSCompression_AppleFSCompressionTypeZlib`
- `%s:%d: Error: unknown type4 flags %llx\n`
- `%s:%d: %s: VNOP_GETXATTR: errno %d\n`
- `%s:%d: %s: vecTotal=%lld is too big for compression algorithm 0x%x\n`
- `%s:%d: invalid offset: %llu\n`
- `%s:%d: chunk %u produced %lld of %lld expected bytes\n`
- `com.apple.AppleFSCompressionTypeZlib load succeeded\n`
- `%s:%d: %s: expected size %u, found %llu\n`
- `%s:%d: %s: invalid zlib header\n`
- `%s:%d: %s: decode failed for compression algorithm 0x%x\n`
- `%s:%d: %s: decmpSize=%zu is too big\n`
- `site.decmpfs_vector`
- `site.com_apple_AppleFSCompression_AppleFSCompressionTypeZlib`
- `%s:%d: %s: VNOP_GETXATTR(%llu,%llu) returned %llu\n`
- `%s:%d: %s: VNOP_GETXATTR(%llu,%llu): errno %d\n`
- `%s:%d: %s: resource fork is too small (actual size: %llu < expected min size: %llu) header: (attr_size %u, compression_type %u, uncompressed_size %llu)\n`
- `%s:%d: %s: invalid resource map\n`
- `%s:%d: %s: unknown chunking scheme %llu\n`
- `%s:%d: %s: unknown compression scheme %llu\n`
- `%s:%d: add overflow: offset %llu, totalSize %llu\n`
- `%s:%d: Error: type %d out of range\n`
- `com.apple.AppleFSCompressionTypeZlib kmod start\n`
- `%s:%d: %s: expected chunk count %u, found %u\n`
- `%s:%d: %s: attempting to read chunk %u from file with %u chunks\n`
- `%s:%d: %s: resource fork offsets are out of order (offsets[1] (%u) <= offsets[0] (%u)) \n`
- `12`

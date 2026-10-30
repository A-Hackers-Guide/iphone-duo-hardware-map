# `com.apple.filesystems.tmpfs`

- Name: tmpfs
- Version: `1`
- UUID: `3940B4E9-419F-34B5-8F8E-D6B1E46817D6`
- Source version: `94.40.4.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 15.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 15.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 15.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 15.0

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
000: LC_SEGMENT_64 sz=0x00000cbe off=0x00e1e190-0x00e1ee4e addr=0xfffffe0007e22190-0xfffffe0007e22e4e r--/r--   __TEXT            
	sz=0x000004b7 off=0x00e1e7b8-0x00e1ec6f addr=0xfffffe0007e227b8-0xfffffe0007e22c6f               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000040 off=0x00e1ec70-0x00e1ecb0 addr=0xfffffe0007e22c70-0xfffffe0007e22cb0               __TEXT.__const            
	sz=0x0000019e off=0x00e1ecb0-0x00e1ee4e addr=0xfffffe0007e22cb0-0xfffffe0007e22e4e               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00009e10 off=0x03bba920-0x03bc4730 addr=0xfffffe000abbe920-0xfffffe000abc8730 r-x/r-x   __TEXT_EXEC       
	sz=0x000097d0 off=0x03bba920-0x03bc40f0 addr=0xfffffe000abbe920-0xfffffe000abc80f0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000640 off=0x03bc40f0-0x03bc4730 addr=0xfffffe000abc80f0-0xfffffe000abc8730          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000005a8 off=0x04a3d528-0x04a3dad0 addr=0xfffffe000ba41528-0xfffffe000ba41ad0 rw-/rw-   __DATA            
	sz=0x00000180 off=0x04a3d528-0x04a3d6a8 addr=0xfffffe000ba41528-0xfffffe000ba416a8               __DATA.__data             
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000ba416a8-0xfffffe000ba416b0               __DATA.__bss              (Zerofill)
	sz=0x00000420 off=0x00000000-0x00000420 addr=0xfffffe000ba416b0-0xfffffe000ba41ad0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000ca0 off=0x014c2a88-0x014c3728 addr=0xfffffe00084c6a88-0xfffffe00084c7728 rw-/rw-   __DATA_CONST      
	sz=0x000004e0 off=0x014c2a88-0x014c2f68 addr=0xfffffe00084c6a88-0xfffffe00084c6f68         __DATA_CONST.__const            
	sz=0x00000480 off=0x014c2f68-0x014c33e8 addr=0xfffffe00084c6f68-0xfffffe00084c73e8         __DATA_CONST.__kalloc_type      
	sz=0x00000320 off=0x014c33e8-0x014c3708 addr=0xfffffe00084c73e8-0xfffffe00084c7708         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x014c3708-0x014c3728 addr=0xfffffe00084c7708-0xfffffe00084c7728         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 204 at 0x04b00aec
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3940B4E9-419F-34B5-8F8E-D6B1E46817D6
008: LC_SOURCE_VERSION           94.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004acf258 size=0xe8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `tmpfs`
- `CFBundleIdentifier`: `com.apple.filesystems.tmpfs`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `tmpfs`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/tmpfs.kext`
- `_PrelinkExecutableLoadAddr`: `-2198890995312`
- `_PrelinkExecutableRelativePath`: `tmpfs`
- `_PrelinkExecutableSize`: `48406`
- `_PrelinkExecutableSourceAddr`: `-2198890995312`
- `_PrelinkKmodInfo`: `-2198827952856`

## Strings (44) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"pageout offset not aligned to page size, node %llu, f_offset %llu, pl_offset %d\\n\" @%s:%d`
- `site.struct tmpfs_extent`
- `11112211111`
- `\"tmpfs_alloc_vp: type %p %d\" @%s:%d`
- `221111`
- `\"existing extent offset %llu, len %zu, data %p when attempting to insert offset %llu, len %zu, data %p\\n\" @%s:%d`
- `site.struct tmpfs_mount`
- `2222211222222222`
- `tmpfs_vnops.c`
- `\"Could not allocate space for rename\" @%s:%d`
- `site.struct tmpfs_node`
- `112222222222222222212221111323321222`
- `tmpfs-vnode-create-wait`
- `\"tmpfs_dir_getdents: type %p %d\" @%s:%d`
- `\"Could not init dirent for rename\" @%s:%d`
- `tmpfs_subr.c`
- `tmpfs_io_lock_shared_to_exclusive`
- `\"tmpfs_alloc_node: type %p %d\" @%s:%d`
- `\"extent overlap for offset %llu, len %zu\\n\" @%s:%d`
- `tmpfs_io_lock_exclusive`
- `com.apple.FinderInfo`
- `\"tmpfs_pagein_range: tn_id %llu, cannot shorten range (%llu + %llu) to exclude tail overlap (%llu + %zu)\\n\" @%s:%d`
- `..`
- `hw.memsize`
- `\"%s : Recursive exclusive lock attempt\" @%s:%d`
- `\"tmpfs_free_node: type %p %d\" @%s:%d`
- `site.struct tmpfs_xattr`
- `1112121`
- `\"tmpfs_pagein_range: tn_id %llu, cannot extend range (%llu + %llu) to include head overlap (%llu + %zu)\\n\" @%s:%d`
- `1111`
- `.`
- `com.apple.system.Security`
- `site.struct tmpfs_link_origin`
- `tmpfs`
- `site.struct tmpfs_dirent`
- `com.apple.ResourceFork`

**[__TEXT.__os_log]**

- `Name too long %lu > %lu\n`
- `root user is required for mounting tmpfs volumes\n`
- `max_pages (%llu) exceeds size limit (%llu)\n`
- `max_nodes (%llu) %lu exceeds size limit (%llu)\n`
- `suspcious delen of zero for drec w/file-id %lld flags 0x%x name_len %d name: %.*s\n`
- `normalizeOptCaseFoldAndCompare failed with %d\n`
- `couldn't allocate memory for link origin\n`
- `normalizeOptCaseFoldAndHash failed with error %d\n`

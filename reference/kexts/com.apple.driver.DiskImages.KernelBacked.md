# `com.apple.driver.DiskImages.KernelBacked`

- Name: AppleDiskImagesKernelBacked
- Version: `493.0.0`
- UUID: `E55C9952-43F9-36F1-BA1D-2D5E389752B7`
- Source version: `710.0.0.0.0`
- Depends on: [`com.apple.driver.DiskImages`](com.apple.driver.DiskImages.md) 128, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### IOHDIXHDDriveInKernel
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.KernelBacked`
- `IOClass`: `IOHDIXHDDriveInKernel`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.KernelBacked`
- `IOProbeScore`: `200`
- `IOProviderClass`: `KDIDiskImageNub`

### KDIDiskImageNub
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.KernelBacked`
- `IOClass`: `KDIDiskImageNub`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages.KernelBacked`
- `IOProbeScore`: `100`
- `IOProviderClass`: `KDIDiskImage`


## C++ classes (7) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IODiskImageBlockStorageDeviceInKernel` | 0x98 | IOHDIXHDDriveNub → IOBlockStorageDevice → IOService → IORegistryEntry |
| `IOHDIXHDDriveInKernel` | 0x160 | IOHDIXHDDrive → IOService → IORegistryEntry |
| `KDIBackingStore` | 0xa8 | KDIObject → IOService → IORegistryEntry |
| `KDIDiskImage` | 0xb0 | KDIObject → IOService → IORegistryEntry |
| `KDIDiskImageNub` | 0xa0 | IOService → IORegistryEntry |
| `KDIEncoding` | 0xb0 | KDIBackingStore → KDIObject → IOService → IORegistryEntry |
| `KDIObject` | 0x98 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000009aa off=0x009f18e0-0x009f228a addr=0xfffffe00079f58e0-0xfffffe00079f628a r--/r--   __TEXT            
	sz=0x00000382 off=0x009f1f08-0x009f228a addr=0xfffffe00079f5f08-0xfffffe00079f628a               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000045d4 off=0x0316b2f0-0x0316f8c4 addr=0xfffffe000a16f2f0-0xfffffe000a1738c4 r-x/r-x   __TEXT_EXEC       
	sz=0x00004304 off=0x0316b2f0-0x0316f5f4 addr=0xfffffe000a16f2f0-0xfffffe000a1735f4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002d0 off=0x0316f5f4-0x0316f8c4 addr=0xfffffe000a1735f4-0xfffffe000a1738c4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001f4 off=0x049f1380-0x049f1574 addr=0xfffffe000b9f5380-0xfffffe000b9f5574 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049f1380-0x049f1444 addr=0xfffffe000b9f5380-0xfffffe000b9f5444               __DATA.__data             
	sz=0x00000128 off=0x00000000-0x00000128 addr=0xfffffe000b9f5448-0xfffffe000b9f5570               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9f5570-0xfffffe000b9f5574               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003118 off=0x01382df0-0x01385f08 addr=0xfffffe0008386df0-0xfffffe0008389f08 rw-/rw-   __DATA_CONST      
	sz=0x00000038 off=0x01382df0-0x01382e28 addr=0xfffffe0008386df0-0xfffffe0008386e28         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000038 off=0x01382e28-0x01382e60 addr=0xfffffe0008386e28-0xfffffe0008386e60         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002d28 off=0x01382e60-0x01385b88 addr=0xfffffe0008386e60-0xfffffe0008389b88         __DATA_CONST.__const            
	sz=0x000001c0 off=0x01385b88-0x01385d48 addr=0xfffffe0008389b88-0xfffffe0008389d48         __DATA_CONST.__kalloc_type      
	sz=0x00000168 off=0x01385d48-0x01385eb0 addr=0xfffffe0008389d48-0xfffffe0008389eb0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x01385eb0-0x01385f08 addr=0xfffffe0008389eb0-0xfffffe0008389f08         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 101 at 0x04af2994
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E55C9952-43F9-36F1-BA1D-2D5E389752B7
008: LC_SOURCE_VERSION           710.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac0300 size=0xf8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiskImagesKernelBacked`
- `CFBundleIdentifier`: `com.apple.driver.DiskImages.KernelBacked`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImagesKernelBacked`
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
- `OSBundleCompatibleVersion`: `128`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDIXController.kext/PlugIns/AppleDiskImagesKernelBacked.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895372064`
- `_PrelinkExecutableRelativePath`: `AppleDiskImagesKernelBacked`
- `_PrelinkExecutableSize`: `33418`
- `_PrelinkExecutableSourceAddr`: `-2198895372064`
- `_PrelinkKmodInfo`: `-2198828264576`

## Strings (39) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1211111212221212121221`
- `lockable`
- `site.IODiskImageBlockStorageDeviceInKernel`
- `12111112122212121111211111222222111122122121`
- `blockcount`
- `KDIBackingStore::readBytes: returning kIOReturnUnsupported\n`
- `KDIEncoding`
- `KDIDiskImageNub`
- `site.KDIDiskImageNub`
- `1211111212221212111`
- `double-buffer`
- `NOTE: double-buffering enabled\n`
- `KDIObject`
- `netboot-image`
- `image-format-read-only`
- `KDIBackingStore`
- `KDIURLDiskImageNubAttached`
- `KDIDiskImage`
- `KDIDiskImageInhibitMatching`
- `removable`
- `IODiskImageBlockStorageDeviceInKernel`
- `site.KDIEncoding`
- `IOHDIXHDDriveInKernel: NOTICE: double buffering: %d\n`
- `throttle-threshold`
- `site.KDIBackingStore`
- `1211111212221212121`
- `KDIBackingStore::writeBytes: returning kIOReturnUnsupported\n`
- `IOHDIXHDDriveInKernel`
- `site.IOHDIXHDDriveInKernel`
- `write-protected`
- `site.KDIObject`
- `blocksize`
- `121111121222121212121`
- `1211111212221212121211`
- `12111112122212121112`
- `KDIDiskImageNubUserClient`
- `ejectable`
- `shadow-path`
- `site.KDIDiskImage`

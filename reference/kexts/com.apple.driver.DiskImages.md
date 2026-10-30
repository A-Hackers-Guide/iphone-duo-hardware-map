# `com.apple.driver.DiskImages`

- Name: AppleDiskImageDriver
- Version: `493.0.0`
- UUID: `64138D28-CD63-3CD9-ABF5-DD6ECDC61EF8`
- Source version: `710.0.0.0.0`
- Depends on: [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOHDIXController
- `CFBundleIdentifier`: `com.apple.driver.DiskImages`
- `IOClass`: `IOHDIXController`
- `IOMatchCategory`: `IOHDIXController`
- `IOPersonalityPublisher`: `com.apple.driver.DiskImages`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`


## C++ classes (7) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOHDIXCommandPool` | 0x38 |  |
| `IOHDIXCommandQueue` | 0x30 |  |
| `IOHDIXController` | 0x118 | IOService → IORegistryEntry |
| `IOHDIXControllerUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `IOHDIXHDDrive` | 0x120 | IOService → IORegistryEntry |
| `IOHDIXHDDriveNub` | 0x98 | IOBlockStorageDevice → IOService → IORegistryEntry |
| `KDIURL` | 0xb0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000013d0 off=0x009efc90-0x009f1060 addr=0xfffffe00079f3c90-0xfffffe00079f5060 r--/r--   __TEXT            
	sz=0x00000da8 off=0x009f02b8-0x009f1060 addr=0xfffffe00079f42b8-0xfffffe00079f5060               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00009690 off=0x031606e0-0x03169d70 addr=0xfffffe000a1646e0-0xfffffe000a16dd70 r-x/r-x   __TEXT_EXEC       
	sz=0x00009220 off=0x031606e0-0x03169900 addr=0xfffffe000a1646e0-0xfffffe000a16d900          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000470 off=0x03169900-0x03169d70 addr=0xfffffe000a16d900-0xfffffe000a16dd70          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001f0 off=0x049f1090-0x049f1280 addr=0xfffffe000b9f5090-0xfffffe000b9f5280 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049f1090-0x049f1158 addr=0xfffffe000b9f5090-0xfffffe000b9f5158               __DATA.__data             
	sz=0x00000128 off=0x00000000-0x00000128 addr=0xfffffe000b9f5158-0xfffffe000b9f5280               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000029b8 off=0x0137fc00-0x013825b8 addr=0xfffffe0008383c00-0xfffffe00083865b8 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x0137fc00-0x0137fc30 addr=0xfffffe0008383c00-0xfffffe0008383c30         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x0137fc30-0x0137fc60 addr=0xfffffe0008383c30-0xfffffe0008383c60         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002320 off=0x0137fc60-0x01381f80 addr=0xfffffe0008383c60-0xfffffe0008385f80         __DATA_CONST.__const            
	sz=0x000002c0 off=0x01381f80-0x01382240 addr=0xfffffe0008385f80-0xfffffe0008386240         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x01382240-0x013822e0 addr=0xfffffe0008386240-0xfffffe00083862e0         __DATA_CONST.__kalloc_var       
	sz=0x00000238 off=0x013822e0-0x01382518 addr=0xfffffe00083862e0-0xfffffe0008386518         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a0 off=0x01382518-0x013825b8 addr=0xfffffe0008386518-0xfffffe00083865b8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 162 at 0x04af25bc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     64138D28-CD63-3CD9-ABF5-DD6ECDC61EF8
008: LC_SOURCE_VERSION           710.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac0180 size=0x150
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOHDIXController`
- `CFBundleIdentifier`: `com.apple.driver.DiskImages`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiskImageDriver`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDIXController.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895379312`
- `_PrelinkExecutableRelativePath`: `IOHDIXController`
- `_PrelinkExecutableSize`: `54792`
- `_PrelinkExecutableSourceAddr`: `-2198895379312`
- `_PrelinkKmodInfo`: `-2198828265328`

## Strings (153) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOHDIXController: NOTE: administrator is creating non-ejectable disk image\n`
- `IOHDIXController::checkPermission: WARNING: UID spoofing detected (and defeated) (%ld, %ld)\n`
- `%x`
- `di-root-image`
- `findAppropriateIOMediaObject: >> whole=TRUE, leaf=TRUE <<\n`
- `createImageInfoDict`
- `file`
- `IOHDIXCommandPool::allocCommand(): inactive command pool after command claim\n`
- `removable`
- `BSD Name`
- `7C3457EF-0000-11AA-AA11-00306543ECAC`
- `!*'(),`
- `idle! `
- `IOHDIXCommandPool`
- `[disk image]`
- `root`
- `BSD Minor`
- `KDIURL`
- `di-root-removable`
- `IOHDIXController::_di_root_image: returning 0x%x (%d)\n`
- `disk image`
- `lockable`
- `abcdefghijklmnopqrstuvwxyz`
- `wake   `
- `site.IOHDIXCommand`
- `12111112122212121212222222222222221`
- `;`
- `IOHDIXCommandQueue`
- `Protocol Characteristics`
- `IOHDIXHDDriveNub`
- `1222111`
- `blocksize`
- `AppleAPFSContainerScheme`
- `File`
- `KDIURLTerminateMatching`
- `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- `:`
- `image-path`
- `KDIURLScheme`
- `KDIURLParameters`
- `//`
- `findAppropriateIOMediaObject: failed to get child iterator for '%s'\n`
- `IOHDIXHDDrive`
- `image-fd`
- `?`
- `write  `
- `IOHDIXCommandPool::allocCommand(): inactive command pool\n`
- `revision`
- `1211111212221212111`
- `KDIURLPort`
- `211111112111`
- `Physical Interconnect Location`
- `site.KDIURL`
- `KDIURLQuery`
- `Disk Image Driver for MacOS X`
- `IOUnit`
- `di-root-ram-file`
- `ramfile`
- `121111121222121211111111111111`
- `blocksize-multiple`
- `system-image`
- `KDIURLExtension`
- `Virtual Interface System Image`
- `IOHDIXController`
- `KDIURLDiskImageNubAttached`
- `IOMedia`
- `throttle-unit`
- `KDIURLPassword`
- `netboot-image`
- `KDIURLUser`
- `sleep! `
- `IOHDIXController::createDriveInKernel: returning error 0x%x\n`
- `findAppropriateIOMediaObject: no matching IOMedia found for drive %d\n`
- `121111121222121211112111112222221111`
- `Virtual Interface`
- `Device Characteristics`
- `#`
- `122222111122222111112`
- `di-root-image-devname`
- `validateImageInfoDict`
- `blockcount`
- `Network`
- `+-.`
- `Apple_HFSX`
- `site.struct DecomposedURL`
- `id ...entry.. ...prev... ...next... ...obj....\n`
- `Apple`
- `site.IOHDIXHDDriveNub`
- `@`
- `121112`
- `term  `
- `vendor`
- `model`
- `findAppropriateIOMediaObject: >> 48465300-0000-11AA-AA11-00306543ECAC (GPT HFS) <<\n`
- `;/?:@&=`
- `IOHDIXCommandQueue::displayQueue 0x%p\n`
- `site.IOHDIXHDDrive`
- `image-type`
- `KDIURLPath`
- `KDIURLFragment`
- `owner-uid`
- `ramfile-memory-descriptor`
- `%s: OSUnserializeXML failure %s\n`
- `%s: Invalid image property.\n`
- `write-protected`
- `ejectable`
- `Virtual Interface Location Path`
- `site.IOHDIXCommandPool`
- `ramfile://%u`
- `image-secrets`
- `IOHDIXHDDrive::sanitizeIOResult: Mapping DI error %d to EIO\n`
- `autodiskmount`
- `:@&=`
- `read   `
- `IOHDIXControllerUserClient`
- `710`
- `IOClass`
- `IOHDIXCommandPool::allocCommand(): failing mallocSingleCommand\n`
- `findAppropriateIOMediaObject: >> Apple_HFS <<\n`
- `findAppropriateIOMediaObject: >> whole=TRUE, leaf=FALSE AppleAPFSContainerScheme child <<\n`
- `IOKitDebug`
- `KDIURLHost`
- `di-root-image-result`
- `BSD Major`
- `$-_.+`
- `;?&=`
- `site.IOHDIXController`
- `48465300-0000-11AA-AA11-00306543ECAC`
- `Apple_HFS`
- `findAppropriateIOMediaObject: >> Apple_HFSX <<\n`
- `com.apple.private.diskimages.kext.user-client-access`
- `IOUserClientClass`
- `1211111212221212121111`
- `Vendor Name`
- `IOHDIXController::_di_root_image: find*IOMediaObject() returned 0x%x\n`
- `findAppropriateIOMediaObject: with %s %d\n`
- `Leaf`
- `site.IOHDIXCommandQueue`
- `Product Revision Level`
- `IOHDIXController::_di_root_image: createDriveInKernel() returned 0x%x (%d)\n`
- `findAppropriateIOMediaObject: >> 7C3457EF-0000-11AA-AA11-00306543ECAC (GPT APFS) <<\n`
- `0123456789abcdefABCDEF`
- `Product Name`
- `KDIURLAttachResult`
- `site.IOHDIXControllerUserClient`
- `IOProviderClass`
- `Physical Interconnect`
- `Disk Image`
- `KDIURLFD`
- `ID %lld: 0x%016qX (%qd) blocks, starting at block 0x%016qX (%qd)\n`
- `di-root-image-devt`
- `IOHDIXHDDrive::doAsyncReadWrite(): failed to allocate command\n`
- `0123456789`

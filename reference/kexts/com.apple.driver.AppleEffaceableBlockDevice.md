# `com.apple.driver.AppleEffaceableBlockDevice`

- Name: AppleEffaceableBlockDevice
- Version: `1.0`
- UUID: `CF57BA97-6184-3E78-8280-7D2B5807CA60`
- Source version: `92.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEffaceableStorage`](com.apple.driver.AppleEffaceableStorage.md) 1.0.0, [`com.apple.iokit.IOStorageFamily`](com.apple.iokit.IOStorageFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleEffaceableBlockDevice
- `CFBundleIdentifier`: `com.apple.driver.AppleEffaceableBlockDevice`
- `IOClass`: `AppleEffaceableBlockDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEffaceableBlockDevice`
- `IOProviderClass`: `IOEffaceableDevice`

### AppleEffaceableBlockDevice-NVMe
- `CFBundleIdentifier`: `com.apple.driver.AppleEffaceableBlockDevice`
- `IOClass`: `AppleEffaceableBlockDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEffaceableBlockDevice`
- `IOProviderClass`: `IONVMeEffaceableDevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEffaceableBlockDevice` | 0x298 | AppleEffaceableStorage → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000073e off=0x0042cd20-0x0042d45e addr=0xfffffe0007430d20-0xfffffe000743145e r--/r--   __TEXT            
	sz=0x00000166 off=0x0042d2f8-0x0042d45e addr=0xfffffe00074312f8-0xfffffe000743145e               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000108c off=0x01bc55d0-0x01bc665c addr=0xfffffe0008bc95d0-0xfffffe0008bca65c r-x/r-x   __TEXT_EXEC       
	sz=0x00000f1c off=0x01bc55d0-0x01bc64ec addr=0xfffffe0008bc95d0-0xfffffe0008bca4ec          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000170 off=0x01bc64ec-0x01bc665c addr=0xfffffe0008bca4ec-0xfffffe0008bca65c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0493d810-0x0493d910 addr=0xfffffe000b941810-0xfffffe000b941910 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493d810-0x0493d8d8 addr=0xfffffe000b941810-0xfffffe000b9418d8               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9418d8-0xfffffe000b941910               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000770 off=0x01063e80-0x010645f0 addr=0xfffffe0008067e80-0xfffffe00080685f0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01063e80-0x01063e88 addr=0xfffffe0008067e80-0xfffffe0008067e88         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01063e88-0x01063e90 addr=0xfffffe0008067e88-0xfffffe0008067e90         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f8 off=0x01063e90-0x01064488 addr=0xfffffe0008067e90-0xfffffe0008068488         __DATA_CONST.__const            
	sz=0x00000080 off=0x01064488-0x01064508 addr=0xfffffe0008068488-0xfffffe0008068508         __DATA_CONST.__kalloc_type      
	sz=0x000000b8 off=0x01064508-0x010645c0 addr=0xfffffe0008068508-0xfffffe00080685c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x010645c0-0x010645f0 addr=0xfffffe00080685c0-0xfffffe00080685f0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 52 at 0x04ad7630
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CF57BA97-6184-3E78-8280-7D2B5807CA60
008: LC_SOURCE_VERSION           92.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9e128 size=0x40
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEffaceableBlockDevice`
- `CFBundleIdentifier`: `com.apple.driver.AppleEffaceableBlockDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEffaceableBlockDevice`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleLibraries_x86_64`:
  - `com.apple.driver.AppleEffaceableStorage`: `1.0.0`
  - `com.apple.iokit.IOStorageFamily`: `1.0.0`
  - `com.apple.kpi.bsd`: `8.0`
  - `com.apple.kpi.iokit`: `8.0`
  - `com.apple.kpi.libkern`: `8.0`
  - `com.apple.kpi.mach`: `8.0`
  - `com.apple.kpi.unsupported`: `8.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEffaceableBlockDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901420768`
- `_PrelinkExecutableRelativePath`: `AppleEffaceableBlockDevice`
- `_PrelinkExecutableSize`: `8250`
- `_PrelinkExecutableSourceAddr`: `-2198901420768`
- `_PrelinkKmodInfo`: `-2198829000688`

## Strings (14) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleEffaceableBlockDevice`
- `ERR `
- `AppleEffaceableBlockDevice.cpp`
- `t8015`
- `\"no memory\" @%s:%d`
- `111`
- `AppleEffaceableBlockDevice`
- `12111112122212121111111111111111111111111111111111111111111111111111111111121111111`
- `[effaceable:%s] bug in kext matching\n`
- `[effaceable:%s] super failed to start\n`
- `\"null context\" @%s:%d`
- `/arm-io`
- `device_type`
- `site.effaceable_bdev_context_t`

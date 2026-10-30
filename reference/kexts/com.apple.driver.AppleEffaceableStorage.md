# `com.apple.driver.AppleEffaceableStorage`

- Name: AppleEffaceableStorage
- Version: `1.0`
- UUID: `9E88A776-5DA3-3F5A-B011-1D864FFBA685`
- Source version: `92.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEffaceableStorage` | 0x250 | IOService → IORegistryEntry |
| `AppleEffaceableStorageUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001b04 off=0x0042d460-0x0042ef64 addr=0xfffffe0007431460-0xfffffe0007432f64 r--/r--   __TEXT            
	sz=0x0000148b off=0x0042da88-0x0042ef13 addr=0xfffffe0007431a88-0xfffffe0007432f13               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000044 off=0x0042ef20-0x0042ef64 addr=0xfffffe0007432f20-0xfffffe0007432f64               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00004f5c off=0x01bc6660-0x01bcb5bc addr=0xfffffe0008bca660-0xfffffe0008bcf5bc r-x/r-x   __TEXT_EXEC       
	sz=0x00004d1c off=0x01bc6660-0x01bcb37c addr=0xfffffe0008bca660-0xfffffe0008bcf37c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000240 off=0x01bcb37c-0x01bcb5bc addr=0xfffffe0008bcf37c-0xfffffe0008bcf5bc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x0493d910-0x0493da38 addr=0xfffffe000b941910-0xfffffe000b941a38 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493d910-0x0493d9d8 addr=0xfffffe000b941910-0xfffffe000b9419d8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9419d8-0xfffffe000b941a38               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000010e0 off=0x010645f0-0x010656d0 addr=0xfffffe00080685f0-0xfffffe00080696d0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x010645f0-0x01064600 addr=0xfffffe00080685f0-0xfffffe0008068600         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01064600-0x01064610 addr=0xfffffe0008068600-0xfffffe0008068610         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c78 off=0x01064610-0x01065288 addr=0xfffffe0008068610-0xfffffe0008069288         __DATA_CONST.__const            
	sz=0x00000300 off=0x01065288-0x01065588 addr=0xfffffe0008069288-0xfffffe0008069588         __DATA_CONST.__kalloc_type      
	sz=0x00000120 off=0x01065588-0x010656a8 addr=0xfffffe0008069588-0xfffffe00080696a8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x010656a8-0x010656d0 addr=0xfffffe00080696a8-0xfffffe00080696d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 77 at 0x04ad7700
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9E88A776-5DA3-3F5A-B011-1D864FFBA685
008: LC_SOURCE_VERSION           92.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9e168 size=0xb0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEffaceableStorage`
- `CFBundleIdentifier`: `com.apple.driver.AppleEffaceableStorage`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEffaceableStorage`
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
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEffaceableStorage.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901418912`
- `_PrelinkExecutableRelativePath`: `AppleEffaceableStorage`
- `_PrelinkExecutableSize`: `31848`
- `_PrelinkExecutableSourceAddr`: `-2198901418912`
- `_PrelinkKmodInfo`: `-2198829000432`

## Strings (114) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1121`
- `[effaceable:%s] external client tried to efface driver private locker\n`
- `site.effaceable_nor_context_t`
- `[effaceable:%s] found current generation, %d, in group %d\n`
- `[effaceable:%s] attempting to read past end of content\n\n`
- `\"null context\" @%s:%d`
- `AppleEffaceableStorageUserClient::%s():[%s] bug in kext matching\n`
- `AppleEffaceableStorageUserClient::%s():[%s] format attempt from untrusted root\n`
- `GroupCount`
- `[effaceable:%s] have 'unknown' generation: 0x%08X\n`
- `[effaceable:%s] group %d will neither store a clone nor can it be effaced\n`
- `AppleEffaceableStorageUserClient`
- `AppleEffaceableStorageUserClient::%s():[%s] failed to determine root trust state\n`
- `AppleEffaceableStorageUserClient::%s():[%s] setLockerWithID: missing input arguments\n`
- `[effaceable:%s] major version mismatch - expect 0x%08X, have 0x%08X\n`
- `IsFormatted`
- `[effaceable:%s] client trying to create locker sentinel\n`
- `[effaceable:%s] locker overflow\n`
- `[effaceable:%s] couldn't acquire command gate\n`
- `[effaceable:%s] unable to commit initial generation to any group\n`
- `[effaceable:%s] wipe %sabled via boot-arg\n`
- `[effaceable:%s] checksum failed - calculated 0x%08X, have 0x%08X\n`
- `Generation`
- `site.locker_t`
- `[effaceable:%s] unable to write any units in group %d during commit\n`
- `start`
- `CopySize`
- `[effaceable:%s] external client tried to overwrite private locker\n`
- `EffaceLocker`
- `externalMethod`
- `AppleEffaceableStorageUserClient::%s():[%s] setLocker: missing input arguments\n`
- `[effaceable:%s] full scan %sabled via boot-arg\n`
- `[effaceable:%s] all %d units unreadable during confirmation of group %d\n`
- `AppleEffaceableStorage`
- `AppleEffaceableStorageUserClient::%s():[%s] wipe attempt from untrusted root\n`
- `AppleEffaceableStorageUserClient::%s():[%s] getLocker: missing input/output arguments\n`
- `UnitsPerGroup`
- `effaceable-enable-wipe`
- `ERROR`
- `VersionMinor`
- `GroupIndex`
- `[effaceable:%s] failed to get lockers\n`
- `[effaceable:%s] cannot get bytes to buffer referenced by NULL pointer\n\n`
- `12111112122212121111111111111111111111111111111111111111111111111111111111`
- `[effaceable:%s] couldn't allocate function symbols\n`
- `AppleEffaceableStorageUserClient::%s():[%s] not authorized\n`
- `AppleEffaceableStorageUserClient::%s():[%s] getCapacity: missing output argument\n`
- `111`
- `AppleEffaceableStorage.cpp`
- `1211111212221212111111111111`
- `AppleEffaceableStorageUserClient::%s():[%s] effaceLocker: missing input argument\n`
- `VersionMajor`
- `[effaceable:%s] format succeeded\n`
- `failed`
- `GetLocker`
- `site.AppleEffaceableStorageUserClient`
- `[effaceable:%s] have 'unknown' minor version: 0x%08X\n`
- `[effaceable:%s] external client tried to read private locker\n`
- `msg @%s:%d`
- `[effaceable:%s] attempting to write past end of content\n`
- `ERR `
- `[effaceable:%s] attempt to efface locker sentinel\n`
- `[effaceable:%s] unable to efface at least %d out of %d groups\n`
- `[effaceable:%s] couldn't init work loop\n`
- `Capacity`
- `[effaceable:%s] unable to find content\n`
- `[effaceable:%s] wipe of formatted storage not permitted without 'effaceable-enable-wipe=1' boot-arg\n`
- `succeeded`
- `22111111111`
- `AppleEffaceableStorageUserClient::%s():[%s] lockerSpace: missing input/output arguments\n`
- `UnitSize`
- `[effaceable:%s] untrusted client trying to create protected locker\n`
- `[effaceable:%s] cannot set bytes from buffer referenced by 0 pointer\n`
- `[effaceable:%s] super did not start\n\n`
- `AppleEffaceableStorageUserClient::%s():[%s] super failed to start\n`
- `INIT`
- `[effaceable:%s] couldn't find the droid you were looking for\n`
- `site.effaceable_storage_context_t`
- `AppleEffaceableStorageUserClient::%s():[%s] generateNonce: missing output argument\n`
- `en`
- `[effaceable:%s] untrusted client trying to overwrite protected locker\n`
- `[effaceable:%s] attempt to wildcard efface from untrusted client\n`
- `[effaceable:%s] unprivileged client attempting to efface protected locker\n`
- `[effaceable:%s] failed to efface nonce\n`
- `AppleEffaceableStorageUserClient::%s():[%s] isFormatted: missing output argument\n`
- `[effaceable:%s] no valid copies found given %d of %d readable units during confirmation of group %d\n`
- `[effaceable:%s] %s\n`
- `AppleEffaceableStorageUserClient::%s():[%s] getBytes is only allowed when kernel debug is enabled\n`
- `[effaceable:%s] have 'invalid' minor version: 0x%08X\n`
- `Space`
- `SecureRoot`
- `AppleEffaceableStorageUserClient::%s():[%s] effaceLocker: untrusted attempt to efface by wildcard\n`
- `effaceable-enable-full-scan`
- `[effaceable:%s] unable to efface group %d after %d attempts\n`
- `[effaceable:%s] untrusted client tried to read protected key\n`
- `[effaceable:%s] unable to set nonce\n`
- `site.AppleEffaceableStorage`
- `AppleEffaceableStorageUserClient::%s():[%s] setBytes from user client to service failed\n`
- `CopiesPerUnit`
- `[effaceable:%s] did not find the locker with type_id - 0x%x\n`
- `[effaceable:%s] internal locker overflow\n`
- `[effaceable:%s] formatting storage\n`
- `AppleEffaceableStorageUserClient::%s():[%s] getBytes from user client to service failed\n`
- `AppleEffaceableStorageUserClient::%s():[%s] bad selector %u\n`
- `[effaceable:%s] have 'invalid' generation: 0x%08X\n`
- `[effaceable:%s] external client tried to write private locker\n`
- `SetLocker`
- `GenerateNonce`
- `root`
- `AppleEffaceableStorageUserClient::%s():[%s] setBytes failed with badArgument\n`
- `AppleEffaceableStorageUserClient::%s():[%s] setBytes is only allowed when kernel debug is enabled\n`
- `[effaceable:%s] started\n`
- `[effaceable:%s] data_size argument is too big 0x%x\n`
- `[effaceable:%s] unable to either write modified content to or efface group %d\n\n`

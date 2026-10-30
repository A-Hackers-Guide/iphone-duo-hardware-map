# `com.apple.iokit.IOReportFamily`

- Name: IOReportFamily
- Version: `47`
- UUID: `FA7F6706-A14F-32CE-BEC0-F6BEEC0EBEC7`
- Source version: `116.0.0.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOReportHub
- `CFBundleIdentifier`: `com.apple.iokit.IOReportFamily`
- `IOClass`: `IOReportHub`
- `IOMatchCategory`: `IOReportHub`
- `IOPersonalityPublisher`: `com.apple.iokit.IOReportFamily`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `IOReportUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOReportHub` | 0x98 | IOService → IORegistryEntry |
| `IOReportUserClient` | 0x108 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000dab off=0x00a51380-0x00a5212b addr=0xfffffe0007a55380-0xfffffe0007a5612b r--/r--   __TEXT            
	sz=0x00000237 off=0x00a519f8-0x00a51c2f addr=0xfffffe0007a559f8-0xfffffe0007a55c2f               __TEXT.__cstring          (CstringLiterals)
	sz=0x000004fc off=0x00a51c2f-0x00a5212b addr=0xfffffe0007a55c2f-0xfffffe0007a5612b               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00003170 off=0x03355420-0x03358590 addr=0xfffffe000a359420-0xfffffe000a35c590 r-x/r-x   __TEXT_EXEC       
	sz=0x00002f60 off=0x03355420-0x03358380 addr=0xfffffe000a359420-0xfffffe000a35c380          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000210 off=0x03358380-0x03358590 addr=0xfffffe000a35c380-0xfffffe000a35c590          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x04a14ff8-0x04a15120 addr=0xfffffe000ba18ff8-0xfffffe000ba19120 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a14ff8-0x04a150c0 addr=0xfffffe000ba18ff8-0xfffffe000ba190c0               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba190c0-0xfffffe000ba19120               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000fb8 off=0x013d5388-0x013d6340 addr=0xfffffe00083d9388-0xfffffe00083da340 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013d5388-0x013d5398 addr=0xfffffe00083d9388-0xfffffe00083d9398         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013d5398-0x013d53a8 addr=0xfffffe00083d9398-0xfffffe00083d93a8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000d18 off=0x013d53a8-0x013d60c0 addr=0xfffffe00083d93a8-0xfffffe00083da0c0         __DATA_CONST.__const            
	sz=0x00000080 off=0x013d60c0-0x013d6140 addr=0xfffffe00083da0c0-0xfffffe00083da140         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x013d6140-0x013d61e0 addr=0xfffffe00083da140-0xfffffe00083da1e0         __DATA_CONST.__kalloc_var       
	sz=0x00000108 off=0x013d61e0-0x013d62e8 addr=0xfffffe00083da1e0-0xfffffe00083da2e8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x013d62e8-0x013d6340 addr=0xfffffe00083da2e8-0xfffffe00083da340         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 77 at 0x04af6674
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     FA7F6706-A14F-32CE-BEC0-F6BEEC0EBEC7
008: LC_SOURCE_VERSION           116.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac4410 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOReportFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOReportFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOReportFamily`
- `CFBundleNumericVersion`: `1191215104`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `47`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2020 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOReportFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894980224`
- `_PrelinkExecutableRelativePath`: `IOReportFamily`
- `_PrelinkExecutableSize`: `20475`
- `_PrelinkExecutableSourceAddr`: `-2198894980224`
- `_PrelinkKmodInfo`: `-2198828118024`

## Strings (44) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.DisableThreadCallContext`
- `111`
- `\"%s\" @%s:%d`
- `IOReportDictionaryInterestChannelListKey`
- `IOReportUserClient`
- `121111121222121211111111111211111`
- `_configureInterests`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `IOReportHub`
- `site.IOReportUserClient`
- `nElements`
- `OSBoundedPtr.h`
- `site.IOReportHub`
- `1211111212221212111`
- `IOReportElement`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `IOReportDictionaryDriverEntryIDsKey`
- `IOReportDictionaryElementCounts`

**[__TEXT.__os_log]**

- `Warning: %s->updateReport(): %#x`
- `IOReporting bad driver: %s->updateReport() added %u elements, %llu bytes, preallocated count = %llu`
- `getSnapshotDelta: cannot create snapshots array`
- `getSnapshotDelta: cannot create iterator`
- `getSnapshotDelta: max number of snapshots reached: %u`
- `driver/channel/elementCount (%u/%u/%u) array size mismatch`
- `getSnapshotDelta: Channel value going backwards. Using latest value`
- `Could not enable channels: %x`
- `IOReporting bad driver: %s->configureReport(kIOReportGetDimensions), negative element count`
- `IOReporting bad driver: %s->updateReport() decreased buffer length or returned a negative result`
- `getSnapshotDelta: getValue returned %08X`
- `getSnapshotDelta: cannot create new snapshots buffer`
- `getSnapshotDelta: Cannot add snapshot to array`
- `channel selection => zero-element buffer`
- `no subscription buffer @[%lld]: %#x`
- `Could not find subscription buffer`
- `getSnapshotDelta: Found channel on reporter that is not simple`
- `%s: %s > INT_MAX / sizeof(%s)!`
- `no subscription to disable`
- `Warning: %s->configureReport(%#x)): %#x`
- `could not unpack subscription dict`
- `getSnapshotDelta: cannot append new SnapshotElement`
- `Could not get subscription buffer sizs: %x`
- `%s: %s <= 0!`
- `couldn't decode list of drivers/channels`
- `IOReturn %#x disabling subscription on user client stop`

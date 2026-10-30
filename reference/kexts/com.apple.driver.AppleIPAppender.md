# `com.apple.driver.AppleIPAppender`

- Name: AppleIPAppender
- Version: `1.0`
- UUID: `6FC3AC52-6630-3991-9D1D-0F3715FB0351`
- Source version: `186.0.0.0.0`
- Depends on: [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 1.4.3, [`com.apple.iokit.IOSkywalkFamily`](com.apple.iokit.IOSkywalkFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleIPAppender
- `CFBundleIdentifier`: `com.apple.driver.AppleIPAppender`
- `IOClass`: `AppleIPAppender`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleIPAppender`
- `IOPersonalityPublisher`: `com.apple.driver.AppleIPAppender`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `AppleIPAppenderUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleIPAppender` | 0x348 | IOService → IORegistryEntry |
| `AppleIPAppenderUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |
| `AppleIPDormancyHandler` | 0x70 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000d30 off=0x00522970-0x005236a0 addr=0xfffffe0007526970-0xfffffe00075276a0 r--/r--   __TEXT            
	sz=0x0000063c off=0x00523038-0x00523674 addr=0xfffffe0007527038-0xfffffe0007527674               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x00523680-0x005236a0 addr=0xfffffe0007527680-0xfffffe00075276a0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000564c off=0x0201da40-0x0202308c addr=0xfffffe0009021a40-0xfffffe000902708c r-x/r-x   __TEXT_EXEC       
	sz=0x000052fc off=0x0201da40-0x02022d3c addr=0xfffffe0009021a40-0xfffffe0009026d3c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000350 off=0x02022d3c-0x0202308c addr=0xfffffe0009026d3c-0xfffffe000902708c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000002b0 off=0x0494d5d0-0x0494d880 addr=0xfffffe000b9515d0-0xfffffe000b951880 rw-/rw-   __DATA            
	sz=0x000000c9 off=0x0494d5d0-0x0494d699 addr=0xfffffe000b9515d0-0xfffffe000b951699               __DATA.__data             
	sz=0x00000120 off=0x00000000-0x00000120 addr=0xfffffe000b9516a0-0xfffffe000b9517c0               __DATA.__common           (Zerofill)
	sz=0x000000c0 off=0x00000000-0x000000c0 addr=0xfffffe000b9517c0-0xfffffe000b951880               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000015c8 off=0x01112f48-0x01114510 addr=0xfffffe0008116f48-0xfffffe0008118510 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x01112f48-0x01112f60 addr=0xfffffe0008116f48-0xfffffe0008116f60         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01112f60-0x01112f78 addr=0xfffffe0008116f60-0xfffffe0008116f78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001030 off=0x01112f78-0x01113fa8 addr=0xfffffe0008116f78-0xfffffe0008117fa8         __DATA_CONST.__const            
	sz=0x00000280 off=0x01113fa8-0x01114228 addr=0xfffffe0008117fa8-0xfffffe0008118228         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x01114228-0x01114318 addr=0xfffffe0008118228-0xfffffe0008118318         __DATA_CONST.__kalloc_var       
	sz=0x000001a8 off=0x01114318-0x011144c0 addr=0xfffffe0008118318-0xfffffe00081184c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x011144c0-0x01114510 addr=0xfffffe00081184c0-0xfffffe0008118510         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 116 at 0x04add3d4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     6FC3AC52-6630-3991-9D1D-0F3715FB0351
008: LC_SOURCE_VERSION           186.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa54d8 size=0xf0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleIPAppender`
- `CFBundleIdentifier`: `com.apple.driver.AppleIPAppender`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleIPAppender`
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
- `NSHumanReadableCopyright`: `Copyright © 2008-2009 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleIPAppender.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900414096`
- `_PrelinkExecutableRelativePath`: `AppleIPAppender`
- `_PrelinkExecutableSize`: `31732`
- `_PrelinkExecutableSourceAddr`: `-2198900414096`
- `_PrelinkKmodInfo`: `-2198828935728`

## Strings (47) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `InvalidTrafficClass`
- `setSkywalkInterfaceGated`
- `baseband`
- `121111121222121211111111111111`
- `site.AppleIPAppender`
- `site.AppleIPAppenderFilterRuleCBInfo`
- `Streaming Media`
- `Interactive Voice`
- `Control`
- `\"tx signal callback not available\" @%s:%d`
- `AppleIPAppender.cpp`
- `Responsive Data`
- `site.AppleIPDormancyHandler`
- `%s: given buffer cannot be NULL\n`
- `bool AppleIPOpenPortsList::getPortListsRaw(const ifnet_t, unsigned int, uint8_t *, unsigned int)`
- `AppleIPAppender`
- `111`
- `setLinkQualityMetricGated`
- `Attempt to enable IONetworkInterface without disabling previous one - %p, %p\n`
- `AppleIPDormancyHandler`
- `12112221111111`
- `site.AppleIPAppenderCompletion`
- `getKeepaliveOffloadFramesGated: Failed to allocate memory\n`
- `com.apple.driver.AppleIPAppender.user-access`
- `%s: The Page Number(%u) cannot exceed the maximum page number (%u)\n`
- `Administration`
- `2211`
- `Best Effort`
- `site.AppleIPAppenderUserClient`
- `11111111`
- `%s: Failed to allocate a buffer\n`
- `%s: BitFieldBuffer is not ready or failed to copy Buffer.\n`
- `bool AppleIPOpenPortsList::copyBitFieldBuffer(uint8_t *, unsigned int)`
- `121111121222121211222221111111222222222222111111111122222211111111111111111111111211111111111111111111111`
- `Responsive Media`
- `AppleIPAppenderUserClient`
- `Background`
- `Interactive Video`
- `kern.wakereason`
- `AppleIPAppender::%s: ifnet_set_link_quality returned: %d\n`
- `AppleIPAppender only supports %u ifNet interfaces - provided %u\n`
- `setIONetworkInterfaceGated`
- `Attempt to disable mismatched IONetworkInterface - held %p  provided %p\n`
- `site.AppleIPAppenderAsyncParamBlock`
- `%s: ifnet_get_local_ports_extended() returns error code: 0x%x (%d)\n`
- `site.ifnet_keepalive_offload_frame`
- `Background System`

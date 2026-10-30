# `com.apple.driver.AppleEmbeddedAudioResourceManager`

- Name: AppleEmbeddedAudioResourceManager
- Version: `1010.2`
- UUID: `C5AAD1FB-BB4E-3921-916C-8350FFAF7003`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/audio-resource-manager`](../devicetree/root__arm-io__audio-resource-manager.md) | `AppleEmbeddedAudioResourceManager` | `audio,embedded-resource-manager` |

## IOKit personalities (1) [KC]

### AppleEmbeddedAudioResourceManager
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudioResourceManager`
- `IOClass`: `AppleEmbeddedAudioResourceManager`
- `IONameMatch`:
  - `audio,embedded-resource-manager`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEmbeddedAudioResourceManager`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEmbeddedAudioResourceManager` | 0xd0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002d24 off=0x00445e00-0x00448b24 addr=0xfffffe0007449e00-0xfffffe000744cb24 r--/r--   __TEXT            
	sz=0x00001ea0 off=0x00446478-0x00448318 addr=0xfffffe000744a478-0xfffffe000744c318               __TEXT.__const            
	sz=0x000003a3 off=0x00448318-0x004486bb addr=0xfffffe000744c318-0xfffffe000744c6bb               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000469 off=0x004486bb-0x00448b24 addr=0xfffffe000744c6bb-0xfffffe000744cb24               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002704 off=0x01c28660-0x01c2ad64 addr=0xfffffe0008c2c660-0xfffffe0008c2ed64 r-x/r-x   __TEXT_EXEC       
	sz=0x00002564 off=0x01c28660-0x01c2abc4 addr=0xfffffe0008c2c660-0xfffffe0008c2ebc4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x01c2abc4-0x01c2ad64 addr=0xfffffe0008c2ebc4-0xfffffe0008c2ed64          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0493eb08-0x0493ec08 addr=0xfffffe000b942b08-0xfffffe000b942c08 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493eb08-0x0493ebd0 addr=0xfffffe000b942b08-0xfffffe000b942bd0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b942bd0-0xfffffe000b942c08               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000810 off=0x0107c7e8-0x0107cff8 addr=0xfffffe00080807e8-0xfffffe0008080ff8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0107c7e8-0x0107c7f0 addr=0xfffffe00080807e8-0xfffffe00080807f0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0107c7f0-0x0107c7f8 addr=0xfffffe00080807f0-0xfffffe00080807f8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000006a0 off=0x0107c7f8-0x0107ce98 addr=0xfffffe00080807f8-0xfffffe0008080e98         __DATA_CONST.__const            
	sz=0x00000040 off=0x0107ce98-0x0107ced8 addr=0xfffffe0008080e98-0xfffffe0008080ed8         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x0107ced8-0x0107cfa8 addr=0xfffffe0008080ed8-0xfffffe0008080fa8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x0107cfa8-0x0107cff8 addr=0xfffffe0008080fa8-0xfffffe0008080ff8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 62 at 0x04ad8528
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C5AAD1FB-BB4E-3921-916C-8350FFAF7003
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9ee40 size=0x48
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEmbeddedAudioResourceManager`
- `CFBundleIdentifier`: `com.apple.driver.AppleEmbeddedAudioResourceManager`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEmbeddedAudioResourceManager`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudioResourceManager.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901318144`
- `_PrelinkExecutableRelativePath`: `AppleEmbeddedAudioResourceManager`
- `_PrelinkExecutableSize`: `23864`
- `_PrelinkExecutableSourceAddr`: `-2198901318144`
- `_PrelinkKmodInfo`: `-2198828995832`

## Strings (55) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s::%s(%p) resourceIDObject cannot be nullptr\n`
- `kci-name`
- `cs35l92-firmware-set`
- `site.AppleEmbeddedAudioResourceManager`
- `start`
- `%s: Error creating a notifier for AKCI '%s'.\n`
- `%s: Not all AKCIs registered for notification (%u, %u)\n`
- `%s: Failed to create AKCI '%s'\n`
- `_getKernelClientInterfaceGivenResource`
- `AppleEmbeddedAudioResourceManager`
- `%s::%s() super::start(..) failed.\n`
- `_resourceRoutingNotificationGated`
- `%s::%s could not find AKCI '%s' (in %s)\n`
- `%s::%s failed to send CS35L92 firmware assets: %u\n`
- `resource-gid-mapping`
- `cs35l92-firmware-kci-name`
- `12111112122212121211111112`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `%s: Error iterating ResourceID\n`
- `%s::%s could not getProperty('%s') in AKCI '%p'\n`
- `%s: Invalid firmware set specified: '%c%c%c%c'\n`
- `%s::%s(%p) resourceTypeObject cannot be nullptr\n`
- `0x%x_%c%c%c%c`
- `%s::%s(%s) failed.\n`
- `_sendCS35L92Firmware`
- `%s::%s failed to generate firmware write request: %u\n`

**[__TEXT.__os_log]**

- `Loading kCS35L92Watch7cFirmwareSet`
- `Loading kCS35L92Watch7eFirmwareSet`
- `%s: Error iterating ResourceID`
- `%s: Looking up service matching AKCI '%s'`
- `%s: Not all AKCIs registered for notification (%u, %u)`
- `%s::%s could not getProperty('%s') in AKCI '%p'`
- `%s::%s(%p) resourceTypeObject cannot be nullptr`
- `Loading kCS35L92Watch6aFirmwareSet`
- `Loading kCS35L92Watch7FirmwareSet`
- `Loading kCS35L92Watch7expFirmwareSet`
- `%s::%s failed to send CS35L92 firmware assets: %u`
- `Loading kCS35L92Watch6FirmwareSet`
- `Loading kCS35L92Watch6bsFirmwareSet`
- `Loading kCS35L92Watch7bFirmwareSet`
- `%s::%s(%s) failed.`
- `%s::%s(%p) resourceIDObject cannot be nullptr`
- `Loading kCS35L92Watch6dFirmwareSet`
- `%s: ByteOffset=%d, ResourceID=%s, AKCIName=%s`
- `%s::%s failed to generate firmware write request: %u`
- `%s::%s() super::start(..) failed.`
- `%s::%s could not find AKCI '%s' (in %s)`
- `Loading kCS35L92Watch6bbFirmwareSet`
- `%s: Error creating a notifier for AKCI '%s'.`
- `%s: Found AKCI for '%s'.`
- `%s: Failed to create AKCI '%s'`
- `Loading kCS35L92Watch6cFirmwareSet`
- `Loading kCS35L92Watch7dFirmwareSet`
- `%s: All (%u) AKCIs found; registering service.`
- `%s: Invalid firmware set specified: '%c%c%c%c'`

# `com.apple.AGXFirmwareKextG19PRTBuddy`

- Name: AGXFirmwareKextG19PRTBuddy
- Version: `1`
- UUID: `7E5CE8A7-0137-3314-B430-DA5AC5D7CD38`
- Source version: `362.5.0.0.0`
- Depends on: [`com.apple.AGXFirmwareKextRTBuddy64`](com.apple.AGXFirmwareKextRTBuddy64.md) 1.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### Firmware-Power
- `CFBundleIdentifier`: `com.apple.AGXFirmwareKextG19PRTBuddy`
- `IOClass`: `AGXFirmwareKextG18RTBuddy`
- `IOMatchCategory`: `AGXFirmwareKextG18RTBuddy`
- `IOPersonalityPublisher`: `com.apple.AGXFirmwareKextG19PRTBuddy`
- `IOPropertyMatch`:
  - `role`: `GFX1`
- `IOProviderClass`: `RTBuddyService`
- `role`: `GFX1`

### Firmware-Sched
- `CFBundleIdentifier`: `com.apple.AGXFirmwareKextG19PRTBuddy`
- `IOClass`: `AGXFirmwareKextG18RTBuddy`
- `IOMatchCategory`: `AGXFirmwareKextG18RTBuddy`
- `IOPersonalityPublisher`: `com.apple.AGXFirmwareKextG19PRTBuddy`
- `IOPropertyMatch`:
  - `role`: `GFX`
- `IOProviderClass`: `RTBuddyService`
- `role`: `GFX`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AGXFirmwareKextG18RTBuddy` | 0x198 | AGXFirmwareKextRTBuddy → IOService → IORegistryEntry |
| `AGXFirmwareKextRTBuddy` | 0x198 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000104a off=0x0011a140-0x0011b18a addr=0xfffffe000711e140-0xfffffe000711f18a r--/r--   __TEXT            
	sz=0x00000268 off=0x0011a7c0-0x0011aa28 addr=0xfffffe000711e7c0-0xfffffe000711ea28               __TEXT.__const            
	sz=0x00000762 off=0x0011aa28-0x0011b18a addr=0xfffffe000711ea28-0xfffffe000711f18a               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002df0 off=0x01526920-0x01529710 addr=0xfffffe000852a920-0xfffffe000852d710 r-x/r-x   __TEXT_EXEC       
	sz=0x00002c20 off=0x01526920-0x01529540 addr=0xfffffe000852a920-0xfffffe000852d540          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001d0 off=0x01529540-0x01529710 addr=0xfffffe000852d540-0xfffffe000852d710          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001b8 off=0x04924378-0x04924530 addr=0xfffffe000b928378-0xfffffe000b928530 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04924378-0x0492443c addr=0xfffffe000b928378-0xfffffe000b92843c               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b928440-0xfffffe000b928478               __DATA.__common           (Zerofill)
	sz=0x000000b8 off=0x00000000-0x000000b8 addr=0xfffffe000b928478-0xfffffe000b928530               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f28 off=0x00f694c8-0x00f6a3f0 addr=0xfffffe0007f6d4c8-0xfffffe0007f6e3f0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x00f694c8-0x00f694d8 addr=0xfffffe0007f6d4c8-0xfffffe0007f6d4d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x00f694d8-0x00f694e8 addr=0xfffffe0007f6d4d8-0xfffffe0007f6d4e8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000d50 off=0x00f694e8-0x00f6a238 addr=0xfffffe0007f6d4e8-0xfffffe0007f6e238         __DATA_CONST.__const            
	sz=0x00000080 off=0x00f6a238-0x00f6a2b8 addr=0xfffffe0007f6e238-0xfffffe0007f6e2b8         __DATA_CONST.__kalloc_type      
	sz=0x000000e8 off=0x00f6a2b8-0x00f6a3a0 addr=0xfffffe0007f6e2b8-0xfffffe0007f6e3a0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x00f6a3a0-0x00f6a3f0 addr=0xfffffe0007f6e3a0-0xfffffe0007f6e3f0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 68 at 0x04acf7b4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     7E5CE8A7-0137-3314-B430-DA5AC5D7CD38
008: LC_SOURCE_VERSION           362.5.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a94f68 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AGXFirmwareKextG19PRTBuddy`
- `CFBundleIdentifier`: `com.apple.AGXFirmwareKextG19PRTBuddy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AGXFirmwareKextG19PRTBuddy`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `362.5`
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
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AGXFirmwareKextG19PRTBuddy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904643264`
- `_PrelinkExecutableRelativePath`: `AGXFirmwareKextG19PRTBuddy`
- `_PrelinkExecutableSize`: `20250`
- `_PrelinkExecutableSourceAddr`: `-2198904643264`
- `_PrelinkKmodInfo`: `-2198829104264`

## Strings (39) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `void AGXFirmwareKextRTBuddy::powerStateChangeGated(unsigned long, unsigned long)`
- `AGXk: %s:%d:%s: !!! Invalid FW role\n`
- `getCLPCDynamicSplitRatioDictKey`
- `AGXk: %s:%d:%s: !!! Scheduler work queues disabled but command submission is still enabled\n`
- `AGXFirmwareKextG18RTBuddy`
- `AGXk: %s:%d:%s: !!! Unimplemented\n`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getBootConfigOffset(AGFIFirmwareRole)`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getFirmwareTextSectionBaseOffset(AGFIFirmwareRole)`
- `AGXFirmwareKextRTBuddy`
- `role`
- `AGXk: %s:%d:%s: !!! Error, trying to change power state with disabled fender power management!\n`
- `virtual const char *AGXFirmwareKextG18RTBuddy::getBuild(AGFIFirmwareRole)`
- `virtual uint64_t AGXFirmwareKextG18RTBuddy::getFirmwareTextSectionSize(AGFIFirmwareRole)`
- `AGXRTBuddyMessageWorkLoop`
- `virtual const char *AGXFirmwareKextG18RTBuddy::getVersion(AGFIFirmwareRole)`
- `AGXk: %s:%d:%s: !!! GFX firmware was not loaded by iBoot\n`
- `agxp_kext_rtbuddy.cpp`
- `virtual size_t AGXFirmwareKextG18RTBuddy::getRuntimeBinSize(AGFIFirmwareRole)`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getFWResumeFlagOffset(AGFIFirmwareRole)`
- `getFilteredGPUPowerToKernelClientFunction`
- `setCLPCDeadlineControlEffortKey`
- `setAGXGameModeKey`
- `121111121222121212222222222222222222211111111111121`
- `site.AGXFirmwareKextG18RTBuddy`
- `agxp_kext_g18_rtbuddy.cpp`
- `getCLPCStandbyCountKey`
- `getCLPCPerfCtrlTargetKey`
- `site.AGXFirmwareKextRTBuddy`
- `virtual bool AGXFirmwareKextRTBuddy::bootFirmware(IOMemoryMap *)`
- `virtual bool AGXFirmwareKextG18RTBuddy::requestFirmwareBinary(const uint8_t **, size_t *, const AGXGPUCoreConfig &, AGFIFirmwareRole)`
- `getCLPCStandbyDurationKey`
- `getCLPCPowerSamplePeriodKey`
- `coredump-copy-buffer`
- `Endpoint1`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getFWPdumpBinPatchDataOffset(AGFIFirmwareRole)`
- `setBudgetToAGXFunction`
- `Endpoint2`
- `i8@?0`
- `virtual IOReturn AGXFirmwareKextRTBuddy::powerStateChange(unsigned long, unsigned long)`

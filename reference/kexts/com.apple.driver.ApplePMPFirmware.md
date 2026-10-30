# `com.apple.driver.ApplePMPFirmware`

- Name: ApplePMPFirmware
- Version: `1`
- UUID: `3D69FDA5-2D88-3369-9417-DAA10A48206F`
- Source version: `1661.40.5.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 24.3.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### ApplePMP0Firmware
- `CFBundleIdentifier`: `com.apple.driver.ApplePMPFirmware`
- `IOClass`: `ApplePMPFirmware`
- `IOMatchCategory`: `RTBuddyFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMPFirmware`
- `IOPropertyMatch`:
  - `role`: `PMP0`
- `IOProviderClass`: `RTBuddy`

### ApplePMP1Firmware
- `CFBundleIdentifier`: `com.apple.driver.ApplePMPFirmware`
- `IOClass`: `ApplePMPFirmware`
- `IOMatchCategory`: `RTBuddyFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMPFirmware`
- `IOPropertyMatch`:
  - `role`: `PMP1`
- `IOProviderClass`: `RTBuddy`

### ApplePMPFirmware
- `CFBundleIdentifier`: `com.apple.driver.ApplePMPFirmware`
- `IOClass`: `ApplePMPFirmware`
- `IOMatchCategory`: `RTBuddyFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePMPFirmware`
- `IOPropertyMatch`:
  - `role`: `PMP`
- `IOProviderClass`: `RTBuddy`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePMPFirmware` | 0xf0 | RTBuddyFirmwareService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a06 off=0x0069c4e0-0x0069cee6 addr=0xfffffe00076a04e0-0xfffffe00076a0ee6 r--/r--   __TEXT            
	sz=0x0000042e off=0x0069cab8-0x0069cee6 addr=0xfffffe00076a0ab8-0xfffffe00076a0ee6               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001530 off=0x023697b0-0x0236ace0 addr=0xfffffe000936d7b0-0xfffffe000936ece0 r-x/r-x   __TEXT_EXEC       
	sz=0x00001420 off=0x023697b0-0x0236abd0 addr=0xfffffe000936d7b0-0xfffffe000936ebd0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000110 off=0x0236abd0-0x0236ace0 addr=0xfffffe000936ebd0-0xfffffe000936ece0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04983fa8-0x049840a8 addr=0xfffffe000b987fa8-0xfffffe000b9880a8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04983fa8-0x04984070 addr=0xfffffe000b987fa8-0xfffffe000b988070               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b988070-0xfffffe000b9880a8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000728 off=0x011969f8-0x01197120 addr=0xfffffe000819a9f8-0xfffffe000819b120 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011969f8-0x01196a00 addr=0xfffffe000819a9f8-0xfffffe000819aa00         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01196a00-0x01196a08 addr=0xfffffe000819aa00-0xfffffe000819aa08         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000618 off=0x01196a08-0x01197020 addr=0xfffffe000819aa08-0xfffffe000819b020         __DATA_CONST.__const            
	sz=0x00000040 off=0x01197020-0x01197060 addr=0xfffffe000819b020-0xfffffe000819b060         __DATA_CONST.__kalloc_type      
	sz=0x00000088 off=0x01197060-0x011970e8 addr=0xfffffe000819b060-0xfffffe000819b0e8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x011970e8-0x01197120 addr=0xfffffe000819b0e8-0xfffffe000819b120         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 41 at 0x04ae19a4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3D69FDA5-2D88-3369-9417-DAA10A48206F
008: LC_SOURCE_VERSION           1661.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004aac950 size=0x28
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePMPFirmware`
- `CFBundleIdentifier`: `com.apple.driver.ApplePMPFirmware`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePMPFirmware`
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
- `NSHumanReadableCopyright`: `Copyright © 2015 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePMPFirmware.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898866976`
- `_PrelinkExecutableRelativePath`: `ApplePMPFirmware`
- `_PrelinkExecutableSize`: `10078`
- `_PrelinkExecutableSourceAddr`: `-2198898866976`
- `_PrelinkKmodInfo`: `-2198828712024`

## Strings (62) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"ApplePMPFirmware: %s:%u REQUIRE failed: %s\" @%s:%d`
- `board-id`
- `IODeviceTree:/arm-io/pmgr`
- `pmp-dram-stats`
- `pmp-assert-energy`
- `121111121222121211111111122222`
- `pmc`
- `pmc-msg-disabled`
- `pmp-pm-device-counter-mask`
- `pmp-test`
- `pmp-pwrs-stats`
- `pmp-trace-capacity`
- `pmc-pmgr`
- `pmp-pm-device-sampling-mask`
- `pmp-dram-capacity`
- `_iopNub`
- `_armIODevice`
- `pmp-debug`
- `pmp-pmon`
- `pmp-pbatt`
- `pmp-msg-queue-panic`
- `pmp-dart`
- `pmp-bw-stats`
- `pmp-energy-breakdown`
- `site.ApplePMPFirmware`
- `%s`
- `dram-vendor-id`
- `dram-capacity`
- `pmp-power-gating`
- `pmp-trace`
- `pmc-max-bwr-latency-us`
- `data`
- `light-em-up`
- `pmp-fast-die`
- `pmp-acc-ovrd-wa`
- `pmp-bw-ctrl-wind-down`
- `ApplePMPFirmware`
- `_role`
- `pmp-dock-fifo`
- `pmp-clock-gating`
- `pmp-dram-energy`
- `tGraphClient`
- `RTBuddyPatchBay.h`
- `virtual bool ApplePMPFirmware::start(IOService *)`
- `ApplePMPFirmware.cpp`
- `dram-channel-disable`
- `pmp-ut-stats`
- `pmp-agx-stats`
- `pmp-soc-energy`
- `pmp-rt-events`
- `\"Variable write size (%ld) does not match patch variable size(%d)\" @%s:%d`
- `firmware-name`
- `pmp-sampler`
- `_slaveProcessor`
- `role`
- `soc-chip-variant`
- `pmp-dram-vendor-id`
- `pmc-customer`
- `pmp-pmu-telemetry`
- `IODeviceTree:/chosen`
- `Role`
- `pmp-disable-energy-panic`

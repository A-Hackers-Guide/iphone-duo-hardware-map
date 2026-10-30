# `com.apple.EXBrightCalibrationConsumer`

- Name: EXBrightCalibrationConsumer
- Version: `1.0.0`
- UUID: `53380225-40F9-3ADD-B118-69EB88CCEFF1`
- Source version: `2300.52.5.0.0`
- Depends on: [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `EXBrightCalibrationConsumer` | 0x50 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000e67 off=0x00919790-0x0091a5f7 addr=0xfffffe000791d790-0xfffffe000791e5f7 r--/r--   __TEXT            
	sz=0x00000060 off=0x00919db8-0x00919e18 addr=0xfffffe000791ddb8-0xfffffe000791de18               __TEXT.__const            
	sz=0x000007df off=0x00919e18-0x0091a5f7 addr=0xfffffe000791de18-0xfffffe000791e5f7               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000f64 off=0x02c38720-0x02c39684 addr=0xfffffe0009c3c720-0xfffffe0009c3d684 r-x/r-x   __TEXT_EXEC       
	sz=0x00000e64 off=0x02c38720-0x02c39584 addr=0xfffffe0009c3c720-0xfffffe0009c3d584          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x02c39584-0x02c39684 addr=0xfffffe0009c3d584-0xfffffe0009c3d684          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x049dbe40-0x049dbf40 addr=0xfffffe000b9dfe40-0xfffffe000b9dff40 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049dbe40-0x049dbf08 addr=0xfffffe000b9dfe40-0xfffffe000b9dff08               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9dff08-0xfffffe000b9dff40               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000230 off=0x012d75f8-0x012d7828 addr=0xfffffe00082db5f8-0xfffffe00082db828 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012d75f8-0x012d7600 addr=0xfffffe00082db5f8-0xfffffe00082db600         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012d7600-0x012d7608 addr=0xfffffe00082db600-0xfffffe00082db608         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000128 off=0x012d7608-0x012d7730 addr=0xfffffe00082db608-0xfffffe00082db730         __DATA_CONST.__const            
	sz=0x00000040 off=0x012d7730-0x012d7770 addr=0xfffffe00082db730-0xfffffe00082db770         __DATA_CONST.__kalloc_type      
	sz=0x00000080 off=0x012d7770-0x012d77f0 addr=0xfffffe00082db770-0xfffffe00082db7f0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x012d77f0-0x012d7828 addr=0xfffffe00082db7f0-0xfffffe00082db828         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 39 at 0x04aee7b4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     53380225-40F9-3ADD-B118-69EB88CCEFF1
008: LC_SOURCE_VERSION           2300.52.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9868 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `EXBrightCalibrationConsumer`
- `CFBundleGetInfoString`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.EXBrightCalibrationConsumer`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `EXBrightCalibrationConsumer`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91014`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91014`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2026 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/EXBrightCalibrationConsumer.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896257136`
- `_PrelinkExecutableRelativePath`: `EXBrightCalibrationConsumer`
- `_PrelinkExecutableSize`: `8443`
- `_PrelinkExecutableSourceAddr`: `-2198896257136`
- `_PrelinkKmodInfo`: `-2198828351936`

## Strings (37) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `EXBrightCalibrationConsumer`
- `EXBrightCalibrationSuccess`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] Status: alsPlacement=%u, alsOrientation=%u, _calibrationSucceeded=%d, _calibrationCompleted=%d. Good bye!\n`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s] newService == nullptr!\n`
- `site.EXBrightCalibrationConsumer`
- `/exbrightpil`
- `[EXBrightCalibrationConsumer] sizeof(als-cal-skip-placements) != sizeof(als-cal-skip-orientations)\n`
- `[EXBrightCalibrationConsumer] OSTypeAlloc failed!\n`
- `RegisterService`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s] Could not create any matching notifications!\n`
- `[EXBrightCalibrationConsumer] EXBright path will not be used on this device!\n`
- `[EXBrightCalibrationConsumer] Unexpected size of als-cal-skip-placements!\n`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s] The notifier already exists!\n`
- `findEXBrightKEXT`
- `EXBrightPILKext`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s] Could not create matching dictionaries!\n`
- `EXBrightALSCalibrationInterest`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] Sent calibration interest to EXBrightKEXT!\n`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] Failed to allocate _registrationLock!\n`
- `[EXBrightCalibrationConsumer] alsPlacement=%u alsOrientation=%u alsNewCalibrationPath=%u alsCalSkipPlacement=%u alsCalSkipOrientation=%u\n`
- `[EXBrightCalibrationConsumer] EXBright calibration path is disabled for alsPlacement=%u alsOrientation=%u!\n`
- `calibrationWasCompleted`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] Registering a companion driver.\n`
- `findEXBrightKEXTCallback`
- `als-new-calibration-path`
- `als-cal-skip-placements`
- `companionDriverIsReadyForRegistration`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s] EXBrightKEXT is already configured!\n`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] calibrationWasCompleted success=%d\n`
- `EXBrightKext`
- `als-cal-skip-orientations`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s] Lock is missing!\n`
- `EXBrightCalibration`
- `1212211112`
- `/exbright`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] Registration will be delayed.\n`
- `[EXBrightCalibrationConsumer] [ALS_%d_%d] [%s]\n`

# `com.apple.driver.AppleGameControllerPersonality`

- Name: AppleGameControllerPersonality
- Version: `14.1.2`
- UUID: `AB7789D2-B108-37F3-819C-F056428633C4`
- Source version: `14.1.2.0.0`
- Depends on: [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 22.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 12.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (24) [KC]

### Access Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `psaccess`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `3679`
- `VendorID`: `1356`

### DualSense Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `ps5`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `3302`
- `VendorID`: `1356`

### DualSense Edge Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `ps5`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `3570`
- `VendorID`: `1356`

### Extended MFi Controller Driver Service
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `5`
    - `DeviceUsagePage`: `1`
- `IOClass`: `AppleGCIOHIDEventDriverPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `10`
- `IOPropertyMatch`:
  - `GameControllerType`: `1`
- `IOProviderClass`: `IOHIDEventDriver`
- `IOProviderMergeProperties`:
  - `GameControllerCategory`: `mfi`
  - `GameControllerSupport`: `True`

### GC User Driver Service
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `10`
- `IOProviderClass`: `AppleGCHIDUserEventDriver`
- `IOProviderMergeProperties`:
  - `GameControllerSupport`: `True`
  - `HIDServiceSupport`: `True`

### Generic Controller Device
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `dynamic`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOParentMatch`:
  - `IOPropertyMatch`:
    - `GameControllerCategory`: `dynamic`
    - `GameControllerSupportedHIDDevice`: `True`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1301`
- `IOProviderClass`: `IOHIDInterface`

### Luna Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `luna`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `1049`
- `VendorID`: `369`

### Nintendo JoyCon Grip IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `switch`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8206`
- `VendorID`: `1406`

### Nintendo JoyCon L IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `switch`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8198`
- `VendorID`: `1406`

### Nintendo JoyCon R IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `switch`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8199`
- `VendorID`: `1406`

### Nintendo Switch N64 Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `switch`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8217`
- `VendorID`: `1406`

### Nintendo Switch Pro Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `switch`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8201`
- `VendorID`: `1406`

### Nintendo Switch SNES Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `switch`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `8215`
- `VendorID`: `1406`

### Playstation Dualshock Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `ps4`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `2508`
- `VendorID`: `1356`

### Standard MFi Controller Driver Service
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `5`
    - `DeviceUsagePage`: `1`
- `IOClass`: `AppleGCIOHIDEventDriverPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `10`
- `IOPropertyMatch`:
  - `GameControllerType`: `0`
- `IOProviderClass`: `IOHIDEventDriver`
- `IOProviderMergeProperties`:
  - `GameControllerCategory`: `mfi`
  - `GameControllerSupport`: `True`

### T1 DualShock 4 Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `ps4`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `1476`
- `VendorID`: `1356`

### Xbox 360 Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `654`
- `VendorID`: `1118`

### Xbox Adaptive Controller
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `2828`
  - `2849`
- `VendorID`: `1118`

### Xbox Elite V2 Controller
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `2818`
  - `2821`
  - `2850`
  - `2876`
- `VendorID`: `1118`

### Xbox Elite V2 USB IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `2816`
- `VendorID`: `1118`

### Xbox Series X Wired Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `2834`
- `VendorID`: `1118`

### Xbox Series X Wireless Controller
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `2835`
  - `2851`
  - `2895`
- `VendorID`: `1118`

### Xbox Wired Controller IOService
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `746`
- `VendorID`: `1118`

### Xbox Wireless Controller
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `GCIOMatchVirtual`: `True`
- `GameControllerCategory`: `xbox`
- `IOClass`: `AppleGCHIDUserEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGameControllerPersonality`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `736`
  - `765`
  - `2848`
- `VendorID`: `1118`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleGCHIDProviderPropertyMerger` | 0x88 | IOProviderPropertyMerger → IOService → IORegistryEntry |
| `AppleGCHIDUserEventDriver` | 0xd0 | IOHIDEventService → IOService → IORegistryEntry |
| `AppleGCIOHIDEventDriverPropertyMerger` | 0x88 | AppleGCHIDProviderPropertyMerger → IOProviderPropertyMerger → IOService → IORegistryEntry |
| `SteamControllerUserEventDriver` | 0xd8 | AppleGCHIDUserEventDriver → IOHIDEventService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000ad2 off=0x004748b0-0x00475382 addr=0xfffffe00074788b0-0xfffffe0007479382 r--/r--   __TEXT            
	sz=0x000002dc off=0x00474f28-0x00475204 addr=0xfffffe0007478f28-0xfffffe0007479204               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000017e off=0x00475204-0x00475382 addr=0xfffffe0007479204-0xfffffe0007479382               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000260c off=0x01d0a810-0x01d0ce1c addr=0xfffffe0008d0e810-0xfffffe0008d10e1c r-x/r-x   __TEXT_EXEC       
	sz=0x000024bc off=0x01d0a810-0x01d0cccc addr=0xfffffe0008d0e810-0xfffffe0008d10ccc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000150 off=0x01d0cccc-0x01d0ce1c addr=0xfffffe0008d10ccc-0xfffffe0008d10e1c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000190 off=0x04942538-0x049426c8 addr=0xfffffe000b946538-0xfffffe000b9466c8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04942538-0x04942600 addr=0xfffffe000b946538-0xfffffe000b946600               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b946600-0xfffffe000b9466b0               __DATA.__common           (Zerofill)
	sz=0x00000018 off=0x00000000-0x00000018 addr=0xfffffe000b9466b0-0xfffffe000b9466c8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001d88 off=0x010b28e0-0x010b4668 addr=0xfffffe00080b68e0-0xfffffe00080b8668 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x010b28e0-0x010b2900 addr=0xfffffe00080b68e0-0xfffffe00080b6900         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x010b2900-0x010b2920 addr=0xfffffe00080b6900-0xfffffe00080b6920         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001b20 off=0x010b2920-0x010b4440 addr=0xfffffe00080b6920-0xfffffe00080b8440         __DATA_CONST.__const            
	sz=0x00000100 off=0x010b4440-0x010b4540 addr=0xfffffe00080b8440-0xfffffe00080b8540         __DATA_CONST.__kalloc_type      
	sz=0x000000a8 off=0x010b4540-0x010b45e8 addr=0xfffffe00080b8540-0xfffffe00080b85e8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x010b45e8-0x010b4668 addr=0xfffffe00080b85e8-0xfffffe00080b8668         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 58 at 0x04ada560
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     AB7789D2-B108-37F3-819C-F056428633C4
008: LC_SOURCE_VERSION           14.1.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa0968 size=0x60
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleGameControllerPersonality`
- `CFBundleIdentifier`: `com.apple.driver.AppleGameControllerPersonality`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleGameControllerPersonality`
- `CFBundleNumericVersion`: `336756736`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `14.1.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleGameControllerPersonality.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901126992`
- `_PrelinkExecutableRelativePath`: `AppleGameControllerPersonality`
- `_PrelinkExecutableSize`: `20470`
- `_PrelinkExecutableSourceAddr`: `-2198901126992`
- `_PrelinkKmodInfo`: `-2198828980936`

## Strings (38) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOProviderMergePropertiesTargetClass`
- `SteamControllerUserEventDriver`
- `Built-In`
- `12111112122212121`
- `PrimaryUsagePage`
- `IOHID`
- `12111112122212121111111211`
- `GameControllerEligible`
- `RegisterService`
- `AppleGCHIDUserEventDriver`
- `site.AppleGCHIDUserEventDriver`
- `GCIOMatchVirtual`
- `IOUserClass`
- `IOProviderMergeProperties`
- `CFBundleIdentifier`
- `HIDVirtualDevice`
- `site.SteamControllerUserEventDriver`
- `com.apple.GameController`
- `AppleGCIOHIDEventDriverPropertyMerger`
- `site.AppleGCIOHIDEventDriverPropertyMerger`
- `GameControllerType`
- `GameControllerPointer`
- `site.AppleGCHIDProviderPropertyMerger`
- `IOCFPlugInTypes`
- `Kernel`
- `bInterfaceNumber`
- `AppleGCHIDProviderPropertyMerger`
- `GCSyntheticDevice`
- `Privileged`
- `121111121222121211111112112`
- `GameControllerCapabilities`
- `GameControllerSupport`

**[__TEXT.__os_log]**

- `AppleGCHIDUserEventDriver::probe(<IOHIDDevice %#010llx>)`
- `AppleGCHIDUserEventDriver::handleStart(<IOHIDInterface %#010llx>)`
- `SteamControllerUserEventDriver::handleStart(<IOHIDInterface %#010llx>)`
- `SteamControllerUserEventDriver connected; registering service`
- `SteamControllerUserEventDriver disconnected; terminating`
- `AppleGCIOHIDEventDriverPropertyMerger::probe(<IOHIDDevice %#010llx>)`

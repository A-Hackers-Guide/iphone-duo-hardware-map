# `com.apple.driver.AppleHIDTransportSCMCommon`

- Name: AppleHIDTransportSCMCommon
- Version: `1010.1`
- UUID: `8EB6BFFA-C023-30F0-BEFF-7708B411C9B8`
- Source version: `10110.1.0.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleHIDTransport`](com.apple.driver.AppleHIDTransport.md) 1.0, [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AHTRTBuddyFirmwareService` | 0xc8 | RTBuddyFirmwareService → IOService → IORegistryEntry |
| `AHTSCMMessage` | 0x30 |  |
| `AppleHIDTransportBootloaderRTBuddy` | 0x198 | AppleHIDTransportBootloader → AIDService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000ccf off=0x004e7fb0-0x004e8c7f addr=0xfffffe00074ebfb0-0xfffffe00074ecc7f r--/r--   __TEXT            
	sz=0x000006f7 off=0x004e8588-0x004e8c7f addr=0xfffffe00074ec588-0xfffffe00074ecc7f               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00004918 off=0x01f1d3b0-0x01f21cc8 addr=0xfffffe0008f213b0-0xfffffe0008f25cc8 r-x/r-x   __TEXT_EXEC       
	sz=0x00004778 off=0x01f1d3b0-0x01f21b28 addr=0xfffffe0008f213b0-0xfffffe0008f25b28          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x01f21b28-0x01f21cc8 addr=0xfffffe0008f25b28-0xfffffe0008f25cc8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04949fc0-0x0494a110 addr=0xfffffe000b94dfc0-0xfffffe000b94e110 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04949fc0-0x0494a088 addr=0xfffffe000b94dfc0-0xfffffe000b94e088               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b94e088-0xfffffe000b94e110               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001310 off=0x010e82a0-0x010e95b0 addr=0xfffffe00080ec2a0-0xfffffe00080ed5b0 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x010e82a0-0x010e82b8 addr=0xfffffe00080ec2a0-0xfffffe00080ec2b8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x010e82b8-0x010e82d0 addr=0xfffffe00080ec2b8-0xfffffe00080ec2d0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001028 off=0x010e82d0-0x010e92f8 addr=0xfffffe00080ec2d0-0xfffffe00080ed2f8         __DATA_CONST.__const            
	sz=0x00000140 off=0x010e92f8-0x010e9438 addr=0xfffffe00080ed2f8-0xfffffe00080ed438         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x010e9438-0x010e9508 addr=0xfffffe00080ed438-0xfffffe00080ed508         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a8 off=0x010e9508-0x010e95b0 addr=0xfffffe00080ed508-0xfffffe00080ed5b0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 73 at 0x04adbea8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8EB6BFFA-C023-30F0-BEFF-7708B411C9B8
008: LC_SOURCE_VERSION           10110.1.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa3b20 size=0xd8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleHIDTransportSCMCommon`
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDTransportSCMCommon`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleHIDTransportSCMCommon`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `"Copyright © 2016 Apple Inc. All rights reserved. [AppleInputDeviceSupport_kexts-10110.1]"`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleHIDTransport.kext/PlugIns/AppleHIDTransportSCMCommon.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900654160`
- `_PrelinkExecutableRelativePath`: `AppleHIDTransportSCMCommon`
- `_PrelinkExecutableSize`: `27207`
- `_PrelinkExecutableSourceAddr`: `-2198900654160`
- `_PrelinkKmodInfo`: `-2198828949568`

## Strings (68) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleHIDTransportBootloaderRTBuddy`
- `AHTRTBuddyFirmwareService`
- `AHTSCMMessage`
- `RTPM8ALL`
- `dapfParentPhandle`
- `matching`
- `[0x%llx][%llx][%s::%s]: Found image binary %s (%u bytes)`
- `[0x%llx][%llx][%s::%s]: ERROR!! Ignoring unknown image type '%s'`
- `[0x%llx][%llx][%s::%s]: %s = %s`
- `initWithData`
- `RTP`
- `iter`
- `ret == 0 `
- `init`
- `checkNewImage`
- `start`
- `pre-loaded`
- `121111121222121211111121111111111221121111111211112`
- `_slaveNub`
- `[0x%llx][%llx][%s::%s]: `
- `result == 0 `
- `payload`
- `site.AHTRTBuddyFirmwareService`
- `Role`
- `result`
- `service`
- `boolRet`
- `Run In Restore`
- `providerString`
- `_firmware`
- `site.Header`
- `AppleHIDTransportBootloaderRTBuddy`
- `waitForAppleDAPF`
- `[0x%llx][%llx][%s::%s]: Waiting for AppleDAPF...`
- `ret`
- `loadFirmware`
- `[0x%llx][%llx][%s::%s]: Nothing to do during restore`
- `!_booted`
- `configString`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/SCMCommon/AppleHIDTransportBootloaderRTBuddy.cpp`
- `handleStart`
- `site.AHTSCMMessage`
- `[0x%llx][%llx][%s::%s]: ERROR!! %s, %s file: %s, line: %d, value: 0x%08X`
- `no-firmware-service`
- `Version`
- `createFirmware`
- `hid-merge-personality`
- `type`
- `[0x%llx][%llx][%s::%s]: Loading image with options: 0x%08X`
- `[0x%llx][%llx][%s::%s]: Found firmware service for %s\n`
- `_device`
- `role`
- `Build`
- `[0x%llx][%llx][%s::%s]: Finished waiting for AppleDAPF`
- `description`
- `[0x%llx][%llx][%s::%s]: Skipping image loading since it was already loaded during pre-fdr update`
- `firmware`
- `AppleDAPF`
- `parentMatching`
- `dapf-parent`
- `phandleData`
- `1211111212221212111111111`
- `[0x%llx][%llx][%s::%s]: Firmware for %s\n`
- `121221`
- `_firmwareService`
- `/Library/Caches/com.apple.xbs/E73FC9D7-BE45-44E9-B88F-6699B0BA54E2/TemporaryDirectory.Q71yhO/Sources/AppleInputDeviceSupport_kexts/AppleHIDTransport/SCMCommon/AHTRTBuddyFirmwareService.cpp`
- `!payload`
- `handleLoadImage`

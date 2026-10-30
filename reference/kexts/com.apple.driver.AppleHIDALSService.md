# `com.apple.driver.AppleHIDALSService`

- Name: AppleHIDALSService
- Version: `1`
- UUID: `1E47DC65-9350-3B8E-A3DE-2B7D5178C5A8`
- Source version: `2300.52.5.0.0`
- Depends on: [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.iokit.IOUSBHostFamily`](com.apple.iokit.IOUSBHostFamily.md) 1.0.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 16.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 16.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### AppleHIDALS
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDALSService`
- `HIDServiceSupport`: `True`
- `IOCFPlugInTypes`:
  - `0516B563-B15B-11DA-96EB-0014519758EF`: `AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin`
- `IOClass`: `AppleUSBALSService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDALSService`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `65`
- `PrimaryUsagePage`: `32`
- `VendorID`: `1452`

### LG_HID_ALS
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDALSService`
- `HIDServiceSupport`: `True`
- `IOCFPlugInTypes`:
  - `0516B563-B15B-11DA-96EB-0014519758EF`: `AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin`
- `IOClass`: `AppleUSBALSService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDALSService`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `65`
- `PrimaryUsagePage`: `32`
- `ProductID`: `39523`
- `VendorID`: `1086`

### LG_HID_ALS_XXL
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDALSService`
- `HIDServiceSupport`: `True`
- `IOCFPlugInTypes`:
  - `0516B563-B15B-11DA-96EB-0014519758EF`: `AppleHIDALSService.kext/PlugIns/AppleHIDALS.plugin`
- `IOClass`: `AppleUSBALSService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleHIDALSService`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `65`
- `PrimaryUsagePage`: `32`
- `ProductID`: `39536`
- `VendorID`: `1086`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBALSService` | 0x98 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000079a off=0x004d1e00-0x004d259a addr=0xfffffe00074d5e00-0xfffffe00074d659a r--/r--   __TEXT            
	sz=0x000000cf off=0x004d2428-0x004d24f7 addr=0xfffffe00074d6428-0xfffffe00074d64f7               __TEXT.__cstring          (CstringLiterals)
	sz=0x000000a3 off=0x004d24f7-0x004d259a addr=0xfffffe00074d64f7-0xfffffe00074d659a               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00000a0c off=0x01e75410-0x01e75e1c addr=0xfffffe0008e79410-0xfffffe0008e79e1c r-x/r-x   __TEXT_EXEC       
	sz=0x0000094c off=0x01e75410-0x01e75d5c addr=0xfffffe0008e79410-0xfffffe0008e79d5c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000c0 off=0x01e75d5c-0x01e75e1c addr=0xfffffe0008e79d5c-0xfffffe0008e79e1c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000108 off=0x04949138-0x04949240 addr=0xfffffe000b94d138-0xfffffe000b94d240 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04949138-0x04949200 addr=0xfffffe000b94d138-0xfffffe000b94d200               __DATA.__data             
	sz=0x00000040 off=0x00000000-0x00000040 addr=0xfffffe000b94d200-0xfffffe000b94d240               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006d0 off=0x010d8ed8-0x010d95a8 addr=0xfffffe00080dced8-0xfffffe00080dd5a8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x010d8ed8-0x010d8ee0 addr=0xfffffe00080dced8-0xfffffe00080dcee0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010d8ee0-0x010d8ee8 addr=0xfffffe00080dcee0-0xfffffe00080dcee8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x010d8ee8-0x010d94d8 addr=0xfffffe00080dcee8-0xfffffe00080dd4d8         __DATA_CONST.__const            
	sz=0x00000040 off=0x010d94d8-0x010d9518 addr=0xfffffe00080dd4d8-0xfffffe00080dd518         __DATA_CONST.__kalloc_type      
	sz=0x00000060 off=0x010d9518-0x010d9578 addr=0xfffffe00080dd518-0xfffffe00080dd578         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x010d9578-0x010d95a8 addr=0xfffffe00080dd578-0xfffffe00080dd5a8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 30 at 0x04adb2d0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1E47DC65-9350-3B8E-A3DE-2B7D5178C5A8
008: LC_SOURCE_VERSION           2300.52.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa2860 size=0x28
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleHIDALSService`
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDALSService`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleHIDALSService`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91014`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91014`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleHIDALSService.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900744704`
- `_PrelinkExecutableRelativePath`: `AppleHIDALSService`
- `_PrelinkExecutableSize`: `6526`
- `_PrelinkExecutableSourceAddr`: `-2198900744704`
- `_PrelinkKmodInfo`: `-2198828953288`

## Strings (18) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1211111212221212111`
- `com.apple.CoreBrightness.AppleUSBALSService`
- `VendorID`
- `ProductID`
- `start`
- `als-lgp-version`
- `com.apple.CoreBrightness`
- `AppleUSBALSService`
- `site.AppleUSBALSService`
- `DeviceUsagePairs`
- `Elements`
- `default`

**[__TEXT.__os_log]**

- `%s::%s(%s@%p) Success`
- `invalid input`
- `publish LGP key (%{public}@)`
- `Failed to create CoreBrightness default log`
- `failed to create log handle`
- `AppleUSBALSService::start`

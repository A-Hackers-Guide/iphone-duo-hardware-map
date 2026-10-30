# `com.apple.driver.AppleSPUSphere`

- Name: AppleSPUSphere
- Version: `1`
- UUID: `4590C8F7-CE10-35D5-BBE6-1FF0A01B2AC8`
- Source version: `1087.40.4.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleSPUSphereDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleSPUSphere`
- `IOClass`: `AppleSPUSphereDriver`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleSPUSphereDriver`
- `IONameMatch`:
  - `AOP_spherecontrol`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPUSphere`
- `IOProviderClass`: `AppleSPUAppInterface`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSPUSphereDriver` | 0x270 | IOService → IORegistryEntry |
| `AppleSPUSphereFunction` | 0x38 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b13 off=0x0077e9c0-0x0077f4d3 addr=0xfffffe00077829c0-0xfffffe00077834d3 r--/r--   __TEXT            
	sz=0x00000338 off=0x0077efe8-0x0077f320 addr=0xfffffe0007782fe8-0xfffffe0007783320               __TEXT.__cstring          (CstringLiterals)
	sz=0x000001b3 off=0x0077f320-0x0077f4d3 addr=0xfffffe0007783320-0xfffffe00077834d3               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00001d14 off=0x0271ba10-0x0271d724 addr=0xfffffe000971fa10-0xfffffe0009721724 r-x/r-x   __TEXT_EXEC       
	sz=0x00001b14 off=0x0271ba10-0x0271d524 addr=0xfffffe000971fa10-0xfffffe0009721524          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000200 off=0x0271d524-0x0271d724 addr=0xfffffe0009721524-0xfffffe0009721724          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001e8 off=0x04999f08-0x0499a0f0 addr=0xfffffe000b99df08-0xfffffe000b99e0f0 rw-/rw-   __DATA            
	sz=0x00000188 off=0x04999f08-0x0499a090 addr=0xfffffe000b99df08-0xfffffe000b99e090               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b99e090-0xfffffe000b99e0f0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000968 off=0x01224880-0x012251e8 addr=0xfffffe0008228880-0xfffffe00082291e8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01224880-0x01224888 addr=0xfffffe0008228880-0xfffffe0008228888         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01224888-0x01224890 addr=0xfffffe0008228888-0xfffffe0008228890         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000780 off=0x01224890-0x01225010 addr=0xfffffe0008228890-0xfffffe0008229010         __DATA_CONST.__const            
	sz=0x00000080 off=0x01225010-0x01225090 addr=0xfffffe0008229010-0xfffffe0008229090         __DATA_CONST.__kalloc_type      
	sz=0x00000100 off=0x01225090-0x01225190 addr=0xfffffe0008229090-0xfffffe0008229190         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x01225190-0x012251e8 addr=0xfffffe0008229190-0xfffffe00082291e8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 75 at 0x04ae6960
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4590C8F7-CE10-35D5-BBE6-1FF0A01B2AC8
008: LC_SOURCE_VERSION           1087.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab2bf8 size=0x50
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSPUSphere`
- `CFBundleIdentifier`: `com.apple.driver.AppleSPUSphere`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSPUSphere`
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
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSPUSphere.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897940032`
- `_PrelinkExecutableRelativePath`: `AppleSPUSphere`
- `_PrelinkExecutableSize`: `13175`
- `_PrelinkExecutableSourceAddr`: `-2198897940032`
- `_PrelinkKmodInfo`: `-2198828622072`

## Strings (36) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `motion_full_rate: num_samples: %d latency: %d - %d\n\n`
- `motion_full_rate: session_samples: %d\n`
- `AppleSPUSphereDriver setEnable(%d) for %s\n`
- `pearl: num_samples: %d latency: %d - %d\n`
- `motion_full_rate: session start ts: %llu, session end ts: %llu\n`
- `motion_full_rate: session_latency_violations: %d\n`
- `motion_full_rate: num_samples: %d sample interval: %d - %d\n`
- `motion: num_samples: %d latency: %d - %d\n`
- `control: num_samples: %d latency: %d - %d\n`

**[__TEXT.__cstring]**

- `motion_1`
- `role`
- `RTBuddyService`
- `AppleSPUSphereDriver:setData[0x%x] isp-ext-swgen-reg_rx, int_num=0x%x \n`
- `AppleSPUSphereFunction`
- `AOP`
- `AppleSPUSphereDriver:setData[0x%x] kSpuPropertySphereEndpointConfiguration -> 0x%x\n`
- `kSphereEndpointControl`
- `kSphereEndpointMotionFullRate`
- `kSphereEndpointCount`
- `UnkownSphereEndpoint`
- `1211112`
- `AppleSPUSphereDriver`
- `control`
- `aop-isp-endpoint-cfg`
- `AppleSPUSphereDriver:setData[0x%x] aop-isp-buffer, address=0x%llx, size=0x%x\n`
- `kSphereEndpointPearl`
- `site.AppleSPUSphereDriver`
- `motion`
- `pearl`
- `isp-aop-%s-config`
- `AppleSPUSphereDriver:setData[0x%x] isp-aop-buffer, address=0x%llx, size=0x%x\n`
- `kSphereEndpointMotion`
- `site.AppleSPUSphereFunction`
- `AppleSPUSphereDriver:setData[0x%x] isp-ext-swgen-reg, reg=0x%llx, value=0x%x\n`
- `121111121222121211112222221222212222212222122222122221222221222212222212222111`
- `motion_full_rate`

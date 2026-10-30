# `com.apple.driver.AOPTouchKext`

- Name: AOPTouchKext
- Version: `314`
- UUID: `A4FB9EBC-237A-30A9-A84E-EC5354E97979`
- Source version: `314.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSPU`](com.apple.driver.AppleSPU.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### Event Service
- `AOPSupportsAggregateDictionary`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AOPTouchKext`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `1`
    - `DeviceUsagePage`: `13`
- `IOClass`: `AOPTouchHIDDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AOPTouchKext`
- `IOProviderClass`: `IOHIDInterface`
- `Manufacturer`: `Apple`
- `Transport`: `SPU`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AOPTouchHIDDriver` | 0x290 | AppleSPUHIDDriver → AppleEmbeddedHIDEventService → IOHIDEventService → IOService → IORegistryEntry |
| `AOPTouchHIDDriverChargingState` | 0x68 | AOPTouchHIDDriverDataSource → IOEventSource |
| `AOPTouchHIDDriverDataSource` | 0x58 | IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000950 off=0x00141120-0x00141a70 addr=0xfffffe0007145120-0xfffffe0007145a70 r--/r--   __TEXT            
	sz=0x00000040 off=0x00141798-0x001417d8 addr=0xfffffe0007145798-0xfffffe00071457d8               __TEXT.__const            
	sz=0x0000016b off=0x001417d8-0x00141943 addr=0xfffffe00071457d8-0xfffffe0007145943               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000012d off=0x00141943-0x00141a70 addr=0xfffffe0007145943-0xfffffe0007145a70               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002638 off=0x0160b630-0x0160dc68 addr=0xfffffe000860f630-0xfffffe0008611c68 r-x/r-x   __TEXT_EXEC       
	sz=0x00002478 off=0x0160b630-0x0160daa8 addr=0xfffffe000860f630-0xfffffe0008611aa8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001c0 off=0x0160daa8-0x0160dc68 addr=0xfffffe0008611aa8-0xfffffe0008611c68          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x0492dbe0-0x0492dd30 addr=0xfffffe000b931be0-0xfffffe000b931d30 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0492dbe0-0x0492dca8 addr=0xfffffe000b931be0-0xfffffe000b931ca8               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b931ca8-0xfffffe000b931d30               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e28 off=0x00f8b2d8-0x00f8c100 addr=0xfffffe0007f8f2d8-0xfffffe0007f90100 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x00f8b2d8-0x00f8b2e8 addr=0xfffffe0007f8f2d8-0xfffffe0007f8f2e8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x00f8b2e8-0x00f8b2f8 addr=0xfffffe0007f8f2e8-0xfffffe0007f8f2f8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000bf0 off=0x00f8b2f8-0x00f8bee8 addr=0xfffffe0007f8f2f8-0xfffffe0007f8fee8         __DATA_CONST.__const            
	sz=0x000000c0 off=0x00f8bee8-0x00f8bfa8 addr=0xfffffe0007f8fee8-0xfffffe0007f8ffa8         __DATA_CONST.__kalloc_type      
	sz=0x000000e0 off=0x00f8bfa8-0x00f8c088 addr=0xfffffe0007f8ffa8-0xfffffe0007f90088         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000078 off=0x00f8c088-0x00f8c100 addr=0xfffffe0007f90088-0xfffffe0007f90100         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 71 at 0x04ad0a74
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A4FB9EBC-237A-30A9-A84E-EC5354E97979
008: LC_SOURCE_VERSION           314.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a96308 size=0x78
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AOPTouchKext`
- `CFBundleIdentifier`: `com.apple.driver.AOPTouchKext`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AOPTouchKext`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `314`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `314`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AOPTouchKext.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904483552`
- `_PrelinkExecutableRelativePath`: `AOPTouchKext`
- `_PrelinkExecutableSize`: `16128`
- `_PrelinkExecutableSourceAddr`: `-2198904483552`
- `_PrelinkKmodInfo`: `-2198829065248`

## Strings (25) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `flags`
- `AOPTouchHIDDriverChargingState`
- `1211121112111`
- `AOPTouchHIDDriverDataSource`
- `site.AOPTouchHIDDriverDataSource`
- `IOPMPowerSource`
- `AdapterDetails`
- `AOPTouchHIDDriver`
- `AuthPassed`
- `site.AOPTouchHIDDriverChargingState`
- `function-ping`
- `AppleAuthCP`
- `12111211121`
- `FamilyCode`
- `site.AOPTouchHIDDriver`
- `1211111212221212111111121111111222222121121122222222222111211112111121211111111112`

**[__TEXT.__os_log]**

- `Dispatching tap event`
- `Couldn't allocate thread call!`
- `Couldn't get flags property!`
- `Polled authenticity state: %u`
- `Dispatching pencil tap event`
- `Couldn't cast flagsObj!`
- `Found touch instance of AppleAuthCPRelay`
- `Received callback for authenticity state: %u`
- `Duplicate authenticity state determined, ignoring`

# `com.apple.driver.AppleS5L8920XPWM`

- Name: AppleS5L8920XPWM
- Version: `1.0.0d1`
- UUID: `D4854844-8884-334D-B5CA-CC6D6B2B296C`
- Source version: `371.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/fpwm`](../devicetree/root__arm-io__fpwm.md) | `AppleS5L8920XFPWM` | `fpwm,s5l8920x` |

## IOKit personalities (2) [KC]

### AppleS5L8920XFPWM
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8920XPWM`
- `IOClass`: `AppleS5L8920XFPWM`
- `IONameMatch`: `fpwm,s5l8920x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleS5L8920XPWM`
- `IOProviderClass`: `AppleARMIODevice`

### AppleS5L8920XPWM
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8920XPWM`
- `IOClass`: `AppleS5L8920XPWM`
- `IONameMatch`: `pwm,s5l8920x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleS5L8920XPWM`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleS5L8920XFPWM` | 0xf8 | AppleARMPWM → IOService → IORegistryEntry |
| `AppleS5L8920XPWM` | 0x100 | AppleARMPWM → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000b45 off=0x006d1e30-0x006d2975 addr=0xfffffe00076d5e30-0xfffffe00076d6975 r--/r--   __TEXT            
	sz=0x00000418 off=0x006d2458-0x006d2870 addr=0xfffffe00076d6458-0xfffffe00076d6870               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000105 off=0x006d2870-0x006d2975 addr=0xfffffe00076d6870-0xfffffe00076d6975               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000335c off=0x02475c50-0x02478fac addr=0xfffffe0009479c50-0xfffffe000947cfac r-x/r-x   __TEXT_EXEC       
	sz=0x0000317c off=0x02475c50-0x02478dcc addr=0xfffffe0009479c50-0xfffffe000947cdcc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001e0 off=0x02478dcc-0x02478fac addr=0xfffffe000947cdcc-0xfffffe000947cfac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001e8 off=0x0498fbb8-0x0498fda0 addr=0xfffffe000b993bb8-0xfffffe000b993da0 rw-/rw-   __DATA            
	sz=0x00000188 off=0x0498fbb8-0x0498fd40 addr=0xfffffe000b993bb8-0xfffffe000b993d40               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b993d40-0xfffffe000b993da0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000ec8 off=0x011c0248-0x011c1110 addr=0xfffffe00081c4248-0xfffffe00081c5110 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x011c0248-0x011c0258 addr=0xfffffe00081c4248-0xfffffe00081c4258         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x011c0258-0x011c0268 addr=0xfffffe00081c4258-0xfffffe00081c4268         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cf0 off=0x011c0268-0x011c0f58 addr=0xfffffe00081c4268-0xfffffe00081c4f58         __DATA_CONST.__const            
	sz=0x00000080 off=0x011c0f58-0x011c0fd8 addr=0xfffffe00081c4f58-0xfffffe00081c4fd8         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x011c0fd8-0x011c10c8 addr=0xfffffe00081c4fd8-0xfffffe00081c50c8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x011c10c8-0x011c1110 addr=0xfffffe00081c50c8-0xfffffe00081c5110         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 69 at 0x04ae3394
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     D4854844-8884-334D-B5CA-CC6D6B2B296C
008: LC_SOURCE_VERSION           371.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaeb28 size=0x70
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleS5L8920XPWM`
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8920XPWM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleS5L8920XPWM`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleS5L8920XPWM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898647504`
- `_PrelinkExecutableRelativePath`: `AppleS5L8920XPWM`
- `_PrelinkExecutableSize`: `20305`
- `_PrelinkExecutableSourceAddr`: `-2198898647504`
- `_PrelinkKmodInfo`: `-2198828663880`

## Strings (46) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s-debug`
- `getPWMCaptureTimestamp`
- `\"ApplePWM: %s:%u \" \"AppleS5L8920XPWM: Failed to send droop event message\" @%s:%d`
- `stopPWMInputPulseSampler`
- `12111112122212121211122111111112`
- `stopPWMOutputPulseGenerator`
- `AppleS5L8920XFPWM`
- `com.apple.driver.AppleS5L8920XFPWM`
- `AppleS5L8920XPWM::start: _pwmBaseAddress: %#lx\n`
- `stopPWM`
- `AppleS5L8920XPWM.cpp`
- `site.AppleS5L8920XFPWM`
- `site.AppleS5L8920XPWM`
- `%s::%s: (%u, %llu, %llu, %d)\n`
- `startPWMCapture`
- `stopPWMCapture`
- `%s::%s: count=%u, now=%llu, timestamp=%llu\n`
- `%s::%s: Missing configuration\n`
- `NULL`
- `startPWMInputPulseSampler`
- `nclk`
- `droop-event-function`
- `void AppleS5L8920XPWM::_pulseInterruptOccurred(IOInterruptEventSource *, int)`
- `%s::%s: Interrupt event source has not been created\n`
- `startPWMOutputPulseGenerator`
- `1211111212221212112111221111122`
- `default`
- `\"stopPWM: invalid non-zero fpwm index\" @%s:%d`
- `AppleS5L8920XPWM`
- `service-gates`
- `%s::%s: (%u)\n`
- `%s::%s: (%u, %#x)\n`
- `initPWMInputPulseSampler`
- `startPWM`
- `FPWM Frequency`
- `setPowerState`
- `\"startPWM: invalid non-zero fpwm index\" @%s:%d`
- `AppleS5L8920XFPWM.cpp`
- `%s::%s: Received new power state: %lu\n`

**[__TEXT.__os_log]**

- `Unable to create log handle for AppleS5L8920XFPWM`
- `_pwmBaseAddress: %#lx\n`
- `Received new power state: %lu`
- `(%u, %llu, %llu, %d)`
- `(%u)`
- `Missing configuration`
- `Interrupt event source has not been created`

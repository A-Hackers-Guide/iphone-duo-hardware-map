# `com.apple.driver.AppleSGPIO`

- Name: AppleSGPIO
- Version: `1.0.1`
- UUID: `3C4C7F00-3FBF-37BC-8F9E-9ACB450E668D`
- Source version: `143.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSPMIPMU`](com.apple.driver.AppleSPMIPMU.md) 1.0.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md) | `AppleSGPIOHostBridgeController` | `sgpio-bridge` |

## IOKit personalities (1) [KC]

### AppleSGPIOHostBridgeController
- `CFBundleIdentifier`: `com.apple.driver.AppleSGPIO`
- `IOClass`: `AppleSGPIOHostBridgeController`
- `IONameMatch`: `sgpio-bridge`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSGPIO`
- `IOProviderClass`: `AppleDialogSPMIPMUNub`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSGPIOHostBridgeController` | 0xb0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000008b4 off=0x0075acf0-0x0075b5a4 addr=0xfffffe000775ecf0-0xfffffe000775f5a4 r--/r--   __TEXT            
	sz=0x000002dc off=0x0075b2c8-0x0075b5a4 addr=0xfffffe000775f2c8-0xfffffe000775f5a4               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001064 off=0x0265ec80-0x0265fce4 addr=0xfffffe0009662c80-0xfffffe0009663ce4 r-x/r-x   __TEXT_EXEC       
	sz=0x00000f54 off=0x0265ec80-0x0265fbd4 addr=0xfffffe0009662c80-0xfffffe0009663bd4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000110 off=0x0265fbd4-0x0265fce4 addr=0xfffffe0009663bd4-0xfffffe0009663ce4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04997058-0x04997158 addr=0xfffffe000b99b058-0xfffffe000b99b158 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04997058-0x0499711c addr=0xfffffe000b99b058-0xfffffe000b99b11c               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b99b120-0xfffffe000b99b158               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000758 off=0x011f6bd0-0x011f7328 addr=0xfffffe00081fabd0-0xfffffe00081fb328 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011f6bd0-0x011f6bd8 addr=0xfffffe00081fabd0-0xfffffe00081fabd8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x011f6bd8-0x011f6be0 addr=0xfffffe00081fabd8-0xfffffe00081fabe0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000658 off=0x011f6be0-0x011f7238 addr=0xfffffe00081fabe0-0xfffffe00081fb238         __DATA_CONST.__const            
	sz=0x00000040 off=0x011f7238-0x011f7278 addr=0xfffffe00081fb238-0xfffffe00081fb278         __DATA_CONST.__kalloc_type      
	sz=0x00000088 off=0x011f7278-0x011f7300 addr=0xfffffe00081fb278-0xfffffe00081fb300         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x011f7300-0x011f7328 addr=0xfffffe00081fb300-0xfffffe00081fb328         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 39 at 0x04ae4f34
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3C4C7F00-3FBF-37BC-8F9E-9ACB450E668D
008: LC_SOURCE_VERSION           143.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab13a8 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSGPIO`
- `CFBundleIdentifier`: `com.apple.driver.AppleSGPIO`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSGPIO`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSGPIO.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898086672`
- `_PrelinkExecutableRelativePath`: `AppleSGPIO`
- `_PrelinkExecutableSize`: `8560`
- `_PrelinkExecutableSourceAddr`: `-2198898086672`
- `_PrelinkKmodInfo`: `-2198828634024`

## Strings (23) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `checkStatus`
- `AppleSGPIOHostBridgeController`
- `site.AppleSGPIOHostBridgeController`
- `no provider name\n`
- `[%s]:%s:%d:[error] sgpio-bus-id\n`
- `[%s]:%s:%d: command = %u, follower = %u, address = 0x%02x, length = %llu\n`
- `writeRegs`
- `1211111212221212111212`
- `super::start(provider)=false\n`
- `%s.livelog`
- `[%s]:%s:%d:[error] provider`
- `start`
- `[%s]:%s:%d:[error] bridge-offset\n`
- `[%s]:%s:%d:[error] %s (0x%x, %llu) returned error 0x%x\n`
- `[%s]:%s:%d:[error] checkStatus returned error 0x%x\n`
- `bridge-offset`
- `sgpio-bus-id`
- `sendCommand`
- `[%s]:%s:%d:[error] writeRegs (0x%x, %zu) returned error 0x%x\n`
- `readRegs`
- `[%s]:%s:%d:[error] readRegs (0x%x, %zu) returned error 0x%x\n`
- `[%s]:%s:%d: bridge_offset = 0x%x, sgpio_bus_id = %d\n`
- `[%s]:%s:%d:[error] getSPMIConfig() returned error %d\n`

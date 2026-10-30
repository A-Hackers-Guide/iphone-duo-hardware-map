# `com.apple.driver.AppleS5L8940XI2C`

- Name: AppleS5L8940XI2C
- Version: `1.0.0d2`
- UUID: `8E0EE5C5-A2B7-32B9-B5C4-919AEF0A6520`
- Source version: `224.40.1.0.1`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleGPIOICController`](com.apple.driver.AppleGPIOICController.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (3) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) | `AppleS5L8940XI2CController` | `i2c,s5l8940x` |
| [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) | `AppleS5L8940XI2CController` | `i2c,s5l8940x` |
| [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) | `AppleS5L8940XI2CController` | `i2c,s5l8940x` |

## IOKit personalities (1) [KC]

### AppleS5L8940XI2CController
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8940XI2C`
- `IOClass`: `AppleS5L8940XI2CController`
- `IONameMatch`: `i2c,s5l8940x`
- `IOPersonalityPublisher`: `com.apple.driver.AppleS5L8940XI2C`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleS5L8940XI2CController` | 0x1e0 | AppleARMIICController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000f5a off=0x006d2980-0x006d38da addr=0xfffffe00076d6980-0xfffffe00076d78da r--/r--   __TEXT            
	sz=0x00000832 off=0x006d2ff8-0x006d382a addr=0xfffffe00076d6ff8-0xfffffe00076d782a               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000018 off=0x006d382c-0x006d3844 addr=0xfffffe00076d782c-0xfffffe00076d7844               __TEXT.__const            
	sz=0x00000096 off=0x006d3844-0x006d38da addr=0xfffffe00076d7844-0xfffffe00076d78da               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00003014 off=0x02478fb0-0x0247bfc4 addr=0xfffffe000947cfb0-0xfffffe000947ffc4 r-x/r-x   __TEXT_EXEC       
	sz=0x00002df4 off=0x02478fb0-0x0247bda4 addr=0xfffffe000947cfb0-0xfffffe000947fda4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000220 off=0x0247bda4-0x0247bfc4 addr=0xfffffe000947fda4-0xfffffe000947ffc4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0498fda0-0x0498fea0 addr=0xfffffe000b993da0-0xfffffe000b993ea0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0498fda0-0x0498fe68 addr=0xfffffe000b993da0-0xfffffe000b993e68               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b993e68-0xfffffe000b993ea0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000800 off=0x011c1110-0x011c1910 addr=0xfffffe00081c5110-0xfffffe00081c5910 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x011c1110-0x011c1118 addr=0xfffffe00081c5110-0xfffffe00081c5118         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x011c1118-0x011c1120 addr=0xfffffe00081c5118-0xfffffe00081c5120         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000650 off=0x011c1120-0x011c1770 addr=0xfffffe00081c5120-0xfffffe00081c5770         __DATA_CONST.__const            
	sz=0x00000040 off=0x011c1770-0x011c17b0 addr=0xfffffe00081c5770-0xfffffe00081c57b0         __DATA_CONST.__kalloc_type      
	sz=0x00000110 off=0x011c17b0-0x011c18c0 addr=0xfffffe00081c57b0-0xfffffe00081c58c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x011c18c0-0x011c1910 addr=0xfffffe00081c58c0-0xfffffe00081c5910         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 78 at 0x04ae34a8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8E0EE5C5-A2B7-32B9-B5C4-919AEF0A6520
008: LC_SOURCE_VERSION           224.40.1.0.1
009: LC_FUNCTION_STARTS          offset=0x004aaeb98 size=0x50
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleS5L8940XI2C`
- `CFBundleIdentifier`: `com.apple.driver.AppleS5L8940XI2C`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleS5L8940XI2C`
- `CFBundleNumericVersion`: `16785410`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleS5L8940XI2C.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898644608`
- `_PrelinkExecutableRelativePath`: `AppleS5L8940XI2C`
- `_PrelinkExecutableSize`: `18542`
- `_PrelinkExecutableSourceAddr`: `-2198898644608`
- `_PrelinkKmodInfo`: `-2198828663392`

## Strings (65) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleS5L8940XI2CController`
- `AppleS5L8940XI2CController::start: %s required function device_reset not found\n`
- `gpio-iic_scl`
- `%s.always-on`
- `skipping malformed tunable, size 0x%x @ (%d/%d)\n`
- `read`
- `Bus is still in a bad state`
- `RxFIFO doesn't have enough bytes`
- `121111121222121211222112111122111112111222222222212212211121`
- `AppleS5L8940XI2CController[%s]: Failed to start controller, filter tunable was malformed in the registry`
- `.delay`
- `timeout waiting for XIP to clear`
- `Time out waiting for _runPolledMode`
- `service-gates`
- `unknown`
- `tbuf-tunable`
- `AppleGPIOICController`
- `_checkInterrupts`
- `AppleS5L8940XI2CController`
- `AppleS5L8940XI2CController[%s]: Failed to start controller, tbuf tunable was malformed in the registry`
- `AppleS5L8940XI2CController::_runInterruptMode timeout waiting for interrupt\n`
- `write`
- `AppleS5L8940XI2C.cpp`
- `%s::%s %s; last %s status %08x int shadow %08x xfer %08x fifo %08x for device %s`
- `IOPlatformHaltRestartAction`
- `filter-tunable`
- `%s.delay`
- `AppleS5L8940XI2CController::start: %s this: %p _i2cBaseAddress: %#lx, external-bus=%d, use-table-div=%d, alwayson=%d, usePSD=%d, powerOffDelay=%u\n`
- `Attempted to execute IIC command on workloop thread`
- `_runPolledModeProcessing`
- `AppleS5L8940XI2CController::_unjamBus Bus unjam unsuccessful, SMSTA: %08x\n`
- `\"%s::%s %s; last %s status %08x int shadow %08x xfer %08x fifo %08x for device %s\" @%s:%d`
- `trigger-level-tunable`
- `external-bus`
- `_drainRxFifo`
- `use-table-div`
- `function-device_reset`
- `idle-off-delay-us`
- `%s-debug`
- `all-i2c.always-on`
- `%s always-on\n`
- `Unkown`
- `executeIICCommand`
- `AppleS5L8940XI2CController[%s]: Malformed %s property: Expecting 2x32-bit mask tunable`
- `iic-tunables`
- `AppleS5L8940XI2CController[%s]: Failed to start controller, trigger level tunable was malformed in the registry`
- `gpio-iic_sda`
- `_checkBusStatus`
- `_runPolledMode`
- `SCL is stuck low`
- `%s : unexpected MCS 0x%x\n`
- `%s failure; transaction history:\n`
- `Timed out waiting for interrupt`
- `%s timeout\n`
- `Attempt to get GPIO device failed`
- `force-polling`
- `_runInterruptMode`
- `timeout with %d of %d bytes read`
- `error interrupt`
- `AppleS5L8940XI2CController::_unjamBus Attempting recovery\n`
- `.always-on`
- `Bus is still jammed (SDA or SCL stuck low)`

**[__TEXT.__os_log]**

- `%s:%s: attempted to execute IIC command on workloop thread`
- `%s:%s: Command gate timeout!\n`
- `%s:%s: Error, unexpected return value from IIC command gate\n`

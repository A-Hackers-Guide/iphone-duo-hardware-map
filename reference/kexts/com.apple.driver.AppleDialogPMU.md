# `com.apple.driver.AppleDialogPMU`

- Name: AppleDialogPMU
- Version: `1.0.1`
- UUID: `8905377F-5EE3-38DA-B763-EF3F8AA10F2F`
- Source version: `1372.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPMU`](com.apple.driver.AppleARMPMU.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedTempSensor`](com.apple.driver.AppleEmbeddedTempSensor.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDialogPMU` | 0x108 | IOInterruptController → IOService → IORegistryEntry |
| `AppleDialogPMUUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000c16 off=0x00417540-0x00418156 addr=0xfffffe000741b540-0xfffffe000741c156 r--/r--   __TEXT            
	sz=0x0000059e off=0x00417bb8-0x00418156 addr=0xfffffe000741bbb8-0xfffffe000741c156               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002e70 off=0x01b6d560-0x01b703d0 addr=0xfffffe0008b71560-0xfffffe0008b743d0 r-x/r-x   __TEXT_EXEC       
	sz=0x00002c20 off=0x01b6d560-0x01b70180 addr=0xfffffe0008b71560-0xfffffe0008b74180          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000250 off=0x01b70180-0x01b703d0 addr=0xfffffe0008b74180-0xfffffe0008b743d0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000220 off=0x0493c868-0x0493ca88 addr=0xfffffe000b940868-0xfffffe000b940a88 rw-/rw-   __DATA            
	sz=0x00000188 off=0x0493c868-0x0493c9f0 addr=0xfffffe000b940868-0xfffffe000b9409f0               __DATA.__data             
	sz=0x00000078 off=0x00000000-0x00000078 addr=0xfffffe000b9409f0-0xfffffe000b940a68               __DATA.__common           (Zerofill)
	sz=0x00000020 off=0x00000000-0x00000020 addr=0xfffffe000b940a68-0xfffffe000b940a88               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001038 off=0x0104bfb8-0x0104cff0 addr=0xfffffe000804ffb8-0xfffffe0008050ff0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0104bfb8-0x0104bfc0 addr=0xfffffe000804ffb8-0xfffffe000804ffc0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0104bfc0-0x0104bfc8 addr=0xfffffe000804ffc0-0xfffffe000804ffc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000da8 off=0x0104bfc8-0x0104cd70 addr=0xfffffe000804ffc8-0xfffffe0008050d70         __DATA_CONST.__const            
	sz=0x00000100 off=0x0104cd70-0x0104ce70 addr=0xfffffe0008050d70-0xfffffe0008050e70         __DATA_CONST.__kalloc_type      
	sz=0x00000128 off=0x0104ce70-0x0104cf98 addr=0xfffffe0008050e70-0xfffffe0008050f98         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x0104cf98-0x0104cfe8 addr=0xfffffe0008050f98-0xfffffe0008050fe8         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x0104cfe8-0x0104cff0 addr=0xfffffe0008050fe8-0xfffffe0008050ff0         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 84 at 0x04ad6d24
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     8905377F-5EE3-38DA-B763-EF3F8AA10F2F
008: LC_SOURCE_VERSION           1372.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9d2a8 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDialogPMU`
- `CFBundleIdentifier`: `com.apple.driver.AppleDialogPMU`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDialogPMU`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDialogPMU.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901508800`
- `_PrelinkExecutableRelativePath`: `AppleDialogPMU`
- `_PrelinkExecutableSize`: `19678`
- `_PrelinkExecutableSourceAddr`: `-2198901508800`
- `_PrelinkKmodInfo`: `-2198829004696`

## Strings (41) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `setDebugProperties`
- `IOPMSystemSleepType`
- `pmu-chargetrap`
- `/chosen`
- `site.AppleDialogPMU`
- `AppleDialogPMUUserClient`
- `121111121222121211112122111111212`
- `no-halt_restart`
- `\n`
- `modReg`
- `_readADCGated`
- `event_name-%s`
- `pmu-debug`
- `pmu-bringup`
- `_writeRegs`
- `pmu-debug-wake`
- `AppleDialogPMU::%s failed: err=0x%08x, addr=0x%04x, data[%u]={`
- `AppleDialogPMU::%s failed: %08x, address=%04x, data=%02x mask=%02x tmp=%02x\n`
- `%s::%s(Debug) debug=%d\n`
- `%s::%sADC timeout %dms\n`
- `%s::%s::_readADCGated(%ld) cannot end conversion (%#x)\n`
- `%s::%s() selector=%d, inputCnt=%d, inputSize=%d, outputCnt=%d, outputSize=%d\n`
- `d240x-int-hack`
- `function-panic_reset`
- `start`
- `_readRegs`
- `1211111212221212111111111111`
- `222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211`
- `software-behavior`
- `config`
- `0x%02x%c`
- `debug`
- `%s::%s::_readADCGated(%ld) ADC read bad state: %d\n`
- `externalMethod`
- `AppleDialogPMU`
- `%s::%s::_readADCGated(%ld) ADC read duration: %lld\n`
- `%s::%s::_readADCGated(%ld) cannot read result (%#x)\n`
- `site.AppleDialogPMUUserClient`
- `site.AppleDialogMemLog`
- `debugWake`
- `%s::%s::_readADCGated(%ld) failed with status=%08x\n\n`

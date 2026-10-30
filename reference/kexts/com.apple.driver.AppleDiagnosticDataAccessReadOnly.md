# `com.apple.driver.AppleDiagnosticDataAccessReadOnly`

- Name: AppleDiagnosticDataAccessReadOnly
- Version: `1.0.0`
- UUID: `3F5FFCFF-A223-3BD0-B636-C7A38ED5EA9B`
- Source version: `55.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleNANDConfigAccess`](com.apple.driver.AppleNANDConfigAccess.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (4) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](../devicetree/root__arm-io__i2c3__display-eeprom__display-eeprom-data.md) | `AppleDiagnosticDataAccessReadOnly` | `diagnostic-data,format1` |
| [`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md) | `AppleDiagnosticDataAccessReadOnly` | `diagnostic-data,format1` |
| [`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](../devicetree/root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md) | `AppleDiagnosticDataAccessReadOnly` | `diagnostic-data,format1` |
| [`/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`](../devicetree/root__arm-io__i2c3__display-eeprom-2-hi__display-eeprom-data-2-hi.md) | `AppleDiagnosticDataAccessReadOnly` | `diagnostic-data,format1` |

## IOKit personalities (2) [KC]

### AppleNANDDiagnosticDataAccess
- `CFBundleIdentifier`: `com.apple.driver.AppleDiagnosticDataAccessReadOnly`
- `IOClass`: `AppleDiagnosticDataAccessReadOnly`
- `IOMatchCategory`: `AppleDiagnosticDataAccess`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDiagnosticDataAccessReadOnly`
- `IOProbeScore`: `99`
- `IOProviderClass`: `AppleNANDConfigAccess`

### AppleNORDiagnosticDataAccess
- `CFBundleIdentifier`: `com.apple.driver.AppleDiagnosticDataAccessReadOnly`
- `IOClass`: `AppleDiagnosticDataAccessReadOnly`
- `IONameMatch`: `diagnostic-data,format1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDiagnosticDataAccessReadOnly`
- `IOProbeScore`: `99`
- `IOProviderClass`: `AppleARMNORFlashDevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDiagnosticDataAccessReadOnly` | 0x1c8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000008f0 off=0x00416c50-0x00417540 addr=0xfffffe000741ac50-0xfffffe000741b540 r--/r--   __TEXT            
	sz=0x00000270 off=0x004172c8-0x00417538 addr=0xfffffe000741b2c8-0xfffffe000741b538               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000008 off=0x00417538-0x00417540 addr=0xfffffe000741b538-0xfffffe000741b540               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00001214 off=0x01b6c340-0x01b6d554 addr=0xfffffe0008b70340-0xfffffe0008b71554 r-x/r-x   __TEXT_EXEC       
	sz=0x000010b4 off=0x01b6c340-0x01b6d3f4 addr=0xfffffe0008b70340-0xfffffe0008b713f4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000160 off=0x01b6d3f4-0x01b6d554 addr=0xfffffe0008b713f4-0xfffffe0008b71554          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000138 off=0x0493c730-0x0493c868 addr=0xfffffe000b940730-0xfffffe000b940868 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493c730-0x0493c7f8 addr=0xfffffe000b940730-0xfffffe000b9407f8               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9407f8-0xfffffe000b940830               __DATA.__common           (Zerofill)
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b940830-0xfffffe000b940868               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000728 off=0x0104b890-0x0104bfb8 addr=0xfffffe000804f890-0xfffffe000804ffb8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x0104b890-0x0104b898 addr=0xfffffe000804f890-0xfffffe000804f898         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x0104b898-0x0104b8a0 addr=0xfffffe000804f898-0xfffffe000804f8a0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f8 off=0x0104b8a0-0x0104be98 addr=0xfffffe000804f8a0-0xfffffe000804fe98         __DATA_CONST.__const            
	sz=0x00000040 off=0x0104be98-0x0104bed8 addr=0xfffffe000804fe98-0xfffffe000804fed8         __DATA_CONST.__kalloc_type      
	sz=0x000000b0 off=0x0104bed8-0x0104bf88 addr=0xfffffe000804fed8-0xfffffe000804ff88         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x0104bf88-0x0104bfb8 addr=0xfffffe000804ff88-0xfffffe000804ffb8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 50 at 0x04ad6c5c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3F5FFCFF-A223-3BD0-B636-C7A38ED5EA9B
008: LC_SOURCE_VERSION           55.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9d278 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDiagnosticDataAccessReadOnly`
- `CFBundleIdentifier`: `com.apple.driver.AppleDiagnosticDataAccessReadOnly`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDiagnosticDataAccessReadOnly`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDiagnosticDataAccessReadOnly.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901511088`
- `_PrelinkExecutableRelativePath`: `AppleDiagnosticDataAccessReadOnly`
- `_PrelinkExecutableSize`: `9060`
- `_PrelinkExecutableSourceAddr`: `-2198901511088`
- `_PrelinkKmodInfo`: `-2198829005008`

## Strings (15) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AppleDiagnosticDataAccessReadOnly`
- `diagnostic-data-partial-region`
- `All Partial regions for the region %u have not enumerated yet.\n`
- `Failed to allocate diags data region %u buffer\n`
- `site.AppleDiagnosticDataAccessReadOnly`
- `\"AppleDiagnosticDataAccess does not support partial region data for NAND backed regions\" @%s:%d`
- `AppleDiagnosticDataDisplay`
- `Failed to match %p\n`
- `AppleDiagnosticDataAccessReadOnly.cpp`
- `\"AppleDiagnosticDataAccessReadOnly does not support unloading\" @%s:%d`
- `AppleDiagnosticDataSysCfg`
- `AppleDiagnosticDataDisplay-3`
- `121111121222121211112111222111211122211121112221112111222`
- `diagnostic-data-regions`
- `AppleDiagnosticData`

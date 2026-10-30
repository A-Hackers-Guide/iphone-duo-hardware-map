# `com.apple.driver.AppleT8030SOCTuner`

- Name: AppleT8030SOCTuner
- Version: `1`
- UUID: `D1413E33-1947-374F-B38B-6B8F05220B5B`
- Source version: `1976.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.ApplePMGR`](com.apple.driver.ApplePMGR.md) 1.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleT8030SOCTuner
- `CFBundleIdentifier`: `com.apple.driver.AppleT8030SOCTuner`
- `IOClass`: `AppleT8030SOCTuner`
- `IONameMatch`: `soc-tuner,t8030`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8030SOCTuner`
- `IOPlatformActiveAction`: `88000`
- `IOPlatformQuiesceAction`: `88000`
- `IOPlatformWakeAction`: `88000`
- `IOProviderClass`: `ApplePMGRNub`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSOCTuner` | 0xe0 | IOService → IORegistryEntry |
| `AppleT8030SOCTuner` | 0x128 | AppleSOCTuner → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000a80 off=0x0079f530-0x0079ffb0 addr=0xfffffe00077a3530-0xfffffe00077a3fb0 r--/r--   __TEXT            
	sz=0x0000041e off=0x0079fb58-0x0079ff76 addr=0xfffffe00077a3b58-0xfffffe00077a3f76               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000030 off=0x0079ff80-0x0079ffb0 addr=0xfffffe00077a3f80-0xfffffe00077a3fb0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00001848 off=0x0278faa0-0x027912e8 addr=0xfffffe0009793aa0-0xfffffe00097952e8 r-x/r-x   __TEXT_EXEC       
	sz=0x00001598 off=0x0278faa0-0x02791038 addr=0xfffffe0009793aa0-0xfffffe0009795038          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002b0 off=0x02791038-0x027912e8 addr=0xfffffe0009795038-0xfffffe00097952e8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049a1978-0x049a1aa0 addr=0xfffffe000b9a5978-0xfffffe000b9a5aa0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049a1978-0x049a1a40 addr=0xfffffe000b9a5978-0xfffffe000b9a5a40               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9a5a40-0xfffffe000b9a5aa0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e90 off=0x012383c8-0x01239258 addr=0xfffffe000823c3c8-0xfffffe000823d258 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012383c8-0x012383d8 addr=0xfffffe000823c3c8-0xfffffe000823c3d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012383d8-0x012383e8 addr=0xfffffe000823c3d8-0xfffffe000823c3e8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c50 off=0x012383e8-0x01239038 addr=0xfffffe000823c3e8-0xfffffe000823d038         __DATA_CONST.__const            
	sz=0x00000080 off=0x01239038-0x012390b8 addr=0xfffffe000823d038-0xfffffe000823d0b8         __DATA_CONST.__kalloc_type      
	sz=0x00000158 off=0x012390b8-0x01239210 addr=0xfffffe000823d0b8-0xfffffe000823d210         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x01239210-0x01239258 addr=0xfffffe000823d210-0xfffffe000823d258         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 95 at 0x04ae7c64
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     D1413E33-1947-374F-B38B-6B8F05220B5B
008: LC_SOURCE_VERSION           1976.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab3798 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleT8030SOCTuner`
- `CFBundleGetInfoString`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleT8030SOCTuner`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleT8030SOCTuner`
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
- `NSHumanReadableCopyright`: `Copyright © 2014 Apple. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleT8030SOCTuner.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897806032`
- `_PrelinkExecutableRelativePath`: `AppleT8030SOCTuner`
- `_PrelinkExecutableSize`: `12928`
- `_PrelinkExecutableSourceAddr`: `-2198897806032`
- `_PrelinkKmodInfo`: `-2198828590728`

## Strings (43) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleSOCTuner`
- `_provider`
- `IOReportLegend`
- `CONFIG`
- `_dispIdleCtrlFunction`
- `gpu-dpe-sync`
- `AppleSOCTuner`
- `\"AppleSOCTuner: %s:%u REQUIRE failed: %s\" @%s:%d`
- `soc-tuning`
- `dcs-power-gating`
- `_reporters`
- `#device-sets`
- `mcc-configs`
- `AppleSOCTuner: New MCC config: %u\n`
- `_legend`
- `function-dispidle_ctrl`
- `site.AppleT8030SOCTuner`
- `AppleSOCTuner: New DCS power gating state: %u\n`
- `_mccConfigReporter`
- `SoC Tuner Stats`
- `IOReportLegendPublic`
- `AppleSOCTuner.cpp`
- `mcc-power-gating`
- `mtp-clk-slowdown`
- `AppleSOCTuner: New SPMI idle handshake state: %u\n`
- `AppleSOCTuner: New Audio LLT state: %u\n`
- `1211111212221212121211221111`
- `fb-caching`
- `soc-tuner-debug`
- `AppleSOCTuner: Device count: %u\n`
- `1211111212221212121211221111222222222`
- `AppleSOCTuner: New ANE DPE config state: %u\n`
- `AppleSOCTuner: MCC config: %u -> %u\n`
- `virtual bool AppleSOCTuner::start(IOService *)`
- `devices`
- `function-mcc_ctrl`
- `_mccCtrlFunction`
- `MCC Config Stats`
- `AppleSOCTuner: Device set count: %u\n`
- `AppleSOCTuner: MCC config count: %u\n`
- `AppleSOCTuner: Started\n`
- `AppleT8030SOCTuner`
- `AppleSOCTuner: New device set states: Display:%u ANE:%u GPU:%u Audio:%u\n`

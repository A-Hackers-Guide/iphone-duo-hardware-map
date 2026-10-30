# `com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`

- Name: AudioDMACLLTEscalationDetector_Gen1p0
- Version: `600.45`
- UUID: `1368A522-F57C-330D-B85D-FFCACB39048C`
- Source version: `600.45.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleEmbeddedAudioLibs`](com.apple.driver.AppleEmbeddedAudioLibs.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (3) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/admac-dispint0-ced-ssw`](../devicetree/root__arm-io__admac-dispint0-ced-ssw.md) | `AudioDMACLLTEscalationDetector` | `admacled,v1p0` |
| [`/arm-io/admac-dispext0-ced-ssw`](../devicetree/root__arm-io__admac-dispext0-ced-ssw.md) | `AudioDMACLLTEscalationDetector` | `admacled,v1p0` |
| [`/arm-io/admac-aop-ced-ssw`](../devicetree/root__arm-io__admac-aop-ced-ssw.md) | `AudioDMACLLTEscalationDetector` | `admacled,v1p0` |

## IOKit personalities (1) [KC]

### AudioDMACLLTEscalationDetector
- `CFBundleIdentifier`: `com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`
- `IOClass`: `AudioDMACLLTEscalationDetector`
- `IONameMatch`:
  - `admacled,v1p0`
- `IOPersonalityPublisher`: `com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`
- `IOPlatformPanicAction`: `89000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ADMACCEDInterface` | 0x88 | IOService → IORegistryEntry |
| `AudioDMACLLTEscalationDetector` | 0x3c0 | ADMACCEDInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000f00 off=0x008f9d30-0x008fac30 addr=0xfffffe00078fdd30-0xfffffe00078fec30 r--/r--   __TEXT            
	sz=0x00000030 off=0x008fa3b0-0x008fa3e0 addr=0xfffffe00078fe3b0-0xfffffe00078fe3e0               __TEXT.__const            
	sz=0x000005f2 off=0x008fa3e0-0x008fa9d2 addr=0xfffffe00078fe3e0-0xfffffe00078fe9d2               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000025e off=0x008fa9d2-0x008fac30 addr=0xfffffe00078fe9d2-0xfffffe00078fec30               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000436c off=0x02bccd50-0x02bd10bc addr=0xfffffe0009bd0d50-0xfffffe0009bd50bc r-x/r-x   __TEXT_EXEC       
	sz=0x000040ec off=0x02bccd50-0x02bd0e3c addr=0xfffffe0009bd0d50-0xfffffe0009bd4e3c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000280 off=0x02bd0e3c-0x02bd10bc addr=0xfffffe0009bd4e3c-0xfffffe0009bd50bc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001e8 off=0x049dab10-0x049dacf8 addr=0xfffffe000b9deb10-0xfffffe000b9decf8 rw-/rw-   __DATA            
	sz=0x00000188 off=0x049dab10-0x049dac98 addr=0xfffffe000b9deb10-0xfffffe000b9dec98               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9dec98-0xfffffe000b9decf8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000f20 off=0x012bea98-0x012bf9b8 addr=0xfffffe00082c2a98-0xfffffe00082c39b8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012bea98-0x012beaa8 addr=0xfffffe00082c2a98-0xfffffe00082c2aa8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012beaa8-0x012beab8 addr=0xfffffe00082c2aa8-0xfffffe00082c2ab8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000d00 off=0x012beab8-0x012bf7b8 addr=0xfffffe00082c2ab8-0xfffffe00082c37b8         __DATA_CONST.__const            
	sz=0x00000080 off=0x012bf7b8-0x012bf838 addr=0xfffffe00082c37b8-0xfffffe00082c3838         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x012bf838-0x012bf978 addr=0xfffffe00082c3838-0xfffffe00082c3978         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x012bf978-0x012bf9b8 addr=0xfffffe00082c3978-0xfffffe00082c39b8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 88 at 0x04aed438
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1368A522-F57C-330D-B85D-FFCACB39048C
008: LC_SOURCE_VERSION           600.45.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab8b10 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AudioDMACLLTEscalationDetector_Gen1p0`
- `CFBundleIdentifier`: `com.apple.driver.AudioDMACLLTEscalationDetector-Gen1p0`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AudioDMACLLTEscalationDetector_Gen1p0`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.45`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2025 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AudioDMACLLTEscalationDetector_Gen1p0.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896386768`
- `_PrelinkExecutableRelativePath`: `AudioDMACLLTEscalationDetector_Gen1p0`
- `_PrelinkExecutableSize`: `25460`
- `_PrelinkExecutableSourceAddr`: `-2198896386768`
- `_PrelinkKmodInfo`: `-2198828356848`

## Strings (61) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AudioDMACLLTEscalationDetector`
- `ced_disable`
- `v12@?0i8`
- `%s: CED/SSW not active.\n`
- `%c%c%c%c`
- `12111112122212121`
- `ced-tunables`
- `ced_rack_config`
- `abs_ltr`
- `override_tunables_aggressive`
- `IOReportLegend`
- `ADMACCEDInterface`
- `site.ADMACCEDInterface`
- `#ssw-register-count`
- `#dma-controllers`
- `23:38:09`
- `No`
- `%03u`
- `Telemetry`
- `%s%s`
- `identity`
- `SIXTEEN_CHAR_CED CLLT Escalated.  CED section      SSW name: SIXTEEN_CHAR_SSW  Rx channels: %% %% %% %%  Tx channels: %% %% %% %%  SSW data: `
- `#dma-channels-rx`
- `telemetry_mode`
- `Oct 13 2026`
- `Yes`
- `121111121222121211111122121212121212121211212121212211112222221112222222222222222222222222222222222222222222222222222222`
- `dma-controllers`
- `#dma-channels-tx`
- `ssw-tunables`
- `\"%s@%llu: At least %u clients are active.\" @%s:%d`
- `\"%s\" @%s:%d`
- `%s CLLT Escalated.\nCED section\n  SSW name: %s\n  Rx channels: %02u %02u %02u %02u\n  Tx channels: %02u %02u %02u %02u\n  SSW data: `
- `\"%s@%llu: %s seen at activation.\" @%s:%d`
- `0x%08x`
- `i8@?0`
- `\"%s: Could not prepare panic string due to 0x%08x.\" @%s:%d`
- `IOReportLegendPublic`
- `site.AudioDMACLLTEscalationDetector`
- `escalation_duration`
- `%s: Built on %s at %s. \n          \tRack tunables = %s\n          \tCED enabled   = %s\n          \tMode          = %s\n          \tAbs CLTR Ovr  = 0x%08x\n          \tEsc Dura Ovr  = 0x%08x\n          \tTrig Thr Ovr  = 0x%08x\n          \tPanic sPS(0)  = %s\n          \tAggressive    = %s\n       `
- `Panic`
- `deactivate_block_invoke`
- `%s\n`
- `%s: Could not prepare panic string due to 0x%08x.\n`
- `%s.%s`
- `panic_on_sps0_actives`
- `AudioDMACLLTEscalationDetector.cpp`
- `\"%s@%llu: %s seen at deactivation.\" @%s:%d`

**[__TEXT.__os_log]**

- `%s: successfully started.`
- `\t%s: Client <%s>.`
- `%s: Captured %u snapshot registers.`
- `%s: Service is not suspended, but an empty tracker seen.`
- `%s: Tunable %s size is wonky (%u).`
- `%s: Property %s is too small (%u < %lu).`
- `%s: Failed to start due to %s.`
- `%s: Tunables ingestion for %s failed with %s (%#08x).`
- `%s: These %u clients are active at sPS(0):`
- `%s: sPS(0) has happened before the last deactivation. Bailing.`
- `%s: Tunable %s not found.`
- `%s: Property %s not found.`

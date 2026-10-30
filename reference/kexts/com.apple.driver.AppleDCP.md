# `com.apple.driver.AppleDCP`

- Name: AppleDCP
- Version: `1`
- UUID: `67A3DA71-EFCA-3ED1-B4A7-FFA0F53CA917`
- Source version: `1317.40.16.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0

## Device-tree nodes it binds (3) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) | `AppleDCPExpert` | `dcp-expert-v1` |
| [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) | `AppleDCPExpert` | `dcp-expert-v1` |
| [`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) | `AppleDCPExpert` | `dcp-expert-v1` |

## IOKit personalities (5) [KC]

### AppleDCPExpert
- `CFBundleIdentifier`: `com.apple.driver.AppleDCP`
- `IOClass`: `AppleDCPExpert`
- `IONameMatch`: `dcp-expert-v1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCP`
- `IOProviderClass`: `AppleARMIODevice`

### BoraDCPEndpoints
- `CFBundleIdentifier`: `com.apple.driver.AppleDCP`
- `IOClass`: `AFKACIPCEndpoint`
- `IONameMatch`:
  - `bora-dcplEndpoint1`
  - `bora-dcplEndpoint2`
  - `bora-dcplEndpoint3`
  - `bora-dcplEndpoint4`
  - `bora-dcplEndpoint5`
  - `bora-dcplEndpoint6`
  - `bora-dcplEndpoint7`
  - `bora-dcplEndpoint8`
  - `bora-dcplEndpoint9`
  - `bora-dcplEndpoint10`
  - `bora-dcplEndpoint11`
  - `bora-dcplEndpoint12`
  - `bora-dcplEndpoint13`
  - `bora-dcplEndpoint14`
  - `bora-dcplEndpoint15`
  - `bora-dcplEndpoint16`
  - `bora-dcplEndpoint17`
  - `bora-dcplEndpoint18`
  - `bora-dcplEndpoint19`
  - `bora-dcplEndpoint20`
  - `bora-dcplEndpoint21`
  - `bora-dcplEndpoint22`
  - `bora-dcplEndpoint23`
  - `bora-dcprEndpoint1`
  - `bora-dcprEndpoint2`
  - `bora-dcprEndpoint3`
  - `bora-dcprEndpoint4`
  - `bora-dcprEndpoint5`
  - `bora-dcprEndpoint6`
  - `bora-dcprEndpoint7`
  - `bora-dcprEndpoint8`
  - `bora-dcprEndpoint9`
  - `bora-dcprEndpoint10`
  - `bora-dcprEndpoint11`
  - `bora-dcprEndpoint12`
  - `bora-dcprEndpoint13`
  - `bora-dcprEndpoint14`
  - `bora-dcprEndpoint15`
  - `bora-dcprEndpoint16`
  - `bora-dcprEndpoint17`
  - `bora-dcprEndpoint18`
  - `bora-dcprEndpoint19`
  - `bora-dcprEndpoint20`
  - `bora-dcprEndpoint21`
  - `bora-dcprEndpoint22`
  - `bora-dcprEndpoint23`
  - `bora-dcpsEndpoint1`
  - `bora-dcpsEndpoint2`
  - `bora-dcpsEndpoint3`
  - `bora-dcpsEndpoint4`
  - `bora-dcpsEndpoint5`
  - `bora-dcpsEndpoint6`
  - `bora-dcpsEndpoint7`
  - `bora-dcpsEndpoint8`
  - `bora-dcpsEndpoint9`
  - `bora-dcpsEndpoint10`
  - `bora-dcpsEndpoint11`
  - `bora-dcpsEndpoint12`
  - `bora-dcpsEndpoint13`
  - `bora-dcpsEndpoint14`
  - `bora-dcpsEndpoint15`
  - `bora-dcpsEndpoint16`
  - `bora-dcpsEndpoint17`
  - `bora-dcpsEndpoint18`
  - `bora-dcpsEndpoint19`
  - `bora-dcpsEndpoint20`
  - `bora-dcpsEndpoint21`
  - `bora-dcpsEndpoint22`
  - `bora-dcpsEndpoint23`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCP`
- `IOProviderClass`: `RTBuddyEndpointService`

### DCPEndpointsV2
- `CFBundleIdentifier`: `com.apple.driver.AppleDCP`
- `IOClass`: `DCPEndpointV2`
- `IONameMatch`:
  - `DCPEndpoint1`
  - `DCPEndpoint2`
  - `DCPEndpoint3`
  - `DCPEndpoint4`
  - `DCPEndpoint5`
  - `DCPEndpoint6`
  - `DCPEndpoint7`
  - `DCPEndpoint8`
  - `DCPEndpoint9`
  - `DCPEndpoint10`
  - `DCPEndpoint11`
  - `DCPEndpoint12`
  - `DCPEndpoint13`
  - `DCPEndpoint14`
  - `DCPEndpoint15`
  - `DCPEndpoint16`
  - `DCPEndpoint17`
  - `DCPEndpoint18`
  - `DCPEndpoint19`
  - `DCPEndpoint20`
  - `DCPEndpoint21`
  - `DCPEndpoint22`
  - `DCPEndpoint23`
  - `DCP0Endpoint1`
  - `DCP0Endpoint2`
  - `DCP0Endpoint3`
  - `DCP0Endpoint4`
  - `DCP0Endpoint5`
  - `DCP0Endpoint6`
  - `DCP0Endpoint7`
  - `DCP0Endpoint8`
  - `DCP0Endpoint9`
  - `DCP0Endpoint10`
  - `DCP0Endpoint11`
  - `DCP0Endpoint12`
  - `DCP0Endpoint13`
  - `DCP0Endpoint14`
  - `DCP0Endpoint15`
  - `DCP0Endpoint16`
  - `DCP0Endpoint17`
  - `DCP0Endpoint18`
  - `DCP0Endpoint19`
  - `DCP0Endpoint20`
  - `DCP0Endpoint21`
  - `DCP0Endpoint22`
  - `DCP0Endpoint23`
  - `DCPSECEndpoint1`
  - `DCPSECEndpoint2`
  - `DCPSECEndpoint3`
  - `DCPSECEndpoint4`
  - `DCPSECEndpoint5`
  - `DCPSECEndpoint6`
  - `DCPSECEndpoint7`
  - `DCPSECEndpoint8`
  - `DCPSECEndpoint9`
  - `DCPSECEndpoint10`
  - `DCPSECEndpoint11`
  - `DCPSECEndpoint12`
  - `DCPSECEndpoint13`
  - `DCPSECEndpoint14`
  - `DCPSECEndpoint15`
  - `DCPSECEndpoint16`
  - `DCPSECEndpoint17`
  - `DCPSECEndpoint18`
  - `DCPSECEndpoint19`
  - `DCPSECEndpoint20`
  - `DCPSECEndpoint21`
  - `DCPSECEndpoint22`
  - `DCPSECEndpoint23`
  - `DCPEXTEndpoint1`
  - `DCPEXTEndpoint2`
  - `DCPEXTEndpoint3`
  - `DCPEXTEndpoint4`
  - `DCPEXTEndpoint5`
  - `DCPEXTEndpoint6`
  - `DCPEXTEndpoint7`
  - `DCPEXTEndpoint8`
  - `DCPEXTEndpoint9`
  - `DCPEXTEndpoint10`
  - `DCPEXTEndpoint11`
  - `DCPEXTEndpoint12`
  - `DCPEXTEndpoint13`
  - `DCPEXTEndpoint14`
  - `DCPEXTEndpoint15`
  - `DCPEXTEndpoint16`
  - `DCPEXTEndpoint17`
  - `DCPEXTEndpoint18`
  - `DCPEXTEndpoint19`
  - `DCPEXTEndpoint20`
  - `DCPEXTEndpoint21`
  - `DCPEXTEndpoint22`
  - `DCPEXTEndpoint23`
  - `DCPEXT0Endpoint1`
  - `DCPEXT0Endpoint2`
  - `DCPEXT0Endpoint3`
  - `DCPEXT0Endpoint4`
  - `DCPEXT0Endpoint5`
  - `DCPEXT0Endpoint6`
  - `DCPEXT0Endpoint7`
  - `DCPEXT0Endpoint8`
  - `DCPEXT0Endpoint9`
  - `DCPEXT0Endpoint10`
  - `DCPEXT0Endpoint11`
  - `DCPEXT0Endpoint12`
  - `DCPEXT0Endpoint13`
  - `DCPEXT0Endpoint14`
  - `DCPEXT0Endpoint15`
  - `DCPEXT0Endpoint16`
  - `DCPEXT0Endpoint17`
  - `DCPEXT0Endpoint18`
  - `DCPEXT0Endpoint19`
  - `DCPEXT0Endpoint20`
  - `DCPEXT0Endpoint21`
  - `DCPEXT0Endpoint22`
  - `DCPEXT0Endpoint23`
  - `DCPEXT1Endpoint1`
  - `DCPEXT1Endpoint2`
  - `DCPEXT1Endpoint3`
  - `DCPEXT1Endpoint4`
  - `DCPEXT1Endpoint5`
  - `DCPEXT1Endpoint6`
  - `DCPEXT1Endpoint7`
  - `DCPEXT1Endpoint8`
  - `DCPEXT1Endpoint9`
  - `DCPEXT1Endpoint10`
  - `DCPEXT1Endpoint11`
  - `DCPEXT1Endpoint12`
  - `DCPEXT1Endpoint13`
  - `DCPEXT1Endpoint14`
  - `DCPEXT1Endpoint15`
  - `DCPEXT1Endpoint16`
  - `DCPEXT1Endpoint17`
  - `DCPEXT1Endpoint18`
  - `DCPEXT1Endpoint19`
  - `DCPEXT1Endpoint20`
  - `DCPEXT1Endpoint21`
  - `DCPEXT1Endpoint22`
  - `DCPEXT1Endpoint23`
  - `DCPEXT2Endpoint1`
  - `DCPEXT2Endpoint2`
  - `DCPEXT2Endpoint3`
  - `DCPEXT2Endpoint4`
  - `DCPEXT2Endpoint5`
  - `DCPEXT2Endpoint6`
  - `DCPEXT2Endpoint7`
  - `DCPEXT2Endpoint8`
  - `DCPEXT2Endpoint9`
  - `DCPEXT2Endpoint10`
  - `DCPEXT2Endpoint11`
  - `DCPEXT2Endpoint12`
  - `DCPEXT2Endpoint13`
  - `DCPEXT2Endpoint14`
  - `DCPEXT2Endpoint15`
  - `DCPEXT2Endpoint16`
  - `DCPEXT2Endpoint17`
  - `DCPEXT2Endpoint18`
  - `DCPEXT2Endpoint19`
  - `DCPEXT2Endpoint20`
  - `DCPEXT2Endpoint21`
  - `DCPEXT2Endpoint22`
  - `DCPEXT2Endpoint23`
  - `DCPEXT3Endpoint1`
  - `DCPEXT3Endpoint2`
  - `DCPEXT3Endpoint3`
  - `DCPEXT3Endpoint4`
  - `DCPEXT3Endpoint5`
  - `DCPEXT3Endpoint6`
  - `DCPEXT3Endpoint7`
  - `DCPEXT3Endpoint8`
  - `DCPEXT3Endpoint9`
  - `DCPEXT3Endpoint10`
  - `DCPEXT3Endpoint11`
  - `DCPEXT3Endpoint12`
  - `DCPEXT3Endpoint13`
  - `DCPEXT3Endpoint14`
  - `DCPEXT3Endpoint15`
  - `DCPEXT3Endpoint16`
  - `DCPEXT3Endpoint17`
  - `DCPEXT3Endpoint18`
  - `DCPEXT3Endpoint19`
  - `DCPEXT3Endpoint20`
  - `DCPEXT3Endpoint21`
  - `DCPEXT3Endpoint22`
  - `DCPEXT3Endpoint23`
  - `DCPEXT4Endpoint1`
  - `DCPEXT4Endpoint2`
  - `DCPEXT4Endpoint3`
  - `DCPEXT4Endpoint4`
  - `DCPEXT4Endpoint5`
  - `DCPEXT4Endpoint6`
  - `DCPEXT4Endpoint7`
  - `DCPEXT4Endpoint8`
  - `DCPEXT4Endpoint9`
  - `DCPEXT4Endpoint10`
  - `DCPEXT4Endpoint11`
  - `DCPEXT4Endpoint12`
  - `DCPEXT4Endpoint13`
  - `DCPEXT4Endpoint14`
  - `DCPEXT4Endpoint15`
  - `DCPEXT4Endpoint16`
  - `DCPEXT4Endpoint17`
  - `DCPEXT4Endpoint18`
  - `DCPEXT4Endpoint19`
  - `DCPEXT4Endpoint20`
  - `DCPEXT4Endpoint21`
  - `DCPEXT4Endpoint22`
  - `DCPEXT4Endpoint23`
  - `DCPEXT5Endpoint1`
  - `DCPEXT5Endpoint2`
  - `DCPEXT5Endpoint3`
  - `DCPEXT5Endpoint4`
  - `DCPEXT5Endpoint5`
  - `DCPEXT5Endpoint6`
  - `DCPEXT5Endpoint7`
  - `DCPEXT5Endpoint8`
  - `DCPEXT5Endpoint9`
  - `DCPEXT5Endpoint10`
  - `DCPEXT5Endpoint11`
  - `DCPEXT5Endpoint12`
  - `DCPEXT5Endpoint13`
  - `DCPEXT5Endpoint14`
  - `DCPEXT5Endpoint15`
  - `DCPEXT5Endpoint16`
  - `DCPEXT5Endpoint17`
  - `DCPEXT5Endpoint18`
  - `DCPEXT5Endpoint19`
  - `DCPEXT5Endpoint20`
  - `DCPEXT5Endpoint21`
  - `DCPEXT5Endpoint22`
  - `DCPEXT5Endpoint23`
  - `DCPEXT6Endpoint1`
  - `DCPEXT6Endpoint2`
  - `DCPEXT6Endpoint3`
  - `DCPEXT6Endpoint4`
  - `DCPEXT6Endpoint5`
  - `DCPEXT6Endpoint6`
  - `DCPEXT6Endpoint7`
  - `DCPEXT6Endpoint8`
  - `DCPEXT6Endpoint9`
  - `DCPEXT6Endpoint10`
  - `DCPEXT6Endpoint11`
  - `DCPEXT6Endpoint12`
  - `DCPEXT6Endpoint13`
  - `DCPEXT6Endpoint14`
  - `DCPEXT6Endpoint15`
  - `DCPEXT6Endpoint16`
  - `DCPEXT6Endpoint17`
  - `DCPEXT6Endpoint18`
  - `DCPEXT6Endpoint19`
  - `DCPEXT6Endpoint20`
  - `DCPEXT6Endpoint21`
  - `DCPEXT6Endpoint22`
  - `DCPEXT6Endpoint23`
  - `DCPEXT7Endpoint1`
  - `DCPEXT7Endpoint2`
  - `DCPEXT7Endpoint3`
  - `DCPEXT7Endpoint4`
  - `DCPEXT7Endpoint5`
  - `DCPEXT7Endpoint6`
  - `DCPEXT7Endpoint7`
  - `DCPEXT7Endpoint8`
  - `DCPEXT7Endpoint9`
  - `DCPEXT7Endpoint10`
  - `DCPEXT7Endpoint11`
  - `DCPEXT7Endpoint12`
  - `DCPEXT7Endpoint13`
  - `DCPEXT7Endpoint14`
  - `DCPEXT7Endpoint15`
  - `DCPEXT7Endpoint16`
  - `DCPEXT7Endpoint17`
  - `DCPEXT7Endpoint18`
  - `DCPEXT7Endpoint19`
  - `DCPEXT7Endpoint20`
  - `DCPEXT7Endpoint21`
  - `DCPEXT7Endpoint22`
  - `DCPEXT7Endpoint23`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCP`
- `IOProbeScore`: `1`
- `IOProviderClass`: `RTBuddyEndpointService`
- `IOProviderMergeProperties`:
  - `dcp-ep`: `True`

### DCPFirmwareServiceEXT
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKFirmwareService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCP`
- `IOPropertyMatch`:
  - `role`: `DCPEXT`
- `IOProviderClass`: `RTBuddyService`

### PMGRDispCtrl
- `CFBundleIdentifier`: `com.apple.driver.AppleDCP`
- `IOClass`: `PMGRDispCtrl`
- `IONameMatch`: `pmgr-disp-ctrl`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDCP`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDCPExpert` | 0x2d08 | IOService → IORegistryEntry |
| `DCPEndpointV2` | 0x1c8 | AFKEPKextV2 → AFKEPKextBaseV2 → IOService → IORegistryEntry |
| `DCPPowerCallback` | 0x28 |  |
| `PMGRDispCtrl` | 0xb0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000024fd off=0x00412650-0x00414b4d addr=0xfffffe0007416650-0xfffffe0007418b4d r--/r--   __TEXT            
	sz=0x00001e4d off=0x00412cc8-0x00414b15 addr=0xfffffe0007416cc8-0xfffffe0007418b15               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000002d off=0x00414b20-0x00414b4d addr=0xfffffe0007418b20-0xfffffe0007418b4d               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00008e70 off=0x01b5b150-0x01b63fc0 addr=0xfffffe0008b5f150-0xfffffe0008b67fc0 r-x/r-x   __TEXT_EXEC       
	sz=0x00008a50 off=0x01b5b150-0x01b63ba0 addr=0xfffffe0008b5f150-0xfffffe0008b67ba0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000420 off=0x01b63ba0-0x01b63fc0 addr=0xfffffe0008b67ba0-0xfffffe0008b67fc0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000188 off=0x0493c408-0x0493c590 addr=0xfffffe000b940408-0xfffffe000b940590 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493c408-0x0493c4d0 addr=0xfffffe000b940408-0xfffffe000b9404d0               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b9404d0-0xfffffe000b940580               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b940580-0xfffffe000b940590               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000018b8 off=0x01047068-0x01048920 addr=0xfffffe000804b068-0xfffffe000804c920 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x01047068-0x01047088 addr=0xfffffe000804b068-0xfffffe000804b088         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x01047088-0x010470a8 addr=0xfffffe000804b088-0xfffffe000804b0a8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000014c0 off=0x010470a8-0x01048568 addr=0xfffffe000804b0a8-0xfffffe000804c568         __DATA_CONST.__const            
	sz=0x00000100 off=0x01048568-0x01048668 addr=0xfffffe000804c568-0xfffffe000804c668         __DATA_CONST.__kalloc_type      
	sz=0x00000210 off=0x01048668-0x01048878 addr=0xfffffe000804c668-0xfffffe000804c878         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a8 off=0x01048878-0x01048920 addr=0xfffffe000804c878-0xfffffe000804c920         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 153 at 0x04ad682c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     67A3DA71-EFCA-3ED1-B4A7-FFA0F53CA917
008: LC_SOURCE_VERSION           1317.40.16.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9cfd0 size=0x110
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleDCP`
- `CFBundleIdentifier`: `com.apple.driver.AppleDCP`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDCP`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91018`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91018`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2019-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDCP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901529008`
- `_PrelinkExecutableRelativePath`: `AppleDCP`
- `_PrelinkExecutableSize`: `52653`
- `_PrelinkExecutableSourceAddr`: `-2198901529008`
- `_PrelinkKmodInfo`: `-2198829005816`

## Strings (195) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `i8@?0`
- `void PMGRDispCtrl::_setPmgrDispCtrlForceWake(bool, IOService * _Nonnull)`
- `_pmgrDispCtrlBaseAddress`
- `DCPEndpointV2`
- `121111121222121211111111112121111211111111222121111111112`
- `conditional-retention-size`
- `conditional-retention-disable`
- `axi2af-reg-index`
- `[AppleDCPExpert:0x%llx] open fail 0x%llx\n`
- `PMGRDispCtrl.cpp`
- `void AppleDCPExpert::_enterTrace(UInt32, void * _Nullable, void * _Nullable, void * _Nullable)`
- `\"[AppleDCPExpert:0x%llx] GAPF error with empty assertion mask\\n\" @%s:%d`
- `failsafe-category-%d`
- `tconHealthFailures`
- `crcConsecutiveErrorThresholdCount`
- `displayDeviceID`
- `DCPEXT0`
- `\"%s PMGR Scratch size mismatch\\n\" @%s:%d`
- `\"missing function-force_wake in EDT\\n\" @%s:%d`
- `DCPExpertPowerState`
- `\"[AppleDCPExpert:0x%llx] GAPF Error (0x%x): failed to find violated GAPF\\n\" @%s:%d`
- `failsafe-telemetry-event`
- `DCPEXT3`
- `frame1Failsafes`
- `PostErrorPLLNotLocked`
- `join-power-plane`
- `\"%s conditional-retention-disable size mismatch\\n\" @%s:%d`
- `require-axi2af-reset`
- `AppleDCPExpert::%s unexpected response size of %u: %zu\n`
- `crcErrors`
- `DCPEXT4`
- `display-post-failed`
- `site.PMGRDispCtrl`
- `void PMGRDispCtrl::_pollReg(IOLogicalAddress, UInt32, UInt32, UInt32, bool)`
- `dcp-power-manage`
- `\"%s missing pmgr-soc-pwrgate-index\\n\" @%s:%d`
- `function-force_wake`
- `\"%s missing axi2af-reg-index\\n\" @%s:%d`
- `B16@?0^{OSObject=^^?i}8`
- `\"%s missing conditional-retention-enable\\n\" @%s:%d`
- `void AppleDCPExpert::_pollReg(IOLogicalAddress, UInt32, UInt32, UInt32, bool)`
- `\"%s invalid state transition from %u to %u\\n\" @%s:%d`
- `\"%s Dynamic Sys/Fe power gate transition not supported from current power state (0x%x)\\n\" @%s:%d`
- `AppleDCPExpert::%s unexpected response size of %u: %u\n`
- `W`
- `skippedScaFrames`
- `12111`
- `virtual bool AppleDCPExpert::start(IOService *)`
- `require-force-wakeup`
- `_pmgrScratchBaseAddress`
- `void AppleDCPExpert::_setDispSysFePowerGateEnable(bool)`
- `_dcpExpertWorkLoop->inGate()`
- `maxConsecutiveErrors`
- `[AppleDCPExpert:0x%llx]_changeDCPPowerStateInternal:%x\n`
- `scaCrcMissing`
- `frameGapTooLarge`
- `videoOverflow`
- `pmgr-soc-pwrgate-index`
- `prevState`
- `mogul-auth-provider`
- `maxEsdDuration`
- `virtual bool PMGRDispCtrl::start(IOService * _Nonnull)`
- `!=`
- `\"%s missing role\" @%s:%d`
- `dcp-pmgr-scratch`
- `\"%s missing PMGR scratch mapping\\n\" @%s:%d`
- `\"%s missing PMGR_SOC_PWRGATE mapping\\n\" @%s:%d`
- `_handleDPTXFIFOEpiResponse`
- `DCPSEC`
- `\"%s %p failed release assertion\\n\" @%s:%d`
- `\"%s conditional-retention-enable size mismatch\\n\" @%s:%d`
- `PostErrorVFTGStatus`
- `DCPPowerRetained`
- `virtual bool DCPEndpointV2::start(IOService *)`
- `%s failed to get AppleDCPExpert\n`
- `site.AppleDCPExpert`
- `support-psd-self-vote`
- `pmgr-scratch-index`
- `\"%s missing DCP_CONTROLS mapping\\n\" @%s:%d`
- `R`
- `==`
- `site.DCPEndpointV2`
- `AppleDCPExpert`
- `\"%s missing conditional-retention-size\\n\" @%s:%d`
- `dcpexpert-epi`
- `[AppleDCPExpert:0x%llx] _setDCPExpertPowerState(%d,%d):%x duration:%lld\n`
- `_submitTelemetryGated`
- `display-post-failsafes`
- `%s:%u: REQUIRE failed: %s  `
- `site.DCPPowerCallback`
- `DebugState`
- `[AppleDCPExpert:0x%llx] mogul auth failed\n`
- `PostFailed`
- `axi2af-tlimit-offset`
- `RTBuddyService`
- `DCPPowerState`
- `[AppleDCPExpert:0x%llx]: support-health-telemetry present but mogul path not in devicetree\n`
- `skippedTconFrames`
- `display-post-error-mask`
- `FrameErrorCount`
- `1211111212221212111212`
- `AppleDCPExpert.cpp`
- `function-enable_autopm`
- `\"%s missing DCP_FORCE_WAKEUP value\\n\" @%s:%d`
- `\"%s Dynamic Sys/Fe power gate on this platform is not supported\\n\" @%s:%d`
- `skip-mogul-auth`
- `transportHealthFailures`
- `DCP`
- `dcp-controls-reg-index`
- `getSupportsDynamicSysFePowerGate()`
- `values`
- `com.apple.display.DPTXFIFOErrors`
- `com.apple.display.HealthMonitor.DisplayPOST`
- `frame4Failsafes`
- `PostErrorLanesStatus`
- `\"%s missing function-enable_autopm\\n\" @%s:%d`
- `IOHibernateState`
- `\"%s DCP standalone on this platform is not supported\\n\" @%s:%d`
- `support-dptx-fifo-telemetry`
- `DCPEXT2`
- `[AppleDCPExpert:0x%llx] mogul provider not found\n`
- `DCPEndpointV2.cpp`
- `newState`
- `timestamp`
- `support-health-telemetry`
- `videoUnderflow`
- `PostErrorLanesSymbolErrors`
- `conditional-retention-offset`
- `dcp-controls-value-on`
- `dcp-remote-power-state`
- `IOReturn AppleDCPExpert::_changeDCPPowerStateInternal(DCPPowerState)`
- `_handleHealthMonitorEpiResponse`
- `\"[AppleDCPExpert:0x%llx] GAPF Error (0x%x): Master ID %u, Address 0x%llx, CMD %s\\n\" @%s:%d`
- `maxConsecutiveCrcErrors`
- `frame2Failsafes`
- `remote-power-state`
- `_dcpForceWakeupBaseAddress`
- `maxConsecutiveTconHealthFailures`
- `com.apple.display.HealthMonitor`
- `frame3Failsafes`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `duration`
- `\"%s missing conditional-retention-offset\\n\" @%s:%d`
- `BootComplete`
- `void AppleDCPExpert::_setDCPForceWakeup(bool)`
- `mogul-auth-key`
- `DCPEXT6`
- `unit`
- `AppleDCPExpert::%s epic unavailable\n`
- `frame0Failsafes`
- `\"%s missing PMGR_DISP_CTRL mapping\\n\" @%s:%d`
- `support-dynamic-sysfe-pg`
- `\"%s conditional-retention-offset size mismatch\\n %lu : %u\" @%s:%d`
- `\"%s missing AXI2AF mapping\\n\" @%s:%d`
- `_PmgrSocPwrGateBaseAddress`
- `DCPEXT7`
- `[AppleDCPExpert:0x%llx] failed to create mogul matching dict\n`
- `PostErrorNoHPD`
- `\"%s missing axi2af-tlimit-offset\\n\" @%s:%d`
- `void AppleDCPExpert::_setPMGRScratchRegion(bool)`
- `PMGRDispCtrl`
- `_lock = IOSimpleLockAlloc() failed\n`
- `\"%s %p failed acquire assertion\\n\" @%s:%d`
- `conditional-retention-enable`
- `\"%s missing conditional-retention-disable\\n\" @%s:%d`
- `DCPEXT`
- `_pmgrConditionalRetentionOffsets`
- `disable-power-manage`
- `pmgr-scratch-value-off`
- `dcp-controls-value-off`
- `^{OSString=^^?ib14b18*}32@?0r*8Q16r*24`
- `maxConsecutiveTransportHealthFailures`
- `DCPEXT5`
- `DCPPowerAssertionCount`
- `DCPPowerCallback`
- `%s power transition defered!\n`
- `failsafe-bool-category-start`
- `%s%s`
- `\"%s missing DCP_FORCE_WAKEUP values\\n\" @%s:%d`
- `\"%s unsupported state: %u\\n\" @%s:%d`
- `void AppleDCPExpert::_setConditionalRetentionEnable(bool)`
- `PostErrorDPTXNoVideo`
- `role`
- `virtual IOReturn DCPEndpointV2::setPowerState(unsigned long, IOService *)`
- `support-standalone`
- `\"%s missing pmgr scratch values\\n\" @%s:%d`
- `dcpexpert-service`
- `\"%s timeout Reg offset 0x%x (status & 0x%08x) %s 0x%08x\\n\" @%s:%d`
- `pmgr-scratch-value-on`
- `v60@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `crcMismatches`
- `DCPEXT1`
- `121111121222121212222222222222222222222222222222222222222211212121111112112221212211221112222111111221222222222222222222222222222222222222222222221111221111212122211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211122111221112211`
- `require-pmgr-scratch`
- `require-conditional-retention`

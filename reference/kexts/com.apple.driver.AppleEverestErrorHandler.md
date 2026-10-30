# `com.apple.driver.AppleEverestErrorHandler`

- Name: AppleEverestErrorHandler
- Version: `1`
- UUID: `E4717057-05D5-3232-9CC8-CF46A7EB7DE7`
- Source version: `54.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleARM64ErrorHandler
- `CFBundleIdentifier`: `com.apple.driver.AppleEverestErrorHandler`
- `IOClass`: `AppleARM64ErrorHandler`
- `IONameMatch`: `cpu-error-handler,everest`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEverestErrorHandler`
- `IOPlatformActiveAction`: `88000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleARM64ErrorHandler` | 0x38 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001497 off=0x00464540-0x004659d7 addr=0xfffffe0007468540-0xfffffe00074699d7 r--/r--   __TEXT            
	sz=0x00000ebf off=0x00464b18-0x004659d7 addr=0xfffffe0007468b18-0xfffffe00074699d7               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001038 off=0x01ca2980-0x01ca39b8 addr=0xfffffe0008ca6980-0xfffffe0008ca79b8 r-x/r-x   __TEXT_EXEC       
	sz=0x00000f58 off=0x01ca2980-0x01ca38d8 addr=0xfffffe0008ca6980-0xfffffe0008ca78d8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000e0 off=0x01ca38d8-0x01ca39b8 addr=0xfffffe0008ca78d8-0xfffffe0008ca79b8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000101 off=0x04940ea0-0x04940fa1 addr=0xfffffe000b944ea0-0xfffffe000b944fa1 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04940ea0-0x04940f68 addr=0xfffffe000b944ea0-0xfffffe000b944f68               __DATA.__data             
	sz=0x00000039 off=0x00000000-0x00000039 addr=0xfffffe000b944f68-0xfffffe000b944fa1               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000009a0 off=0x01097a38-0x010983d8 addr=0xfffffe000809ba38-0xfffffe000809c3d8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01097a38-0x01097a40 addr=0xfffffe000809ba38-0xfffffe000809ba40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01097a40-0x01097a48 addr=0xfffffe000809ba40-0xfffffe000809ba48         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000008c0 off=0x01097a48-0x01098308 addr=0xfffffe000809ba48-0xfffffe000809c308         __DATA_CONST.__const            
	sz=0x00000040 off=0x01098308-0x01098348 addr=0xfffffe000809c308-0xfffffe000809c348         __DATA_CONST.__kalloc_type      
	sz=0x00000070 off=0x01098348-0x010983b8 addr=0xfffffe000809c348-0xfffffe000809c3b8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x010983b8-0x010983d8 addr=0xfffffe000809c3b8-0xfffffe000809c3d8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 32 at 0x04ad98b0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E4717057-05D5-3232-9CC8-CF46A7EB7DE7
008: LC_SOURCE_VERSION           54.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f9b0 size=0x38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEverestErrorHandler`
- `CFBundleIdentifier`: `com.apple.driver.AppleEverestErrorHandler`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEverestErrorHandler`
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
- `NSHumanReadableCopyright`: `Copyright © 2012-2020 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEverestErrorHandler.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901193408`
- `_PrelinkExecutableRelativePath`: `AppleEverestErrorHandler`
- `_PrelinkExecutableSize`: `12144`
- `_PrelinkExecutableSourceAddr`: `-2198901193408`
- `_PrelinkKmodInfo`: `-2198828986720`

## Strings (117) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `acc_cifl2c_cmd_rd_st_up`
- `acc_biuafi_cmd_cpbkrsp_d`
- `IODeviceTree:/defaults`
- `l2c_prb_cmd_l1wb`
- `acc_biuafi_cmd_fills`
- `L1C I-side data parity`
- `DPC Error thrtl unsafe`
- `acc_biuafi_cmd_ccleaninv`
- `acc_biuafi_cmd_ncwrrsp_ro`
- `Multi-hit Error in L2-TLB(for D-side accesses)`
- `site.AppleARM64ErrorHandler`
- `ErrDet_Addr: VA=%#llx`
- `acc_cifl2c_cmd_rd_pli`
- `l2c_prb_cmd_ramzero`
- `acc_biuafi_cmd_ncrdincrrsp_do`
- `1211112`
- `Multi-hit Error in L1-dTLB-LargerPage-SideArray (for D-side accesses)`
- `acc_biuafi_cmd_datav`
- `acc_biuafi_cmd_acki`
- `\"LLC %s error: FAR=%#lx LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx way=0x%x syndrome=%#x%s\" @%s:%d`
- `\"MMU err (%s%s) on %c-core: FAR=%#lx MMU_ERR_STS=%#llx way=%#x set=%#x\" @%s:%d`
- `acc_biuafi_cmd_fillm`
- `\"LLC %s error: FAR=%#lx LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx way=%#x syndrome=%#x%s\" @%s:%d`
- `A PIO-read/write attempts to a locked system-register`
- `All CPU-Cores are in powered-down state, but AMX has a valid context`
- `acc_cifl2c_cmd_rd_ld_m`
- `acc_cifl2c_cmd_rd_ld_m_pre`
- `Multi-hit Error in TWC or S2TLB(for D-side accesses, recorded by MMU)`
- `AppleARM64ErrorHandler: will %spanic on correctible ECC errors\n`
- ` (addr map hole/size mis-match)`
- `l2c_prb_cmd_flush`
- `acc_biuafi_cmd_ncwrincr_do`
- `acc_biuafi_cmd_cwrbk_d`
- `acc_biuafi_cmd_ctoe`
- `L1 I-TLB main array multi-hit`
- `acc_cifl2c_cmd_rd_ld`
- `cpu%d`
- `DPC Error mtraccess lock`
- `acc_cifl2c_cmd_dczva`
- `acc_biuafi_cmd_crd`
- `acc_biuafi_cmd_ctoecond`
- `acc_biuafi_cmd_fillp`
- `acc_biuafi_cmd_cpfws`
- `way predictor`
- `single-bit ECC`
- `\"FED err (%s) on %c-core: FAR=%#lx FED_ERR_STS=%#llx MMU_ERR_STS=%#llx %s\" @%s:%d`
- `acc_biuafi_cmd_crds`
- `L2 mTLB I-side multi-hit`
- `acc_biuafi_cmd_ncwrrsp_do`
- `acc_biuafi_cmd_ctoifw`
- `snoop`
- `\"LLC %s multi-hit error: FAR=%#lx LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx way_mask=%#x\" @%s:%d`
- `double-bit ECC`
- `\"Unhandled %c-core error: \" \"LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx \" \"LSU_ERR_STS(P/E)=%#llx/%#llx \" \"FED_ERR_STS(P/E)=%#llx/%#llx \" \"MMU_ERR_STS(P/E)=%#llx/%#llx \" \"DPC_ERR_STS=(P/E)=%#llx/%#llx\" @%s:%d`
- `DPC Error incpl epoch`
- `acc_cifl2c_cmd_rd_st_cond`
- `acc_biuafi_cmd_pullv`
- `acc_biuafi_cmd_acke`
- `acc_biuafi_cmd_ctoibk`
- `\"LLC %s error%s from %s: FAR=%#lx LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx addr=%#llx cmd=%#x(%s)\" @%s:%d`
- `DPC Error lose lock`
- `l2c_prb_cmd_pullv`
- `acc_biuafi_cmd_cpbknc`
- `single-bit ECC overflow`
- `\"LLC %s error: FAR=%#lx LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx\" @%s:%d`
- `DPC Error time backward`
- `PIO`
- `Bus`
- `\"LSU err (%s) on %c-core: FAR=%#lx LSU_ERR_STS=%#llx MMU_ERR_STS=%#llx addr=%#llx\" @%s:%d`
- `acc_biuafi_cmd_bzero_ro`
- `acc_biuafi_cmd_cmaint`
- `acc_biuafi_cmd_fille`
- ` (bad mask)`
- ` (bad cmd)`
- `uncorrectible overflow`
- `acc_biuafi_cmd_ncrdincr_ro`
- `acc_biuafi_cmd_ackirsp_d`
- `acc_biuafi_cmd_ackm`
- `AppleEverestErrorHandler.cpp`
- `acc_biuafi_cmd_cpfwi`
- `Multi-hit Error in L1-dTLB-16KPage-MainArray (for D-side accesses)`
- `acc_cifl2c_cmd_rd_mmu`
- `acc_biuafi_cmd_crde`
- `acc_biuafi_cmd_cpbkrsp_c`
- `acc_biuafi_cmd_ncrdincrrsp_ro`
- `Multi-hit Error in L2-TLB(for I-side accesses, recorded by MMU)`
- `Multi-hit Error in TWC or S2TLB(for I-side accesses, recorded by MMU)`
- `acc_cifl2c_cmd_mnt_op`
- `acc_biuafi_cmd_cwrbk_c`
- `acc_biuafi_cmd_cpbki`
- `not `
- `\"DPC err (%s%s) on %c-core: FAR=%#lx DPC_ERR_STS=%#llx\" @%s:%d`
- `acc_biuafi_cmd_ackop`
- `\"LLC dup tag multi-hit error by CPU %d: FAR=%#lx LLC_ERR_STS/ADR/INF=%#llx/%#llx/%#llx way_mask=%#x\" @%s:%d`
- `acc_biuafi_cmd_nop`
- `acc_biuafi_cmd_cdrop`
- `acc_biuafi_cmd_fillo`
- `\"DPC err (%s%s) on %c-core: FAR=%#lx DPC_ERR_STS=%#llx ErrDet_Info=%#llx\" @%s:%d`
- `L1 I-TLB side array multi-hit`
- `acc_cifl2c_cmd_sw_op`
- `acc_biuafi_cmd_ncwrincr_ro`
- `L2 RAM addr out of range`
- `:multiple`
- `acc_cifl2c_cmd_mva_op`
- `acc_cifl2c_cmd_ncwr`
- `way=%#x set=%#x`
- `acc_cifl2c_cmd_rd_ld_pre`
- `acc_biuafi_cmd_ackirsp_c`
- `l2-ecc-correctable-panic`
- `UNKNOWN`
- `acc_biuafi_cmd_ncrdincr_do`
- `AppleARM64ErrorHandler`
- `tag`
- `acc_cifl2c_cmd_rd_istrm`
- `acc_biuafi_cmd_cpbks`
- ` (bad size)`
- `Multi-hit Error in mTLB(for D-side accesses, recorded by MMU)`

# `com.apple.driver.AppleInterruptControllerV3`

- Name: AppleInterruptControllerV3
- Version: `1.0.0d1`
- UUID: `28C69E63-FC42-3C7D-9F4C-797589D9AF36`
- Source version: `102.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aic`](../devicetree/root__arm-io__aic.md) | `AppleInterruptControllerV3` | `aic,3` |

## IOKit personalities (1) [KC]

### AppleInterruptControllerV3
- `CFBundleIdentifier`: `com.apple.driver.AppleInterruptControllerV3`
- `IOClass`: `AppleInterruptControllerV3`
- `IONameMatch`: `aic,3`
- `IOPersonalityPublisher`: `com.apple.driver.AppleInterruptControllerV3`
- `IOPlatformActiveAction`: `97000`
- `IOPlatformQuiesceAction`: `97000`
- `IOProviderClass`: `AppleARMIODevice`
- `IOUserClientClass`: `AppleInterruptControllerUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AICInterruptTimestampFunction` | 0x38 | AppleARMFunctionEventTimestamp → AppleARMFunction |
| `AppleInterruptControllerUserClient` | 0xf0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AppleInterruptControllerV3` | 0x4e8 | IOInterruptController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000119d off=0x0053d260-0x0053e3fd addr=0xfffffe0007541260-0xfffffe00075423fd r--/r--   __TEXT            
	sz=0x00000b75 off=0x0053d888-0x0053e3fd addr=0xfffffe0007541888-0xfffffe00075423fd               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000043b0 off=0x02063ec0-0x02068270 addr=0xfffffe0009067ec0-0xfffffe000906c270 r-x/r-x   __TEXT_EXEC       
	sz=0x00004140 off=0x02063ec0-0x02068000 addr=0xfffffe0009067ec0-0xfffffe000906c000          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000270 off=0x02068000-0x02068270 addr=0xfffffe000906c000-0xfffffe000906c270          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x0494e780-0x0494e8d0 addr=0xfffffe000b952780-0xfffffe000b9528d0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0494e780-0x0494e848 addr=0xfffffe000b952780-0xfffffe000b952848               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b952848-0xfffffe000b9528d0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000012f8 off=0x011270c0-0x011283b8 addr=0xfffffe000812b0c0-0xfffffe000812c3b8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x011270c0-0x011270d0 addr=0xfffffe000812b0c0-0xfffffe000812b0d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x011270d0-0x011270e0 addr=0xfffffe000812b0d0-0xfffffe000812b0e0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000fd8 off=0x011270e0-0x011280b8 addr=0xfffffe000812b0e0-0xfffffe000812c0b8         __DATA_CONST.__const            
	sz=0x000000c0 off=0x011280b8-0x01128178 addr=0xfffffe000812c0b8-0xfffffe000812c178         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x01128178-0x01128218 addr=0xfffffe000812c178-0xfffffe000812c218         __DATA_CONST.__kalloc_var       
	sz=0x00000138 off=0x01128218-0x01128350 addr=0xfffffe000812c218-0xfffffe000812c350         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x01128350-0x011283b8 addr=0xfffffe000812c350-0xfffffe000812c3b8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 91 at 0x04adde10
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     28C69E63-FC42-3C7D-9F4C-797589D9AF36
008: LC_SOURCE_VERSION           102.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa6070 size=0xa0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleInterruptControllerV3`
- `CFBundleGetInfoString`: `Copyright © 2009-2019 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleInterruptControllerV3`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleInterruptControllerV3`
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
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleInterruptControllerV3.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900305312`
- `_PrelinkExecutableRelativePath`: `AppleInterruptControllerV3`
- `_PrelinkExecutableSize`: `27029`
- `_PrelinkExecutableSourceAddr`: `-2198900305312`
- `_PrelinkKmodInfo`: `-2198828931200`

## Strings (72) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `cap0-offset`
- `pubstampstride-mask`
- `\"Interrupt storm: last int %d total int fired %lld times, iack=%x, vector=%p,storm_debug=%p, index=%lld\" @%s:%d`
- `121111121222121211111111111112`
- `\"Couldnt find aic-iack-offset device tree property\" @%s:%d`
- `AppleInterruptControllerV3::start: _aicRevision = %d _aicBaseAddress = %p _aicNumVectors = 0x%08x Num Shared Timestamps = %u \n`
- `\"AppleInterruptControllerV3::handleInterrupt: unexpected vectorType: 0x%08x, IACK=0x%08x\" @%s:%d`
- `#main-cpus`
- `\"Interrupt vector %p (%u) changed preemption level from %d to %d\" @%s:%d`
- `\"Invalid interrupt number %d\" @%s:%d`
- `\"AIC writing register after quiesce offset = 0x%08x value = 0x%08x\\n\" @%s:%d`
- `site.IOInterruptVector`
- `21121111`
- `#shared-timestamps`
- `aicglbcfg-offset`
- `\"Length of the devicetree property (%s) is unexpected (expected : %d byte , result: %d byte\" @%s:%d`
- `\"_aicIackOffset (0x%llx) > _aicMemoryMapLength (0x%llx)\" @%s:%d`
- `\"Unsupported max die count _aicMaxDies(%d) > MAX_DIES(%d)\" @%s:%d`
- `AppleInterruptControllerV3::startInterruptTimestamping: Timestamp already enabled for requested interrupt\n`
- `\"AppleInterruptControllerV3::startInterruptTimestamping: invalid config: 0x%08x\" @%s:%d`
- `\"AIC reading register after quiesce offset = 0x%08x\\n\" @%s:%d`
- `pubstamplo0-offset`
- `extint-baseaddress`
- `aic-numdies-per-die`
- `aic-iack-offset`
- `site.AppleInterruptControllerV3`
- `\"Invalid vector number %d max %d\" @%s:%d`
- `\"AppleInterruptControllerV3::getTimestamp: invalid config: 0x%08x\" @%s:%d`
- `\"_aicNumDies is not defined in DT\\n\" @%s:%d`
- `intmaskclear-stride`
- `pubstampcfg0inttype-mask`
- `aic-numdies`
- `\"_aicExternalInterruptMap[i].irq_num (%d) > _aicNumVectors (%d)\" @%s:%d`
- `hwintmon-stride`
- `aic-soc-offset-stride`
- `\"Not able to get Device Memory map\\n\" @%s:%d`
- `\"AppleInterruptControllerV3::stopInterruptTimestamping: invalid config: 0x%08x\" @%s:%d`
- `aic-rev`
- `IOUserClientDefaultLockingSetProperties`
- `IOUserClientEntitlements`
- `pubstampcfg0-offset`
- `1211111212221212111111222222222222222222222111111111112221121111111212121212122111211211211211211211211211211211211211211211211211211211211211211211211211211`
- `AppleInterruptControllerV3.cpp`
- `\"_aicExternalInterruptMapCount (%zu) > _aicNumVectors (%d)\" @%s:%d`
- `site.AICInterruptTimestampFunction`
- `extintrcfg-stride`
- `max_irq_interrupt_umask`
- `AICInterruptTimestampFunction`
- `AppleInterruptControllerUserClient`
- `rev-offset`
- `aic-die-offset-stride`
- `InterruptControllerName`
- `aic-ext-intr-cfg`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `maxnumirq-offset`
- `cap0_max_interrupt_umask`
- `\"_aicNumDies and _aicNumDiesPerDie are not defined in DT\\n\" @%s:%d`
- `vector number out of range.\n`
- `site.AICTimestampObject`
- `Restore AIC settings during Wake\n`
- `site.AppleInterruptControllerUserClient`
- `IOUserClientDefaultLocking`
- `pubstampdcfg0en-mask`
- `max-extint-num`
- `sleep-unmasked-interrupts`
- `112`
- `AppleInterruptControllerV3::_aicPlatformQuiesceActions: Unmask %u interrupts required in SLP_MEDIA\n`
- `com.apple.private.appleaic.user-access`
- `intmaskset-stride`
- `pubstampdhi-offset`
- `AppleInterruptControllerV3`
- `1211112`

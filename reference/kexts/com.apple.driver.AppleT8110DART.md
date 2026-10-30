# `com.apple.driver.AppleT8110DART`

- Name: AppleT8110DART
- Version: `1`
- UUID: `11C74070-70AA-37F2-83F4-ED9C2BD07FBE`
- Source version: `501.40.4.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.IODARTFamily`](com.apple.driver.IODARTFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.4.1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.4.1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.4.1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (23) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/dart-sep`](../devicetree/root__arm-io__dart-sep.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-sio`](../devicetree/root__arm-io__dart-sio.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-sbr`](../devicetree/root__arm-io__dart-sbr.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-usb0`](../devicetree/root__arm-io__dart-usb0.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dcp`](../devicetree/root__arm-io__dart-dcp.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-disp0`](../devicetree/root__arm-io__dart-disp0.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dispgrt`](../devicetree/root__arm-io__dart-dispgrt.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-disp0-isoc`](../devicetree/root__arm-io__dart-disp0-isoc.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dcpsec`](../devicetree/root__arm-io__dart-dcpsec.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dispsec`](../devicetree/root__arm-io__dart-dispsec.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dispsecgrt`](../devicetree/root__arm-io__dart-dispsecgrt.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dcpext0`](../devicetree/root__arm-io__dart-dcpext0.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dispext0`](../devicetree/root__arm-io__dart-dispext0.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-dispext0-isoc`](../devicetree/root__arm-io__dart-dispext0-isoc.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-scaler`](../devicetree/root__arm-io__dart-scaler.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-jpeg`](../devicetree/root__arm-io__dart-jpeg.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-isp`](../devicetree/root__arm-io__dart-isp.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-ave`](../devicetree/root__arm-io__dart-ave.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-avd`](../devicetree/root__arm-io__dart-avd.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-ane0`](../devicetree/root__arm-io__dart-ane0.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-ane1`](../devicetree/root__arm-io__dart-ane1.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `AppleT8110DART` | `dart,t8110` |
| [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `AppleT8110DART` | `dart,t8110` |

## IOKit personalities (1) [KC]

### AppleT8110DART
- `CFBundleIdentifier`: `com.apple.driver.AppleT8110DART`
- `IOClass`: `AppleT8110DART`
- `IONameMatch`: `dart,t8110`
- `IOPersonalityPublisher`: `com.apple.driver.AppleT8110DART`
- `IOPlatformActiveAction`: `80000`
- `IOPlatformSleepAction`: `80000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleT8110DART` | 0x1978 | IODART → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00003093 off=0x0079ffb0-0x007a3043 addr=0xfffffe00077a3fb0-0xfffffe00077a7043 r--/r--   __TEXT            
	sz=0x00000060 off=0x007a0680-0x007a06e0 addr=0xfffffe00077a4680-0xfffffe00077a46e0               __TEXT.__const            
	sz=0x00002963 off=0x007a06e0-0x007a3043 addr=0xfffffe00077a46e0-0xfffffe00077a7043               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000101fc off=0x027912f0-0x027a14ec addr=0xfffffe00097952f0-0xfffffe00097a54ec r-x/r-x   __TEXT_EXEC       
	sz=0x0000feac off=0x027912f0-0x027a119c addr=0xfffffe00097952f0-0xfffffe00097a519c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000350 off=0x027a119c-0x027a14ec addr=0xfffffe00097a519c-0xfffffe00097a54ec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000148 off=0x049a1aa0-0x049a1be8 addr=0xfffffe000b9a5aa0-0xfffffe000b9a5be8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049a1aa0-0x049a1b68 addr=0xfffffe000b9a5aa0-0xfffffe000b9a5b68               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9a5b68-0xfffffe000b9a5ba0               __DATA.__common           (Zerofill)
	sz=0x00000048 off=0x00000000-0x00000048 addr=0xfffffe000b9a5ba0-0xfffffe000b9a5be8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001058 off=0x01239258-0x0123a2b0 addr=0xfffffe000823d258-0xfffffe000823e2b0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01239258-0x01239260 addr=0xfffffe000823d258-0xfffffe000823d260         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01239260-0x01239268 addr=0xfffffe000823d260-0xfffffe000823d268         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000790 off=0x01239268-0x012399f8 addr=0xfffffe000823d268-0xfffffe000823d9f8         __DATA_CONST.__const            
	sz=0x000002c0 off=0x012399f8-0x01239cb8 addr=0xfffffe000823d9f8-0xfffffe000823dcb8         __DATA_CONST.__kalloc_type      
	sz=0x00000410 off=0x01239cb8-0x0123a0c8 addr=0xfffffe000823dcb8-0xfffffe000823e0c8         __DATA_CONST.__kalloc_var       
	sz=0x000001a8 off=0x0123a0c8-0x0123a270 addr=0xfffffe000823e0c8-0xfffffe000823e270         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x0123a270-0x0123a2b0 addr=0xfffffe000823e270-0xfffffe000823e2b0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 114 at 0x04ae7de0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     11C74070-70AA-37F2-83F4-ED9C2BD07FBE
008: LC_SOURCE_VERSION           501.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab3800 size=0xf0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleT8110DART`
- `CFBundleIdentifier`: `com.apple.driver.AppleT8110DART`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleT8110DART`
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
- `NSHumanReadableCopyright`: `Copyright © 2019-2021 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleT8110DART.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897803344`
- `_PrelinkExecutableRelativePath`: `AppleT8110DART`
- `_PrelinkExecutableSize`: `82991`
- `_PrelinkExecutableSourceAddr`: `-2198897803344`
- `_PrelinkKmodInfo`: `-2198828590432`

## Strings (235) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"%s: translation not permitted for %s SID (%d)\" @%s:%d`
- `(%s) %s:%u: VERIFY failed`
- `\"%s (%p): Secondary exception DART instance %u %sSID %d\" @%s:%d`
- `sid`
- `dapf-instance-%d`
- `retention-force-quiesce`
- `STTMismatch`
- `PSWRDIS`
- `CTE invalid`
- `*UNKNOWN*`
- `allow-dram-apf-slices-%d`
- `real-time`
- `2112`
- `\"%s: Per-SID vm-base/vm-size override not supported for this class of DART\" @%s:%d`
- `no active exception`
- `\"%s: Missing '%s' property\" @%s:%d`
- `site.exceptionInfo_t`
- `\"%s[%d]: access region protection is incorrectly configured: EDT config: 0x%x Hardware config: 0x%x\" @%s:%d`
- `\"%s: max %s instances exceeded\" @%s:%d`
- `site.IODART::capability_t`
- `trans-idle-timeout`
- `\"%s (%p): Segment table changed: md %p page %#x segmentRefs[%#llx] %p totalSegs %#x pthandle expected %p actual %p\" @%s:%d`
- `/AppleT8110DART.cpp`
- `\"%s: failed to unregister mapper %p SID 0x%x: 0x%08x\" @%s:%d`
- `site.apfCapturedState_t`
- `/AppleT8110DART.h`
- `InvalidCTE`
- `TTBR invalid`
- `\"%s (%p): %s %s Exclave SID exception%s SID %d ERROR_SID_SUMMARY 0x%08x ERROR_ADDRESS 0x%016llx%s\" @%s:%d`
- `(%s) %s::%s: WARNING: %s gapf %x instance %s[%u] clock protection %s enabled\n`
- `instance`
- `retention`
- `max-sids-in-mismatch`
- `GAPF`
- `site.t8110dart_apf_slice`
- `bypassed`
- `(%s) %s::%s: SMMU state capture %p\n`
- `site.smmuCapturedState_t`
- `\"%s: Obsolete 'sids', 'bypass', and/or 'bypass-address' properties present\" @%s:%d`
- `SecondaryError`
- `(%s) %s::%s: DART interrupt while disabled by the client\n`
- `_prepareForPowerDown`
- `bypass-address`
- ` after shutdown`
- `(%s) %s::%s: DART(%s) return from _handleFatalException after shutdown: interruptState %p\n`
- `(%s) %s::%s: Full state capture log option ignored -- requires lock-on-error\n`
- `122212`
- `dart-ps-wr-dis-entries`
- `region protect`
- `\"%s: end(%#llx) < start(%#llx) for slice %d instance %u\" @%s:%d`
- `pio-vm-base`
- `\"%s requires %s\" @%s:%d`
- `dart-id`
- `site.t8110dart_sid_init_data`
- `\"%s (%p): Invalid page sid %d atOffset %#x pageCount %#x refCount %p type %d\" @%s:%d`
- `dram-base`
- `flush-by-dva`
- `%s (%p): %s(%s) error: SID %u %s exception%s on %s of DVA %#llx (%sSEG %#x PTE %#x) ERROR_STATUS 0x%08x TIME %#llx TTE %#llx AXI_ID %#x`
- `\"%s: PIO mapping is not supported by this class of DART\" @%s:%d`
- ` (no exceptionInfo)`
- `\"%s: missing '%s' property\" @%s:%d`
- `\"%s[%d]: page size is incorrectly configured: config %#x actual %#x\" @%s:%d`
- `InvalidTTBR`
- `PTE invalid`
- `AppleT8110DART`
- `121111121222121211122112111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222`
- `\"%s: SID %u has been remapped -> %u\" @%s:%d`
- `\"%s (%p): _forceAvailable not supported\" @%s:%d`
- `BPFReject`
- `_fatalExceptionPreGen2_2`
- `fill region`
- `\"%s (%p): transaction idle timeout idlePorts=%d/%d idleInstances=%d/%d\" @%s:%d`
- `sid-ocla`
- `21`
- `secondary`
- `_fatalException`
- `DAPF`
- `\"%s (%p): %s(%s) error: secondary exception ERROR_STATUS 0x%08x ERR_SECONDARY %08x %08x %08x %08x %08x %08x %08x %08x\" @%s:%d`
- `vm-base`
- `not`
- `reg`
- ` when unavailable`
- `bypass`
- `_handleInterrupt`
- `site.uint32_t`
- `read protect`
- `_handleFatalExceptionPreGen2_2`
- `_secondaryException`
- `STT mismatch`
- `site.dartCapturedState_t`
- `site.smmuSTTData_t`
- `\"%s requires %s and is mutually exclusive with %s\" @%s:%d`
- `CTRR write protect`
- `(%s) %s::%s: %s (%p): Secondary exception DART instance %u %sSID %d\n`
- `(%s) %s::%s: APF state capture %p\n`
- `WriteProtect`
- `AXIError`
- `vm-offset`
- `22222223312322`
- `InterfaceTest`
- `\"%s: Per-SID vm-base/vm-size override may increase VM limits\" @%s:%d`
- `tz`
- `\"%s (%p): %s %s exception%s SID %d ERROR_SID_SUMMARY 0x%08x ERROR_ADDRESS 0x%016llx%s\" @%s:%d`
- `exclave-sid`
- `filter-data-instance-%d`
- `AXIDecode`
- `(%s) %s::%s: %s (%p): %s %s exception%s ERROR_STATUS 0x%08x ERROR_ADDRESS 0x%016llx\n`
- `inclusive-tz-range`
- `allow-pte-remap`
- `Unknown`
- `read`
- `\"%s (%p): Instance %d SID %d TTBR (0x%08x) PA 0x%016llx != expected PA 0x%016llx\" @%s:%d`
- `sid-mcw`
- `(%s) %s::%s: Spurious DART/SMMU interrupt: interrupt index %d\n`
- `vm-alignment`
- `dart-tunables-instance-%d`
- `_dartInitializeStateCapture`
- `start`
- `sids`
- `ioa-parent`
- `APF reject`
- `ipce-hw-retention`
- `CTE %#x `
- `BPF reject`
- `site.IODART::ptRef`
- `InvalidSTE`
- `\"%s (%p): Chunk table changed: md %p page %#x chunkRefs[%#llx] %p pthandle expected %p actual %p\" @%s:%d`
- `\"%s (%p): Instance %d is not locked\" @%s:%d`
- `dual-vc-llt-workaround-%d`
- `RegionProtect`
- `CTRRProtect`
- `PIOGW`
- `\"%s: invalid instance type: 0x%08x\" @%s:%d`
- `1`
- `\"%s (%p): pmap_iommu_iovmalloc status %#x sid %d atOffset %#x pageCount %#x refCount %p type %d\" @%s:%d`
- `pio-vm-size`
- `Gen1_0`
- `IllegalSID`
- `drop protect`
- `DARTHwException`
- `Ignored %s\n`
- `remap`
- `(%s) %s::%s: DART(%s) perf interrupt asserted after shutdown 0x%08x\n`
- `(%s) %s::%s: DART state capture %p\n`
- `site.AppleT8110DART`
- `allow-apf-sid-remap`
- `FillRegionError`
- `\"%s (%p): Instance %d SID %d TTBR (0x%08x) is not valid\" @%s:%d`
- `source`
- `222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222`
- `site.dartSetWayTagPA`
- `\"%s\" @%s:%d`
- `_interruptAction`
- `(%s) %s::%s: TLIMITs clamped. Client reset required!\n`
- `\"%s gapf %x instance %s[%u] clock protection %s enabled\" @%s:%d`
- `AXI decode`
- `\"%s (%p): %s %s SID exception%s SID %d ERROR_SID_SUMMARY 0x%08x ERROR_ADDRESS 0x%016llx%s\" @%s:%d`
- `site.mapperData_t`
- `%s-%d`
- `no `
- `sid-count`
- `dart-ungang-shared-ps`
- `STE invalid`
- `exclave-sids-only`
- `\"%s: failed to create dynamic SID %u for mapper %p: 0x%x\" @%s:%d`
- `IODeviceTree:/chosen`
- `DropProtect`
- `APFReject`
- `destination`
- `_gapfAssertState`
- `(%s) %s::%s: %s (%p): %s %s SID exception%s ERROR_SID_SUMMARY 0x%08x ERROR_ADDRESS 0x%016llx\n`
- `\"%s: dual-vc-llt-workaround requires an APF configuration\" @%s:%d`
- `%s (%p): %s(%s) error: SID %u %s exception%s on %s of DVA %#llx (%sSEG %#x PTE %#x) ERROR_SID_SUMMARY 0x%08x TIME %#llx TTE %#llx AXI_ID %#x`
- `vm-size`
- `_apfInitializeStateCapture`
- `dart-clock-protection`
- `InvalidPTE`
- `Illegal SID`
- `(%s) %s::%s: %s (%p): %s(%s) error: secondary exception ERROR_STATUS 0x%08x ERR_SECONDARY %08x %08x %08x %08x %08x %08x %08x %08x\n`
- `(%s) %s::%s: DART interrupt while dirty shutdown is in progress\n`
- `clock-protection-slice-index`
- `noncompliant-dead-mappings`
- `\"%s: Reserved DVA range %u [0x%016llx..0x%016llx) overlaps with range %u [0x%016llx..0x%016llx)\" @%s:%d`
- `%s (%p): %s(%s) error: SID %u %s exception%s on %s of address %#llx`
- `\"%s (%p): Secondary exception on instance %u SID %d while handling instance %u SID %u %s error 0x%08x DVA %#llx (%sSEG %#x PTE %#x) TIME %#llx\" @%s:%d`
- `STTAccessFlush`
- `ExternalException`
- `\"%s (%p): %s %s exception%s SID %d ERROR_STATUS 0x%08x ERROR_ADDRESS 0x%016llx%s\" @%s:%d`
- `DART`
- `no-sleep`
- `\"%s and %s are mutually exclusive\" @%s:%d`
- `sid-trace`
- `222222222222212122`
- `interrupts`
- `(%s) %s:%u: REQUIRE failed`
- `tz-disabled`
- `exclave`
- `enable-perf-counters`
- `Gen2_0`
- `\"%s: Duplicate SID %u\" @%s:%d`
- `\"%s: '%s' property not supported -- use dapf-instance-%d\" @%s:%d`
- `\"%s: quiescing without valid saved state\" @%s:%d`
- `external`
- `unknown`
- `\"%s (%p): Max spurious DART interrupts: interrupt index %d\" @%s:%d`
- `AXI error`
- `apf-bypass`
- `always-on`
- `SMMUHwException`
- `ReadProtect`
- `invalid `
- `\"%s: Unsupported DART version %x\" @%s:%d`
- `_smmuInitializeStateCapture`
- `pio-granularity`
- `\"%s: unexpected unregister request for mapper %p SID 0x%x\" @%s:%d`
- `clamp-tlimits`
- `ignore-sid-count-mismatch`
- `AppleT8110DART.cpp`
- `ignore-secondary`
- `write protect`
- `(%s) %s::%s: %s (%p): Secondary exception on instance %u SID %d while handling instance %u SID %u %s error 0x%08x DVA %#llx (%sSEG %#x PTE %#x) TIME %#llx\n`
- `write`
- `_interruptHandlerPreGen2_2`
- `STT flush`
- `\"%s: dual VC LLT limit %d is invalid: [%#llx,%#llx]\" @%s:%d`
- `protection-granularity`
- `allow-vm-reserve-mapping`
- `\"%s[%d]: full bypass mode not supported and bypass-%d property does not specify a bypass address\" @%s:%d`
- `_dartPrepareForPowerDown`
- `SMMU`
- `allow-mixed-bypass-mode`
- `\"%s: Remap %s SID %u already remapped to %u\" @%s:%d`
- `vm-reserve`
- `site.bool`
- `still`

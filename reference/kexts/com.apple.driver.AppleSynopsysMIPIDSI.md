# `com.apple.driver.AppleSynopsysMIPIDSI`

- Name: AppleSynopsysMIPIDSI
- Version: `1.0.0`
- UUID: `735F773D-A3F9-3303-8430-D9D86A61577D`
- Source version: `96.0.2.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleSynopsysMIPIDSIController
- `CFBundleIdentifier`: `com.apple.driver.AppleSynopsysMIPIDSI`
- `IOClass`: `AppleSynopsysMIPIDSIController`
- `IONameMatch`: `mipi-dsim-1,synopsys`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSynopsysMIPIDSI`
- `IOPlatformPanicAction`: `85000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSynopsysMIPIDSIController` | 0x65e0 | AppleARMMIPIDSIController → IOService → IORegistryEntry |
| `AppleSynopsysMIPIDSIFrameDoneFunction` | 0x30 | AppleARMFunction |
| `AppleSynopsysMIPIDSIProgramPartialFrameFunction` | 0x30 | AppleARMFunction |
| `AppleSynopsysMIPIDSIResetClockFunction` | 0x30 | AppleARMFunction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002d72 off=0x0079c7b0-0x0079f522 addr=0xfffffe00077a07b0-0xfffffe00077a3522 r--/r--   __TEXT            
	sz=0x00000010 off=0x0079ce28-0x0079ce38 addr=0xfffffe00077a0e28-0xfffffe00077a0e38               __TEXT.__const            
	sz=0x000026ea off=0x0079ce38-0x0079f522 addr=0xfffffe00077a0e38-0xfffffe00077a3522               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00008c10 off=0x02786e90-0x0278faa0 addr=0xfffffe000978ae90-0xfffffe0009793aa0 r-x/r-x   __TEXT_EXEC       
	sz=0x000088f0 off=0x02786e90-0x0278f780 addr=0xfffffe000978ae90-0xfffffe0009793780          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000320 off=0x0278f780-0x0278faa0 addr=0xfffffe0009793780-0xfffffe0009793aa0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000178 off=0x049a1800-0x049a1978 addr=0xfffffe000b9a5800-0xfffffe000b9a5978 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049a1800-0x049a18c8 addr=0xfffffe000b9a5800-0xfffffe000b9a58c8               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b9a58c8-0xfffffe000b9a5978               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001248 off=0x01237180-0x012383c8 addr=0xfffffe000823b180-0xfffffe000823c3c8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01237180-0x01237188 addr=0xfffffe000823b180-0xfffffe000823b188         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01237188-0x01237190 addr=0xfffffe000823b188-0xfffffe000823b190         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000a00 off=0x01237190-0x01237b90 addr=0xfffffe000823b190-0xfffffe000823bb90         __DATA_CONST.__const            
	sz=0x00000100 off=0x01237b90-0x01237c90 addr=0xfffffe000823bb90-0xfffffe000823bc90         __DATA_CONST.__kalloc_type      
	sz=0x00000550 off=0x01237c90-0x012381e0 addr=0xfffffe000823bc90-0xfffffe000823c1e0         __DATA_CONST.__kalloc_var       
	sz=0x00000190 off=0x012381e0-0x01238370 addr=0xfffffe000823c1e0-0xfffffe000823c370         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000058 off=0x01238370-0x012383c8 addr=0xfffffe000823c370-0xfffffe000823c3c8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 111 at 0x04ae7aa8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     735F773D-A3F9-3303-8430-D9D86A61577D
008: LC_SOURCE_VERSION           96.0.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab3670 size=0x128
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSynopsysMIPIDSI`
- `CFBundleIdentifier`: `com.apple.driver.AppleSynopsysMIPIDSI`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSynopsysMIPIDSI`
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
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSynopsysMIPIDSI.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897817680`
- `_PrelinkExecutableRelativePath`: `AppleSynopsysMIPIDSI`
- `_PrelinkExecutableSize`: `52546`
- `_PrelinkExecutableSourceAddr`: `-2198897817680`
- `_PrelinkKmodInfo`: `-2198828591104`

## Strings (150) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `121111`
- `AppleSynopsysMIPIDSIController::start Failed to get phy settings count\n`
- `mipi-support-lpm`
- `%s:%u: REQUIRE failed: %s  `
- `AppleSynopsysMIPIDSIController::start: Sad SAC enabled, switch between MIPI freq highest and lowest\n`
- `\"Inconsistent state _swmprEnabled %d, kSWMPR_ENABLE 0x%x \\n\" @%s:%d`
- `\"%s frequency list count (%d) does not match the number of elements (%d)\" @%s:%d`
- `site.AppleSynopsysMIPIDSIProgramPartialFrameFunction`
- `site.AppleSynopsysMIPIDSIFrameDoneFunction`
- `\"AppleSynopsysMIPIDSIController::_sacGenerateFrequencyList: failed to generate any valid frequencies\" @%s:%d`
- `display-timing`
- `IOReturn AppleSynopsysMIPIDSIController::sendSWMPRShortCommandGated(UInt8, UInt8, UInt8)`
- `IOReturn AppleSynopsysMIPIDSIController::sendShortCommandGated(UInt8, UInt8, UInt8)`
- `==`
- `\"_dsimSACDivisor == 0\\n\" @%s:%d`
- `%s panicOnError Enabled\n`
- `phy-test`
- `mipi-command`
- `\"AppleSynopsysMIPIDSIController:_leaveAPIFunction usage count < 0\" @%s:%d`
- `function-gpio`
- `invert-interrupt-mask`
- `mipi_dsim_read_long_command: timing out\n`
- `IOReturn AppleSynopsysMIPIDSIController::_enableDSIM(bool)`
- `sac-memory-index`
- `\"_dsimInterruptSources > MAX_MIPI_INTERRUPT_COUNT :: %d > %d\" @%s:%d`
- `AppleARMSlowAdaptiveClockingNoiseWidthList`
- `AppleSynopsysMIPIDSIProgramPartialFrameFunction`
- `AppleARMSlowAdaptiveClockingFrequencyIndex`
- `IOReturn AppleSynopsysMIPIDSIController::enableInterfaceGated(bool)`
- `IOReturn AppleSynopsysMIPIDSIController::receiveLongCommandGated(UInt8, UInt8 *, IOByteCount *)`
- `\"%s missing lpm SAC information\\n\" @%s:%d`
- `mipi-panic-on-error`
- `phy-test-num`
- `\"%s device with LPM doesn't support sac-range SAC\\n\" @%s:%d`
- `AppleARMSlowAdaptiveClockingFrequencyList`
- `\"AppleSynopsysMIPIDSIController::start: Failed to create the SAC thread\" @%s:%d`
- `dsimEnabled`
- `\"SWMPR FIFO not empty kSWMPR_MIPI_STATUS 0x%x, MipiRegWrFifoOccupancy 0x%x, Active %d/n\" @%s:%d`
- `\"SWMPR should be disabled but swmpr_state %d, _swmprEnabled %d\" @%s:%d`
- `mipi-version`
- `mipi-sac`
- `sac-range`
- `AppleARMSlowAdaptiveClockingFrequencyValid`
- `IOReturn AppleSynopsysMIPIDSIController::sendLongCommandGated(UInt8, const UInt8 *, IOByteCount)`
- `mipi: timing out\n`
- `121111121222121212112211111111111111112212221111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `sac-frequency-list`
- `IOReturn AppleSynopsysMIPIDSIController::enableVideoGated(bool)`
- `\"unlocked too many times _swmprUsageCount %d\\n\" @%s:%d`
- `sac-enable`
- `sac-frequency-list-lpm-count`
- `function-saca_lpm`
- `IOReturn AppleSynopsysMIPIDSIController::enableHighSpeedModeGated(bool)`
- `_swmprEnabled`
- `_dsimHSClockOn`
- `\"SWMPR memory map not defined on a device supporting SWMPR\" @%s:%d`
- `AppleSynopsysMIPIDSIController.cpp`
- `site.dsimSACAggressor_t`
- `\"AppleSynopsysMIPIDSIController::start Not enough information to enable SAC \" @%s:%d`
- `\"%s timeout Reg offset 0x%x (status & 0x%08x) %s 0x%08x\\n\" @%s:%d`
- `void AppleSynopsysMIPIDSIController::_sacGetFrequencyList(UInt32 *, sac_pll_t **, const char *, const char *)`
- `\"swmpr-memory-index not found on device supporting SWMPR\" @%s:%d`
- `_dsimSACModeCount >= 2`
- `timing`
- `_dsimMIPIVersion >= 5`
- `IOReturn AppleSynopsysMIPIDSIController::_enableSWMPRGated(bool)`
- `\"errors found : ST0 0x%lx ST1 0x%lx\" @%s:%d`
- `getWorkLoop()->inGate()`
- `%s LPM %sabled!\n`
- `\"Enabling SWMPR when its already enabled\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::_resetHSClockGated()`
- `\"AppleSynopsysMIPIDSIController::_waitPhyStatus timeout \" \"(status & 0x%08x) %s 0x%08x\\n\" @%s:%d`
- `AppleSynopsysMIPIDSIFrameDoneFunction`
- `\"AppleSynopsysMIPIDSIController::start Could not create lock\" @%s:%d`
- `virtual bool AppleSynopsysMIPIDSIController::start(IOService *)`
- `AppleSynopsysMIPIDSIController::start Failed to get phy settings\n`
- `sac-mode-count`
- `void AppleSynopsysMIPIDSIController::_pollReg(UInt32, UInt32, UInt32, bool)`
- `void AppleSynopsysMIPIDSIController::_sacThread()`
- `\"%s: Setting up interrupt %d event source failed\" @%s:%d`
- `site.UInt32`
- `IOReturn AppleSynopsysMIPIDSIController::_isDMMExitedGated()`
- `void AppleSynopsysMIPIDSIController::_initSWMPR()`
- `AppleSynopsysMIPIDSIController::start: Sad SAC enabled, switch between desense priority highest and lowest\n`
- `partial-display`
- `function-device_reset`
- `_dsimSACVersion >= 3`
- `AppleSynopsysMIPIDSIController::enableInterface %d: _readReg32(kSynopsysDSIM_CORE_PHY_STATUS)  0x%x status_mask 0x%x\n`
- `IOReturn AppleSynopsysMIPIDSIController::_calculateRegisterValues(UInt32 *, UInt32 *, display_timing_t *, mipi_lpm_t *)`
- `1222`
- `\"AppleSynopsysMIPIDSIController::_sacGenerateFrequencyList: kSACMaxFrequencyCount exceeded\" @%s:%d`
- `apply-testcode`
- `\"_dsimInterruptSources * sizeof(uint32_t)) != tmpData->getLength() :: %d bytes != %d bytes\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::_isCommitDoneGated()`
- `AppleSynopsysMIPIDSIResetClockFunction`
- `swmpr-memory-index`
- `sac-noise-width`
- `IOReturn AppleSynopsysMIPIDSIController::sendSWMPRLongCommandGated(UInt8, const UInt8 *, IOByteCount)`
- `IOReturn AppleSynopsysMIPIDSIController::receiveShortCommandGated(UInt8, UInt8 *)`
- `mipi cmd error 0x%x\n`
- `display_config`
- `\"Disabling SWMPR when its already disabled\" @%s:%d`
- `nclk`
- `%s panicOnError NOT Supported\n`
- `display-timing-lpm`
- `agile-line-count`
- `en`
- `AppleSynopsysMIPIPLLMaxLockAttempts`
- `\"AppleSynopsysMIPIDSIController::start _sacGenerateFrequencyList failed: %08x\" @%s:%d`
- `AppleSynopsysMIPIDSIController::start: Sad SAC enabled, round robin MIPI desense priority freqeuncies\n`
- `\"AppleSynopsysMIPIDSIController::enableInterfaceGated : MIPI PLL Failed to lock: 0x%08x\" @%s:%d`
- `site.AppleSACPLLConfig`
- `site.AppleSynopsysMIPIDSIResetClockFunction`
- `\"Timing out on DMM Exit. Waited %d s. kSWMPR_INTERRUPT_AP:0x%x\" @%s:%d`
- `_supportsSWMPR`
- `sac-divisor`
- `\"%s: _dsimRegisterTopDefaults array size too small\\n\" @%s:%d`
- `sac-frequency-list-count`
- `#lanes`
- `mipi-top-size`
- `interrupts`
- `mipi-swmpr`
- `AppleSynopsysMIPIDSIController::start: this: %p, _dsimBaseAddress = %#lx physical = %#lx length %llu\n`
- `site.UInt64`
- `mipi-sad-sac`
- `\"Timing out on commit. Waited %d s. kSWMPR_INTERRUPT_AP:0x%x\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::setLPMEnableGated(bool)`
- `site.AppleSynopsysMIPIDSIController`
- `\"%s: Device Tree missing mipi-top-size property\" @%s:%d`
- `supports-partial-display`
- `sac-frequency-lpm-list`
- `\"AppleSynopsysMIPIDSIController::start AppleARMFunctionSlowAdaptiveClockingAggressor::withProvider() failed\" @%s:%d`
- `virtual IOReturn AppleSynopsysMIPIDSIController::getDisplayTiming(bool, display_timing_t *)`
- `dis`
- `%s %d: Failed to go idle\n`
- `\"SWMPR interrupt not defined. _dsimInterruptSources < SWMPR_INTERRUPT_INDEX :: %d < %d\" @%s:%d`
- `22211112222`
- `function-saca`
- `%s  Slow Adaptive Clocking enabled with %d frequencies\n`
- `%s %d Unknown pll configuration\n`
- `AppleSynopsysMIPIDSIController`
- `sac-version`
- `\"AppleSynopsysMIPIDSIController::start AppleARMFunctionSlowAdaptiveClockingAggressor::withProvider() LPM failed\" @%s:%d`
- `AppleARMSlowAdaptiveClockingFrequency`
- `!dsimEnabled`
- `\"AppleSynopsysMIPIDSIController::_sacGenerateFrequencyList: unsupported SAC Version (%d)\" @%s:%d`
- `1`
- `mipi-config-lpm`
- `!=`
- `site.OSData*`

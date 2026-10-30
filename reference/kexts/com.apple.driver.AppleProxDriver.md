# `com.apple.driver.AppleProxDriver`

- Name: AppleProxDriver
- Version: `59`
- UUID: `E9F7A5BB-82CC-3938-AC5D-5DA6FB2E1A2B`
- Source version: `59.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### AppleAtlantisProxHIDEventDriver
- `Built-In`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AppleProxDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `8`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleAtlantisProxHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProxDriver`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOHIDInterface`
- `NeedsHostState`: `True`
- `Placement`: `1`
- `ProcessingPlan`: `AtlantisProcessingPlan`
- `ProductID`: `1361`
- `ProximitySupportsLPAEventTransitions`: `True`
- `SuggestedLPAScreenOffHysteresisMs`: `2000`
- `Transport`: `SPU`
- `VendorID`: `1452`

### AppleProxHIDEventDriver
- `AOPSupportsAggregateDictionary`: `True`
- `Built-In`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AppleProxDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `8`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleProxHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProxDriver`
- `IOProbeScore`: `9000`
- `IOProviderClass`: `IOHIDInterface`
- `Placement`: `1`
- `Transport`: `SPU`

### AppleSphinxProxHIDEventDriver
- `Built-In`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AppleProxDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `8`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleSphinxProxHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProxDriver`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOHIDInterface`
- `NeedsHostState`: `True`
- `Placement`: `1`
- `ProductID`: `1362`
- `ProximitySupportsLPAEventTransitions`: `True`
- `SuggestedLPAScreenOffHysteresisMs`: `0`
- `Transport`: `SPU`
- `VendorID`: `1452`

### AppleStargateLProxHIDEventDriver
- `Built-In`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AppleProxDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `8`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `AppleAtlantisProxHIDEventDriver`
- `IOPersonalityPublisher`: `com.apple.driver.AppleProxDriver`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOHIDInterface`
- `NeedsHostState`: `True`
- `Placement`: `1`
- `ProcessingPlan`: `StargateLProcessingPlan`
- `ProductID`: `1363`
- `ProximitySupportsLPAEventTransitions`: `True`
- `SuggestedLPAScreenOffHysteresisMs`: `0`
- `Transport`: `SPU`
- `VendorID`: `1452`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAtlantisProxHIDEventDriver` | 0x148 | AppleProxAbstractHIDEventDriver → IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleProxAbstractHIDEventDriver` | 0x130 | IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleProxAnalyticsReporter` | 0x28 |  |
| `AppleProxHIDEventDriver` | 0x168 | AppleProxAbstractHIDEventDriver → IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleSphinxProxHIDEventDriver` | 0x170 | AppleProxAbstractHIDEventDriver → IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001769 off=0x006d06c0-0x006d1e29 addr=0xfffffe00076d46c0-0xfffffe00076d5e29 r--/r--   __TEXT            
	sz=0x00000040 off=0x006d0d40-0x006d0d80 addr=0xfffffe00076d4d40-0xfffffe00076d4d80               __TEXT.__const            
	sz=0x000008f1 off=0x006d0d80-0x006d1671 addr=0xfffffe00076d4d80-0xfffffe00076d5671               __TEXT.__cstring          (CstringLiterals)
	sz=0x000007b8 off=0x006d1671-0x006d1e29 addr=0xfffffe00076d5671-0xfffffe00076d5e29               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000a938 off=0x0246b310-0x02475c48 addr=0xfffffe000946f310-0xfffffe0009479c48 r-x/r-x   __TEXT_EXEC       
	sz=0x0000a628 off=0x0246b310-0x02475938 addr=0xfffffe000946f310-0xfffffe0009479938          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x02475938-0x02475c48 addr=0xfffffe0009479938-0xfffffe0009479c48          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001b8 off=0x0498fa00-0x0498fbb8 addr=0xfffffe000b993a00-0xfffffe000b993bb8 rw-/rw-   __DATA            
	sz=0x000000e0 off=0x0498fa00-0x0498fae0 addr=0xfffffe000b993a00-0xfffffe000b993ae0               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b993ae0-0xfffffe000b993bb8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000024d8 off=0x011bdd70-0x011c0248 addr=0xfffffe00081c1d70-0xfffffe00081c4248 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x011bdd70-0x011bdd98 addr=0xfffffe00081c1d70-0xfffffe00081c1d98         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x011bdd98-0x011bddc0 addr=0xfffffe00081c1d98-0xfffffe00081c1dc0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002138 off=0x011bddc0-0x011bfef8 addr=0xfffffe00081c1dc0-0xfffffe00081c3ef8         __DATA_CONST.__const            
	sz=0x00000140 off=0x011bfef8-0x011c0038 addr=0xfffffe00081c3ef8-0xfffffe00081c4038         __DATA_CONST.__kalloc_type      
	sz=0x00000188 off=0x011c0038-0x011c01c0 addr=0xfffffe00081c4038-0xfffffe00081c41c0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x011c01c0-0x011c0248 addr=0xfffffe00081c41c0-0xfffffe00081c4248         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 115 at 0x04ae31c8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E9F7A5BB-82CC-3938-AC5D-5DA6FB2E1A2B
008: LC_SOURCE_VERSION           59.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aaea20 size=0x108
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleProxDriver`
- `CFBundleIdentifier`: `com.apple.driver.AppleProxDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleProxDriver`
- `CFBundleNumericVersion`: `1493204992`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `59`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `59`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleProxDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898653504`
- `_PrelinkExecutableRelativePath`: `AppleProxDriver`
- `_PrelinkExecutableSize`: `59185`
- `_PrelinkExecutableSourceAddr`: `-2198898653504`
- `_PrelinkKmodInfo`: `-2198828664320`

## Strings (168) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `DetectionMode`
- `floodCalibrationCurrent`
- `perc_smudge_releases`
- `sac-requested-index`
- `AppleProxAbstractHIDEventDriver`
- `site.AppleProxAbstractHIDEventDriver`
- `end_delta_baseline_kcpsps`
- `avg_signal_onhead`
- `call_day`
- `ReleaseAnalytics`
- `AppleProxHIDEventDriver`
- `was_BH`
- `call_pickups`
- `begin_delta_baseline_pct`
- `site.AppleAtlantisProxHIDEventDriver`
- `12111112122212121111111211111122111112121`
- `thermal-cal`
- `disable-ui-usage`
- `EnableDebugMode`
- `was_SM`
- `SecureIndicatorConditionsMet`
- `long_calls_day`
- `pocket_residency`
- `mode_residency_distribution`
- `ranging-cal`
- `sac-frequency-list`
- `off_head_duration`
- `trig_residency`
- `range_temp_time`
- `calls_day_f`
- `pocket_client`
- `mode`
- `AtlantisProcessingPlan`
- `num_temp_samples`
- `on_head_duration`
- `min_in_spec`
- `residency`
- `hid-driver`
- `max_temp`
- `mean_abs_diff_temp_1s`
- `AppleSphinxProxHIDEventDriver`
- `temperature_range_int`
- `pocket_baseline`
- `lowfreq_residency`
- `mode_residency`
- `floodT0Resistance`
- `%s.%s`
- `avg_reflect_estimate`
- `SA`
- `ProxDetectionMode`
- `ProxAlive`
- `AppleProxAnalyticsReporter`
- `min_temp`
- `std_temp`
- `end_field_baseline_kcpsps`
- `pocket_ece_residency`
- `max_diff_temp_1s`
- `range_temp`
- `num_entries`
- `1211111212221212111111121111112211111212112221`
- `prox-calibration`
- `IsVirtual`
- `ALG`
- `max_AMB_off_head`
- `final_temp`
- `highfreq_residency`
- `ProxOutputEvent`
- `HostStateNotification`
- `12111`
- `old_baseline`
- `BH_calls_day`
- `HA_calls_day`
- `temperature_tracking_enabled`
- `is_unlock`
- `UpdateCriticalError`
- `FW`
- `CoreAnalyticsHub`
- `initial_temp`
- `perc_external_releases`
- `DetectionMask`
- `call`
- `duration_day`
- `lowfreq_ece_residency`
- `ChangeSource`
- `[%s] Failed to register to SAC\n`
- `gesture_ece_residency`
- `CallAnalytics`
- `ProcessingPlan`
- `CriticalError`
- `ReceiverProximityReset`
- `SuggestedLPAScreenOffHysteresisMs`
- `121111121222121211111112111111221111121212222`
- `calls_day`
- `active_ece_residency`
- `active_residency`
- `site.AppleSphinxProxHIDEventDriver`
- `baseline_at_trigger`
- `min_diff_temp_1s`
- `releases`
- `gesture_residency`
- `client_type`
- `DisplayState`
- `RAW`
- `com.apple.aop.prox`
- `onhead`
- `begin_field_baseline_kcpsps`
- `ProxClearSeen`
- `call_duration`
- `DisableUIUsage`
- `%02X `
- `site.AppleProxHIDEventDriver`
- `ProxState`
- `begin_delta_baseline_kcpsps`
- `standby_residency`
- `AppleAtlantisProxHIDEventDriver`
- `ScreenUnlocked`
- `new_baseline`
- `sleep_residency`
- `function-saca`
- `site.AppleProxAnalyticsReporter`
- `long_calls_day_f`
- `com.apple.AppleProxSupport`
- `12111112122212121111111211111122111112`
- `DispatchProxEvent`
- `was_HA`
- `mean_temp`
- `floodComplianceRevision`
- `end_delta_baseline_pct`

**[__TEXT.__os_log]**

- `Unable to init input buffer`
- `No input buffer to receive report`
- `Error sending change source`
- `Prox aggressor index: %d, scheduling (%u redundant requests ignored since last transition)`
- `Handling property %s=%d ret = 0x%x`
- `%s%d: [%s]`
- `Found analytics hub`
- `Received thermal calibration - length: %u`
- `Updating CriticalError = 0x%X`
- `Report is empty`
- `Enabling prox debug mode`
- `Proximity detection mode : %d, ret : 0x%x`
- `Handling property %s=true`
- `DetectionMode: %d SignalRateTotal: %u SignalRateBaseline: %u CurrentRange: %u HabcBaseline: %u PocketBaseline: %u Cookie: %d`
- `Error casting CoreAnalyticsHub`
- `Failed to get prox SAC map: 0x%X`
- `Prox is alive again!`
- `Prox not alive for %llu ms`
- `Error updating face touches`
- `Set ProxClearSeen`
- `Ranging cal load status: 0x%x`
- `Failed to register to SAC`
- `Prox aggressor index: %d, scheduled (%u redundant requests ignored since last transition)`
- `Failed to get aggressor frequency list: 0x%X`
- `Failed to get aggressor noiseBW list: 0x%X`
- `Dispatching proximity event [0x%X]`
- `Fetching external data failed`
- `Thermal cal load status: 0x%x`
- `Failed to read report`
- `Disabling prox debug mode`
- `Unable to init sac lock`
- `Error sending ap active`
- `Prox Event Debug Info (Scaled by 1000)`
- `Sending analytics event with name: %s - status: 0x%x`
- `Unable to init sac thread`
- `Received ranging calibration - length: %u`
- `Could not dispatch event`
- `Baseline capture instead of Algs reset in %d detection mode`
- `Proximity detection mode: %d display state: %d change source: %d ap active: %d FW mode: %d ret: 0x%x`
- `Using processing plan %s`

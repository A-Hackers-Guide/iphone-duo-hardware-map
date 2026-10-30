# `com.apple.driver.AppleARMPMU`

- Name: AppleARMPMU
- Version: `1.0`
- UUID: `956D608D-79C4-3AB0-9468-871D0EC510DC`
- Source version: `1150.40.5.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleARMCharger
- `CFBundleIdentifier`: `com.apple.driver.AppleARMPMU`
- `IOClass`: `AppleARMPMUCharger`
- `IONameMatch`: `charger`
- `IOPersonalityPublisher`: `com.apple.driver.AppleARMPMU`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOService`
- `battery-data`:
  - `0003-default`: `<data 384 chars>`
  - `0004-default`: `<data 4160 chars>`
  - `0005-default`: `<data 1387 chars>`
  - `0006-default`: `<data 1368 chars>`
- `built-in`: `True`

### AppleARMPassthroughPowerSource
- `CFBundleIdentifier`: `com.apple.driver.AppleARMPMU`
- `IOClass`: `AppleARMPassthroughPowerSource`
- `IONameMatch`: `charger,passthrough`
- `IOPersonalityPublisher`: `com.apple.driver.AppleARMPMU`
- `IOProbeScore`: `2000`
- `IOProviderClass`: `IOService`
- `built-in`: `True`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleARMFunctionCharger` | 0x40 | AppleARMFunction |
| `AppleARMFunctionChargerMux` | 0x40 | AppleARMFunctionCharger → AppleARMFunction |
| `AppleARMPMUAccessoryPS` | 0xf8 | IOAccessoryPowerSource → IOAccessoryTransport → IOService → IORegistryEntry |
| `AppleARMPMUCharger` | 0x4a8 | AppleARMPMUPowerSource → IOPMPowerSource → IOService → IORegistryEntry |
| `AppleARMPMUPowerSource` | 0x258 | IOPMPowerSource → IOService → IORegistryEntry |
| `AppleARMPassthroughPowerSource` | 0x258 | AppleARMPMUPowerSource → IOPMPowerSource → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00003459 off=0x00169890-0x0016cce9 addr=0xfffffe000716d890-0xfffffe0007170ce9 r--/r--   __TEXT            
	sz=0x00000064 off=0x00169f10-0x00169f74 addr=0xfffffe000716df10-0xfffffe000716df74               __TEXT.__const            
	sz=0x00002d75 off=0x00169f74-0x0016cce9 addr=0xfffffe000716df74-0xfffffe0007170ce9               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00014e20 off=0x016d4310-0x016e9130 addr=0xfffffe00086d8310-0xfffffe00086ed130 r-x/r-x   __TEXT_EXEC       
	sz=0x00014740 off=0x016d4310-0x016e8a50 addr=0xfffffe00086d8310-0xfffffe00086eca50          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000006e0 off=0x016e8a50-0x016e9130 addr=0xfffffe00086eca50-0xfffffe00086ed130          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000368 off=0x0492f5d8-0x0492f940 addr=0xfffffe000b9335d8-0xfffffe000b933940 rw-/rw-   __DATA            
	sz=0x000001e8 off=0x0492f5d8-0x0492f7c0 addr=0xfffffe000b9335d8-0xfffffe000b9337c0               __DATA.__data             
	sz=0x00000148 off=0x00000000-0x00000148 addr=0xfffffe000b9337c0-0xfffffe000b933908               __DATA.__common           (Zerofill)
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b933908-0xfffffe000b933940               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000025c0 off=0x00fac758-0x00faed18 addr=0xfffffe0007fb0758-0xfffffe0007fb2d18 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x00fac758-0x00fac768 addr=0xfffffe0007fb0758-0xfffffe0007fb0768         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x00fac768-0x00fac778 addr=0xfffffe0007fb0768-0xfffffe0007fb0778         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001e50 off=0x00fac778-0x00fae5c8 addr=0xfffffe0007fb0778-0xfffffe0007fb25c8         __DATA_CONST.__const            
	sz=0x00000300 off=0x00fae5c8-0x00fae8c8 addr=0xfffffe0007fb25c8-0xfffffe0007fb28c8         __DATA_CONST.__kalloc_type      
	sz=0x00000370 off=0x00fae8c8-0x00faec38 addr=0xfffffe0007fb28c8-0xfffffe0007fb2c38         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x00faec38-0x00faed18 addr=0xfffffe0007fb2c38-0xfffffe0007fb2d18         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 248 at 0x04ad1da8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     956D608D-79C4-3AB0-9468-871D0EC510DC
008: LC_SOURCE_VERSION           1150.40.5.0.0
009: LC_FUNCTION_STARTS          offset=0x004a97330 size=0x178
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleARMPMU`
- `CFBundleGetInfoString`: `Copyright © 2009 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleARMPMU`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleARMPMU`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleARMPMU.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904317808`
- `_PrelinkExecutableRelativePath`: `AppleARMPMU`
- `_PrelinkExecutableSize`: `109473`
- `_PrelinkExecutableSourceAddr`: `-2198904317808`
- `_PrelinkKmodInfo`: `-2198829058600`

## Strings (398) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `determinePowerSupply`
- `charger-ramp-on-wakeup`
- `kern.monotonicclock`
- `BootCapacityEstimate`
- `external`
- `BatteryMinFCC`
- `%s::%s: %s: WARNING: Got early Interrupt before _chargerEventSource is setup\n`
- `%s::%s: %s: Exiting PoSM mode ...\n`
- `FullyCharged`
- `%s::%s: %s: _voltage=%d _atvCurrentVoltageTier=%d/%d i=%d,upperV=%d,margin=%d,vsetLimit=%d  now=%ld,deadline=%ld,interval=%ld atvTimerExpired=%d\n`
- `start`
- `AppleARMPMUPowerSource.cpp`
- `BatteryMinTemp`
- `1222222`
- `ui_pct_multiplier`
- `charger-sleep-interval`
- `TimeRemaining`
- `AppleResetUSBCurrentLimit`
- `%s::%s: %s: _backlightLevel=%d newLevel=%d enableRailNoiseMitigation=%d (%x)\n`
- `TO`
- `BatteryHighAvgCurrentLastRun`
- `%04x-default`
- `%s::%s: %s: stop forcing UISOC\n\n`
- `END`
- `checkHvcSelection`
- `AppleVoltageDictionary`
- `usb_det`
- `InflowInhibit`
- `disable-atv`
- `BootBBCapacity`
- `CycleCountLastQmax`
- `%s::%s: %s:  resetting charge END\n`
- `AppleARMPassthroughPowerSource`
- `unsupported`
- `firewire`
- `usb`
- `VDD_OUT`
- `%s: limiting USB input current to %lu mA\n`
- `usb-input-limit-max`
- `MaxCurrent`
- `site.ApplePowerSourceMemLog`
- `battery-reserved-capacity`
- `causeChargerEvent`
- `value`
- `function-firewire_det`
- `%s::%s: %s: InputNotSupp %d ChrgNot %d \n`
- `UsbHvcMenu`
- `batt`
- `%s:%d ChargeLimitDisplayOn OFF\n`
- `ChargeLimitVoltage`
- `max-charge-voltage`
- `battery-alert-capacity`
- `charge-currents`
- `forceUiSocTimerAction`
- `%s::%s: %s: PoSMLowerThreshold=%d\n`
- `MinimumQmax`
- `PresentDOD`
- `DisplayFilterInterval`
- `CarrierChargingModeMitigation`
- `LifetimeData`
- `%s::%s: %s: _lastBatteryDataProcessed=%lld, _lastBatteryDataUpdate=%lld skip filter\n`
- `%s::%s: %s: ecc=%d capacityLevel*1000=%d fullyCharged=%d isCharging=%d\n`
- `handleUSBInputFlags`
- `max`
- `12222`
- `function-dock%d_%s`
- `12111112122212121211111111111111111111112111111111111222112222222211112212111111111112222121222222222222211222221222121222222221111122222212121111212`
- `site.AppleARMFunctionChargerExpansionData`
- `SharedSource`
- `ChargeTable`
- `ChargeLimits`
- `%s:%d New ChargeLimits [`
- `%s::%s: %s: intCapacity=%d, maxCapacity=%d rawCurrentCapacity=%d, rawMaxCapacity=%d\n`
- `AppleARMPMUCharger: dock %lu inputCurrentLimit %lu chargeLimit NONE\n`
- `BatteryChargeCurrent`
- `penalty-box-temp-lth`
- `RaUpdateCounter`
- `%s::%s: %s: _capacityReported=%d  using voltage to measure capacity\n`
- `ExternalConnected`
- `DesignCapacity`
- `AppleChargeRateLimitIndex`
- `MinimumDeltaVoltage`
- `%s::%s: %s: [%d] hvc[%d] in debounce zone cap %d\n`
- `AC`
- `gatedSetProperties`
- `CycleCount`
- `%s::%s: %s: %s: current limit backoff reporting needs more %lld ms\n\n`
- `external4`
- `pmu-measured`
- `min-charge-capable-current`
- `%s::%s: %s: Starting GGEOC delayed timer ...\n`
- `%s::%s: %s: dock %d availI %d _chargeCapableCurrent %d offset %d ncap %d unsup %d \n`
- `USB`
- `site.AppleARMPMUAccessoryPS`
- `CarrierChargingMode`
- `OCVTakenFlag`
- `AppleARMFunctionCharger`
- `setHvcAdapter`
- `ChargerData`
- `BatteryMaxTemp`
- `SOCBasedShutdown`
- `/Library/Caches/com.apple.xbs/FBB9B734-F955-49B1-83B2-A607CD738984/TemporaryDirectory.jIvHmi/Sources/AppleARMPMU/AppleARMPMUCharger.cpp`
- `FieldDiagsInflowInhibit`
- `pmu-debug`
- `num-docks`
- `site.AppleARMPMUCharger`
- `AtWarnLevel`
- `ForceCapacityOverwrite`
- `%s::%s: %s:  carrier mode%slowV=%d mV, highV=%d mV\n`
- `ChemID`
- `ForceFullGGUpdateOnBoot`
- `AppleARMPMUCharger: dock %lu inputCurrentLimit %lu chargeLimit %lu\n`
- `%s::%s: %s: to=%d end=%d . ci=%d ec=%d ai=%d\n`
- `BatteryFlashWriteCnt`
- `%s::%s: %s:  _ggEOCTimer: _isGGEOC %d\n`
- `BatteryData`
- `setChargerWakeAlarm`
- `AppleARMPMUPowerSource`
- `force-usb-power`
- `function-ac_detect`
- `%s::%s: %s: Dock %d: adapterInfo %x xConn %d xChrg %d rawConn %d _enableACSleep %d allowIdleSleep %d\n`
- `TristarCurrent`
- `0000`
- `rd`
- ` enabled `
- ` `
- `Amperage`
- `FamilyCode`
- `%s: limiting USB input current to %lu mA (measured %lld mA)\n`
- `battery-family`
- `PoSMUpperThreshold`
- `%s::%s: %s: forcing UISOC for up to '%u' seconds\n\n`
- `222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211122221112222111222211`
- `BatteryMinPackVoltage`
- `BatteryOverDischargedCurrent`
- `%s:%d DisplayFilterInterval =%d\n`
- `%s::%s: %s: Entering PoSM mode ...\n`
- `AppleRawDrainVoltages`
- `getChargeLimit`
- `%s::%s: %s: Charging disabled - in PenaltyBox :: SOC(%d >= %d), temp(%d >= %d)\n`
- `BatteryLowAvgCurrentLastRun`
- `TotalOperatingTime`
- `%s::%s: %s: UI_Multiplier: _capacityDropPoint*1000=%d, capacityLevel*1000=%d (%d), _uiPctMultiplier=%d (%%), \n`
- `AppleARMPMUAccessoryPS`
- `BatteryOverChargedCurrent`
- `BatteryChemID`
- `min-charge-voltage`
- `MaximimDischargeCurrent`
- `MaximumFCC`
- `%s:%d _carrierModeUpperVoltage=_carrierModeLowerVoltage=%d\n`
- `%s::%s: %s: UIFastTrack: clear _updateCount=%d\n`
- `%s::%s: %s:  to=%d end=%d . currentUpcount=%d, chargeTimeoutUpcount=%d _chargerAttachUpcount=%d. _cap=%d, _max=%d\n`
- `ChargeStatus`
- `%s::%s: %s: fullyCharged|= _isChargeEnd=%d || _isGGEOC=%d (%d) \n`
- `External3`
- `usb-hvc-current-max`
- `charge-limits`
- `%s::%s: %s:  uiUpdateTimerAction: updateRegistry %d\n`
- `FlashWriteCount`
- `\"%s: could not start power source\" @%s:%d`
- `error`
- `BatteryRDISCnt`
- `BatteryTotalOperatingTime`
- `charger-curve`
- `function-rail_noise_ctl`
- `%s::%s: %s:  _socBasedShutdown => %d (%d) \n`
- `%s::%s: %s:  carrier mode lowV=%d mV, highV=%d mV\n`
- `%s:  step from %d mA to %d mA (%d mA) delayed for power supply debounce\n`
- `site.AppleARMPMUPowerSource`
- `BatteryMaxFCC`
- ` %u @ %u `
- `%s::%s: %s: PoSMEnabled=%d\n`
- `handleBacklightUpdate`
- `%s: sample %ld mv, load %ld mv, out %ld mv, nc %ld, av %ld (%ld/%d)\n`
- `AppleRawAdapterDetails`
- `boot-adapter-id`
- `%s::%s: %s: (dock=%d) HPM Data %p requested[%d] confirmed %d [%d]\n`
- `BatteryCycleCount`
- `function-dock%d_set_charger%u`
- `carrier-mode`
- `gg-eoc-enable`
- `battery-factory-id`
- `AppleDialogPMU`
- `(no provider)`
- `LowAvgCurrentLastRun`
- `penalty-box-soc-uth`
- `MinimumRa0-8`
- `AbsoluteCapacity`
- `%s: resetCurrentLimitTimerAction usbInputLimitBackoff=%lu\n`
- `site.DisplayCapacityCurve`
- `AdapterID`
- `setInputPower`
- `function-tristar_current`
- `BatteryMinQMax`
- `InstantAmperage`
- `MaximimOverChargedCapacity`
- `VBAT`
- `UsbHvcHvcIndex`
- ` AppleARMPMUCharger::%s(displayCapacity*1000=%d _previousDisplayCapacity*1000=%d slope=%d connected=%d):  newDisplayCapacity*1000=%d, maxChangeAmount*1000=%d, diff=%u now=%u nextUpdate=%u cis=%u\n`
- `%s::%s: %s: [%d]\n`
- `BatteryMinDeltaVoltage`
- `battery-capacity`
- `PoSMLowerThreshold`
- `MaximumTemperature`
- `handleUSBInputFlagsAction`
- `12111111`
- `\"%s: could not create power source\" @%s:%d`
- `AverageTemperature`
- `%s:%d ChargeLimitDisplayOn NO OP\n`
- `boot-voltage`
- `%s::%s: %s:  time = %ld waiting for %d\n`
- `1211111212221212112222111221121`
- `AppleARMPMUCharger`
- `atv-vset-margin`
- `ggEOCTimerAction`
- `DisplayCapacityLevel`
- `%s::%s: %s: _currentTempTable=%p\n`
- `kern.boottime`
- `dis`
- `%s::%s: %s: \t[%d] %d mV %d mA\n`
- `BatteryminRa0-8`
- `eoc-force-charge-limit`
- `ITSimulationCounter`
- `%s::%s: %s: previousLevel:%d.%d previousSlope:%d\n`
- `%s::%s: %s: WARNING: CapacityCurveOption modified, Restoring it back: _capacityCurveOptions=0x0%x\n`
- `AppleARMPMUPowerSource::powerSupplyDebounce(%u)\n`
- `%s::%s: %s: [%d] ILIM %d chargerAttached %d\n`
- `external3`
- `penalty-box-enable`
- `MinimumPackVoltage`
- `LowTemperature`
- `setChargerHvcAction`
- `AdapterVoltage`
- `%s::%s: %s: [%d] select hvc[%d] batt cap %d %sHVC\n`
- `AppleARMPMUPowerSource::start`
- `battery-id`
- ` %dC %dC [%d] [`
- `UpperVoltage`
- `PredictiveChargingInhibit`
- `BatteryFCCData`
- `ChargeLimitDisplayOn`
- `updateChargeStatusAction`
- `dock_parent`
- `\"%s::handleStartGated() failed\" @%s:%d`
- `atv-vset-top-tier`
- `copyAndSetAdapterDetailFromChargerFunction`
- `NominalChargeCapacity`
- `MaximumQmax`
- `BestAdapterIndex`
- `Temperature`
- `PoSMEnabled`
- `%s::%s: %s: currentCapacity:%d maxCapacity:%d capacityLevel:%d.%d\n`
- `%s:  failed to set input current limit to %umA: %s\n`
- `site.AppleARMFunctionChargerMux`
- `Voltage`
- `MaximumRa0-8`
- `%s::%s: %s: _reportCapacity=%d fullyCharged=%d capacityLevel*1000=%d displayCapacity*1000=%d\n`
- `CapacityEstimated`
- `usb-hvc-voltage-max`
- `ac`
- `battery-data`
- `Apple`
- `%s::%s: %s:  failed to fetch adapter detail \"%s\" from charger function\n`
- `MaximimOverDischargedCapacity`
- `BatteryShutdownReason`
- `GasGaugeFirmwareVersion`
- `%s:%d ChargeLimitDisplayOn _chargeLimitDisplayOn=%d\n`
- `%s::%s: %s:  kAppleARMPMUPowerSourceMaxPowerState (%x)\n`
- `BatteryTimeAbove98Perc`
- `usb-hvc-to-5V`
- `%04x-%c`
- `AppleRawBatteryVoltage`
- `%s: backlight level 0x%x\n`
- `%s::%s: %s: to=%d end=%d . currentUpcount=%d, chargeTimeoutUpcount=%d _chargerAttachUpcount=%d. _cap=%d, _max=%d\n`
- `site.DisplayCapacityFilter`
- `External4`
- `RDISCnt`
- `DisplayFilterMaxChange`
- `%s: crit=%d level=%d voltage=%d _shutdownVoltage=%d _shutdownVoltageCount=%d backlightLevel=%d\n`
- `External`
- `top-off-pct`
- `battery-shutdown-voltage`
- `IsCharging`
- `PMUConfiguration`
- `createReplacementCapacityCurve`
- `%s::%s: %s: dock %u _powerSupplyType %s, usbDetect %d\n`
- `CurrentCapacity`
- `121111121222121212111111111111111111111121111111111112221122222222111122121`
- `fw-supported`
- `MaxVoltage`
- `LowerVoltage`
- `AppleATVTierDeadlineInterval`
- `NotChargingReason`
- `BatteryMaxDeltaVoltage`
- `BatteryMaxQmax`
- `%s::%s: %s: Charging disabled - in PoSM topOff :: SOC(%d)>LowerThreshold(%d)\n`
- `Enter`
- ` AppleARMPMUCharger::%s(displayCapacity*1000=%d _previousDisplayCapacity*1000=%d slope=%d):  newDisplayCapacity*1000=%d, now=%u nextUpdate=%u\n`
- `setHvcConfigParams`
- `%s: failed to set 'ChargingCurrent'\n`
- `atv-tier-deadline`
- `charger-limit-display-on`
- `likely an error\n`
- `brightness`
- `%s::%s: %s:  attached = %lu, resetting charge %s\n`
- `AppleARMFunctionChargerMux`
- `_smoothSOC`
- `BatteryMaxPackVoltage`
- `TristarCurrentuA`
- `%s::%s: %s:  _socBasedShutdown => %d \n`
- `%s::%s: %s: PoSMUpperThreshold=%d\n`
- `MaximumPackVoltage`
- `MaximumDeltaVoltage`
- `TimeAbove95Perc`
- `handleUpdateRegistry`
- `penalty-box-soc-lth`
- `force-uisoc-interval`
- `\n`
- `MinimumTemperature`
- `IODisplayParameters`
- `%s:  currentStepLimit=%d, previousStepLimit=%d was limited, cleared now\n`
- `ExternalUnsupported`
- `Index`
- `BatteryTempSamples`
- `BatteryNominalChargeCapacity`
- `%s::%s: %s: voltage=%d\n`
- `Exit`
- `%s: capacityLevel=%d.%d displayCapacity=%d.%d charging=%d PoSM=%u reducedFullChargelevel=%d.%d\n`
- `AdapterDetails`
- `function-%s`
- `external2`
- `%s::handleStartGated() dock=%u chargers=%u\n`
- `penalty-box-temp-uth`
- `%s: FAIL cannot register for backlight notifications\n`
- `%s::%s: %s: Charging disabled - in PoSM :: SOC(%d)>UpperThreshold(%d)\n`
- `%s: step from %d mA to mA %d (%d mA), target %u mA, %lld ms since last step\n`
- `enable-acsleep`
- `\"post init failed\\n\" @%s:%d`
- `BatteryAvgTemp`
- `rootdev`
- `External2`
- `Description`
- `Watts`
- `setCharger`
- `BatteryKey`
- `uiUpdateTimerAction`
- `%s:%d DisplayFilterMaxChange =%d.%d\n`
- `%s::%s: %s: _socBasedShutdown=%d, _voltage=%d _noSleepAssertion=%d _atCriticalLevel=%d atCriticalLevel=%d\n`
- `%s::%s: %s: _backlightLevel=%d newLevel=%d enableRailNoiseMitigation=%d\n`
- `%s:  step from %d mA to %d mA (%d mA) needs %lld ms, only %lld ms passed\n`
- `ui-update-interval`
- `ErrorFlags`
- `TemperatureSamples`
- `%s::%s: %s: Cancel GGEOC delayed timer ...\n`
- `%s::%s: %s: previousLevel*1000=%d capacityLevel*1000=%d displayCapacity*1000=%d\n`
- `%s::%s: %s: ILimitBkf %d ITarg %d \n`
- `UpdateTime`
- `AppleARMPMUPowerSource::handleInterrupt[%p] (count %d)\n`
- `BatteryDischargeCurrent`
- `ChargingCurrent`
- `ITMiscStatus`
- `ChargingOverride`
- `ChargerConfiguration`
- `Source`
- ` %d`
- `MaximimChargeCurrent`
- `%s:%d ChargeLimitDisplayOn SETUP & _chargeLimitDisplayOn=%d\n`
- `HighTemperature`
- `IORTC`
- `site.AppleARMPassthroughPowerSource`
- `BatteryMaxRa0-8`
- `BatteryIDChanged`
- `Battery`
- `charger-load`
- `IOPMUBootPosm`
- `MinimumFCC`
- `%s::%s: %s:  time = %ld, resetting charge TO\n`
- `en`
- `BootVoltage`
- `%s::%s: %s: InputNotSupp %d PwrHshk %d ChrgNot %d\n`
- `Current`
- `%s:  limit %d used %d usbChargerAttached %d vsetLimit %d\n`
- `FireWire`
- `function-set_charger%u`
- `AtCriticalLevel`
- `HighAvgCurrentLastRun`
- `FCFlag`
- `%s:  step down from %d mA needs %lld ms, only %lld ms passed\n`
- `site.AppleARMFunctionCharger`
- `BatteryCycleCntLastQmax`
- `backlight-control`
- `failed to store POSM state\n`
- `%s::%s: %s: UIFastTrack: changeIntervalSecs=%u, _updateCount=%d\n`
- `%s::%s: %s: Charging disabled - PenaltyBox triggered:: SOC(%d >= %d), temp(%d >= %d)\n`
- `%s: %sabling idle sleep\n`
- `MaxCapacity`
- ` ]\n`
- `GaugeFlagRaw`

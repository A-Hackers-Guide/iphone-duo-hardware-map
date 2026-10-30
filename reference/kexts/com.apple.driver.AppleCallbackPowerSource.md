# `com.apple.driver.AppleCallbackPowerSource`

- Name: AppleCallbackPowerSource
- Version: `1`
- UUID: `400F984E-531F-305A-85AB-D5EA9826D2C4`
- Source version: `2043.40.52.0.2`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 22.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 22.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 22.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 22.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleCallbackPowerSourceProvider
- `CFBundleIdentifier`: `com.apple.driver.AppleCallbackPowerSource`
- `IOClass`: `AppleCallbackPowerSource`
- `IOMatchCategory`: `PowerSource`
- `IOPersonalityPublisher`: `com.apple.driver.AppleCallbackPowerSource`
- `IOProviderClass`: `AppleCallbackPowerSourceProvider`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleCallbackPowerSource` | 0x178 | IOPMPowerSource → IOService → IORegistryEntry |
| `AppleCallbackPowerSourceProvider` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000017dc off=0x003bcf60-0x003be73c addr=0xfffffe00073c0f60-0xfffffe00073c273c r--/r--   __TEXT            
	sz=0x000010ee off=0x003bd5d8-0x003be6c6 addr=0xfffffe00073c15d8-0xfffffe00073c26c6               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000076 off=0x003be6c6-0x003be73c addr=0xfffffe00073c26c6-0xfffffe00073c273c               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00004bdc off=0x01a2e3d0-0x01a32fac addr=0xfffffe0008a323d0-0xfffffe0008a36fac r-x/r-x   __TEXT_EXEC       
	sz=0x0000495c off=0x01a2e3d0-0x01a32d2c addr=0xfffffe0008a323d0-0xfffffe0008a36d2c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000280 off=0x01a32d2c-0x01a32fac addr=0xfffffe0008a36d2c-0xfffffe0008a36fac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00001858 off=0x04934960-0x049361b8 addr=0xfffffe000b938960-0xfffffe000b93a1b8 rw-/rw-   __DATA            
	sz=0x000000d0 off=0x04934960-0x04934a30 addr=0xfffffe000b938960-0xfffffe000b938a30               __DATA.__data             
	sz=0x00000198 off=0x00000000-0x00000198 addr=0xfffffe000b938a30-0xfffffe000b938bc8               __DATA.__common           (Zerofill)
	sz=0x000015f0 off=0x00000000-0x000015f0 addr=0xfffffe000b938bc8-0xfffffe000b93a1b8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e40 off=0x01005e98-0x01006cd8 addr=0xfffffe0008009e98-0xfffffe000800acd8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01005e98-0x01005ea8 addr=0xfffffe0008009e98-0xfffffe0008009ea8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01005ea8-0x01005eb8 addr=0xfffffe0008009ea8-0xfffffe0008009eb8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c00 off=0x01005eb8-0x01006ab8 addr=0xfffffe0008009eb8-0xfffffe000800aab8         __DATA_CONST.__const            
	sz=0x00000080 off=0x01006ab8-0x01006b38 addr=0xfffffe000800aab8-0xfffffe000800ab38         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x01006b38-0x01006c78 addr=0xfffffe000800ab38-0xfffffe000800ac78         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x01006c78-0x01006cd8 addr=0xfffffe000800ac78-0xfffffe000800acd8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 92 at 0x04ad460c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     400F984E-531F-305A-85AB-D5EA9826D2C4
008: LC_SOURCE_VERSION           2043.40.52.0.2
009: LC_FUNCTION_STARTS          offset=0x004a9b3c8 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleCallbackPowerSource`
- `CFBundleIdentifier`: `com.apple.driver.AppleCallbackPowerSource`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleCallbackPowerSource`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
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
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleCallbackPowerSource.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901878944`
- `_PrelinkExecutableRelativePath`: `AppleCallbackPowerSource`
- `_PrelinkExecutableSize`: `35408`
- `_PrelinkExecutableSourceAddr`: `-2198901878944`
- `_PrelinkKmodInfo`: `-2198829037216`

## Strings (257) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ExternalChargeCapable`
- `ShutDownUISoc`
- `[DEBUG] (%s:%#llx): psCallback: type:%s data:%s\n\n`
- `ChargeAccum`
- `FilteredCurrentRc4`
- `SOCAlarm`
- `ShutDownPrevVoltage`
- `VoltageCell0`
- `VoltageCell1`
- `QmaxCell1`
- `RaTableCell1`
- `NominalChargeCapacity`
- `UUID`
- `Count`
- `PresentDODCell0`
- `[ERROR] (%s:%#llx): Cannot handle type for %s\n\n`
- `ChemID`
- `ShutDownPresentDOD`
- `AppleCallbackPowerSourceProvider`
- `MaximumInternalTemperature`
- `FilteredCurrentRc3`
- `CellCurrentAccumulatorCount`
- `LowAvgCurrentLastRun`
- `TimeSinceLastOCV`
- `ResetDataComms`
- `DynamicSoc1Vcut`
- `RebalanceHWBypassFETStatus`
- `ShutDownRSS`
- `Watts`
- `ResetDataHardware`
- `ShutDownDynSdSoc`
- `batman`
- `DOD0`
- `QmaxUpdSuccessCount`
- `MinimumRa8`
- `KioskModeHighSocDays`
- `Current`
- `GaugeResetCounter`
- `AppleRawCurrentCapacity`
- `SkinTemperatureVirtual`
- `VacVoltageLimit`
- `ChargerID`
- `MinimumDeltaVoltage`
- `MinimumQmax`
- `NCCMax`
- `StateOfCharge`
- `MfgData`
- `CurrentSenseMonitorStatus`
- `FlashWriteCount`
- `AdapterRevision`
- `RSSFiltered`
- `RebalanceEnableStatus`
- `SerialNumber`
- `BatteryData`
- `GaugeFlagRaw`
- `KioskModeFullChargeVoltage`
- `CycleCount`
- `BootVoltage`
- `ShutDownAverageCurrent`
- `IdealCRate`
- `ChargerInhibitReason`
- `IsCharging`
- `AtCriticalLevel`
- `ShutDownPrevAverageCurrent`
- `KioskModeLastHighSocHours`
- `PMUConfiguration`
- `Qstart`
- `UpdateTime`
- `MiscStatus`
- `iMaxAndSocSmoothTable`
- `TimeAtHighSoc`
- `ResetCnt`
- `WeightedRaCell1`
- `AdapterDetails`
- `SkinTemperature`
- `SlowChargingReason`
- `SafetyFaultCounter`
- `RawA`
- `ShutDownResScale`
- `DailyMaxSoc`
- `ShutDownSWRemcap`
- `ShutDownSWFcc`
- `BatteryHealthServiceFlags`
- `VoltageCell2`
- `AlgoTemperature`
- `WeightedRa`
- `LifetimeData`
- `DesignCapacity`
- `ChargingVoltage`
- `DOD0Cell2`
- `PresentDOD`
- `Raw`
- `CycleCountLastQmax`
- `PTATFaultCounter`
- `AppleRawMaxCapacity`
- `VirtualTemperature`
- `ShutDownTimestamp`
- `PresentDODCell1`
- `DateOfFirstUse`
- `RebalanceData`
- `MaximumTemperature`
- `RaTableCell3`
- `AppleCallbackPowerSource`
- `ShelfLifeModeAutoEntry`
- `MinimumPackVoltage`
- `MaximumOverDischargedCapacity`
- `BatteryShutdownReason`
- `MaximumDischargeCurrent`
- `MaximumOverChargedCapacity`
- `RDISCnt`
- `ShutDownPassedCharge`
- `ShutDownSocSoc2`
- `WeightedRaCell2`
- `QmaxDisqualificationReason`
- `UISoc`
- `NotChargingReason`
- `MaximumRa0-8`
- `OCVData`
- `ShutDownPrevFullChargeCapacity`
- `site.AppleCallbackPowerSourceProvider`
- `MaximumFCC`
- `QmaxUpdateDisqualified`
- `BestAdapterIndex`
- `FullyCharged`
- `CellVoltage`
- `ShutDownFilteredCurrent`
- `BatteryHealthServiceOption`
- `QmaxCell2`
- `MinimumRa0-8`
- `PresentDODCell2`
- `RebalanceInrushCurrentDebug`
- `ShutDownRemainingCapacity`
- `AppleRawAdapterDetails`
- `Description`
- `AdapterPower`
- `AppleRawBatteryVoltage`
- `Soc1Voltage`
- `SystemDisconnectCountScrPad`
- `RebalanceTimeSeconds`
- `ResistanceUpdatedDisabledCount`
- `MaximumWRdc`
- `CellCurrentAccumulator`
- `AlgoCycleCountDbgData`
- `ShutDownSocAlarm`
- `ShutDownDynSdVoltage`
- `KioskModeEntryCount`
- `ErrorFlags`
- `12111112122212121211111111111111111111111211111`
- `SystemPower`
- `SKTMData`
- `RaUpdateDisqualified`
- `Source`
- `ResetData`
- `BatteryModelID`
- `ChargingCurrent`
- `RebalanceNotRebalancingReason`
- `DOD0Cell3`
- `WatchdogDebugDump`
- `BatteryNeedsRest`
- `RawB`
- `ShutDownTemperature`
- `ShutDownVoltage`
- `ShutDownPrevNominalChargeCapacity`
- `RaTableCell2`
- `PresentDODCell3`
- `Flags`
- `FilteredCurrent`
- `QmaxCell3`
- `FccComp1`
- `RebalanceErrorFlags`
- `LowVoltageResidencyCounters`
- `com.apple.iopmps`
- `Qmax`
- `BatteryCellDisconnectCount`
- `KioskModeMode`
- `QmaxCell0`
- `CurrentCapacity`
- `MaximumQmax`
- `DOD0Cell0`
- `AppleRawExternalConnected`
- `ShutDownMaxDischargeCurrent`
- `KioskModeHighSocSeconds`
- `AdapterVoltage`
- `[INFO] (%s:%#llx): notification deferred\n\n`
- `ISS`
- `ShutDownDOD0`
- `AdapterPowerTier`
- `MaxCapacity`
- `PMUConfigured`
- `MinimumFCC`
- `QmaxUpdFailCount`
- `MaximumRa8`
- `NCCMin`
- `12111112122212121`
- `TrueRemainingCapacity`
- `OCV`
- `VoltageCell3`
- `PassedCharge`
- `ResScale`
- `AbsoluteCapacity`
- `PackCurrentAccumulator`
- `PackCurrentAccumulatorCount`
- `CellWom`
- `ShutDownFullChargeCapacity`
- `ShutDownPrevRemainingCapacity`
- `ResetDataFirmware`
- `ShelfLifeModeExitCounters`
- `RebalanceOutputStruct`
- `MaximumChargeCurrent`
- `AverageTemperature`
- `ExternalConnected`
- `RaTableRaw`
- `HighAvgCurrentLastRun`
- `NccpFiltered`
- `BatteryRsenseOpenCount`
- `ResetDataSoftware`
- `DataFlashWriteCount`
- `ChargerStatus`
- `RaTableCell0`
- `applecbps`
- `SimRate`
- `AlgoChemID`
- `TemperatureSamples`
- `SystemDisconnectCount`
- `ShutDownUpoReboot`
- `ShutDownLpemSocfThresh`
- `BatteryHealthMaxCapacity`
- `ShutDownRaTableRaw`
- `WeightedRaCell3`
- `BatteryState`
- `BatteryHealthMetric`
- `ChargerData`
- `MaximumDeltaVoltage`
- `MaximumPackVoltage`
- `KioskMode`
- `IsWireless`
- `DailyMinSoc`
- `TotalOperatingTime`
- `WeightedRaCell0`
- `FamilyCode`
- `RSS`
- `ResetDataWatchDog`
- `TimeToEmptyDbgData`
- `ShutDownDataError`
- `site.AppleCallbackPowerSource`
- `Voltage`
- `ITMiscStatus`
- `GgDataFlashUpdate`
- `FccComp2`
- `ShutDownNominalChargeCapacity`
- `ShutDownLPEMMode`
- `BatteryHealthData`
- `MinimumTemperature`
- `DOD0Cell1`

**[__TEXT.__os_log]**

- `(%s:%#llx): notification deferred\n\n`
- `(%s:%#llx): Cannot handle type for %s\n\n`
- `(%s:%#llx): psCallback: type:%s data:%s\n\n`

# `com.apple.driver.IOHIDPowerSource`

- Name: IOHIDPowerSource
- Version: `1`
- UUID: `94C8DA5E-FD60-3487-B1D3-E462D91459FA`
- Source version: `2360.40.13.0.1`
- Depends on: [`com.apple.driver.AppleCallbackPowerSource`](com.apple.driver.AppleCallbackPowerSource.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 11.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 16.1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 16.1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 16.1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 16.1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### IOHIDPowerSourceController
- `CFBundleIdentifier`: `com.apple.driver.IOHIDPowerSource`
- `IOClass`: `IOHIDPowerSourceController`
- `IOMatchCategory`: `IOHIDPowerSourceController`
- `IOPersonalityPublisher`: `com.apple.driver.IOHIDPowerSource`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `InterfaceMatching`:
  - `IOPropertyMatch`:
    - `Type`: `PowerPack`
  - `IOProviderClassKey`: `IOHIDTranslationService`

### IOHIDPowerSourceDebugClient
- `CFBundleIdentifier`: `com.apple.driver.IOHIDPowerSource`
- `IOClass`: `IOHIDPowerSourceDebugClient`
- `IOMatchCategory`: `IOHIDPowerSourceDebugClient`
- `IOPersonalityPublisher`: `com.apple.driver.IOHIDPowerSource`
- `IOProviderClass`: `IOHIDPowerSource`

### IOHIDTranslationService
- `CFBundleIdentifier`: `com.apple.driver.IOHIDPowerSource`
- `Events`:
  - `BMU Info`:
    -
      - `key`: `CycleCount`
      - `page`: `65280`
      - `usage`: `33`
    -
      - `key`: `ChemID`
      - `page`: `65524`
      - `usage`: `5`
    -
      - `key`: `GasGaugeFirmwareVersion`
      - `page`: `65524`
      - `usage`: `3`
    -
      - `denominator`: `36`
      - `key`: `DesignCapacity`
      - `numerator`: `10`
      - `page`: `133`
      - `usage`: `131`
    -
      - `key`: `KioskModeMode`
      - `page`: `65524`
      - `usage`: `80`
    -
      - `key`: `KioskModeFullChargeVoltage`
      - `page`: `65524`
      - `usage`: `81`
    -
      - `key`: `KioskModeHighSocSeconds`
      - `page`: `65524`
      - `usage`: `82`
    -
      - `key`: `KioskModeHighSocDays`
      - `page`: `65524`
      - `usage`: `83`
    -
      - `key`: `KioskModeLastHighSocHours`
      - `page`: `65524`
      - `usage`: `84`
    -
      - `key`: `Serial`
      - `page`: `132`
      - `type`: `string`
      - `usage`: `255`
    -
      - `denominator`: `36`
      - `key`: `PackReserve`
      - `numerator`: `10`
      - `page`: `65293`
      - `usage`: `159`
  - `Battery State`:
    -
      - `denominator`: `36`
      - `key`: `NominalChargeCapacity`
      - `numerator`: `10`
      - `page`: `65293`
      - `usage`: `2`
    -
      - `denominator`: `36`
      - `key`: `AppleRawMaxCapacity`
      - `numerator`: `10`
      - `page`: `133`
      - `usage`: `103`
    -
      - `key`: `UISoc`
      - `page`: `133`
      - `usage`: `100`
    -
      - `denominator`: `36`
      - `key`: `AppleRawCurrentCapacity`
      - `numerator`: `10`
      - `page`: `65293`
      - `usage`: `1`
    -
      - `denominator`: `36`
      - `key`: `CurrentCapacity`
      - `numerator`: `10`
      - `page`: `133`
      - `usage`: `102`
    -
      - `key`: `Voltage`
      - `page`: `132`
      - `usage`: `48`
    -
      - `key`: `Amperage`
      - `page`: `132`
      - `usage`: `49`
    -
      - `key`: `VirtualTemperature`
      - `page`: `132`
      - `usage`: `54`
    -
      - `key`: `ChargingVoltage`
      - `page`: `65293`
      - `usage`: `6`
    -
      - `key`: `NotChargingReason`
      - `page`: `65293`
      - `usage`: `56`
    -
      - `key`: `ChargerStatus`
      - `page`: `65293`
      - `usage`: `4097`
    -
      - `key`: `Temperature`
      - `page`: `133`
      - `usage`: `64`
    -
      - `key`: `ChargingCurrent`
      - `page`: `132`
      - `usage`: `65`
    -
      - `key`: `Flags`
      - `page`: `133`
      - `usage`: `69`
    -
      - `key`: `ITMiscStatus`
      - `page`: `65293`
      - `usage`: `115`
    -
      - `key`: `ExternalChargeCapable`
      - `page`: `132`
      - `usage`: `114`
    -
      - `key`: `PresentDODCell0`
      - `page`: `65293`
      - `usage`: `99`
    -
      - `key`: `PresentDODCell1`
      - `page`: `65293`
      - `usage`: `100`
    -
      - `key`: `PresentDODCell2`
      - `page`: `65293`
      - `usage`: `101`
  - `Charging`:
    -
      - `key`: `AdapterVoltage`
      - `page`: `65293`
      - `usage`: `11`
    -
      - `key`: `Current`
      - `page`: `65293`
      - `usage`: `12`
    -
      - `key`: `ExternalConnected`
      - `page`: `133`
      - `type`: `bool`
      - `usage`: `208`
    -
      - `key`: `IsCharging`
      - `page`: `133`
      - `type`: `bool`
      - `usage`: `68`
    -
      - `key`: `FamilyCode`
      - `page`: `65293`
      - `usage`: `57`
    -
      - `key`: `FullyCharged`
      - `page`: `133`
      - `type`: `bool`
      - `usage`: `70`
  - `Cycle Count`:
    -
      - `key`: `CycleCount`
      - `page`: `133`
      - `usage`: `107`
    -
      - `key`: `CycleCountLastQmax`
      - `page`: `65293`
      - `usage`: `48`
  - `Debug Information`:
    -
      - `key`: `FlashWearLevelData`
      - `page`: `65293`
      - `usage`: `257`
    -
      - `key`: `VacVoltageLimit`
      - `page`: `65293`
      - `usage`: `158`
    -
      - `key`: `FirmwareThermalControlEffortCharging`
      - `page`: `65293`
      - `usage`: `258`
  - `Fast Battery Data`:
    -
      - `key`: `InstantAmperage`
      - `page`: `65293`
      - `usage`: `75`
    -
      - `key`: `FirmwarePBat10ms`
      - `page`: `65293`
      - `usage`: `144`
    -
      - `key`: `FirmwarePBat100ms`
      - `page`: `65293`
      - `usage`: `145`
    -
      - `key`: `FirmwareVBat5ms`
      - `page`: `65293`
      - `usage`: `156`
    -
      - `key`: `FirmwareVBat10ms`
      - `page`: `65293`
      - `usage`: `146`
    -
      - `key`: `FirmwareVBat100ms`
      - `page`: `65293`
      - `usage`: `147`
    -
      - `key`: `FirmwareVMonCE`
      - `page`: `65293`
      - `usage`: `148`
    -
      - `key`: `FirmwareVMonIS`
      - `page`: `65293`
      - `usage`: `149`
    -
      - `key`: `FirmwareIBat5ms`
      - `page`: `65293`
      - `usage`: `157`
    -
      - `key`: `FirmwareIBat10ms`
      - `page`: `65293`
      - `usage`: `150`
    -
      - `key`: `FirmwareIBat100ms`
      - `page`: `65293`
      - `usage`: `151`
    -
      - `key`: `FirmwareIMonCE`
      - `page`: `65293`
      - `usage`: `152`
    -
      - `key`: `FirmwareIMonIS`
      - `page`: `65293`
      - `usage`: `153`
    -
      - `key`: `FirmwareVDroopStatus`
      - `page`: `65293`
      - `usage`: `154`
    -
      - `key`: `FirmwareIDroopStatus`
      - `page`: `65293`
      - `usage`: `155`
    -
      - `key`: `Lifetime Cell0 Max Q`
      - `page`: `65293`
      - `usage`: `44`
    -
      - `key`: `Lifetime Cell1 Max Q`
      - `page`: `65293`
      - `usage`: `45`
    -
      - `key`: `Lifetime Cell2 Max Q`
      - `page`: `65293`
      - `usage`: `72`
    -
      - `key`: `QmaxCell0`
      - `page`: `65293`
      - `usage`: `76`
    -
      - `key`: `QmaxCell1`
      - `page`: `65293`
      - `usage`: `77`
    -
      - `key`: `QmaxCell2`
      - `page`: `65293`
      - `usage`: `78`
    -
      - `key`: `BatteryTemperatureMcu`
      - `page`: `65293`
      - `usage`: `68`
    -
      - `key`: `BatteryTemperatureCharger`
      - `page`: `65293`
      - `usage`: `66`
    -
      - `key`: `BatteryTemperatureBuckBoost`
      - `page`: `65293`
      - `usage`: `67`
    -
      - `key`: `BatteryTemperatureBmuTs1`
      - `page`: `65293`
      - `usage`: `69`
    -
      - `key`: `BatteryTemperatureBmuTs2`
      - `page`: `65293`
      - `usage`: `70`
    -
      - `key`: `BatteryTemperatureBmuTs3`
      - `page`: `65293`
      - `usage`: `71`
    -
      - `key`: `Temperature`
      - `page`: `132`
      - `usage`: `54`
    -
      - `denominator`: `36`
      - `key`: `PassedCharge`
      - `numerator`: `10`
      - `page`: `65293`
      - `usage`: `50`
  - `Health`:
    -
      - `key`: `BatteryHealthMaxCapacity`
      - `page`: `65293`
      - `usage`: `63`
    -
      - `key`: `BatteryHealthServiceOption`
      - `page`: `65293`
      - `usage`: `59`
    -
      - `key`: `BatteryHealthServiceFlags`
      - `page`: `65293`
      - `usage`: `60`
    -
      - `key`: `AtCriticalLevel`
      - `page`: `132`
      - `type`: `bool`
      - `usage`: `105`
  - `Lifetime`:
    -
      - `key`: `TotalOperatingTime`
      - `page`: `65293`
      - `usage`: `24`
    -
      - `key`: `MaximumTemperature`
      - `page`: `65293`
      - `usage`: `22`
    -
      - `key`: `MinimumTemperature`
      - `page`: `65293`
      - `usage`: `23`
    -
      - `key`: `MaximumChargeCurrent`
      - `page`: `65293`
      - `usage`: `20`
    -
      - `key`: `MaximumDischargeCurrent`
      - `page`: `65293`
      - `usage`: `21`
    -
      - `key`: `VoltageCell0`
      - `page`: `65293`
      - `usage`: `13`
    -
      - `key`: `VoltageCell1`
      - `page`: `65293`
      - `usage`: `14`
    -
      - `key`: `VoltageCell2`
      - `page`: `65293`
      - `usage`: `15`
    -
      - `key`: `DOD0Cell0`
      - `page`: `65293`
      - `usage`: `96`
    -
      - `key`: `DOD0Cell1`
      - `page`: `65293`
      - `usage`: `97`
    -
      - `key`: `DOD0Cell2`
      - `page`: `65293`
      - `usage`: `98`
    -
      - `key`: `RaTableCell0`
      - `page`: `65293`
      - `usage`: `112`
    -
      - `key`: `RaTableCell1`
      - `page`: `65293`
      - `usage`: `113`
    -
      - `key`: `RaTableCell2`
      - `page`: `65293`
      - `usage`: `114`
    -
      - `key`: `WeightedRaCell0`
      - `page`: `65293`
      - `usage`: `129`
    -
      - `key`: `WeightedRaCell1`
      - `page`: `65293`
      - `usage`: `130`
    -
      - `key`: `WeightedRaCell2`
      - `page`: `65293`
      - `usage`: `131`
    -
      - `key`: `TimeAtHighSoc`
      - `page`: `65293`
      - `usage`: `256`
    -
      - `key`: `ResScale`
      - `page`: `65293`
      - `usage`: `116`
  - `Unknown`:
    -
      - `key`: `WeightedRa`
      - `page`: `65293`
      - `usage`: `52`
- `IOClass`: `IOHIDTranslationService`
- `IOMatchCategory`: `IOHIDTranslationService`
- `IOPersonalityPublisher`: `com.apple.driver.IOHIDPowerSource`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `88`
  - `PrimaryUsagePage`: `65280`
  - `VendorID`: `1452`
- `IOProviderClass`: `IOHIDInterface`
- `Type`: `PowerPack`


## C++ classes (7) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOHIDPowerSource` | 0x90 | AppleCallbackPowerSourceProvider → IOService → IORegistryEntry |
| `IOHIDPowerSourceClient` | 0x20 |  |
| `IOHIDPowerSourceController` | 0x90 | IOService → IORegistryEntry |
| `IOHIDTranslationEvent` | 0x28 |  |
| `IOHIDTranslationEventReq` | 0x20 |  |
| `IOHIDTranslationService` | 0x90 | IOService → IORegistryEntry |
| `IOHIDTranslationServiceClient` | 0x20 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000012f7 off=0x009ff7c0-0x00a00ab7 addr=0xfffffe0007a037c0-0xfffffe0007a04ab7 r--/r--   __TEXT            
	sz=0x00000018 off=0x009ffe88-0x009ffea0 addr=0xfffffe0007a03e88-0xfffffe0007a03ea0               __TEXT.__const            
	sz=0x000007e4 off=0x009ffea0-0x00a00684 addr=0xfffffe0007a03ea0-0xfffffe0007a04684               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000433 off=0x00a00684-0x00a00ab7 addr=0xfffffe0007a04684-0xfffffe0007a04ab7               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00008b5c off=0x031f5e70-0x031fe9cc addr=0xfffffe000a1f9e70-0xfffffe000a2029cc r-x/r-x   __TEXT_EXEC       
	sz=0x000087cc off=0x031f5e70-0x031fe63c addr=0xfffffe000a1f9e70-0xfffffe000a20263c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000390 off=0x031fe63c-0x031fe9cc addr=0xfffffe000a20263c-0xfffffe000a2029cc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000218 off=0x049f3080-0x049f3298 addr=0xfffffe000b9f7080-0xfffffe000b9f7298 rw-/rw-   __DATA            
	sz=0x000000cc off=0x049f3080-0x049f314c addr=0xfffffe000b9f7080-0xfffffe000b9f714c               __DATA.__data             
	sz=0x00000138 off=0x00000000-0x00000138 addr=0xfffffe000b9f7150-0xfffffe000b9f7288               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9f7288-0xfffffe000b9f7298               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00002050 off=0x0139bf48-0x0139df98 addr=0xfffffe000839ff48-0xfffffe00083a1f98 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x0139bf48-0x0139bf68 addr=0xfffffe000839ff48-0xfffffe000839ff68         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x0139bf68-0x0139bf88 addr=0xfffffe000839ff68-0xfffffe000839ff88         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001a78 off=0x0139bf88-0x0139da00 addr=0xfffffe000839ff88-0xfffffe00083a1a00         __DATA_CONST.__const            
	sz=0x00000340 off=0x0139da00-0x0139dd40 addr=0xfffffe00083a1a00-0xfffffe00083a1d40         __DATA_CONST.__kalloc_type      
	sz=0x000001c8 off=0x0139dd40-0x0139df08 addr=0xfffffe00083a1d40-0xfffffe00083a1f08         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000090 off=0x0139df08-0x0139df98 addr=0xfffffe00083a1f08-0xfffffe00083a1f98         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 132 at 0x04af336c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     94C8DA5E-FD60-3487-B1D3-E462D91459FA
008: LC_SOURCE_VERSION           2360.40.13.0.1
009: LC_FUNCTION_STARTS          offset=0x004ac13e0 size=0x138
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOHIDPowerSource`
- `CFBundleIdentifier`: `com.apple.driver.IOHIDPowerSource`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOHIDPowerSource`
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
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHIDPowerSource.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895315008`
- `_PrelinkExecutableRelativePath`: `IOHIDPowerSource`
- `_PrelinkExecutableSize`: `49339`
- `_PrelinkExecutableSourceAddr`: `-2198895315008`
- `_PrelinkKmodInfo`: `-2198828257152`

## Strings (107) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IOHIDTranslationServiceClient`
- `site.IOHIDTranslationServiceClient`
- `usage`
- `value`
- `event`
- `[ERROR] (%s:%#llx): attach failed\n\n`
- `[ERROR] (%s:%#llx): Failed to open %s:0x%llx\n`
- `type`
- `IOReportLegendPublic`
- `(%s:%#llx): start:%d\n`
- `[ERROR] (%s:%#llx): _commandGate\n`
- `[ERROR]getElementValue(usage:0x%x page:0x%x)\n`
- `InterfaceMatching`
- `site.IOHIDPowerSource::IOHIDPowerSource_ivar`
- `1111211`
- `[ERROR] (%s:%#llx): _timerES\n`
- `com.apple.iohid`
- `site.IOHIDTranslationEventReq`
- `[ERROR] (%s:%#llx): _copyEventsReq\n`
- `[ERROR] (%s:%#llx): start failed\n\n`
- `LastTimeStamp`
- `(%s:%#llx): finalize\n`
- `IOHIDTranslationEvent`
- `site.IOHIDPowerSourceController`
- `IOHIDTranslationService`
- `[ERROR] (%s:%#llx): No Events\n`
- `[ERROR] (%s:%#llx): interfaceTerminateNotifier\n`
- `site.IOHIDPowerSource`
- `DebugState`
- `v16@?0^{OSArray=^^?iIIIII^^{OSMetaClassBase}}8`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `12112`
- `121111121222121211`
- `site.IOHIDPowerSourceClient`
- `site.IOHIDTranslationService`
- `[ERROR] (%s:%#llx): Incorrect vent description\n`
- `key`
- `bool`
- `numerator`
- `i8@?0`
- `(%s:%#llx): publish:%s(0x%llx)\n`
- `(%s:%#llx): setInterface:0x%llx\n`
- `[DEBUG] (%s:%#llx): handleInterruptReport reportID:0x%x timeStamp:%lld\n`
- `1111`
- `(%s:%#llx): stop\n`
- `(%s:%#llx): terminate:%s(0x%llx)\n`
- `1211`
- `(%s:%#llx): opened by 0x%llx\n`
- `IOHIDTranslationEventReq`
- `1111111221112`
- `reportSize`
- `[ERROR] (%s:%#llx): addSource\n\n`
- `iohidps`
- `IOReportLegend`
- `reportID`
- `site.IOHIDPowerSourceController::IOHIDPowerSourceController_ivar`
- `[ERROR] (%s:%#llx): No InterfaceMatching dict\n\n`
- `(%s:%#llx): closed by 0x%llx\n`
- `B16@?0^{OSObject=^^?i}8`
- `[DEBUG] (%s:%#llx): logEvent eventValue:%s\n`
- `elements`
- `[ERROR] (%s:%#llx): Could not create IOHIDPowerSource\n\n`
- `site.IOHIDTranslationService::IOHIDTranslationService_ivar`
- `Event`
- `IOHIDInterface`
- `site.IOHIDTranslationEvent`
- `page`
- `IOHIDPowerSourceController`
- `IOHIDPowerSource`
- `[ERROR] (%s:%#llx): _lock\n`
- `Input Reports`
- `timestamp`
- `[ERROR] (%s:%#llx): init failed\n\n`
- `Events`
- `string`
- `IOHIDPS`
- `[ERROR] (%s:%#llx): interfacePublishNotifier\n`
- `IOHIDPowerSourceClient`
- `[ERROR] (%s:%#llx): createReporters\n`
- `denominator`

**[__TEXT.__os_log]**

- `(%s:%#llx): _commandGate\n`
- `(%s:%#llx): _copyEventsReq\n`
- `(%s:%#llx): createReporters\n`
- `(%s:%#llx): finalize\n`
- `(%s:%#llx): interfaceTerminateNotifier\n`
- `(%s:%#llx): start:%d\n`
- `(%s:%#llx): init failed\n\n`
- `(%s:%#llx): Incorrect vent description\n`
- `(%s:%#llx): logEvent eventValue:%s\n`
- `(%s:%#llx): No InterfaceMatching dict\n\n`
- `(%s:%#llx): publish:%s(0x%llx)\n`
- `(%s:%#llx): terminate:%s(0x%llx)\n`
- `(%s:%#llx): No Events\n`
- `(%s:%#llx): handleInterruptReport reportID:0x%x timeStamp:%lld\n`
- `getElementValue(usage:0x%x page:0x%x)\n`
- `(%s:%#llx): _timerES\n`
- `(%s:%#llx): interfacePublishNotifier\n`
- `(%s:%#llx): stop\n`
- `(%s:%#llx): Could not create IOHIDPowerSource\n\n`
- `(%s:%#llx): attach failed\n\n`
- `(%s:%#llx): start failed\n\n`
- `(%s:%#llx): closed by 0x%llx\n`
- `(%s:%#llx): Failed to open %s:0x%llx\n`
- `(%s:%#llx): addSource\n\n`
- `(%s:%#llx): _lock\n`
- `(%s:%#llx): opened by 0x%llx\n`
- `(%s:%#llx): setInterface:0x%llx\n`

# `com.apple.driver.ApplePhoneBTM`

- Name: ApplePhoneBTM
- Version: `1.0.1`
- UUID: `668D122A-46A0-3A75-9D71-BF9EC1FACE14`
- Source version: `223.40.1.0.1`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.ApplePMGR`](com.apple.driver.ApplePMGR.md) 1.0, [`com.apple.driver.AppleSMC`](com.apple.driver.AppleSMC.md) 1.0.0, [`com.apple.driver.IOHIDPowerSource`](com.apple.driver.IOHIDPowerSource.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `AppleBTM` | `btm,phone` |

## IOKit personalities (3) [KC]

### AppleBPIC
- `CFBundleIdentifier`: `com.apple.driver.ApplePhoneBTM`
- `IOClass`: `AppleBPIC`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleBPIC`
- `IONameMatch`: `btm,bpic`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePhoneBTM`
- `IOProviderClass`: `AppleARMSPMIDevice`

### ApplePMGRBTM
- `CFBundleIdentifier`: `com.apple.driver.ApplePhoneBTM`
- `IOClass`: `AppleBTM`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleBTMPMGR`
- `IONameMatch`: `btm,pmgr`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePhoneBTM`
- `IOProviderClass`: `ApplePMGRNub`

### ApplePhoneBTM
- `CFBundleIdentifier`: `com.apple.driver.ApplePhoneBTM`
- `IOClass`: `AppleBTM`
- `IOKitDebug`: `65535`
- `IOMatchCategory`: `AppleBTM`
- `IONameMatch`: `btm,phone`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePhoneBTM`
- `IOProviderClass`: `AppleARMSPMIDevice`


## C++ classes (28) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleATVAintreeBTM` | 0x248 | AppleSeraBTM → AppleBTMPMUAgent |
| `AppleAintreeBTM` | 0x250 | AppleCotaBTM → AppleBTMPMUAgent |
| `AppleAvusBTM` | 0x238 | AppleBTMPMUAgent |
| `AppleBPIC` | 0xe0 | IOHIDDevice → IOService → IORegistryEntry |
| `AppleBTM` | 0xf0 | IOHIDDevice → IOService → IORegistryEntry |
| `AppleBTMAONPMUAgent` | 0x2a0 | AppleBTMPMUAgent |
| `AppleBTMBPICAgent` | 0x38 |  |
| `AppleBTMBatteryDataAgent` | 0x1caa0 |  |
| `AppleBTMDataClient` | 0x48 |  |
| `AppleBTMDataClientPPM` | 0x50 | AppleBTMDataClient |
| `AppleBTMDataClientSMC` | 0x50 | AppleBTMDataClient |
| `AppleBTMFunction` | 0x40 | AppleARMFunction |
| `AppleBTMPMUAgent` | 0x230 |  |
| `AppleBakuBTM` | 0x250 | AppleCotaBTM → AppleBTMPMUAgent |
| `AppleBakuBTM2` | 0x250 | AppleBakuBTM → AppleCotaBTM → AppleBTMPMUAgent |
| `AppleCotaBTM` | 0x250 | AppleBTMPMUAgent |
| `AppleCplBTM` | 0x248 | AppleSeraBTM → AppleBTMPMUAgent |
| `AppleEstBTM` | 0x250 | AppleCotaBTM → AppleBTMPMUAgent |
| `AppleFermiumBTM` | 0x2d8 | AppleBTMPMUAgent |
| `AppleMaverickBTM` | 0x248 | AppleSeraBTM → AppleBTMPMUAgent |
| `ApplePassThroughBakuBTM` | 0x248 | AppleSeraBTM → AppleBTMPMUAgent |
| `ApplePassThroughEstBTM` | 0x248 | AppleSeraBTM → AppleBTMPMUAgent |
| `AppleSeraBTM` | 0x248 | AppleBTMPMUAgent |
| `AppleSeraBTMiPad` | 0x250 | AppleSeraBTM → AppleBTMPMUAgent |
| `AppleStonehengeBPIC` | 0xe0 | AppleBTMBPICAgent |
| `AppleStoweBTM` | 0x248 | AppleSeraBTM → AppleBTMPMUAgent |
| `AppleStoweBTMiPad` | 0x250 | AppleSeraBTMiPad → AppleSeraBTM → AppleBTMPMUAgent |
| `AppleStoweBTMxr` | 0x250 | AppleStoweBTMiPad → AppleSeraBTMiPad → AppleSeraBTM → AppleBTMPMUAgent |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000560b off=0x006b4eb0-0x006ba4bb addr=0xfffffe00076b8eb0-0xfffffe00076be4bb r--/r--   __TEXT            
	sz=0x000041b3 off=0x006b5618-0x006b97cb addr=0xfffffe00076b9618-0xfffffe00076bd7cb               __TEXT.__cstring          (CstringLiterals)
	sz=0x000005f0 off=0x006b97d0-0x006b9dc0 addr=0xfffffe00076bd7d0-0xfffffe00076bddc0               __TEXT.__const            
	sz=0x000006fb off=0x006b9dc0-0x006ba4bb addr=0xfffffe00076bddc0-0xfffffe00076be4bb               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00019e08 off=0x023c2f10-0x023dcd18 addr=0xfffffe00093c6f10-0xfffffe00093e0d18 r-x/r-x   __TEXT_EXEC       
	sz=0x00019a38 off=0x023c2f10-0x023dc948 addr=0xfffffe00093c6f10-0xfffffe00093e0948          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003d0 off=0x023dc948-0x023dcd18 addr=0xfffffe00093e0948-0xfffffe00093e0d18          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000066c off=0x04984b28-0x04985194 addr=0xfffffe000b988b28-0xfffffe000b989194 rw-/rw-   __DATA            
	sz=0x00000177 off=0x04984b28-0x04984c9f addr=0xfffffe000b988b28-0xfffffe000b988c9f               __DATA.__data             
	sz=0x00000470 off=0x00000000-0x00000470 addr=0xfffffe000b988ca0-0xfffffe000b989110               __DATA.__common           (Zerofill)
	sz=0x00000084 off=0x00000000-0x00000084 addr=0xfffffe000b989110-0xfffffe000b989194               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00004760 off=0x0119fb20-0x011a4280 addr=0xfffffe00081a3b20-0xfffffe00081a8280 rw-/rw-   __DATA_CONST      
	sz=0x000000d8 off=0x0119fb20-0x0119fbf8 addr=0xfffffe00081a3b20-0xfffffe00081a3bf8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x000000d8 off=0x0119fbf8-0x0119fcd0 addr=0xfffffe00081a3bf8-0xfffffe00081a3cd0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003b20 off=0x0119fcd0-0x011a37f0 addr=0xfffffe00081a3cd0-0xfffffe00081a77f0         __DATA_CONST.__const            
	sz=0x00000740 off=0x011a37f0-0x011a3f30 addr=0xfffffe00081a77f0-0xfffffe00081a7f30         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x011a3f30-0x011a3fd0 addr=0xfffffe00081a7f30-0xfffffe00081a7fd0         __DATA_CONST.__kalloc_var       
	sz=0x000001e8 off=0x011a3fd0-0x011a41b8 addr=0xfffffe00081a7fd0-0xfffffe00081a81b8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000c0 off=0x011a41b8-0x011a4278 addr=0xfffffe00081a81b8-0xfffffe00081a8278         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x011a4278-0x011a4280 addr=0xfffffe00081a8278-0xfffffe00081a8280         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 146 at 0x04ae2730
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     668D122A-46A0-3A75-9D71-BF9EC1FACE14
008: LC_SOURCE_VERSION           223.40.1.0.1
009: LC_FUNCTION_STARTS          offset=0x004aad0a8 size=0x500
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePhoneBTM`
- `CFBundleIdentifier`: `com.apple.driver.ApplePhoneBTM`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePhoneBTM`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePhoneBTM.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898766160`
- `_PrelinkExecutableRelativePath`: `ApplePhoneBTM`
- `_PrelinkExecutableSize`: `147935`
- `_PrelinkExecutableSourceAddr`: `-2198898766160`
- `_PrelinkKmodInfo`: `-2198828709080`

## Strings (543) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `voltage-thresholds_mV`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to config PMU. ret: 0x%08X\" @%s:%d`
- `virtual bool AppleBPIC::start(IOService *)`
- `config-fixed-PMU-rate-flag`
- `site.AppleATVAintreeBTM`
- `AppleAintreeBTM`
- `ApplePMUFirmwareDriver`
- `IOReturn AppleBTMAONPMUAgent::readWorstCaseData(uint32_t)`
- `Flags`
- `site.AppleCplBTM`
- `AppleBakuBTM2::start (%p)\n`
- `AppleBTMBatteryDataAgent: UseSamplingThreshold %s`
- `getValidDataBit`
- `_interruptFIFOThreshold`
- `ApplePassThroughEstBTM::start (%p)\n`
- `1211111222222222222222222221211222222222222222222222222222222222222222222222222222222222111`
- `RSS`
- `1211122`
- `_ppmMatchingNotifier`
- `AppleBTMBatteryDataAgent::start (%p)\n`
- `AppleBTMPMUAgent::free\n`
- `btm-pmu-type`
- `APPL`
- `readBatteryData`
- `site.AppleSeraBTM`
- `SPMI`
- `AppleStoweBTMiPad::start (%p)\n`
- `bool AppleBTMBPICAgent::initWithParent(AppleBPIC *, IOService *)`
- `enabled`
- `IOReturn AppleCotaBTM::PMUInterruptHandler(IOInterruptEventSource *, int)`
- `FirmwareIBat5ms`
- `_interrupt_GLOBAL_STBY_INT`
- `AppleStoweBTM::start (%p)\n`
- `AppleBTM::start\n`
- `virtual IOReturn AppleBTMFunction::callFunction(void *, void *, void *)`
- `virtual bool AppleFermiumBTM::initWithProvider(IOService *)`
- `AppleBTMPMUAgent`
- `ITMiscStatus`
- `\"AppleBTM: %s:%u \" \"REQUIRE failed: %s\" @%s:%d`
- `AppleMaverickBTM::start (%p)\n`
- `value`
- `void AppleBTMBatteryDataAgent::asbArrivalHandler(void *, IOService *, IONotifier *)`
- `AppleCplBTM`
- `AppleCplBTM::start (%p)\n`
- `AppleBPIC.cpp`
- `AppleBTMDataClientPPM`
- `IOReturn AppleCotaBTM::readPICtrl()`
- `AppleSeraBTM::start success\n`
- `CurrentCapacity`
- `_commandLock`
- `packCountNum != nullptr`
- `ChemID`
- `site.AppleAintreeBTM`
- `virtual IOReturn AppleBPIC::newReportDescriptor(IOMemoryDescriptor **) const`
- `\"AppleBTM: %s:%u \" \"AppleBTM: BPIC V Hysteresis EDT value out of range %u\" @%s:%d`
- `data`
- `_interrupt_SNS_LP_INT`
- `btm: %s batteryDataProvider:%d\n`
- `static AppleCplBTM *AppleCplBTM::withParent(AppleBTM *, IOService *)`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: spec input is NULL\" @%s:%d`
- `site.AppleBTMDataClientSMC`
- `ChargingCurrent`
- `AppleBTMDataClientSMC.cpp`
- `static AppleStonehengeBPIC *AppleStonehengeBPIC::withParent(AppleBPIC *, IOService *)`
- `_packEntries`
- `AppleCplBTM.cpp`
- `AppleBakuBTM2`
- `VoltageCell0`
- `ExternalConnected`
- `static AppleBTMAONPMUAgent *AppleBTMAONPMUAgent::withParent(AppleBTM *, IOService *)`
- `12111121`
- `VoltageCell2`
- `AppleATVAintreeBTM`
- `bankArray`
- `AppleBTMDataClient`
- `FirmwarePBat100ms`
- `instance`
- `PPMParametersHF`
- `BatteryTemperatureCharger`
- `_interrupt_SNS_HP_INT`
- `AppleStoweBTMiPad.cpp`
- `AppleFermiumBTM`
- `static AppleStoweBTMxr *AppleStoweBTMxr::withParent(AppleBTM *, IOService *)`
- `VirtualTemperature`
- `config-vddmain-data-read`
- `values[i] < kAppleBTMDataClientCount`
- `site.AppleSeraBTMiPad`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to clear/ack SPMI event\" @%s:%d`
- `parent`
- `pmu-filter-spec`
- `FirmwareVBat100ms`
- `bool AppleBTM::getDTProperty(const char *, uint32_t *, IOService *)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read Dynamic Agent data from PMU. ret: 0x%08X\" @%s:%d`
- `AppleBTMBatteryDataAgent::start success\n`
- `pmuSampleSpecLen > 0`
- `AppleAvusBTM`
- `PmaxOCV`
- `AppleSmartBatteryPack`
- `batteryDataConsumption`
- `arr`
- `_batteryPowerCallbackEvent`
- `btm->_batteryDataAgent`
- `number-of-PMUs`
- `low-voltage-residency`
- `ApplePPMCPMS`
- `void AppleBTMAONPMUAgent::ApplePMUSecondaryDriverArrivalHandler(void *, IOService *, IONotifier *)`
- `packEntry`
- `AppleBTM: unable to update PMU ret: 0x%08X`
- `site.AppleFermiumBTM`
- `AppleCotaBTM::start success\n`
- `site.AppleBTMDataClientPPM`
- `matchDict`
- `site.AppleBTMBatteryDataAgent`
- `use-sampling-thresholds`
- `121111121222121211211122211111`
- `PMUName`
- `current-thresholds_mA`
- `IOReturn AppleSeraBTMiPad::readDutyCycles()`
- `AppleCotaBTM::start (%p)\n`
- `service`
- `static AppleAvusBTM *AppleAvusBTM::withParent(AppleBTM *, IOService *)`
- `AppleStoweBTMiPad`
- `ApplePassThroughBakuBTM.cpp`
- `_parent->getDTPropertyArray(kBTMVoltageThresholds_mV, &values, &size, _provider)`
- `bpic-V-hysteresis-override`
- `virtual IOReturn AppleFermiumBTM::configSampling()`
- `AppleBTMDataClient.cpp`
- `ppm->_event`
- `overrideInitialConfig`
- `void AppleBTMBatteryDataAgent::initSamplingThreshold()`
- `_bankEntries`
- `AppleSeraBTM`
- `_interrupt_DMT_OVFL_INT`
- `AppleStonehengeBPIC::start (%p)\n`
- `AppleBTMBatteryDataAgent.cpp`
- `AppleStoweBTMxr::%s\n`
- `packIDNum != nullptr`
- `static AppleBakuBTM2 *AppleBakuBTM2::withParent(AppleBTM *, IOService *)`
- `virtual IOReturn AppleSeraBTMiPad::configSampling()`
- `_hidReportBuffer`
- `com.apple.private.btm.client`
- `_ptdReadMultFunction`
- `AppleSeraBTMiPad::start (%p)\n`
- `_interrupt_VCELL_WARN_INT`
- `IOReturn AppleBTMAONPMUAgent::readDynamicAgentData()`
- `haveSamplesExceededVIThreshold`
- `\"AppleBTM: %s:%u \" \"Invalid context\" @%s:%d`
- `IOReturn AppleFermiumBTM::reconfigureSampling(uint32_t, uint32_t)`
- `IOReturn AppleSeraBTM::readPICtrl()`
- `virtual bool AppleBTM::start(IOService *)`
- `_bpicAgent`
- `bool AppleBPIC::getDTProperty(const char *, uint32_t *, IOService *)`
- `AppleSMC`
- `static AppleAintreeBTM *AppleAintreeBTM::withParent(AppleBTM *, IOService *)`
- `initWithParent`
- `AppleBTMBatteryDataAgent::Pack %d Null dict passed`
- `UISoc`
- `AppleBTMBatteryDataAgent::ASBM arrival success\n`
- `QmaxCell0`
- `AppleStoweBTMxr`
- `AppleStoweBTMxr::start success\n`
- `site.AppleAvusBTM`
- `virtual IOReturn AppleBTMAONPMUAgent::updateVthresold(uint32_t, uint8_t)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read filters buffer from PMU. ret: 0x%08X\" @%s:%d`
- `VoltageCell1`
- `AppleStonehengeBPIC.cpp`
- `ApplePassThroughBakuBTM::start (%p)\n`
- `AppleStoweBTM.cpp`
- `AppleATVAintreeBTM::start success\n`
- `FirmwareVDroopStatus`
- `_interrupt_BP_PROT_ACTV_INT`
- `AppleStoweBTM::start success\n`
- `IOReturn AppleBTMAONPMUAgent::readFilterData(uint32_t)`
- `AppleBTMBPICAgent`
- `matchingDict`
- `\"AppleBTM: %s:%u \" \"Offset %d is not within results_buffer bounds\" @%s:%d`
- `size`
- `12111112222222222222222222212112222222222222222222222222222222222222221`
- `AppleEstBTM::start (%p)\n`
- `AppleEstBTM.cpp`
- `121111122222222222222222222121122222222222222222222222222222222222222211111221111122`
- `static AppleFermiumBTM *AppleFermiumBTM::withParent(AppleBTM *, IOService *)`
- `ppm->isEnabled()`
- `PresentDODCell2`
- `event`
- `AppleEstBTM`
- `secondary-pmu-name`
- `CaptureTime`
- `ApplePassThroughEstBTM.cpp`
- `IOReturn AppleSeraBTM::readFilterData()`
- `WeightedRaCell2`
- `AppleBTMPMUAgent.cpp`
- `success`
- `site.pmuDataLayout`
- `ret == true`
- `_bpicSampleTimer`
- `BatteryTemperatureBmuTs2`
- `BankID`
- `ID`
- `bankCount > 0`
- `IOReturn AppleCotaBTM::readLowVoltageResidency()`
- `_event`
- `1211112221`
- `_interrupt_BP_PMAX_INT`
- `\"AppleBTM: %s:%u \" \"Unsupported battery data provider: %d\\n\" @%s:%d`
- `setValidDataBit`
- `i8@?0`
- `num-dod-percent-segments`
- `AppleBPIC::free\n`
- `AppleBTM: unable to config BPIC. ret: 0x%08X \n`
- `IOReturn AppleBTMAONPMUAgent::readPICtrl(uint32_t)`
- `AppleBTMBatteryDataAgent`
- `AppleSeraBTMiPad::start success\n`
- `numDODSegments > 0 && numDODSegments <= MAX_NUM_DOD_SEGMENTS`
- `Timestamp`
- `void AppleBTMDataClient::publish(void *)`
- `bool AppleBTM::getDTPropertyString(const char *, const char **, IOService *)`
- `BDAOperationMode`
- `arrived == false`
- `static void AppleBTMBatteryDataAgent::batteryProviderDataCallback(void *, const OSSymbol *, OSDictionary *)`
- `_spmiDevice`
- `initWithProvider`
- `\"AppleBTM: %s:%u \" \"getPmuSampleSpec returned NULL\" @%s:%d`
- `site.AppleBakuBTM2`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to reset worst case I/V buffer. ret: 0x%08X\" @%s:%d`
- `packIter`
- `AppleBTM: unable to config new Vthreshold proportional target. ret: 0x%08X`
- `site.AppleBTM`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read Duty Cycle data from PMU. ret: 0x%08X\" @%s:%d`
- `AppleFermiumBTM.cpp`
- `AppleBTMDataClientSMC`
- `target`
- `provider`
- `AppleT8030BTM::start success\n`
- `\"AppleBTM: %s:%u \" \"Failed to init data client %d\\n\" @%s:%d`
- `bankIDNum != nullptr`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read Battery data from PMU. ret: 0x%08X\" @%s:%d`
- `site.AppleBTMPMUAgent`
- `_pmgrNub`
- `AppleBTMBatteryDataAgent::free\n`
- `eventType`
- `btm-bpic-type`
- `AppleFermiumBTM::start (%p)\n`
- `1211111222222222222222222221211222222222222222222222222222222222222222`
- `key`
- `AppleBTMBatteryDataAgent::Pack %d failed to get %s`
- `static AppleBTMBatteryDataAgent *AppleBTMBatteryDataAgent::withParent(AppleBTM *, IOService *)`
- `count <= kAppleBTMDataClientCount`
- `AppleStoweBTM`
- `enable-PI-Ctrl-max-func`
- `descriptor`
- `virtual bool AppleBTMAONPMUAgent::initWithProvider(IOService *)`
- `AppleBTMDataClientPPM.cpp`
- `_batteryDataAgent`
- `\"AppleBTM: %s:%u \" \"Failed to create data client %d\\n\" @%s:%d`
- `void AppleBTMPMUAgent::ppmArrivalHandler(IOService *)`
- `1211122111111111111111111111`
- `IOReturn AppleStonehengeBPIC::ICELL_ERR_INT_Handler(IOInterruptEventSource *, int)`
- `ApplePassThroughEstBTM`
- `virtual bool AppleCotaBTM::initWithProvider(IOService *)`
- `virtual IOReturn AppleCotaBTM::resetWorstCaseIVTrigger()`
- `virtual IOReturn AppleBTMDataClientSMC::initialize(IOService *, OSObject *)`
- `IOReturn AppleStonehengeBPIC::ICELL_WARN_INT_Handler(IOInterruptEventSource *, int)`
- `static AppleMaverickBTM *AppleMaverickBTM::withParent(AppleBTM *, IOService *)`
- `config-duty-cycle-data-read`
- `AppleT8030BTM::start (%p)\n`
- `AppleBakuBTM::start success\n`
- `Voltage`
- `1211111222222222222222222221211222222222222222222222222222222222222222121`
- `AppleBTMAONPMUAgent`
- `IOReturn AppleBTMAONPMUAgent::readVddMainData(uint32_t)`
- `_batteryWorkLoop`
- `IOReturn AppleStonehengeBPIC::VCELL_WARN_INT_Handler(IOInterruptEventSource *, int)`
- `IOReturn AppleBTMAONPMUAgent::readDutyCycleData(uint32_t)`
- `void AppleBTMBatteryDataAgent::findPackEntries()`
- `AppleSeraBTMiPad`
- `virtual IOReturn AppleCotaBTM::configSampling()`
- `site.AppleMaverickBTM`
- `_parent->getDTPropertyArray(kBTMDODPercentSegmentBreakPoints, &values, &size, _provider)`
- `ret == kIOReturnSuccess`
- `BatteryDataCollectionReady`
- `agent`
- `AppleBTMFunction`
- `static AppleSeraBTMiPad *AppleSeraBTMiPad::withParent(AppleBTM *, IOService *)`
- `site.AppleCotaBTM`
- `_interrupt_BP_ORFUNCT1_TEMP_INT`
- `AppleBTM`
- `_workLoop`
- `virtual IOReturn AppleBTMDataClientPPM::publishSynchronous(OSArray *)`
- `12111112222222222222222222212112222222222222222222222222222222222222221212`
- `IOReturn AppleStonehengeBPIC::BST_ERR_INT_Handler(IOInterruptEventSource *, int)`
- `AppleBTMAONPMUAgent.cpp`
- `primary-pmu-name`
- `smc->_client`
- `_interrupt_BST_ERR_INT`
- `pmu-main`
- `AppleBakuBTM::start (%p)\n`
- `AppleBTM: unable to write new Vthreshold integrator target. ret: 0x%08X`
- `AppleStoweBTMxr::start (%p)\n`
- `FirmwareThermalControlEffortCharging`
- `site.AppleBakuBTM`
- `_interrupt_GLOBAL_RDY_INT`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read Worst Case data from PMU. ret: 0x%08X\" @%s:%d`
- `LPEMData`
- `FirmwareVMonCE`
- `AppleBTMBatteryDataAgent::Pack %d failed to get PresentDOD`
- `void AppleBTMBatteryDataAgent::batteryProviderArrivalHandler(void *, IOService *, IONotifier *)`
- `void AppleBTMBatteryDataAgent::initDataClients()`
- `bankCountNum != nullptr`
- `ApplePassThroughEstBTM::start success\n`
- `batteryDataCapability`
- `disabled`
- `AppleBTMBatteryDataAgent::Pack %d failed to get data from key %s`
- `AppleBTMFunction.cpp`
- `site.ApplePassThroughEstBTM`
- `virtual bool AppleStonehengeBPIC::initWithProvider(IOService *)`
- `static AppleBakuBTM *AppleBakuBTM::withParent(AppleBTM *, IOService *)`
- `IOReturn AppleCotaBTM::readDutyCycles()`
- `site.AppleBTMDataClient`
- `IOReturn AppleSeraBTM::PMUInterruptHandler(IOInterruptEventSource *, int)`
- `static void AppleBTMDataClientPPM::eventHandler(OSObject *, IOInterruptEventSource *, int)`
- `client`
- `site.AppleStonehengeBPIC`
- `AppleEstBTM::start success\n`
- `ApplePMUFWDSetCPMSRate`
- `dod-segment-breakpoints`
- `static AppleSeraBTM *AppleSeraBTM::withParent(AppleBTM *, IOService *)`
- `virtual bool AppleAvusBTM::initWithProvider(IOService *)`
- `site.AppleStoweBTMiPad`
- `virtual IOReturn AppleBTMDataClientPPM::initialize(IOService *, OSObject *)`
- `BatteryTemperatureBuckBoost`
- `BTM`
- `AppleBTMAONPMUAgent::start (%p)\n`
- `offset < sizeof(results_buffer.filtered)`
- `AppleSeraBTM::start (%p)\n`
- `AlgoTemperature`
- `PresentDODCell1`
- `static AppleStoweBTM *AppleStoweBTM::withParent(AppleBTM *, IOService *)`
- `site.AppleEstBTM`
- `\"AppleBTM: %s:%u \" \"Invalid specLen %d\" @%s:%d`
- `static AppleEstBTM *AppleEstBTM::withParent(AppleBTM *, IOService *)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to clear/ack SPMI event. ret: 0x%08X\" @%s:%d`
- `AppleBTM: unable to config new Duty Cycler threshold value. ret: 0x%08X`
- `bpic-revision-num`
- `QmaxCell1`
- `_interrupt_BST_UV_INT`
- `BatteryTemperatureBmuTs3`
- `config-auto-rate-change-flag`
- `virtual IOReturn AppleBTM::newReportDescriptor(IOMemoryDescriptor **) const`
- `_asbmSampleTimer`
- `void AppleBTMBatteryDataAgent::findBankEntries(uint32_t)`
- `AppleCplBTM::start success\n`
- `AppleBTM.cpp`
- `AppleStonehengeBPIC`
- `BankBatteryData`
- `FirmwareVMonIS`
- `IOReturn AppleBTMBPICAgent::configBPICHysteresisOverride(uint32_t)`
- `_interrupt_BST_WIRE_INT`
- `AppleMaverickBTM.cpp`
- `BootPathUpdated`
- `AppleSeraBTM.cpp`
- `_interrupt_CHOKE_INT`
- `AppleBTMBPICAgent.cpp`
- `AppleATVAintreeBTM.cpp`
- `DataCaptureTrigger`
- `AppleCotaBTM.cpp`
- `void AppleBTMAONPMUAgent::ApplePMUDriverArrivalHandler(void *, IOService *, IONotifier *)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read vddmain data from PMU. ret: 0x%08X\" @%s:%d`
- `loadPMUFilterSpec`
- `pmuSampleSpec`
- `static AppleStoweBTMiPad *AppleStoweBTMiPad::withParent(AppleBTM *, IOService *)`
- `bool AppleBTMPMUAgent::initWithParent(AppleBTM *, IOService *)`
- `AppleBTMBPICAgent::free\n`
- `121111222`
- `collection`
- `smc && smc->isEnabled()`
- `static AppleATVAintreeBTM *AppleATVAintreeBTM::withParent(AppleBTM *, IOService *)`
- `AppleCotaBTM`
- `FirmwareIMonCE`
- `AppleSmartBatteryBank`
- `static ApplePassThroughEstBTM *ApplePassThroughEstBTM::withParent(AppleBTM *, IOService *)`
- `virtual IOReturn AppleCotaBTM::readSamples()`
- `_interruptFIFO_FULL`
- `site.HIDReportBuffer`
- `_interrupt_TEMP_WARN_INT`
- `AppleBTMAONPMUAgent::start success\n`
- `AppleFermiumBTM::start success\n`
- `smc->_event`
- `_interrupt_ICELL_WARN_INT`
- `AppleStonehengeBPIC::start success\n`
- `static ApplePassThroughBakuBTM *ApplePassThroughBakuBTM::withParent(AppleBTM *, IOService *)`
- `bool AppleBTM::isDTPropertyPresent(const char *, IOService *)`
- `FirmwareIBat10ms`
- `AppleMaverickBTM::start success\n`
- `disable-pmu-filtered-data-read`
- `_interrupt_VCELL_ERR_INT`
- `_pmuAgent`
- `AppleAintreeBTM::start success\n`
- `PresentDOD`
- `virtual IOReturn AppleSeraBTMiPad::readSamples()`
- `AppleBPIC::start\n`
- `_interruptFIFOUnderflow`
- `FirmwareIMonIS`
- `configSampling`
- `FirmwareIBat100ms`
- `DOD0Cell0`
- `DOD0Cell1`
- `QmaxCell2`
- `_serviceNotifier`
- `site.AppleBTMAONPMUAgent`
- `size / sizeof(*values) == numDODSegments`
- `bool AppleBTMBatteryDataAgent::initWithParent(AppleBTM *, IOService *)`
- `BatteryPackCount`
- `packID < packCount`
- `AppleBakuBTM2::start success\n`
- `Amperage`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read PI controller data from PMU. ret: 0x%08X\" @%s:%d`
- `ApplePMUFWDSetCPMSVDDDroopThreshold`
- `battery-data-clients`
- `site.AppleBTMFunction`
- `dataAgent`
- `ApplePassThroughBakuBTM`
- `static bool AppleBTMDataClientSMC::serviceMatchNotification(void *, void *, IOService *, IONotifier *)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to stop config PMU. ret: 0x%08X\" @%s:%d`
- `static bool AppleBTMDataClientPPM::serviceMatchNotification(void *, void *, IOService *, IONotifier *)`
- `site.ApplePassThroughBakuBTM`
- `_pmuSampleTimer`
- `_parent->getDTPropertyArray(kBTMCurrentThresholds_mA, &values, &size, _provider)`
- `PresentDODCell0`
- `AppleMaverickBTM`
- `AppleSmartBattery`
- `_interrupt_BST_BPIC_INT`
- `AppleBTM: unable to config PMU. ret: 0x%08X \n`
- `AppleAintreeBTM::start (%p)\n`
- `ApplePMUFWDUCHostIRQ`
- `1211111212221212112111222111`
- `void AppleBTMPMUAgent::initializePmuSampleSpec(int, const pmuDataLayout *)`
- `InstantAmperage`
- `BankCount`
- `FirmwareVBat10ms`
- `ApplePassThroughBakuBTM::start success\n`
- `function_ptd_read_mult`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read duty cycle from PMU. ret: 0x%08X\" @%s:%d`
- `AppleBPIC`
- `DOD0Cell2`
- `AppleStoweBTMxr.cpp`
- `\"AppleBTM: %s:%u \" \"Invalid battery data: client: %d _invalid: %u _total: %u\\n\" @%s:%d`
- `packCount > 0 && packCount <= MAX_NUM_BATTERIES`
- `virtual IOReturn AppleFermiumBTM::stopSampling()`
- `_interrupt_ICELL_ERR_INT`
- `IOReturn AppleStonehengeBPIC::VCELL_ERR_INT_Handler(IOInterruptEventSource *, int)`
- `IOReturn AppleStonehengeBPIC::BP_VCELL_DUTY_INT_Handler(IOInterruptEventSource *, int)`
- `index < _numPMUs`
- `static AppleCotaBTM *AppleCotaBTM::withParent(AppleBTM *, IOService *)`
- `_interrupt_SNS_ULP_INT`
- `pmu-secondary`
- `AppleBTMBatteryDataAgent: No EDT entries for DOD-based thresholds. Using defaults`
- `AppleStoweBTMiPad::start success\n`
- `AppleAintreeBTM.cpp`
- `_batteryDataProvider`
- `_asbm`
- `AppleBakuBTM.cpp`
- `refcon`
- `battery-data-collection`
- `IOHIDPowerSource`
- `site.AppleBPIC`
- `_parent->getWorkLoop()`
- `AppleBTM::free\n`
- `bool AppleBTM::getDTPropertyArray(const char *, uint32_t **, uint32_t *, IOService *)`
- `AppleAvusBTM.cpp`
- `_interruptPMUbtm[idx]`
- `packIndex < _packEntries->getCount()`
- `BPIC`
- `BatteryTemperatureBmuTs1`
- `BatteryData`
- `static void AppleBTMDataClientSMC::eventHandler(OSObject *, IOInterruptEventSource *, int)`
- `eventData`
- `AppleSeraBTMiPad.cpp`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: length %d exceeds maximum %d\" @%s:%d`
- `IOReturn AppleStonehengeBPIC::BP_ORFUNCT1_TEMP_INT_Handler(IOInterruptEventSource *, int)`
- `site.AppleStoweBTM`
- `AppleATVAintreeBTM::start (%p)\n`
- `AppleBakuBTM`
- `_interruptPMU`
- `virtual bool AppleSeraBTM::initWithProvider(IOService *)`
- `isEnabled()`
- `FirmwarePBat10ms`
- `site.AppleStoweBTMxr`
- `name`
- `WeightedRaCell0`
- `WeightedRaCell1`
- `IsCharging`
- `%s::Init failed, error in loading PMU filter spec\n`
- `FirmwareVBat5ms`
- `_interrupt_BP_VCELL_DUTY_INT`
- `_numPMUs <= MAX_PMU`
- `_batteryProviderNotifier`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: length == 0\" @%s:%d`
- `ResScale`
- `BatteryTemperatureMcu`
- `site.AppleBTMBPICAgent`
- `config-worst-case-data-read`

**[__TEXT.__os_log]**

- `%s: Invalid dstId %d (max supported %d)\n`
- `null battery data`
- `null bankArray for pack %d`
- `ASBM not ready yet (kBootPathKey)`
- `%s: Invalid srcId %d (max supported %d)\n`
- `Null Battery Array`
- `failed to create bank arrays for pack %d`
- `%s: Using default primary PMU driver name: %s\n`
- `%s: Failed to allocate memory for EDT PMU spec\n`
- `failed to create batteryArray`
- `BTM: Reconfigure Sampling`
- `%s: Result Buffer Index[%d]: Filter Index[%d], Report Index[%d], Scale=%d\n`
- `btm: dataClients[%d] disabled\n`
- `kBootPathKey still 0`
- `null _packEntries`
- `BTM: Start Sampling`
- `%s: Using primary PMU driver name from EDT: %s\n`
- `BTM: batteryDataArray allocation failed`
- `non IOService bank entry at index %d for pack %d`
- `%s: Using secondary PMU driver name from EDT: %s\n`
- `%s: Unable to set PMU 1 sample rate to %ums (retStatus : 0x%08X)`
- `%s: No provider available to access EDT properties\n`
- `%s: EDT config error, pmu-filter-spec array count %d is 0 or not multiple of %d\n`
- `Pack %d: vi_t %u dod %u dod_t %d c %d last_c %d c_diff %d v_t %d v %d last_v %d v_diff %d`
- `non IOService entry at index %d`
- `%s: _pmuDriver is NULL`
- `BTM: %s Invalid pack index %d`
- `BTM: batteryTimeSeriesArray allocation failed for pack %d`
- `null HF data`
- `null BatteryData for bank %d pack %d`
- `BTM: Stop Sampling`
- `%s: Using default secondary PMU driver name: %s\n`
- `%s: Invalid scale %d (must be greater than 0)\n`
- `DOD breakpoint %d current threshold %d voltage threshold %d`
- `Pack %d: Full mode capture %d %d force_sym %d f_f %d f_r %d`
- `BTM: OSDictionary allocation failed for pack %d`
- `null IsCharging Key`
- `null batteryDict for pack %d`
- `%s: Unable to set PMU 0 sample rate to %ums (retStatus : 0x%08X)`
- `%s: _pmuSecondaryDriver is NULL`
- `%s: No 'pmu-filter-spec' EDT property, using default PMU spec\n`

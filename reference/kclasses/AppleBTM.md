# `AppleBTM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b988dc8`; metaclass vtable `0xfffffe00081a4f80`; class vtable `0xfffffe00081a48f0`
- Registration (init): `0xfffffe00093ce34c`
- Superclasses: [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `ApplePMGRBTM` in [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md): `IOProviderClass` = `ApplePMGRNub`, `IONameMatch` = `btm,pmgr`, `IOMatchCategory` = `AppleBTMPMGR`
- `ApplePhoneBTM` in [`com.apple.driver.ApplePhoneBTM`](../kexts/com.apple.driver.ApplePhoneBTM.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `btm,phone`, `IOMatchCategory` = `AppleBTM`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) on `btm,phone`

## Strings in its kext that name it (60)

- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to config PMU. ret: 0x%08X\" @%s:%d`
- `IOReturn AppleBTMAONPMUAgent::readWorstCaseData(uint32_t)`
- `AppleBTMBatteryDataAgent: UseSamplingThreshold %s`
- `AppleBTMBatteryDataAgent::start (%p)\n`
- `AppleBTMPMUAgent::free\n`
- `bool AppleBTMBPICAgent::initWithParent(AppleBPIC *, IOService *)`
- `AppleBTM::start\n`
- `virtual IOReturn AppleBTMFunction::callFunction(void *, void *, void *)`
- `AppleBTMPMUAgent`
- `\"AppleBTM: %s:%u \" \"REQUIRE failed: %s\" @%s:%d`
- `void AppleBTMBatteryDataAgent::asbArrivalHandler(void *, IOService *, IONotifier *)`
- `AppleBTMDataClientPPM`
- `\"AppleBTM: %s:%u \" \"AppleBTM: BPIC V Hysteresis EDT value out of range %u\" @%s:%d`
- `static AppleCplBTM *AppleCplBTM::withParent(AppleBTM *, IOService *)`
- `\"AppleBTM: %s:%u \" \"AppleBTMPMUAgent::initializePmuSampleSpec: spec input is NULL\" @%s:%d`
- `site.AppleBTMDataClientSMC`
- `AppleBTMDataClientSMC.cpp`
- `static AppleBTMAONPMUAgent *AppleBTMAONPMUAgent::withParent(AppleBTM *, IOService *)`
- `AppleBTMDataClient`
- `static AppleStoweBTMxr *AppleStoweBTMxr::withParent(AppleBTM *, IOService *)`
- `values[i] < kAppleBTMDataClientCount`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to clear/ack SPMI event\" @%s:%d`
- `bool AppleBTM::getDTProperty(const char *, uint32_t *, IOService *)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read Dynamic Agent data from PMU. ret: 0x%08X\" @%s:%d`
- `AppleBTMBatteryDataAgent::start success\n`
- `void AppleBTMAONPMUAgent::ApplePMUSecondaryDriverArrivalHandler(void *, IOService *, IONotifier *)`
- `AppleBTM: unable to update PMU ret: 0x%08X`
- `site.AppleBTMDataClientPPM`
- `site.AppleBTMBatteryDataAgent`
- `static AppleAvusBTM *AppleAvusBTM::withParent(AppleBTM *, IOService *)`
- `AppleBTMDataClient.cpp`
- `void AppleBTMBatteryDataAgent::initSamplingThreshold()`
- `AppleBTMBatteryDataAgent.cpp`
- `static AppleBakuBTM2 *AppleBakuBTM2::withParent(AppleBTM *, IOService *)`
- `IOReturn AppleBTMAONPMUAgent::readDynamicAgentData()`
- `\"AppleBTM: %s:%u \" \"Invalid context\" @%s:%d`
- `virtual bool AppleBTM::start(IOService *)`
- `static AppleAintreeBTM *AppleAintreeBTM::withParent(AppleBTM *, IOService *)`
- `AppleBTMBatteryDataAgent::Pack %d Null dict passed`
- `AppleBTMBatteryDataAgent::ASBM arrival success\n`
- `virtual IOReturn AppleBTMAONPMUAgent::updateVthresold(uint32_t, uint8_t)`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read filters buffer from PMU. ret: 0x%08X\" @%s:%d`
- `IOReturn AppleBTMAONPMUAgent::readFilterData(uint32_t)`
- `AppleBTMBPICAgent`
- `\"AppleBTM: %s:%u \" \"Offset %d is not within results_buffer bounds\" @%s:%d`
- `static AppleFermiumBTM *AppleFermiumBTM::withParent(AppleBTM *, IOService *)`
- `AppleBTMPMUAgent.cpp`
- `\"AppleBTM: %s:%u \" \"Unsupported battery data provider: %d\\n\" @%s:%d`
- `AppleBTM: unable to config BPIC. ret: 0x%08X \n`
- `IOReturn AppleBTMAONPMUAgent::readPICtrl(uint32_t)`
- `AppleBTMBatteryDataAgent`
- `void AppleBTMDataClient::publish(void *)`
- `bool AppleBTM::getDTPropertyString(const char *, const char **, IOService *)`
- `static void AppleBTMBatteryDataAgent::batteryProviderDataCallback(void *, const OSSymbol *, OSDictionary *)`
- `\"AppleBTM: %s:%u \" \"getPmuSampleSpec returned NULL\" @%s:%d`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to reset worst case I/V buffer. ret: 0x%08X\" @%s:%d`
- `AppleBTM: unable to config new Vthreshold proportional target. ret: 0x%08X`
- `site.AppleBTM`
- `\"AppleBTM: %s:%u \" \"AppleBTM: unable to read Duty Cycle data from PMU. ret: 0x%08X\" @%s:%d`
- `AppleBTMDataClientSMC`

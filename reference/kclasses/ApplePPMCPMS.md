# `ApplePPMCPMS`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x9830` (38,960 bytes)
- Metaclass: `0xfffffe000b9dbe00`; metaclass vtable `0xfffffe00082bae70`; class vtable `0xfffffe00082ba6b8`
- Registration (init): `0xfffffe0009b8b4a4`
- Superclasses: [`ApplePPM`](ApplePPM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`ApplePPMCPMSv2`](ApplePPMCPMSv2.md) — `com.apple.driver.AppleiPhoneACSKPPM`

## Strings in its kext that name it (60)

- `site.ApplePPMCPMSMeasuredPowerHelper`
- `static void ApplePPMCPMS::updateSignalCallback(OSObject *, uint64_t)`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::updateSystemCapabilityWithPPM()`
- `bool ApplePPMCPMSPeakPowerEnvelope::peakPowerEnvelopeUpdateValues(float, peakPowerEnvelopeValues *)`
- `site.ApplePPMCPMSPeakPowerEnvelope`
- `static ApplePPMCPMSSystemCapabilityMonitor *ApplePPMCPMSSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t, uint8_t)`
- `void ApplePPMPredictivePmax::addDeviceTreeClientPredictivePowerProperties(ApplePPMCPMSClientPredictivePmaxPowersEDT)`
- `virtual IOReturn ApplePPMCPMS::requestPowerBudget(CPMSPPMPowerBudget *, CPMSPPMPowerBudget *)`
- `virtual void ApplePPMCPMSPowerInputHelperBatteryFirmware::inputHandler(OSArray *, uint32_t)`
- `virtual IOReturn ApplePPMCPMS::PPMInterfaceAPICallBack(OSObject *, OSDictionary *, OSDictionary **)`
- `bool ApplePPMCPMSPeakPowerEnvelope::filterOutData(peakPowerEnvelopeValues *)`
- `virtual bool ApplePPMCPMSv2::setSystemCapability(const int *, int32_t, uint8_t)`
- `virtual uint32_t ApplePPMCPMSv2::powerValueToBudgetScalar(uint32_t, UniqueClientID_t)`
- `ApplePPMCPMSv2`
- `void ApplePPMPolicyCPMS::constructLanes(ApplePPMCPMSLaneEDT *, int, ApplePPMCPMSDecisionTreeCurveEDT *, int)`
- `void ApplePPMCPMS::constructTimescalesAvailable(CPMSPPMPowerBudget *, uint32_t)`
- `ApplePPMCPMSTableDrivenBatteryModelFallBack::ApplePPMCPMSTableDrivenBatteryModelFallBack(const uint32_t *, uint32_t, uint32_t, int32_t, int32_t)`
- `bool ApplePPMCPMSSignalManager::initWithParams(IOService *, IOKitMessageCallbackType)`
- `virtual uint32_t ApplePPMCPMS::powerValueToBudgetScalar(uint32_t, UniqueClientID_t)`
- `virtual ApplePPMPolicyCPMS *ApplePPMCPMS::createPolicy(IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `virtual void ApplePPMCPMSSystemCapabilityMonitor::stepBatteryModel()`
- `ApplePPMCPMSPowerInputHelper.cpp`
- `static ApplePPMCPMSDecisionTree *ApplePPMCPMSDecisionTree::withParams(ApplePPMCPMSDecisionTreeCurve **, int)`
- `ApplePPMCPMSPowerInputHelperBatteryFirmware`
- `virtual bool ApplePPMCPMS::initLocal(IOService *)`
- `site.ApplePPMCPMSSignalManager`
- `void ApplePPMCPMSPowerInputHelperBatteryFirmware::processSystemCapabilityData(OSDictionary *, uint8_t)`
- `\"ApplePPM: %s:%u \" \"ApplePPMCPMS: Could not register client id %d. Error code 0x%8x\\n\" @%s:%d`
- `void ApplePPMCPMS::AppleDieTempControllerArrivalHandler(void *, IOService *, IONotifier *)`
- `float ApplePPMCPMSDecisionTree::normalizedOutput(UniqueClientID_t, float)`
- `void ApplePPMCPMSPowerInputHelper::setOverrideSystemCapability(OSArray *, uint8_t)`
- `static void ApplePPMCPMS::powerReportCallback(OSObject *, uint64_t, int32_t *, uint32_t)`
- `ApplePPMCPMSBatteryModelFallback.cpp`
- `void ApplePPMCPMSSignalManager::update()`
- `ApplePPMCPMSDecisionTree.cpp`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::getCPMSBatteryPmaxState(CPMSPPMBatteryPmaxData *)`
- `site.ApplePPMCPMSSystemCapabilityFilter`
- `IOReturn ApplePPMCPMS::coalesceAndDispatchBudgets(UniqueClientID_t, UniqueClientID_t, bool *)`
- `ApplePPMCPMSSignalManager.cpp`
- `void ApplePPMPredictivePmax::addDeviceTreePredictiveHorizonPmaxProperties(ApplePPMCPMSPredictiveHorizonPmaxEDT)`
- `ApplePPMCPMS::Peak Power Envelope Enabled\n`
- `site.ApplePPMCPMSDecisionTree`
- `void ApplePPMCPMSLane::assertValidity(int)`
- `virtual int32_t *ApplePPMCPMSv2::systemCapabilityToUse()`
- `static ApplePPMCPMSSysCapMonitorv2 *ApplePPMCPMSSysCapMonitorv2::withParent(ApplePPM *, uint8_t, uint8_t)`
- `bool ApplePPMCPMSPeakPowerEnvelope::peakPowerEnvelopeGetInst(peakPowerEnvelopInst **)`
- `virtual void ApplePPMCPMSSystemCapabilityMonitor::initFallbackTables(ApplePPM *)`
- `virtual IOReturn ApplePPMCPMS::getCPMSControlState(CPMSPPMControlState *, uint32_t *)`
- `ApplePPMCPMSBatteryModelFallback.hpp`
- `void ApplePPMCPMSPowerInputHelperBatteryFirmware::processPowerConsumptionData(OSDictionary *, uint8_t)`
- `site.ApplePPMCPMSTableDrivenBatteryModelFallBack`
- `IOReturn ApplePPMCPMS::processClientRegistration(ApplePPM *, IOService *, ApplePPMKernelClient::ClientInfoData *, ApplePPMKernelClient *, bool)`
- `ApplePPMCPMS::initLocal (%p)\n`
- `ApplePPMCPMSPeakPowerEnvelope.cpp`
- `void ApplePPMCPMSSystemCapabilityMonitor::consumeInternalSourceData(OSDictionary *)`
- `bool ApplePPMCPMSSignalManager::initWithParams(ApplePPMPowerServo *, float *, float *, IOService *, IOKitMessageCallbackType)`
- `void ApplePPMCPMS::smcTargetsUpdateEventHandler(IOInterruptEventSource *, int)`
- `site.ApplePPMCPMSPowerInputHelper`
- `void ApplePPMCPMSSignalManager::update(unsigned int, unsigned int)`
- `void ApplePPMPredictivePmax::addDeviceTreeClientPredictivePmaxProperties(ApplePPMCPMSClientPredictivePmaxEDT)`

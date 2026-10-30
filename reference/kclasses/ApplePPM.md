# `ApplePPM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x34a0` (13,472 bytes)
- Metaclass: `0xfffffe000b9dbdb0`; metaclass vtable `0xfffffe00082ba188`; class vtable `0xfffffe00082b9a58`
- Registration (init): `0xfffffe0009b7ba30`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`ApplePPMCPMS`](ApplePPMCPMS.md) — `com.apple.driver.AppleiPhoneACSKPPM`

## Strings in its kext that name it (60)

- `\"ApplePPM: %s:%u \" \"ptML returned zero entries for SMC->PPM range\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"no client defined for power list for uniqueId %d\" @%s:%d`
- `site.ApplePPMCPMSMeasuredPowerHelper`
- `static void ApplePPMCPMS::updateSignalCallback(OSObject *, uint64_t)`
- `ApplePPMPolicyCPMSPowerServoLowerLayerCEs.cpp`
- `void ApplePPMSystemCapabilityMonitor::findBatteryPackEntry()`
- `\"ApplePPM: %s:%u \" \"%s, lane %d, effort %d out of range\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"timescale %d\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"length %u\" @%s:%d`
- `IOReturn ApplePPM::sleepWakeNotification(void *, UInt32, IOService *, void *, vm_size_t)`
- `virtual bool ApplePPMCPMSSystemCapabilityMonitor::updateSystemCapabilityWithPPM()`
- `bool ApplePPMDroopController::initWithParent(ApplePPM *)`
- `site.ApplePPMKernelClient`
- `\"ApplePPM: %s:%u \" \"SOC range %u not a multiple of col dim %u\\n\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"enablePTDEntryInterrupt returned 0x%08x\" @%s:%d`
- `bool ApplePPMCPMSPeakPowerEnvelope::peakPowerEnvelopeUpdateValues(float, peakPowerEnvelopeValues *)`
- `bool ApplePPMPolicyCPMSv2::initWithParams(IOService *, uint32_t, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `site.ApplePPMCPMSPeakPowerEnvelope`
- `static ApplePPMCPMSSystemCapabilityMonitor *ApplePPMCPMSSystemCapabilityMonitor::withParent(ApplePPM *, uint8_t, uint8_t)`
- `\"ApplePPM: %s:%u \" \"unsupported filter tau %d, index %d\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"readPTDEntry returned 0x%08x\" @%s:%d`
- `bool ApplePPMPolicyCPMS::initWithParams(ApplePPMEDTData *, IOKitMessageCallbackType)`
- `\"ApplePPM: %s:%u \" \"_multiEMAMaxTracker not initialized for index=%d\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"Mismatch in number of elements in predictive powers (%d) and predictive budgets (%d) in the EDT for clientID  %d\" @%s:%d`
- `bool ApplePPMPowerServo::initWithParams(int, BatteryPowerConsumptionFilterTau, float, float, int)`
- `\"ApplePPM: %s:%u \" \"getPTDRangeInfo for range %d returned 0x%08x\" @%s:%d`
- `virtual IOReturn ApplePPMPmgrAdapter::enableInterruptForSMCToPPM()`
- `static ApplePPMPTDManagerBase *ApplePPMPTDManagerBase::withPmgrProvider(ApplePMGRNub *, IOService *, lowerLayerUpdateHandlerType, fetchClientPowerConsumptionHandlerType, uint32_t)`
- `void ApplePPMPredictivePmax::addDeviceTreeClientPredictivePowerProperties(ApplePPMCPMSClientPredictivePmaxPowersEDT)`
- `virtual IOReturn ApplePPMCPMS::requestPowerBudget(CPMSPPMPowerBudget *, CPMSPPMPowerBudget *)`
- `\"ApplePPM: %s:%u \" \"no client defined for budget list for uniqueId %d\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"unknown policy type %d\" @%s:%d`
- `virtual void ApplePPMCPMSPowerInputHelperBatteryFirmware::inputHandler(OSArray *, uint32_t)`
- `virtual IOReturn ApplePPMCPMS::PPMInterfaceAPICallBack(OSObject *, OSDictionary *, OSDictionary **)`
- `void ApplePPMPolicyCPMS::addDeviceTreeClientPredictiveBudgetPowerProperties(int, OSData *, OSData *)`
- `\"ApplePPM: %s:%u \" \"client ID %u registration: admission check failed. error 0x%08x\" @%s:%d`
- `bool ApplePPMCPMSPeakPowerEnvelope::filterOutData(peakPowerEnvelopeValues *)`
- `virtual bool ApplePPMCPMSv2::setSystemCapability(const int *, int32_t, uint8_t)`
- `virtual uint32_t ApplePPMCPMSv2::powerValueToBudgetScalar(uint32_t, UniqueClientID_t)`
- `site.ApplePPMPolicyCPMSPowerServoLowerLayerCEs`
- `void ApplePPM::getTGraphClientData(ApplePPMTGraphClientData **)`
- `ApplePPMCPMSv2`
- `virtual IOReturn ApplePPMPmgrAdapter::disableInterruptForSMCToPPM()`
- `\"ApplePPM: %s:%u \" \"unexpected CLPC budget request, %d timescales\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"lane %d, output timescale %d\" @%s:%d`
- `\"ApplePPM: %s:%u \" \"count %u of %u\" @%s:%d`
- `ApplePPMARMFunction`
- `ApplePPMKernelClient.cpp`
- `ApplePPMSystemCapabilityMonitor *ApplePPM::getSystemCapabilityMonitor(uint8_t, uint8_t)`
- `virtual IOReturn ApplePPMKernelClient::getMinMaxClientPowerPolicy(uint8_t, clientPowerPolicyRange *)`
- `site.ApplePPMPolicyCPMSv2`
- `void ApplePPMPolicyCPMS::constructLanes(ApplePPMCPMSLaneEDT *, int, ApplePPMCPMSDecisionTreeCurveEDT *, int)`
- `bool ApplePPMPolicyCPMSPowerServo::initWithParams(ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `ApplePPM::initLocal success\n`
- `void ApplePPMCPMS::constructTimescalesAvailable(CPMSPPMPowerBudget *, uint32_t)`
- `ApplePPMCPMSTableDrivenBatteryModelFallBack::ApplePPMCPMSTableDrivenBatteryModelFallBack(const uint32_t *, uint32_t, uint32_t, int32_t, int32_t)`
- `bool ApplePPMCPMSSignalManager::initWithParams(IOService *, IOKitMessageCallbackType)`
- `\"ApplePPM: %s:%u \" \"Invalid clientId %d in multiClientList\" @%s:%d`
- `ApplePPM_ACSK_signalTracer.cpp`
- `static ApplePPMPolicyCPMSPowerServoLowerLayerBudgets *ApplePPMPolicyCPMSPowerServoLowerLayerBudgets::withParams(IOService *, IOKitMessageCallbackType, IOKitMessageCallbackType)`

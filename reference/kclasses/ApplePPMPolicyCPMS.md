# `ApplePPMPolicyCPMS`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x5528` (21,800 bytes)
- Metaclass: `0xfffffe000b9dbd78`; metaclass vtable `0xfffffe00082b97e0`; class vtable `0xfffffe00082b95a0`
- Registration (init): `0xfffffe0009b75124`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (2; 4 in total)

- [`ApplePPMPolicyCPMSPowerServo`](ApplePPMPolicyCPMSPowerServo.md) — `com.apple.driver.AppleiPhoneACSKPPM`
- [`ApplePPMPolicyCPMSPowerServoLowerLayerBudgets`](ApplePPMPolicyCPMSPowerServoLowerLayerBudgets.md) — `com.apple.driver.AppleiPhoneACSKPPM`

## Strings in its kext that name it (59)

- `ApplePPMPolicyCPMSPowerServoLowerLayerCEs.cpp`
- `bool ApplePPMPolicyCPMSv2::initWithParams(IOService *, uint32_t, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `bool ApplePPMPolicyCPMS::initWithParams(ApplePPMEDTData *, IOKitMessageCallbackType)`
- `void ApplePPMPolicyCPMS::addDeviceTreeClientPredictiveBudgetPowerProperties(int, OSData *, OSData *)`
- `site.ApplePPMPolicyCPMSPowerServoLowerLayerCEs`
- `site.ApplePPMPolicyCPMSv2`
- `void ApplePPMPolicyCPMS::constructLanes(ApplePPMCPMSLaneEDT *, int, ApplePPMCPMSDecisionTreeCurveEDT *, int)`
- `bool ApplePPMPolicyCPMSPowerServo::initWithParams(ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `static ApplePPMPolicyCPMSPowerServoLowerLayerBudgets *ApplePPMPolicyCPMSPowerServoLowerLayerBudgets::withParams(IOService *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `virtual ApplePPMPolicyCPMS *ApplePPMCPMS::createPolicy(IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `bool ApplePPMPolicyCPMS::setDetailedThermalPowerBudget(DetailedThermalBudget *)`
- `ApplePPMPolicyCPMSPowerServoLowerLayerBudgets.cpp`
- `site.ApplePPMPolicyCPMSPowerServo`
- `virtual float ApplePPMPolicyCPMSv2::controlEffortForLane(int)`
- `IOReturn ApplePPMPolicyCPMS::getClientBudgetForGeneralControlEfforts(UniqueClientID_t, int *, float *)`
- `ApplePPMPolicyCPMS`
- `bool ApplePPMPolicyCPMSPowerServoLowerLayerBudgets::initWithParams(IOService *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `virtual void ApplePPMPolicyCPMSv2::updateACSKDroop(float)`
- `ApplePPMPolicyCPMSPowerServoLowerLayerCEs`
- `void ApplePPMPolicyCPMS::ackClientBudgetNoLock(CPMSPPMPowerBudgetAck *)`
- `static ApplePPMPolicyCPMSPowerServo *ApplePPMPolicyCPMSPowerServo::withParams(IOService *, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `void ApplePPMPolicyCPMSv2::executeACSKBlocks()`
- `IOReturn ApplePPMPolicyCPMS::ackClientBudget(CPMSPPMPowerBudgetAck *)`
- `IOReturn ApplePPMPolicyCPMS::getClientGrantedBudget(UniqueClientID_t, CPMSPPMPowerBudget *)`
- `virtual void ApplePPMPolicyCPMSv2::setSystemStress(uint32_t, bool)`
- `ApplePPMPolicyCPMSPowerServoLowerLayerCEs.h`
- `virtual void ApplePPMPolicyCPMSv2::setIBInputs(uint32_t, float)`
- `ApplePPMPolicyCPMS.cpp`
- `IOReturn ApplePPMPolicyCPMS::getClientRequestedBudget(UniqueClientID_t, CPMSPPMPowerBudget *)`
- `site.ApplePPMPolicyCPMSPowerServoLowerLayerBudgets`
- `ApplePPMPolicyCPMSPowerServo`
- `void ApplePPMPolicyCPMSPowerServo::setupPowerServoIntegratorMinimums(OSData *)`
- `void ApplePPMPolicyCPMS::copyDetailedThermalBudgetsResolved(const UniqueClientID_t, const DetailedThermalBudgetsForClient *)`
- `ApplePPMPolicyCPMS skipping %s, lane %d\n`
- `IOReturn ApplePPMPolicyCPMS::getClientState(UniqueClientID_t, CPMSPPMClientState *)`
- `IOReturn ApplePPMPolicyCPMS::requestPowerBudget(CPMSPPMPowerBudget *)`
- `ApplePPMPolicyCPMSv2`
- `virtual void ApplePPMPolicyCPMSv2::setPredictiveSysCap(uint32_t, int32_t, int32_t)`
- `virtual bool ApplePPMPolicyCPMSv2::getBrownoutRiskBool()`
- `virtual ApplePPMPowerServo *ApplePPMPolicyCPMSPowerServo::createPowerServo(CPMSPPMLaneInput, float, float)`
- `virtual void ApplePPMPolicyCPMSv2::advanceServosWithPmargin(float)`
- `virtual bool ApplePPMPolicyCPMSv2::anyServosEngaged()`
- `ApplePPMPolicyCPMS.h`
- `bool ApplePPMPolicyCPMS::initWithParams(IOService *, ApplePPMEDTData *, IOKitMessageCallbackType)`
- `void ApplePPMPolicyCPMS::addDeviceTreeClientPredictiveHorizonPmaxProperties(OSData *, OSData *, OSData *)`
- `IOReturn ApplePPMPolicyCPMS::getClientAwakeState(UniqueClientID_t, bool *)`
- `ApplePPMPolicyCPMSPowerServo.cpp`
- `void ApplePPMPolicyCPMS::addDeviceTreeClientPredictivePmaxProperties(OSData *, OSData *, OSData *)`
- `virtual IOReturn ApplePPMPolicyCPMS::configureReport(IOReportChannelList *, IOReportConfigureAction, void *, void *)`
- `bool ApplePPMPolicyCPMSPowerServo::initWithParams(IOService *, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `ApplePPMPolicyCPMSPowerServoLowerLayerBudgets`
- `IOReturn ApplePPMPolicyCPMS::setDetailedThermalPowerBudgets(DetailedThermalBudgets *)`
- `static ApplePPMPolicyCPMSv2 *ApplePPMPolicyCPMSv2::withParams(IOService *, uint32_t, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `IOReturn ApplePPMPolicyCPMS::registerCPMSClient(CPMSPPMClientDescription *)`
- `ApplePPMPolicyCPMSv2.cpp`
- `bool ApplePPMPolicyCPMSPowerServoLowerLayerCEs::initWithParams(IOService *, ApplePPMEDTData *, IOKitMessageCallbackType, IOKitMessageCallbackType)`
- `void ApplePPMPolicyCPMS::forceTransientGrantedBudgetUpdate(CPMSPPMPowerBudget *)`
- `virtual ApplePPMPowerServo *ApplePPMPolicyCPMSPowerServoLowerLayerCEs::createPowerServo(CPMSPPMLaneInput, float, float)`
- `site.ApplePPMPolicyCPMS`

# `AppleSARService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0x268` (616 bytes)
- Metaclass: `0xfffffe000b994c90`; metaclass vtable `0xfffffe00081d10a0`; class vtable `0xfffffe00081d0b40`
- Registration (init): `0xfffffe0009536290`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSARService` in [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `IOKit`, `IOMatchCategory` = `AppleSARService`

## Strings in its kext that name it (60)

- `static IOReturn AppleSARServiceUserClient::extBudgetScalingFactor(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCallState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `site.AppleSARServiceUserClient`
- `static IOReturn AppleSARServiceUserClient::extSARSensingCALastSubmit(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extGripState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extUpdateOrientation(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extFaceDetection(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extSARConsumed(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extWifiResidual(AppleSARService *, void *, IOExternalMethodArguments *)`
- `IOReturn AppleSARServiceUserClient::registerCallback(void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCentralSAR(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extRegisterReceivingKernelMessage(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extBtResidual(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extWiFiState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCentralMPE(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extConnectivityResidual(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extVoiceState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extConnectivityHSARSupported(AppleSARService *, void *, IOExternalMethodArguments *)`
- `virtual IOReturn AppleSARServiceUserClient::clientClose()`
- `static IOReturn AppleSARServiceUserClient::extSARSensingCAInfo(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extUpdateE85MitigationRequest(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCentralWiFi(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extSARFusionStateINT(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extSarServiceProfile(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCellularHSARSupported(AppleSARService *, void *, IOExternalMethodArguments *)`
- `AppleSARServiceUserClient`
- `static IOReturn AppleSARServiceUserClient::extSARSelectionTunerState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extAccessoryState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extUpdateScreenState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extVSWRLearning(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extBtSAR(AppleSARService *, void *, IOExternalMethodArguments *)`
- `AppleSARService: Failed to create Logging instance!\n`
- `static IOReturn AppleSARServiceUserClient::extGetSPMIEventTrackingArray(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extSARTransitionWaitTime(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCentralBT(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extRegulatoryAverage(AppleSARService *, void *, IOExternalMethodArguments *)`
- `virtual IOReturn AppleSARServiceUserClient::clientDied()`
- `static IOReturn AppleSARServiceUserClient::extSarRFSensingSignal(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extConnectivitySAR(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extCentralTotalMPE(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extAntennaOnTop(AppleSARService *, void *, IOExternalMethodArguments *)`
- `%s::%s:%d: Trying to setup AppleSARService service\n`
- `static IOReturn AppleSARServiceUserClient::extTotalSAR(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extStateABOsiris(AppleSARService *, void *, IOExternalMethodArguments *)`
- `AppleSARService Userclient`
- `static IOReturn AppleSARServiceUserClient::extFrontCameraState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extMPEConsumed(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extPTDUnRegisterInterrupt(AppleSARService *, void *, IOExternalMethodArguments *)`
- `site.AppleSARService`
- `static IOReturn AppleSARServiceUserClient::extConfigSARFusion(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extSARFusionStateMAV(AppleSARService *, void *, IOExternalMethodArguments *)`
- `AppleSARServiceUserClient: Failed to create Logging instance!\n`
- `static IOReturn AppleSARServiceUserClient::extThreadState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extSARSelectionState(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extUWBRadio(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extConfigHSAR(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extWifiSAR(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extoverrideUseCaseDetection(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extConnectivityRegulatoryInfo(AppleSARService *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSARServiceUserClient::extUplinkConstraintCondition(AppleSARService *, void *, IOExternalMethodArguments *)`

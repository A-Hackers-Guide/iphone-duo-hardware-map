# `AppleSEPUserClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b99a750`; metaclass vtable `0xfffffe00081f3210`; class vtable `0xfffffe00081f2c28`
- Registration (init): `0xfffffe0009631cdc`
- Superclasses: [`IOUserClient`](IOUserClient.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (51)

- `IOReturn AppleSEPUserClient::getOrGenerateNonce(IOExternalMethodArguments *, bool)`
- `AppleSEPUserClient`
- `static IOReturn AppleSEPUserClient::DispatchUserClientInvalidateNonce(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloSetGainParamSet(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientCommitHash(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloGetLthTransferMessage(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLynxSetProvisionalSlot(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchDiscoveryGetEndpointInfo(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloGetDisasterRecoveryLthBackup(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloGetLthBackup(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `site.AppleSEPUserClient`
- `static IOReturn AppleSEPUserClient::DispatchHiloAccumulateTestPattern(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloGetDisplayParams(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloCheckGainTestPattern(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLoadRestoreFirmwareWithART(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLoadRestoreFirmware(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `virtual bool AppleSEPUserClient::initWithTask(task_t, void *, UInt32)`
- `static IOReturn AppleSEPUserClient::DispatchGetTraceRecordState(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientGigalockerStressTest(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloLoadLthTransferMessage(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLynxGetProvisionalSlot(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloGetLthTransferAttestation(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloUpdateTimer(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLoadFirmware(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLynxGetCPSN(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloLoadLthBackup(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloAdvanceGainRestrictionPhase(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientEraseAllContentAndSettings(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientGetART(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `virtual IOReturn AppleSEPUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `virtual bool AppleSEPUserClient::start(IOService *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloGetLthRaw(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloLoadLthRaw(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientPairKey(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `AppleSEPUserClient.cpp`
- `static IOReturn AppleSEPUserClient::DispatchHiloTestGainRestriction(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLynxGetAppHash(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchDynamicObjectOp(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchGetEpochs(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientGigalockerShutdown(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientPurgeSystemToken(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientSetART(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientCounterSelfTest(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `virtual IOReturn AppleSEPUserClient::clientMemoryForType(uint32_t, IOOptionBits *, IOMemoryDescriptor **)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPUserClient.cpp`
- `static IOReturn AppleSEPUserClient::DispatchHiloLoadDisasterRecoveryLthBackup(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientGenerateNonceAndSlot(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLcrtVerify(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientLynxGetPubKey(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchUserClientClearART(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`
- `static IOReturn AppleSEPUserClient::DispatchHiloTestLthTransferAttestation(AppleSEPUserClient *, void *, IOExternalMethodArguments *)`

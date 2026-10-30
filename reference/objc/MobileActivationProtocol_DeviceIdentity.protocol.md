# `MobileActivationProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity`](../userland/System__Library__PrivateFrameworks__DeviceIdentity.framework__DeviceIdentity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 34 instance methods, 0 class methods

## Instance methods

```
-[MobileActivationProtocol copyActivationRecordWithCompletionBlock:];
-[MobileActivationProtocol copyAttestationDictionaryWithCompletionBlock:options:completion:];
-[MobileActivationProtocol copyAutomaticTimeEnabledWithCompletion:];
-[MobileActivationProtocol copyDCRTWithCompletionBlock:withCompletion:];
-[MobileActivationProtocol copyLegacyDeviceIdentityWithCompletionBlock:];
-[MobileActivationProtocol copyMonotonicClockWithCompletionBlock:];
-[MobileActivationProtocol copyPCRTTokenWithCompletionBlock:];
-[MobileActivationProtocol copyRTCResetCountWithCompletionBlock:];
-[MobileActivationProtocol copyUCRTVersionInfoWithCompletionBlock:];
-[MobileActivationProtocol copyUCRTWithCompletionBlock:];
-[MobileActivationProtocol createActivationInfoWithCompletionBlock:];
-[MobileActivationProtocol createTunnel1ActivationInfo:options:withCompletionBlock:];
-[MobileActivationProtocol createTunnel1SessionInfoWithCompletionBlock:];
-[MobileActivationProtocol deactivateDeviceWithCompletionBlock:];
-[MobileActivationProtocol deleteLegacyDeviceIdentityWithCompletionBlock:];
-[MobileActivationProtocol getActivationBuildWithCompletionBlock:];
-[MobileActivationProtocol getActivationStateWithCompletionBlock:];
-[MobileActivationProtocol getDCRTStateWithCompletionBlock:withCompletion:];
-[MobileActivationProtocol getUCRTSalvageStateWithCompletionBlock:];
-[MobileActivationProtocol handleActivationInfo:withCompletionBlock:];
-[MobileActivationProtocol handleActivationInfoWithSession:activationSignature:completionBlock:];
-[MobileActivationProtocol isDeviceBrickedWithCompletionBlock:];
-[MobileActivationProtocol isInFieldCollectedWithCompletionBlock:];
-[MobileActivationProtocol issueClientCertificateLegacy:WithCompletionBlock:];
-[MobileActivationProtocol issueClientCertificateWithReferenceKey:options:completion:];
-[MobileActivationProtocol issueCollection:withCompletionBlock:];
-[MobileActivationProtocol issueDCRT:withCompletionBlock:];
-[MobileActivationProtocol issueUCRT:withCompletionBlock:];
-[MobileActivationProtocol performMigrationWithCompletion:completion:];
-[MobileActivationProtocol recertifyDeviceWithCompletionBlock:];
-[MobileActivationProtocol requestDeviceReactivationWithCompletionBlock:];
-[MobileActivationProtocol ucrtUpgradeRequiredWithCompletionBlock:];
-[MobileActivationProtocol unbrickDeviceWithCompletionBlock:];
-[MobileActivationProtocol updateBasebandTicket:baaCertData:baaIntermediateCert:options:withCompletionBlock:];
```

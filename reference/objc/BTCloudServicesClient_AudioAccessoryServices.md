# `BTCloudServicesClient`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Instance methods

```
-[BTCloudServicesClient testListenerEndpoint];
-[BTCloudServicesClient dispatchQueue];
-[BTCloudServicesClient _ensureXPCStarted];
-[BTCloudServicesClient setTestListenerEndpoint:];
-[BTCloudServicesClient setInvalidationHandler:];
-[BTCloudServicesClient init];
-[BTCloudServicesClient interruptionHandler];
-[BTCloudServicesClient setDispatchQueue:];
-[BTCloudServicesClient invalidate];
-[BTCloudServicesClient _interrupted];
-[BTCloudServicesClient setInterruptionHandler:];
-[BTCloudServicesClient invalidationHandler];
-[BTCloudServicesClient _invalidated];
-[BTCloudServicesClient deleteSoundProfileRecordWithCompletion:];
-[BTCloudServicesClient fetchSoundProfileRecordWithCompletion:];
-[BTCloudServicesClient createSoundProfileRecord:completion:];
-[BTCloudServicesClient magicSettingsRecord:completion:];
-[BTCloudServicesClient accountInfoWithCompletion:];
-[BTCloudServicesClient cloudPairingIdentifierForPeripheral:completion:];
-[BTCloudServicesClient createDeviceRecord:completion:];
-[BTCloudServicesClient createDeviceSupportInformationRecord:completion:];
-[BTCloudServicesClient createMagicSettingsRecord:completion:];
-[BTCloudServicesClient deleteDeviceRecord:completion:];
-[BTCloudServicesClient deleteDeviceSupportInformationRecord:completion:];
-[BTCloudServicesClient deleteMagicSettingsRecord:completion:];
-[BTCloudServicesClient deviceRecord:completion:];
-[BTCloudServicesClient deviceRecordsWithCompletion:];
-[BTCloudServicesClient deviceSupportInformationRecord:completion:];
-[BTCloudServicesClient deviceSupportInformationRecordsWithCompletion:];
-[BTCloudServicesClient forceCloudPairingForIdentifiers:completion:];
-[BTCloudServicesClient magicSettingsRecordsWithCompletion:];
-[BTCloudServicesClient modifyDeviceRecord:completion:];
-[BTCloudServicesClient modifyDeviceSupportInformationRecord:completion:];
-[BTCloudServicesClient modifyMagicSettingsRecord:completion:];
-[BTCloudServicesClient modifySoundProfileRecord:completion:];
```

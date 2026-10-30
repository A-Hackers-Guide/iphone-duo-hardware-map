# `AACloudServicesClient`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 7 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _clientID;
I _internalFlags;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@? _hmDeviceCloudRecordUpdateHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (TI,N,V_internalFlags) internalFlags;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_hmDeviceCloudRecordUpdateHandler) hmDeviceCloudRecordUpdateHandler;
```

## Class methods

```
+[AACloudServicesClient supportsSecureCoding];
```

## Instance methods

```
-[AACloudServicesClient testListenerEndpoint];
-[AACloudServicesClient setInternalFlags:];
-[AACloudServicesClient internalFlags];
-[AACloudServicesClient clientID];
-[AACloudServicesClient dispatchQueue];
-[AACloudServicesClient _activate];
-[AACloudServicesClient _ensureXPCStarted];
-[AACloudServicesClient activateWithCompletion:];
-[AACloudServicesClient setTestListenerEndpoint:];
-[AACloudServicesClient setClientID:];
-[AACloudServicesClient setInvalidationHandler:];
-[AACloudServicesClient init];
-[AACloudServicesClient interruptionHandler];
-[AACloudServicesClient setDispatchQueue:];
-[AACloudServicesClient invalidate];
-[AACloudServicesClient _interrupted];
-[AACloudServicesClient encodeWithCoder:];
-[AACloudServicesClient setInterruptionHandler:];
-[AACloudServicesClient _reportError:];
-[AACloudServicesClient initWithCoder:];
-[AACloudServicesClient invalidationHandler];
-[AACloudServicesClient _invalidated];
-[AACloudServicesClient fetchAAProxCardsInfoForDeviceWithAddress:completion:];
-[AACloudServicesClient fetchHMDeviceCloudRecordInfoWithAddress:completion:];
-[AACloudServicesClient hmDeviceCloudRecordInfosUpdated:];
-[AACloudServicesClient hmDeviceCloudRecordUpdateHandler];
-[AACloudServicesClient modifyAAProxCardsInfo:completion:];
-[AACloudServicesClient modifyHMDeviceCloudRecordInfo:completion:];
-[AACloudServicesClient removeAAProxCardsInfoForDeviceWithAddress:completion:];
-[AACloudServicesClient removeHMDeviceCloudRecordInfoForDeviceWithAddress:completion:];
-[AACloudServicesClient setHmDeviceCloudRecordUpdateHandler:];
```

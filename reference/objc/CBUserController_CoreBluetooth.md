# `CBUserController`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBStackUserController`, `CBActivatable`, `CBErrorReporting`, `CBInterruptable`, `CBUserControllerInterface`
- 12 instance variables, 10 properties, 36 instance methods, 2 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _invalidateCalled;
B _invalidateDone;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _errorHandler;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBUserController readPrefKeys:source:error:];
+[CBUserController writePrefKey:value:source:error:];
```

## Instance methods

```
-[CBUserController testListenerEndpoint];
-[CBUserController _activateXPCStart:];
-[CBUserController clientID];
-[CBUserController dispatchQueue];
-[CBUserController _activate];
-[CBUserController _ensureXPCStarted];
-[CBUserController activateWithCompletion:];
-[CBUserController setTestListenerEndpoint:];
-[CBUserController setClientID:];
-[CBUserController setInvalidationHandler:];
-[CBUserController init];
-[CBUserController dealloc];
-[CBUserController interruptionHandler];
-[CBUserController setDispatchQueue:];
-[CBUserController invalidate];
-[CBUserController _interrupted];
-[CBUserController setInterruptionHandler:];
-[CBUserController diagnosticShow:completion:];
-[CBUserController invalidationHandler];
-[CBUserController setErrorHandler:];
-[CBUserController _invalidated];
-[CBUserController errorHandler];
-[CBUserController appleAudioAccessoryLimitedLoggingWithCompletion:];
-[CBUserController setAppleAudioAccessoryLimitedLogging:completion:];
-[CBUserController readPrefKeys:source:completion:];
-[CBUserController storeControllerInfo:completion:];
-[CBUserController deleteControllerInfoForDevice:completion:];
-[CBUserController getCloudPairedDevicesWithCompletionHandler:];
-[CBUserController getControllerInfoForDevice:completion:];
-[CBUserController getCurrentUserGivenNameWithCompletion:];
-[CBUserController getDistributedLoggingStatusWithCompletion:];
-[CBUserController recordEventWithDeviceIdentifier:initiator:starting:useCase:];
-[CBUserController recordEventWithStarting:useCase:];
-[CBUserController setDistributedLoggingStatus:completion:];
-[CBUserController userNotificationEvent:completion:];
-[CBUserController writePrefKey:value:source:completion:];
```

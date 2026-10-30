# `BTServicesClient`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 16 instance methods, 0 class methods

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
-[BTServicesClient testListenerEndpoint];
-[BTServicesClient dispatchQueue];
-[BTServicesClient _ensureXPCStarted];
-[BTServicesClient setTestListenerEndpoint:];
-[BTServicesClient setInvalidationHandler:];
-[BTServicesClient init];
-[BTServicesClient diagnosticControl:completion:];
-[BTServicesClient interruptionHandler];
-[BTServicesClient setDispatchQueue:];
-[BTServicesClient invalidate];
-[BTServicesClient _interrupted];
-[BTServicesClient setInterruptionHandler:];
-[BTServicesClient diagnosticShow:completion:];
-[BTServicesClient invalidationHandler];
-[BTServicesClient _invalidated];
-[BTServicesClient showHIDConnectedBannerAperture:completion:];
```

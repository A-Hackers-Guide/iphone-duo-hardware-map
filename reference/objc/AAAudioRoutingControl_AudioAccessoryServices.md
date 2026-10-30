# `AAAudioRoutingControl`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 5 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _direct;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSString" _appBundleID;
@"NSString" _deviceAddress;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSString",C,N,V_appBundleID) appBundleID;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
```

## Class methods

```
+[AAAudioRoutingControl supportsSecureCoding];
```

## Instance methods

```
-[AAAudioRoutingControl testListenerEndpoint];
-[AAAudioRoutingControl _invalidateDirect];
-[AAAudioRoutingControl clientID];
-[AAAudioRoutingControl dispatchQueue];
-[AAAudioRoutingControl _activate];
-[AAAudioRoutingControl _ensureXPCStarted];
-[AAAudioRoutingControl activateWithCompletion:];
-[AAAudioRoutingControl setTestListenerEndpoint:];
-[AAAudioRoutingControl setClientID:];
-[AAAudioRoutingControl init];
-[AAAudioRoutingControl _activateDirect:];
-[AAAudioRoutingControl setDispatchQueue:];
-[AAAudioRoutingControl invalidate];
-[AAAudioRoutingControl _interrupted];
-[AAAudioRoutingControl encodeWithCoder:];
-[AAAudioRoutingControl _reportError:];
-[AAAudioRoutingControl setAppBundleID:];
-[AAAudioRoutingControl description];
-[AAAudioRoutingControl initWithCoder:];
-[AAAudioRoutingControl appBundleID];
-[AAAudioRoutingControl _invalidated];
-[AAAudioRoutingControl deviceAddress];
-[AAAudioRoutingControl setDeviceAddress:];
-[AAAudioRoutingControl _activateXPC:];
-[AAAudioRoutingControl areHeadphonesNearbyAndEligibleToPlay:];
-[AAAudioRoutingControl prewarmAudioAccessoriesForFitnessWorkout];
-[AAAudioRoutingControl _handleServerDied];
-[AAAudioRoutingControl hrmSessionStateChanged:completion:];
-[AAAudioRoutingControl setArbitrationBlockingModeWithCompletion:completion:];
```

# `BTAudioRoutingRequest`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServices.framework/BluetoothServices`](../userland/System__Library__PrivateFrameworks__BluetoothServices.framework__BluetoothServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 13 instance variables, 10 properties, 35 instance methods, 2 class methods

## Instance variables

```
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
i _audioScore;
I _flags;
I _clientID;
@"NSString" _appBundleID;
@"NSString" _deviceAddress;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSDictionary" _options;
@"NSString" _reason;
@? _responseHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (Ti,N,V_audioScore) audioScore;
@property (T@"NSString",C,N,V_appBundleID) appBundleID;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (TI,N,V_flags) flags;
@property (T@"NSDictionary",&,N,V_options) options;
@property (T@"NSString",C,N,V_reason) reason;
@property (T@?,C,N,V_responseHandler) responseHandler;
```

## Class methods

```
+[BTAudioRoutingRequest supportsSecureCoding];
+[BTAudioRoutingRequest isSupported];
```

## Instance methods

```
-[BTAudioRoutingRequest testListenerEndpoint];
-[BTAudioRoutingRequest clientID];
-[BTAudioRoutingRequest dispatchQueue];
-[BTAudioRoutingRequest _activate];
-[BTAudioRoutingRequest _ensureXPCStarted];
-[BTAudioRoutingRequest responseHandler];
-[BTAudioRoutingRequest setOptions:];
-[BTAudioRoutingRequest setFlags:];
-[BTAudioRoutingRequest setAudioScore:];
-[BTAudioRoutingRequest setTestListenerEndpoint:];
-[BTAudioRoutingRequest setClientID:];
-[BTAudioRoutingRequest flags];
-[BTAudioRoutingRequest init];
-[BTAudioRoutingRequest audioScore];
-[BTAudioRoutingRequest setResponseHandler:];
-[BTAudioRoutingRequest setReason:];
-[BTAudioRoutingRequest setDispatchQueue:];
-[BTAudioRoutingRequest invalidate];
-[BTAudioRoutingRequest _interrupted];
-[BTAudioRoutingRequest encodeWithCoder:];
-[BTAudioRoutingRequest activate];
-[BTAudioRoutingRequest _reportError:];
-[BTAudioRoutingRequest setAppBundleID:];
-[BTAudioRoutingRequest description];
-[BTAudioRoutingRequest initWithCoder:];
-[BTAudioRoutingRequest options];
-[BTAudioRoutingRequest reason];
-[BTAudioRoutingRequest appBundleID];
-[BTAudioRoutingRequest _invalidated];
-[BTAudioRoutingRequest deviceAddress];
-[BTAudioRoutingRequest setDeviceAddress:];
-[BTAudioRoutingRequest activateSync];
-[BTAudioRoutingRequest _activateSync];
-[BTAudioRoutingRequest _handleServerDied];
-[BTAudioRoutingRequest updateAudioState:withState:];
```

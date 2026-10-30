# `AA3PDeviceRoutingControl`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 4 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _direct;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSString" _deviceAddress;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSString",C,N,V_deviceAddress) deviceAddress;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
```

## Class methods

```
+[AA3PDeviceRoutingControl supportsSecureCoding];
```

## Instance methods

```
-[AA3PDeviceRoutingControl testListenerEndpoint];
-[AA3PDeviceRoutingControl clientID];
-[AA3PDeviceRoutingControl dispatchQueue];
-[AA3PDeviceRoutingControl _ensureXPCStarted];
-[AA3PDeviceRoutingControl setTestListenerEndpoint:];
-[AA3PDeviceRoutingControl setClientID:];
-[AA3PDeviceRoutingControl init];
-[AA3PDeviceRoutingControl setProperty:value:];
-[AA3PDeviceRoutingControl setDispatchQueue:];
-[AA3PDeviceRoutingControl invalidate];
-[AA3PDeviceRoutingControl _interrupted];
-[AA3PDeviceRoutingControl encodeWithCoder:];
-[AA3PDeviceRoutingControl _reportError:];
-[AA3PDeviceRoutingControl description];
-[AA3PDeviceRoutingControl initWithCoder:];
-[AA3PDeviceRoutingControl _invalidated];
-[AA3PDeviceRoutingControl deviceAddress];
-[AA3PDeviceRoutingControl setDeviceAddress:];
-[AA3PDeviceRoutingControl _handleServerDied];
-[AA3PDeviceRoutingControl setInEarState:inEarStateSecondary:];
```

# `AAAppleCareAccessoryControl`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 4 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
B _targetUserSession;
I _clientID;
@? _headphoneUpdateHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (TB,N,V_targetUserSession) targetUserSession;
@property (T@?,C,N,V_headphoneUpdateHandler) headphoneUpdateHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
```

## Class methods

```
+[AAAppleCareAccessoryControl supportsSecureCoding];
```

## Instance methods

```
-[AAAppleCareAccessoryControl targetUserSession];
-[AAAppleCareAccessoryControl clientID];
-[AAAppleCareAccessoryControl dispatchQueue];
-[AAAppleCareAccessoryControl _activate];
-[AAAppleCareAccessoryControl _ensureXPCStarted];
-[AAAppleCareAccessoryControl setTargetUserSession:];
-[AAAppleCareAccessoryControl activateWithCompletion:];
-[AAAppleCareAccessoryControl setClientID:];
-[AAAppleCareAccessoryControl init];
-[AAAppleCareAccessoryControl setDispatchQueue:];
-[AAAppleCareAccessoryControl invalidate];
-[AAAppleCareAccessoryControl _interrupted];
-[AAAppleCareAccessoryControl encodeWithCoder:];
-[AAAppleCareAccessoryControl _reportError:];
-[AAAppleCareAccessoryControl description];
-[AAAppleCareAccessoryControl initWithCoder:];
-[AAAppleCareAccessoryControl _invalidated];
-[AAAppleCareAccessoryControl headphoneConfigurationUpdateReceived:];
-[AAAppleCareAccessoryControl headphoneUpdateHandler];
-[AAAppleCareAccessoryControl send:btAddress:completion:];
-[AAAppleCareAccessoryControl setHeadphoneUpdateHandler:];
```

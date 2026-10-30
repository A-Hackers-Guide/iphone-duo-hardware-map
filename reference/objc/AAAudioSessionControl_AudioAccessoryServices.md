# `AAAudioSessionControl`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 6 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
i _conversationDetectSignal;
B _direct;
B _invalidateCalled;
B _invalidateDone;
@"NSXPCConnection" _xpcCnx;
I _clientID;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (Ti,N,V_conversationDetectSignal) conversationDetectSignal;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Class methods

```
+[AAAudioSessionControl supportsSecureCoding];
```

## Instance methods

```
-[AAAudioSessionControl testListenerEndpoint];
-[AAAudioSessionControl _invalidateDirect];
-[AAAudioSessionControl clientID];
-[AAAudioSessionControl dispatchQueue];
-[AAAudioSessionControl _ensureXPCStarted];
-[AAAudioSessionControl activateWithCompletion:];
-[AAAudioSessionControl setTestListenerEndpoint:];
-[AAAudioSessionControl setClientID:];
-[AAAudioSessionControl setInvalidationHandler:];
-[AAAudioSessionControl init];
-[AAAudioSessionControl _activateXPC:reactivate:];
-[AAAudioSessionControl _activateDirect:];
-[AAAudioSessionControl interruptionHandler];
-[AAAudioSessionControl setDispatchQueue:];
-[AAAudioSessionControl invalidate];
-[AAAudioSessionControl _activate:];
-[AAAudioSessionControl _interrupted];
-[AAAudioSessionControl encodeWithCoder:];
-[AAAudioSessionControl setInterruptionHandler:];
-[AAAudioSessionControl _reportError:];
-[AAAudioSessionControl description];
-[AAAudioSessionControl initWithCoder:];
-[AAAudioSessionControl invalidationHandler];
-[AAAudioSessionControl _invalidated];
-[AAAudioSessionControl setMuteAction:auditToken:bundleIdentifier:];
-[AAAudioSessionControl conversationDetectSignal];
-[AAAudioSessionControl isAnySmartRoutingDeviceConnected:];
-[AAAudioSessionControl setConversationDetectSignal:];
-[AAAudioSessionControl setMuteAction:auditToken:];
```

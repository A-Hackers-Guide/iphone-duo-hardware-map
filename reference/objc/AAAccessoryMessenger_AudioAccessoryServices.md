# `AAAccessoryMessenger`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _activateCalled;
B _invalidateCalled;
B _invalidateDone;
I _subscribedCustomMsgTypes;
@"NSObject<OS_xpc_object>" _xpcConnection;
I _clientID;
@? _customMsgReceivedHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@?,C,N,V_customMsgReceivedHandler) customMsgReceivedHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Instance methods

```
-[AAAccessoryMessenger _xpcReceivedMessage:];
-[AAAccessoryMessenger clientID];
-[AAAccessoryMessenger dispatchQueue];
-[AAAccessoryMessenger _ensureXPCStarted];
-[AAAccessoryMessenger activateWithCompletion:];
-[AAAccessoryMessenger setClientID:];
-[AAAccessoryMessenger setInvalidationHandler:];
-[AAAccessoryMessenger init];
-[AAAccessoryMessenger unsubscribeAll];
-[AAAccessoryMessenger interruptionHandler];
-[AAAccessoryMessenger setDispatchQueue:];
-[AAAccessoryMessenger invalidate];
-[AAAccessoryMessenger _activate:];
-[AAAccessoryMessenger _interrupted];
-[AAAccessoryMessenger setInterruptionHandler:];
-[AAAccessoryMessenger description];
-[AAAccessoryMessenger invalidationHandler];
-[AAAccessoryMessenger _invalidated];
-[AAAccessoryMessenger _activateXPC:];
-[AAAccessoryMessenger _xpcConnectionEventHandler:];
-[AAAccessoryMessenger _xpcReceivedCustomMsg:];
-[AAAccessoryMessenger customMsgReceivedHandler];
-[AAAccessoryMessenger sendCustomMessage:msgType:destinationIdentifier:completionHandler:];
-[AAAccessoryMessenger setCustomMsgReceivedHandler:];
-[AAAccessoryMessenger subscribeToCustomMsgs:];
-[AAAccessoryMessenger unsubscribeFromCustomMsgs:];
```

# `AAProxManager`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AAServicesXPCClientInterface`
- 8 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
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
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Instance methods

```
-[AAProxManager testListenerEndpoint];
-[AAProxManager clientID];
-[AAProxManager dispatchQueue];
-[AAProxManager _ensureXPCStarted];
-[AAProxManager setTestListenerEndpoint:];
-[AAProxManager setClientID:];
-[AAProxManager setInvalidationHandler:];
-[AAProxManager init];
-[AAProxManager interruptionHandler];
-[AAProxManager setDispatchQueue:];
-[AAProxManager invalidate];
-[AAProxManager _interrupted];
-[AAProxManager setInterruptionHandler:];
-[AAProxManager _reportError:];
-[AAProxManager description];
-[AAProxManager invalidationHandler];
-[AAProxManager _invalidated];
-[AAProxManager forceLaunchProxCard:completion:];
-[AAProxManager launchProxCard:completion:];
```

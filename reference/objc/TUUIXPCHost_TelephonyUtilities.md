# `TUUIXPCHost`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUUIXPCHostConnectionDelegate`, `NSXPCListenerDelegate`
- 6 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _clientsShouldConnectToken;
@"NSObject<OS_dispatch_queue>" _queue;
@"<TUUIXPCHostDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NSXPCListener" _xpcListener;
@"NSMutableSet" _connections;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<TUUIXPCHostDelegate>",W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_delegateQueue) delegateQueue;
@property (T@"NSXPCListener",&,N,V_xpcListener) xpcListener;
@property (T@"NSMutableSet",&,N,V_connections) connections;
@property (Ti,R,N,V_clientsShouldConnectToken) clientsShouldConnectToken;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUUIXPCHost connections];
-[TUUIXPCHost listener:shouldAcceptNewConnection:];
-[TUUIXPCHost init];
-[TUUIXPCHost connectionInvalidated:];
-[TUUIXPCHost setConnections:];
-[TUUIXPCHost dealloc];
-[TUUIXPCHost endpoint];
-[TUUIXPCHost queue];
-[TUUIXPCHost clientsShouldConnectToken];
-[TUUIXPCHost setDelegate:];
-[TUUIXPCHost setDelegateQueue:];
-[TUUIXPCHost delegate];
-[TUUIXPCHost delegateQueue];
-[TUUIXPCHost initWithDelegate:delegateQueue:];
-[TUUIXPCHost xpcListener];
-[TUUIXPCHost setQueue:];
-[TUUIXPCHost setXpcListener:];
-[TUUIXPCHost broadcastRemoteControlStatusChanged:];
```

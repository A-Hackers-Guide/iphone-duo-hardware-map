# `TUUIXPCHostConnection`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUUIXPCHost`
- 5 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _wantsRemoteControlStatus;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _connection;
@"<TUUIXPCHostConnectionDelegate>" _connectionDelegate;
@"<TUUIXPCHostDelegate>" _hostDelegate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"<TUUIXPCHostConnectionDelegate>",W,N,V_connectionDelegate) connectionDelegate;
@property (T@"<TUUIXPCHostDelegate>",W,N,V_hostDelegate) hostDelegate;
@property (TB,N,V_wantsRemoteControlStatus) wantsRemoteControlStatus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUUIXPCHostConnection connectionDelegate];
-[TUUIXPCHostConnection ping];
-[TUUIXPCHostConnection init];
-[TUUIXPCHostConnection hostDelegate];
-[TUUIXPCHostConnection setHostDelegate:];
-[TUUIXPCHostConnection dealloc];
-[TUUIXPCHostConnection shouldHostHandleMRCommand:sourceIdentifier:completion:];
-[TUUIXPCHostConnection fetchRemoteControlStatus:];
-[TUUIXPCHostConnection queue];
-[TUUIXPCHostConnection shouldHostHandleMRCommand:completion:];
-[TUUIXPCHostConnection setConnectionDelegate:];
-[TUUIXPCHostConnection connection];
-[TUUIXPCHostConnection fetchInCallUIState:];
-[TUUIXPCHostConnection setConnection:];
-[TUUIXPCHostConnection handleRedialCommandWhileScreening:];
-[TUUIXPCHostConnection remoteObjectProxy];
-[TUUIXPCHostConnection setQueue:];
-[TUUIXPCHostConnection initWithConnection:hostDelegate:connectionDelegate:queue:];
-[TUUIXPCHostConnection setWantsRemoteControlStatus:];
-[TUUIXPCHostConnection subscribeToRemoteControlStatusWithReply:];
-[TUUIXPCHostConnection wantsRemoteControlStatus];
```

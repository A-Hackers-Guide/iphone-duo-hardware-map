# `TUUIXPCClientConnection`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUUIXPCClient`, `TUUIDataSource`
- 5 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _hasSubscribedToRemoteControlStatus;
@? _remoteControlStatusChangedHandler;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _connection;
@"TUCallCenter" _callCenter;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (T@"TUCallCenter",W,N,V_callCenter) callCenter;
@property (TB,N,V_hasSubscribedToRemoteControlStatus) hasSubscribedToRemoteControlStatus;
@property (T@?,C,N,V_remoteControlStatusChangedHandler) remoteControlStatusChangedHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUUIXPCClientConnection setCallCenter:];
-[TUUIXPCClientConnection remoteControlStatusChanged:];
-[TUUIXPCClientConnection ping];
-[TUUIXPCClientConnection dealloc];
-[TUUIXPCClientConnection setRemoteControlStatusChangedHandler:];
-[TUUIXPCClientConnection setHasSubscribedToRemoteControlStatus:];
-[TUUIXPCClientConnection shouldHostHandleMRCommand:sourceIdentifier:completion:];
-[TUUIXPCClientConnection fetchRemoteControlStatus:];
-[TUUIXPCClientConnection queue];
-[TUUIXPCClientConnection initWithListenerEndpoint:callCenter:];
-[TUUIXPCClientConnection shouldHostHandleMRCommand:completion:];
-[TUUIXPCClientConnection hostWithErrorHandler:];
-[TUUIXPCClientConnection connection];
-[TUUIXPCClientConnection fetchInCallUIState:];
-[TUUIXPCClientConnection setConnection:];
-[TUUIXPCClientConnection hasSubscribedToRemoteControlStatus];
-[TUUIXPCClientConnection handleRedialCommandWhileScreening:];
-[TUUIXPCClientConnection subscribeToRemoteControlStatus];
-[TUUIXPCClientConnection remoteControlStatusChangedHandler];
-[TUUIXPCClientConnection callCenter];
-[TUUIXPCClientConnection host];
-[TUUIXPCClientConnection setQueue:];
```

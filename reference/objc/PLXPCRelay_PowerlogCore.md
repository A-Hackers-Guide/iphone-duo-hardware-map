# `PLXPCRelay`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _relayActive;
@"NSObject<OS_xpc_object>" _xpcConnection;
@"NSObject<OS_xpc_object>" _relayConnection;
@"NSObject<OS_xpc_object>" _xpcCrashMoverConn;
@"NSObject<OS_dispatch_queue>" _crashMoverQueue;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,V_xpcConnection) xpcConnection;
@property (T@"NSObject<OS_xpc_object>",&,N,V_relayConnection) relayConnection;
@property (T@"NSObject<OS_xpc_object>",&,V_xpcCrashMoverConn) xpcCrashMoverConn;
@property (T@"NSObject<OS_dispatch_queue>",&,V_crashMoverQueue) crashMoverQueue;
@property (TB,V_relayActive) relayActive;
```

## Class methods

```
+[PLXPCRelay sharedInstance];
```

## Instance methods

```
-[PLXPCRelay init];
-[PLXPCRelay setXpcConnection:];
-[PLXPCRelay xpcConnection];
-[PLXPCRelay isDebugEnabled];
-[PLXPCRelay startRelay];
-[PLXPCRelay stopRelay];
-[PLXPCRelay relayConnection];
-[PLXPCRelay setRelayActive:];
-[PLXPCRelay crashMoverQueue];
-[PLXPCRelay handleCrashMoverConnection:];
-[PLXPCRelay handlePeer:forEvent:];
-[PLXPCRelay movePowerlogs];
-[PLXPCRelay relayActive];
-[PLXPCRelay resetRelayConnection];
-[PLXPCRelay setCrashMoverQueue:];
-[PLXPCRelay setRelayConnection:];
-[PLXPCRelay setXpcCrashMoverConn:];
-[PLXPCRelay xpcCrashMoverConn];
```

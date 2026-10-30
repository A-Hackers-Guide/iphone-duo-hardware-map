# `PLHUDControl`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _isInvalidated;
@"BSServiceConnection<BSServiceConnectionClient>" _connection;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
```

## Properties

```
@property (T@"BSServiceConnection<BSServiceConnectionClient>",&,N,V_connection) connection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_connectionQueue) connectionQueue;
@property (TB,N,V_isInvalidated) isInvalidated;
@property (TB,N) internalHUDEnabled;
```

## Instance methods

```
-[PLHUDControl connectionQueue];
-[PLHUDControl setConnectionQueue:];
-[PLHUDControl init];
-[PLHUDControl dealloc];
-[PLHUDControl isInvalidated];
-[PLHUDControl invalidate];
-[PLHUDControl connection];
-[PLHUDControl setConnection:];
-[PLHUDControl setIsInvalidated:];
-[PLHUDControl _ensureConnection];
-[PLHUDControl _hudServer];
-[PLHUDControl internalHUDEnabled];
-[PLHUDControl setInternalHUDEnabled:];
```

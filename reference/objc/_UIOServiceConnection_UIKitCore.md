# `_UIOServiceConnection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIOverlayServiceClientToServerInterface`
- 3 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"BSServiceConnection<BSServiceConnectionHost>" _connection;
@"UIOServer" _server;
```

## Properties

```
@property (T@"BSServiceConnection<BSServiceConnectionHost>",R,W,N,V_connection) connection;
@property (T@"UIOServer",R,W,N,V_server) server;
@property (Tq,R,N) pid;
@property (T@"NSString",R,N) bundleIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIOServiceConnection connectionWithBSServiceConnection:toServer:];
```

## Instance methods

```
-[_UIOServiceConnection removeAllObservers];
-[_UIOServiceConnection server];
-[_UIOServiceConnection removeObserver:];
-[_UIOServiceConnection bundleIdentifier];
-[_UIOServiceConnection addObserver:];
-[_UIOServiceConnection pid];
-[_UIOServiceConnection sendAction:];
-[_UIOServiceConnection connection];
-[_UIOServiceConnection hash];
-[_UIOServiceConnection isEqual:];
-[_UIOServiceConnection clientHasEntitlement:];
-[_UIOServiceConnection performOverlayServerAction:];
-[_UIOServiceConnection serviceConnectionDidInvalidate];
```

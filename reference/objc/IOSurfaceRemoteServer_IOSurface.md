# `IOSurfaceRemoteServer`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _listener;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _clients;
```

## Properties

```
@property (T@"NSObject<OS_xpc_object>",&,N,V_listener) listener;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSMutableArray",&,N,V_clients) clients;
```

## Instance methods

```
-[IOSurfaceRemoteServer clients];
-[IOSurfaceRemoteServer shutdown];
-[IOSurfaceRemoteServer setClients:];
-[IOSurfaceRemoteServer dealloc];
-[IOSurfaceRemoteServer setListener:];
-[IOSurfaceRemoteServer queue];
-[IOSurfaceRemoteServer listener];
-[IOSurfaceRemoteServer setQueue:];
-[IOSurfaceRemoteServer _handleClientConnection:];
-[IOSurfaceRemoteServer _handleClientDisconnected:];
-[IOSurfaceRemoteServer initWithListener:options:];
```

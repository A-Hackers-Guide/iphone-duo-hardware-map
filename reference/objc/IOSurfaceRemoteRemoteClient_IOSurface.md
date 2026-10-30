# `IOSurfaceRemoteRemoteClient`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _pid;
@"NSMutableDictionary" _surfaceStates;
@"NSObject<OS_xpc_object>" _remoteConnection;
@"NSObject<OS_dispatch_queue>" _disconnectedQueue;
@? _disconnectedHandler;
```

## Properties

```
@property (Ti,N,V_pid) pid;
@property (T@"NSMutableDictionary",&,N,V_surfaceStates) surfaceStates;
@property (T@"NSObject<OS_xpc_object>",&,N,V_remoteConnection) remoteConnection;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_disconnectedQueue) disconnectedQueue;
@property (T@?,C,N,V_disconnectedHandler) disconnectedHandler;
```

## Instance methods

```
-[IOSurfaceRemoteRemoteClient _handleError:];
-[IOSurfaceRemoteRemoteClient setPid:];
-[IOSurfaceRemoteRemoteClient dealloc];
-[IOSurfaceRemoteRemoteClient pid];
-[IOSurfaceRemoteRemoteClient _handleMessage:];
-[IOSurfaceRemoteRemoteClient description];
-[IOSurfaceRemoteRemoteClient _removeSurface:];
-[IOSurfaceRemoteRemoteClient initWithRemoteConnection:disconnectedQueue:disconnectedHandler:];
-[IOSurfaceRemoteRemoteClient _addSurface:mappedAddress:mappedSize:extraData:];
-[IOSurfaceRemoteRemoteClient _getClient:inboundExtradata:outboundExtraData:];
-[IOSurfaceRemoteRemoteClient disconnectedHandler];
-[IOSurfaceRemoteRemoteClient disconnectedQueue];
-[IOSurfaceRemoteRemoteClient remoteConnection];
-[IOSurfaceRemoteRemoteClient setDisconnectedHandler:];
-[IOSurfaceRemoteRemoteClient setDisconnectedQueue:];
-[IOSurfaceRemoteRemoteClient setRemoteConnection:];
-[IOSurfaceRemoteRemoteClient setSurfaceStates:];
-[IOSurfaceRemoteRemoteClient surfaceStates];
```

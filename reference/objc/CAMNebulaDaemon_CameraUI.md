# `CAMNebulaDaemon`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `CAMNebulaDaemonConnectionManagerDelegate`, `CAMPersistenceResultDelegate`
- 6 instance variables, 10 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" __queue;
@"CAMTimelapseBackendController" __timelapseBackendController;
@"CAMPersistenceController" __persistenceController;
@"CAMNebulaKeepAliveController" __keepAliveController;
@"NSXPCListener" __listener;
@"NSMutableArray" __connections;
```

## Properties

```
@property (T@"CAMTimelapseBackendController",R,N,V__timelapseBackendController) _timelapseBackendController;
@property (T@"CAMPersistenceController",R,N,V__persistenceController) _persistenceController;
@property (T@"CAMNebulaKeepAliveController",R,N,V__keepAliveController) _keepAliveController;
@property (T@"NSXPCListener",R,N,V__listener) _listener;
@property (T@"NSMutableArray",R,N,V__connections) _connections;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__queue) _queue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMNebulaDaemon listener:shouldAcceptNewConnection:];
-[CAMNebulaDaemon init];
-[CAMNebulaDaemon _persistenceController];
-[CAMNebulaDaemon _queue];
-[CAMNebulaDaemon _keepAliveController];
-[CAMNebulaDaemon _listener];
-[CAMNebulaDaemon _connections];
-[CAMNebulaDaemon allowedProtocolForClientAccess:];
-[CAMNebulaDaemon _timelapseBackendController];
-[CAMNebulaDaemon daemonConnectionManagerHasBeenDisconnected:];
-[CAMNebulaDaemon performPendingWorkAfterDelay:];
-[CAMNebulaDaemon persistenceController:didGenerateVideoLocalPersistenceResult:forCaptureResult:fromRequest:];
```

# `_UIDragMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 6 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSString" _serviceName;
@"<_UIDragMonitorDelegate>" _delegate;
@"NSXPCListener" _xpcListener;
@"_UIDragMonitorSessionLifecyleListener" _lifecycleListener;
@"NSMutableArray" _activeConnections;
@"NSObject<OS_dispatch_queue>" _xpcQueue;
```

## Properties

```
@property (T@"NSString",&,N,V_serviceName) serviceName;
@property (T@"NSXPCListener",&,N,V_xpcListener) xpcListener;
@property (T@"_UIDragMonitorSessionLifecyleListener",&,N,V_lifecycleListener) lifecycleListener;
@property (T@"NSMutableArray",&,N,V_activeConnections) activeConnections;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_xpcQueue) xpcQueue;
@property (T@"<_UIDragMonitorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDragMonitor initWithMachServiceName:];
-[_UIDragMonitor listener:shouldAcceptNewConnection:];
-[_UIDragMonitor dealloc];
-[_UIDragMonitor invalidate];
-[_UIDragMonitor serviceName];
-[_UIDragMonitor setDelegate:];
-[_UIDragMonitor setServiceName:];
-[_UIDragMonitor activate];
-[_UIDragMonitor delegate];
-[_UIDragMonitor setXpcQueue:];
-[_UIDragMonitor activeConnections];
-[_UIDragMonitor xpcQueue];
-[_UIDragMonitor xpcListener];
-[_UIDragMonitor setXpcListener:];
-[_UIDragMonitor _tearDownConnections];
-[_UIDragMonitor lifecycleListener];
-[_UIDragMonitor setActiveConnections:];
-[_UIDragMonitor setLifecycleListener:];
```

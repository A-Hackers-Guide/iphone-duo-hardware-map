# `UIDraggingSystemMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`, `_DUIClientSystemApp`
- 4 instance variables, 6 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSXPCListener" _systemListener;
@"NSObject<OS_dispatch_queue>" _xpcQueue;
@"NSMapTable" _sessionsBySessionInfo;
@"<UIDraggingSystemMonitorDelegate>" _delegate;
```

## Properties

```
@property (T@"NSSet",R,N) sessions;
@property (T@"<UIDraggingSystemMonitorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDraggingSystemMonitor sharedInstance];
+[UIDraggingSystemMonitor new];
```

## Instance methods

```
-[UIDraggingSystemMonitor listener:shouldAcceptNewConnection:];
-[UIDraggingSystemMonitor init];
-[UIDraggingSystemMonitor sessions];
-[UIDraggingSystemMonitor _init];
-[UIDraggingSystemMonitor setDelegate:];
-[UIDraggingSystemMonitor delegate];
-[UIDraggingSystemMonitor dragDidBeginWithSystemSession:info:reply:];
-[UIDraggingSystemMonitor dragDidEndWithSystemSession:];
-[UIDraggingSystemMonitor sessionForDropSession:];
-[UIDraggingSystemMonitor xpcQueue_acceptNewConnection:];
-[UIDraggingSystemMonitor xpcQueue_shouldAcceptNewConnection:];
```

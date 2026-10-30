# `SBApplicationUserQuitMonitorServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"BSServiceConnectionListener" _connectionListener;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _connections;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationUserQuitMonitorServer listener:didReceiveConnection:withContext:];
-[SBApplicationUserQuitMonitorServer init];
-[SBApplicationUserQuitMonitorServer userClosedLastSceneOfApplicationWithBundleID:];
-[SBApplicationUserQuitMonitorServer _queue_addConnection:];
-[SBApplicationUserQuitMonitorServer _queue_removeConnection:];
```

# `SBSystemApertureLayoutMonitorServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `BSInvalidatable`
- 7 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _clientServiceCollectionLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _framesCollectionLock;
@"NSMutableArray" _connections;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnectionListener" _connectionListener;
@"NSArray" _frames;
B _isValid;
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
-[SBSystemApertureLayoutMonitorServer listener:didReceiveConnection:withContext:];
-[SBSystemApertureLayoutMonitorServer init];
-[SBSystemApertureLayoutMonitorServer _systemApertureLayoutDidChange:];
-[SBSystemApertureLayoutMonitorServer invalidate];
-[SBSystemApertureLayoutMonitorServer _notifyConnectedListenersOfUpdatedFrames];
```

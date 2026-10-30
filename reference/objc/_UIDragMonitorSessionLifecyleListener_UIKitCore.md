# `_UIDragMonitorSessionLifecyleListener`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_DUIDragSessionLifecycleListening`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<_UIDragMonitorDelegate>" _delegate;
@"_UIDragMonitor" _dragMonitor;
```

## Properties

```
@property (T@"<_UIDragMonitorDelegate>",W,N,V_delegate) delegate;
@property (T@"_UIDragMonitor",W,N,V_dragMonitor) dragMonitor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDragMonitorSessionLifecyleListener setDelegate:];
-[_UIDragMonitorSessionLifecyleListener delegate];
-[_UIDragMonitorSessionLifecyleListener setDragMonitor:];
-[_UIDragMonitorSessionLifecyleListener dragDidBeginWithSession:identifier:reply:];
-[_UIDragMonitorSessionLifecyleListener dragDidEndWithSession:];
-[_UIDragMonitorSessionLifecyleListener dragDidEndWithSession:identifier:];
-[_UIDragMonitorSessionLifecyleListener dragMonitor];
-[_UIDragMonitorSessionLifecyleListener initWithDragMonitor:];
```

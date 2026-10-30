# `SBSecureIndicatorElevationServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `BSInvalidatable`
- 7 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _assertionsLock;
@"NSMutableArray" _assertions;
@"NSMutableArray" _connections;
q _requestedElevationStyle;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"BSServiceConnectionListener" _connectionListener;
@"<SBSecureIndicatorElevationServerDelegate>" _delegate;
```

## Properties

```
@property (Tq,R,N) requestedElevationStyle;
@property (T@"<SBSecureIndicatorElevationServerDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSecureIndicatorElevationServer listener:didReceiveConnection:withContext:];
-[SBSecureIndicatorElevationServer initWithDelegate:];
-[SBSecureIndicatorElevationServer invalidate];
-[SBSecureIndicatorElevationServer delegate];
-[SBSecureIndicatorElevationServer _recomputeAggregateStyle];
-[SBSecureIndicatorElevationServer requestedElevationStyle];
```

# `DCSelectorDelayer`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _waitToFireUntilRequestsStop;
B _callOnMainThread;
@ _target;
: _selector;
d _delay;
@"NSObject<OS_dispatch_queue>" _requestQueue;
@? _fireBlock;
```

## Properties

```
@property (T@,W,N,V_target) target;
@property (T:,N,V_selector) selector;
@property (TB,N,V_waitToFireUntilRequestsStop) waitToFireUntilRequestsStop;
@property (TB,N,V_callOnMainThread) callOnMainThread;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_requestQueue) requestQueue;
@property (T@?,C,N,V_fireBlock) fireBlock;
@property (Td,V_delay) delay;
@property (TB,R,N) isScheduledToFire;
```

## Instance methods

```
-[DCSelectorDelayer selector];
-[DCSelectorDelayer requestQueue];
-[DCSelectorDelayer cancelPreviousFireRequests];
-[DCSelectorDelayer dealloc];
-[DCSelectorDelayer fireImmediately];
-[DCSelectorDelayer setSelector:];
-[DCSelectorDelayer delay];
-[DCSelectorDelayer waitToFireUntilRequestsStop];
-[DCSelectorDelayer callTargetSelector];
-[DCSelectorDelayer _cancelFireRequests];
-[DCSelectorDelayer setTarget:];
-[DCSelectorDelayer setDelay:];
-[DCSelectorDelayer requestFire];
-[DCSelectorDelayer target];
-[DCSelectorDelayer callOnMainThread];
-[DCSelectorDelayer initWithTarget:selector:delay:waitToFireUntilRequestsStop:callOnMainThread:];
-[DCSelectorDelayer setCallOnMainThread:];
-[DCSelectorDelayer setWaitToFireUntilRequestsStop:];
-[DCSelectorDelayer setFireBlock:];
-[DCSelectorDelayer fireBlock];
-[DCSelectorDelayer isScheduledToFire];
-[DCSelectorDelayer setRequestQueue:];
```

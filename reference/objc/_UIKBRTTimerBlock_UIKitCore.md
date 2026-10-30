# `_UIKBRTTimerBlock`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _selfQueue;
@"NSTimer" _timer;
@"NSObject<OS_dispatch_queue>" _queue;
@? _onTimer;
@ _owner;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_selfQueue) selfQueue;
@property (T@"NSTimer",R,N,V_timer) timer;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@?,R,C,N,V_onTimer) onTimer;
@property (T@,R,N,V_owner) owner;
```

## Instance methods

```
-[_UIKBRTTimerBlock owner];
-[_UIKBRTTimerBlock timer];
-[_UIKBRTTimerBlock dealloc];
-[_UIKBRTTimerBlock queue];
-[_UIKBRTTimerBlock invalidate];
-[_UIKBRTTimerBlock timerFired:];
-[_UIKBRTTimerBlock fireNow];
-[_UIKBRTTimerBlock onTimer];
-[_UIKBRTTimerBlock initWithTimeInterval:onQueue:do:owner:];
-[_UIKBRTTimerBlock selfQueue];
```

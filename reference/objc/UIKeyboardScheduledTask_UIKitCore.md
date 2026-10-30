# `UIKeyboardScheduledTask`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@? _task;
d _timeInterval;
@"UIKeyboardTaskQueue" _taskQueue;
@"NSTimer" _timer;
@"_UIActionWhenIdle" _deferredAction;
@? _enqueuedTask;
@? _breadcrumb;
```

## Properties

```
@property (T@"UIKeyboardTaskQueue",R,N,V_taskQueue) taskQueue;
@property (T@"NSTimer",&,N,V_timer) timer;
@property (T@"_UIActionWhenIdle",&,N,V_deferredAction) deferredAction;
@property (T@?,C,N,V_enqueuedTask) enqueuedTask;
@property (T@?,C,N,V_breadcrumb) breadcrumb;
@property (T@?,R,N,V_task) task;
@property (Td,R,N,V_timeInterval) timeInterval;
@property (TB,R,N) repeats;
```

## Instance methods

```
-[UIKeyboardScheduledTask taskQueue];
-[UIKeyboardScheduledTask repeats];
-[UIKeyboardScheduledTask timeInterval];
-[UIKeyboardScheduledTask setTimer:];
-[UIKeyboardScheduledTask initWithTaskQueue:timeInterval:repeats:task:breadcrumb:];
-[UIKeyboardScheduledTask timer];
-[UIKeyboardScheduledTask dealloc];
-[UIKeyboardScheduledTask breadcrumb];
-[UIKeyboardScheduledTask invalidate];
-[UIKeyboardScheduledTask enqueuedTask];
-[UIKeyboardScheduledTask setDeferredAction:];
-[UIKeyboardScheduledTask isValid];
-[UIKeyboardScheduledTask resetTimer];
-[UIKeyboardScheduledTask setEnqueuedTask:];
-[UIKeyboardScheduledTask task];
-[UIKeyboardScheduledTask deferredAction];
-[UIKeyboardScheduledTask timerFired:];
-[UIKeyboardScheduledTask handleDeferredTimerFiredEvent];
-[UIKeyboardScheduledTask setBreadcrumb:];
```

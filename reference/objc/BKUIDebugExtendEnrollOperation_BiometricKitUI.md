# `BKUIDebugExtendEnrollOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKExtendEnrollTouchIDOperation`
- 5 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _simulatedState;
@"NSTimer" _timer;
q _presses;
B _endReported;
@"NSObject<OS_os_log>" _log;
```

## Instance methods

```
-[BKUIDebugExtendEnrollOperation startWithError:];
-[BKUIDebugExtendEnrollOperation init];
-[BKUIDebugExtendEnrollOperation dealloc];
-[BKUIDebugExtendEnrollOperation cancel];
-[BKUIDebugExtendEnrollOperation state];
-[BKUIDebugExtendEnrollOperation _stop:];
-[BKUIDebugExtendEnrollOperation _reportEndReason:];
-[BKUIDebugExtendEnrollOperation _reportStateChanged:];
-[BKUIDebugExtendEnrollOperation _scheduledPressTimer];
-[BKUIDebugExtendEnrollOperation _simulatePress];
```

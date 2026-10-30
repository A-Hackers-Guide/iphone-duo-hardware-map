# `BKUIDebugEnrollOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKEnrollTouchIDOperation`
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
-[BKUIDebugEnrollOperation startWithError:];
-[BKUIDebugEnrollOperation init];
-[BKUIDebugEnrollOperation dealloc];
-[BKUIDebugEnrollOperation cancel];
-[BKUIDebugEnrollOperation state];
-[BKUIDebugEnrollOperation _stop:];
-[BKUIDebugEnrollOperation _reportEndReason:];
-[BKUIDebugEnrollOperation _reportStateChanged:];
-[BKUIDebugEnrollOperation _scheduledPressTimer];
-[BKUIDebugEnrollOperation _simulatePress];
```

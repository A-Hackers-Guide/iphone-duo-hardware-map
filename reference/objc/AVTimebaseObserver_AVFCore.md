# `AVTimebaseObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _timerQueue;
@"AVWeakReference" _weakReference;
@"NSObject<OS_dispatch_source>" _timerSource;
^{OpaqueCMTimebase=} _timebase;
B _isObservingTimebase;
d _lastRate;
d _currentRate;
B _invalid;
```

## Properties

```
@property (T@"AVWeakReference",R,N,G_weakReference,V_weakReference) weakReference;
@property (T^{OpaqueCMTimebase=},R) timebase;
@property (TB,R,N) invalidated;
```

## Instance methods

```
-[AVTimebaseObserver timebase];
-[AVTimebaseObserver invalidated];
-[AVTimebaseObserver dealloc];
-[AVTimebaseObserver invalidate];
-[AVTimebaseObserver _effectiveRateChanged];
-[AVTimebaseObserver _weakReference];
-[AVTimebaseObserver _handleTimeDiscontinuity];
-[AVTimebaseObserver _resetNextFireTime];
-[AVTimebaseObserver _attachTimerSourceToTimebase];
-[AVTimebaseObserver _finishInitializationWithTimerEventHandler:];
-[AVTimebaseObserver _reallyInvalidate];
-[AVTimebaseObserver _removeTimebaseFromTimerSource];
-[AVTimebaseObserver _startObservingTimebaseNotifications];
-[AVTimebaseObserver _stopObservingTimebaseNotifications];
-[AVTimebaseObserver initWithTimebase:queue:];
```

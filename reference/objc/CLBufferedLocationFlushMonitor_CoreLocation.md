# `CLBufferedLocationFlushMonitor`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
d _flushThreshold;
@"NSObject<OS_dispatch_queue>" _completionQueue;
@"NSObject<OS_dispatch_queue>" _stateQueue;
@? _completion;
@"NSObject<OS_dispatch_source>" _timer;
@"NSDate" _lastTimestamp;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _fired;
```

## Properties

```
@property (TB,R,N) hasFired;
```

## Instance methods

```
-[CLBufferedLocationFlushMonitor hasFired];
-[CLBufferedLocationFlushMonitor dealloc];
-[CLBufferedLocationFlushMonitor abortWithError:];
-[CLBufferedLocationFlushMonitor fireCompletionWithOutcome:error:];
-[CLBufferedLocationFlushMonitor initWithFlushDate:timeoutSeconds:completionQueue:completion:];
-[CLBufferedLocationFlushMonitor noteDeliveredTimestamp:];
```

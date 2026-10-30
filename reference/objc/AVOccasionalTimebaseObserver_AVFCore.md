# `AVOccasionalTimebaseObserver`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVTimebaseObserver`
- 2 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _times;
@? _block;
```

## Instance methods

```
-[AVOccasionalTimebaseObserver dealloc];
-[AVOccasionalTimebaseObserver _effectiveRateChanged];
-[AVOccasionalTimebaseObserver _handleTimeDiscontinuity];
-[AVOccasionalTimebaseObserver _resetNextFireTime];
-[AVOccasionalTimebaseObserver _fireBlock];
-[AVOccasionalTimebaseObserver _nextFiringTimeAfterTime:];
-[AVOccasionalTimebaseObserver _previousFiringTimeBeforeTime:];
-[AVOccasionalTimebaseObserver initWithTimebase:times:queue:block:];
```

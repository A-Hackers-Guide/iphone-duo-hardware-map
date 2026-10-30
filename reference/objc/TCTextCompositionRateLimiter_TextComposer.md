# `TCTextCompositionRateLimiter`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _previousExecutionDates;
@"NSDate" _overriddenCurrentDate;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Instance methods

```
-[TCTextCompositionRateLimiter currentDate];
-[TCTextCompositionRateLimiter init];
-[TCTextCompositionRateLimiter allowRequest];
-[TCTextCompositionRateLimiter overrideCurrentDateForThrottleTesting:];
-[TCTextCompositionRateLimiter resetRateLimiter];
```

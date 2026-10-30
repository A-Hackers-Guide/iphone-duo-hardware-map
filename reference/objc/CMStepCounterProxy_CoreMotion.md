# `CMStepCounterProxy`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
B fStartedUpdates;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
q fStepCountFromStart;
q fPrevStepCount;
```

## Instance methods

```
-[CMStepCounterProxy init];
-[CMStepCounterProxy dealloc];
-[CMStepCounterProxy _handleQueryResponse:onQueue:withHandler:];
-[CMStepCounterProxy _teardown];
-[CMStepCounterProxy _queryStepCountStartingFromInternal:to:toQueue:withHandler:];
-[CMStepCounterProxy _startStepCountingUpdatesToQueue:updateOn:withHandler:];
```

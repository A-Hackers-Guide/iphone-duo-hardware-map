# `ULHomeSlamStopDetection`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 30 instance methods, 0 class methods

## Instance variables

```
^{ULDatabaseStoreInterface=^^?} _dbStore;
q _state;
@"ULHomeSlamFence" _largeFence;
@"ULHomeSlamFence" _smallFence;
@"ULHomeSlamFence" _staticFence;
@"ULHomeSlamTimer" _longTimer;
@"ULHomeSlamTimer" _shortTimer;
```

## Properties

```
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (Tq,N,V_state) state;
@property (T@"ULHomeSlamFence",&,N,V_largeFence) largeFence;
@property (T@"ULHomeSlamFence",&,N,V_smallFence) smallFence;
@property (T@"ULHomeSlamFence",&,N,V_staticFence) staticFence;
@property (T@"ULHomeSlamTimer",&,N,V_longTimer) longTimer;
@property (T@"ULHomeSlamTimer",&,N,V_shortTimer) shortTimer;
```

## Instance methods

```
-[ULHomeSlamStopDetection setState:];
-[ULHomeSlamStopDetection state];
-[ULHomeSlamStopDetection longTimer];
-[ULHomeSlamStopDetection _setStaticFence];
-[ULHomeSlamStopDetection dbStore];
-[ULHomeSlamStopDetection runStopDetectionAnalysisFromTime:toTime:withOdometrySourceType:];
-[ULHomeSlamStopDetection setStaticFence:];
-[ULHomeSlamStopDetection _enterMotionStateAtTime:];
-[ULHomeSlamStopDetection _enterStaticState];
-[ULHomeSlamStopDetection _getStopMotionTriggersFromOdometryEntries:];
-[ULHomeSlamStopDetection _runMotionStateLogicWithEntry:andTriggers:];
-[ULHomeSlamStopDetection _runStaticStateLogicWithEntry:andTriggers:];
-[ULHomeSlamStopDetection _setLargeMotionFence];
-[ULHomeSlamStopDetection _setLongMotionTimerStartingDate:];
-[ULHomeSlamStopDetection _setShortMotionTimerStartingDate:];
-[ULHomeSlamStopDetection _setSmallMotionFence];
-[ULHomeSlamStopDetection _shouldExitMotionState:];
-[ULHomeSlamStopDetection _shouldExitStaticState:];
-[ULHomeSlamStopDetection _timepointToDate:];
-[ULHomeSlamStopDetection _updateFencesAndTimersInMotionStateWithEntry:];
-[ULHomeSlamStopDetection initWithDbStore:];
-[ULHomeSlamStopDetection largeFence];
-[ULHomeSlamStopDetection setDbStore:];
-[ULHomeSlamStopDetection setLargeFence:];
-[ULHomeSlamStopDetection setLongTimer:];
-[ULHomeSlamStopDetection setShortTimer:];
-[ULHomeSlamStopDetection setSmallFence:];
-[ULHomeSlamStopDetection shortTimer];
-[ULHomeSlamStopDetection smallFence];
-[ULHomeSlamStopDetection staticFence];
```

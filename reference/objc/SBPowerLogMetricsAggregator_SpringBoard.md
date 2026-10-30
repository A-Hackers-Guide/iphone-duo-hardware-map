# `SBPowerLogMetricsAggregator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _backgroundPowerLogQueue;
B _flushScheduled;
@"NSMutableDictionary" _eventsWithDuration;
@"NSCalendar" _gregorian;
```

## Instance methods

```
-[SBPowerLogMetricsAggregator init];
-[SBPowerLogMetricsAggregator _flushEvents];
-[SBPowerLogMetricsAggregator _startTimerIfNecessary];
-[SBPowerLogMetricsAggregator emitEventOfType:];
-[SBPowerLogMetricsAggregator emitEventOfType:withDuration:];
-[SBPowerLogMetricsAggregator flushEventsDueToIminentPowerdown];
```

# `ULHomeSlamAnalyticEventAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 7 instance methods, 3 class methods

## Class methods

```
+[ULHomeSlamAnalyticEventAnalyzer _timepointToDate:];
+[ULHomeSlamAnalyticEventAnalyzer aggregateTimeBetweenEvent:andEvent:startDate:endDate:withDBStore:];
+[ULHomeSlamAnalyticEventAnalyzer countEventOccurrences:fromDate:untilDate:fromDBStore:];
```

## Instance methods

```
-[ULHomeSlamAnalyticEventAnalyzer init];
-[ULHomeSlamAnalyticEventAnalyzer _analyzeTriggersAndGetCA:fromDate:untilDate:withDBStore:];
-[ULHomeSlamAnalyticEventAnalyzer _checkIfScreenTransitionedToOnBefore:after:withEvents:];
-[ULHomeSlamAnalyticEventAnalyzer _daemonWasRestartedWithEvents:];
-[ULHomeSlamAnalyticEventAnalyzer _hoursFromFirstEventToDate:withDBStore:];
-[ULHomeSlamAnalyticEventAnalyzer _wasLastScreenStateOnBefore:withEvents:];
-[ULHomeSlamAnalyticEventAnalyzer runStopDetectionAnalysisAtTimepoint:withDBStore:];
```

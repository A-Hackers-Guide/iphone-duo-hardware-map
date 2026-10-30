# `PLTimeReferenceDynamic`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLTimeReference`
- 7 instance variables, 7 properties, 27 instance methods, 1 class methods

## Instance variables

```
i _offsetHistoryHead;
@"NSMutableDictionary" _timeChangeBlocks;
d _tooFarInFutureDistance;
d _tooFarInPastDistance;
@"NSDate" _lastQueryTime;
@"NSMutableArray" _offsetHistory;
@"PLTimer" _periodicCurrentTime;
```

## Properties

```
@property (T@"NSMutableArray",&,V_offsetHistory) offsetHistory;
@property (Ti,V_offsetHistoryHead) offsetHistoryHead;
@property (T@"PLTimer",&,V_periodicCurrentTime) periodicCurrentTime;
@property (T@"NSMutableDictionary",&,V_timeChangeBlocks) timeChangeBlocks;
@property (Td,V_tooFarInFutureDistance) tooFarInFutureDistance;
@property (Td,V_tooFarInPastDistance) tooFarInPastDistance;
@property (T@"NSDate",&,V_lastQueryTime) lastQueryTime;
```

## Class methods

```
+[PLTimeReferenceDynamic nearestDistanceFromDate:toRegionWithStartDate:andEndDate:];
```

## Instance methods

```
-[PLTimeReferenceDynamic registerForClockSetNotification];
-[PLTimeReferenceDynamic registerForTimeChangedNotification];
-[PLTimeReferenceDynamic initWithTimeManager:entryDefinitionKey:timeReferenceType:];
-[PLTimeReferenceDynamic setOffset:];
-[PLTimeReferenceDynamic checkForTimeChangeWithCurrentTime:];
-[PLTimeReferenceDynamic initializeOffsetHistoryWithEntries:];
-[PLTimeReferenceDynamic initializeOffsetWithEntries:];
-[PLTimeReferenceDynamic lastQueryTime];
-[PLTimeReferenceDynamic newOffsetEntryWithCurrentTime];
-[PLTimeReferenceDynamic notifyTimeChange:];
-[PLTimeReferenceDynamic offsetHistory];
-[PLTimeReferenceDynamic offsetHistoryHead];
-[PLTimeReferenceDynamic periodicCurrentTime];
-[PLTimeReferenceDynamic registerForTimeChangedCallbackWithIdentifier:usingBlock:];
-[PLTimeReferenceDynamic removeTimeOffsetFromReferenceTime:];
-[PLTimeReferenceDynamic setLastQueryTime:];
-[PLTimeReferenceDynamic setOffsetHistory:];
-[PLTimeReferenceDynamic setOffsetHistoryHead:];
-[PLTimeReferenceDynamic setPeriodicCurrentTime:];
-[PLTimeReferenceDynamic setTimeChangeBlocks:];
-[PLTimeReferenceDynamic setTooFarInFutureDistance:];
-[PLTimeReferenceDynamic setTooFarInPastDistance:];
-[PLTimeReferenceDynamic shouldQueryCurrentTime];
-[PLTimeReferenceDynamic timeChangeBlocks];
-[PLTimeReferenceDynamic tooFarInFutureDistance];
-[PLTimeReferenceDynamic tooFarInPastDistance];
-[PLTimeReferenceDynamic unregisterForTimeChangedCallbackWithIdentifier:];
```

# `PLIntervalData`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
i _intervalDuration;
@"NSMutableDictionary" _metrics;
@"NSDate" _currentInterval;
Q _aggdValue;
@"NSDateFormatter" _dateFormat;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_metrics) metrics;
@property (T@"NSDate",&,V_currentInterval) currentInterval;
@property (TQ,V_aggdValue) aggdValue;
@property (T@"NSDateFormatter",&,V_dateFormat) dateFormat;
@property (Ti,V_intervalDuration) intervalDuration;
```

## Instance methods

```
-[PLIntervalData setMetrics:];
-[PLIntervalData init];
-[PLIntervalData metrics];
-[PLIntervalData dateFormat];
-[PLIntervalData setDateFormat:];
-[PLIntervalData resetMetrics];
-[PLIntervalData currentInterval];
-[PLIntervalData intervalDuration];
-[PLIntervalData setIntervalDuration:];
-[PLIntervalData setCurrentInterval:];
-[PLIntervalData addMetric:];
-[PLIntervalData aggdValue];
-[PLIntervalData setAggdValue:];
-[PLIntervalData submitIntervalData];
-[PLIntervalData submitToCA:];
-[PLIntervalData updateMetric:withTimestamp:forEvent:withValue:];
```

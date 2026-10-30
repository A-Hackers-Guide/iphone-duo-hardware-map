# `PLActivityCriterionTime`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLActivityCriterion`
- 3 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
d _interval;
d _rescheduleDelay;
@"PLMonotonicTimer" _timer;
```

## Properties

```
@property (Td,V_interval) interval;
@property (Td,N,V_rescheduleDelay) rescheduleDelay;
@property (T@"PLMonotonicTimer",&,V_timer) timer;
```

## Class methods

```
+[PLActivityCriterionTime minTimeInterval];
+[PLActivityCriterionTime timeCriterionWithInterval:];
```

## Instance methods

```
-[PLActivityCriterionTime setTimer:];
-[PLActivityCriterionTime setInterval:];
-[PLActivityCriterionTime interval];
-[PLActivityCriterionTime timer];
-[PLActivityCriterionTime dealloc];
-[PLActivityCriterionTime description];
-[PLActivityCriterionTime initWithInterval:];
-[PLActivityCriterionTime rescheduleDelay];
-[PLActivityCriterionTime didCompleteActivity:];
-[PLActivityCriterionTime didDisableActivity:];
-[PLActivityCriterionTime didEnableActivity:];
-[PLActivityCriterionTime didInterruptActivity:];
-[PLActivityCriterionTime setRescheduleDelay:];
```

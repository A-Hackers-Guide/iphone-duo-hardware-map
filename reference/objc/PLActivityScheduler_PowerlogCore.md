# `PLActivityScheduler`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _activities;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_activities) activities;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
```

## Class methods

```
+[PLActivityScheduler sharedInstance];
```

## Instance methods

```
-[PLActivityScheduler setWorkQueue:];
-[PLActivityScheduler activities];
-[PLActivityScheduler init];
-[PLActivityScheduler workQueue];
-[PLActivityScheduler setActivities:];
-[PLActivityScheduler cancelActivityWithIdentifier:];
-[PLActivityScheduler lastCompletedDateWithIdentifier:];
-[PLActivityScheduler scheduleActivityWithIdentifier:withCriteria:withMustRunCriterion:withQueue:withInterruptBlock:withActivityBlock:];
```

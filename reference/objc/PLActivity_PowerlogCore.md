# `PLActivity`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLActivityCriterionDelegate`
- 10 instance variables, 14 properties, 33 instance methods, 3 class methods

## Instance variables

```
B _enabled;
q _state;
@"NSString" _identifier;
@"NSObject<OS_dispatch_queue>" _queue;
@? _activityBlock;
@? _interruptBlock;
@"NSArray" _criteria;
@"PLActivityCriterion" _mustRunCriterion;
@"PLEntry" _activityEntry;
@"NSDate" _lastCompletedDate;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@?,C,V_activityBlock) activityBlock;
@property (T@?,C,V_interruptBlock) interruptBlock;
@property (T@"NSArray",&,V_criteria) criteria;
@property (T@"PLActivityCriterion",&,V_mustRunCriterion) mustRunCriterion;
@property (T@"PLEntry",&,V_activityEntry) activityEntry;
@property (T@"NSDate",&,V_lastCompletedDate) lastCompletedDate;
@property (T@"NSString",R,V_identifier) identifier;
@property (TB,N,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLActivity workQueue];
+[PLActivity activityEntryKey];
+[PLActivity activityStatesEntryKey];
```

## Instance methods

```
-[PLActivity enable];
-[PLActivity criteria];
-[PLActivity syncWithDB];
-[PLActivity lastCompletedDate];
-[PLActivity setMustRunCriterion:];
-[PLActivity setState:];
-[PLActivity enabled];
-[PLActivity identifier];
-[PLActivity activityBlock];
-[PLActivity interruptActivity];
-[PLActivity enumerateCriteriaWithBlock:];
-[PLActivity didChangeCriterion:];
-[PLActivity queue];
-[PLActivity setActivityBlock:];
-[PLActivity disable];
-[PLActivity allCriteriaSatisfied];
-[PLActivity setEnabled:];
-[PLActivity logEntry];
-[PLActivity mustRunCriterionSatisfied];
-[PLActivity runActivity];
-[PLActivity setLastCompletedDate:];
-[PLActivity activityEntry];
-[PLActivity description];
-[PLActivity criteriaString];
-[PLActivity mustRunCriterion];
-[PLActivity initWithIdentifier:withCriteria:withMustRunCriterion:withQueue:withInterruptBlock:withActivityBlock:];
-[PLActivity setCriteria:];
-[PLActivity mustRunCriterionString];
-[PLActivity setActivityEntry:];
-[PLActivity setInterruptBlock:];
-[PLActivity interruptBlock];
-[PLActivity state];
-[PLActivity setQueue:];
```

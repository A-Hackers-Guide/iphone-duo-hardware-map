# `PLActivityCriterionEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLActivityCriterion`
- 4 instance variables, 4 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSString" _entryKey;
@? _criterionBlock;
@"NSDictionary" _filter;
@"PLEntryNotificationOperatorComposition" _entryListener;
```

## Properties

```
@property (T@?,C,V_criterionBlock) criterionBlock;
@property (T@"NSDictionary",&,V_filter) filter;
@property (T@"PLEntryNotificationOperatorComposition",&,V_entryListener) entryListener;
@property (T@"NSString",R,V_entryKey) entryKey;
```

## Class methods

```
+[PLActivityCriterionEntry audioOffCriterion];
+[PLActivityCriterionEntry displayOffCriterion];
+[PLActivityCriterionEntry pluggedInCriterion];
```

## Instance methods

```
-[PLActivityCriterionEntry filter];
-[PLActivityCriterionEntry setFilter:];
-[PLActivityCriterionEntry entryKey];
-[PLActivityCriterionEntry description];
-[PLActivityCriterionEntry criterionBlock];
-[PLActivityCriterionEntry didDisableActivity:];
-[PLActivityCriterionEntry didEnableActivity:];
-[PLActivityCriterionEntry entryListener];
-[PLActivityCriterionEntry initWithEntryKey:withCriterionBlock:];
-[PLActivityCriterionEntry initWithEntryKey:withFilter:withCriterionBlock:];
-[PLActivityCriterionEntry scheduleEntryListener];
-[PLActivityCriterionEntry setCriterionBlock:];
-[PLActivityCriterionEntry setEntryListener:];
```

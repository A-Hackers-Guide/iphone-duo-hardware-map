# `PLAWDAuxMetrics`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"PLOperator" _operator;
@"NSMutableSet" _runningMetrics;
```

## Properties

```
@property (T@"PLOperator",W,V_operator) operator;
@property (T@"NSMutableSet",&,N,V_runningMetrics) runningMetrics;
```

## Class methods

```
+[PLAWDAuxMetrics entryEventPointDefinitions];
+[PLAWDAuxMetrics entryAggregateDefinitions];
+[PLAWDAuxMetrics getSharedObjWithOperator:];
```

## Instance methods

```
-[PLAWDAuxMetrics operator];
-[PLAWDAuxMetrics setOperator:];
-[PLAWDAuxMetrics initWithOperator:];
-[PLAWDAuxMetrics doesInterfereWithChargerWithStartDate:withEndDate:];
-[PLAWDAuxMetrics dropFirstEntryReceived:usingFilter:andStartTime:];
-[PLAWDAuxMetrics getRailEnergyWithEntry:withFilter:isRailForward:];
-[PLAWDAuxMetrics handleChargerChangeWithState:withDate:];
-[PLAWDAuxMetrics resetTableWithEntryKey:];
-[PLAWDAuxMetrics runningMetrics];
-[PLAWDAuxMetrics setRunningMetrics:];
-[PLAWDAuxMetrics startMetricCollection:];
-[PLAWDAuxMetrics stopMetricCollection:];
-[PLAWDAuxMetrics submitDataToAWDServer:withAwdConn:];
```

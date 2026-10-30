# `PLDTCostElement`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _startDate;
@"NSDate" _costReturnedTillDate;
d _costAggregated;
@"NSDate" _lastOverheadStart;
```

## Properties

```
@property (T@"NSDate",&,V_startDate) startDate;
@property (T@"NSDate",&,V_costReturnedTillDate) costReturnedTillDate;
@property (Td,V_costAggregated) costAggregated;
@property (T@"NSDate",&,V_lastOverheadStart) lastOverheadStart;
```

## Class methods

```
+[PLDTCostElement getCostElementInstance];
```

## Instance methods

```
-[PLDTCostElement startDate];
-[PLDTCostElement setStartDate:];
-[PLDTCostElement init];
-[PLDTCostElement addCpuEvent:atTime:withPid:withAppState:];
-[PLDTCostElement addDisplayEvent:atTime:withPid:withAppState:];
-[PLDTCostElement addEvent:atTime:];
-[PLDTCostElement addGpuEvent:atTime:withPid:withAppState:];
-[PLDTCostElement addLocationEvent:atTime:withPid:withAppState:];
-[PLDTCostElement addNetworkingEvent:atTime:withPid:withAppState:withQueryCount:];
-[PLDTCostElement costAggregated];
-[PLDTCostElement costReturnedTillDate];
-[PLDTCostElement getApplicationCostUptoTime:withPid:withLastActiveStart:withLastSuspendStart:withAppState:];
-[PLDTCostElement getCostUptoTime:];
-[PLDTCostElement getCpuCostUptoTime:withPid:withLastActiveStart:withLastSuspendStart:withAppState:];
-[PLDTCostElement getDisplayCostUptoTime:withPid:withLastActiveStart:withLastSuspendStart:withAppState:];
-[PLDTCostElement getGpuCostUptoTime:withPid:withLastActiveStart:withLastSuspendStart:withAppState:];
-[PLDTCostElement getLocationCostUptoTime:withPid:withLastActiveStart:withLastSuspendStart:withAppState:];
-[PLDTCostElement getNetworkingCostUptoTime:withPid:withLastActiveStart:withLastSuspendStart:withAppState:withQueryCount:];
-[PLDTCostElement initWithTime:];
-[PLDTCostElement lastOverheadStart];
-[PLDTCostElement setCostAggregated:];
-[PLDTCostElement setCostReturnedTillDate:];
-[PLDTCostElement setLastOverheadStart:];
```

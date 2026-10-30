# `PLBatteryUIService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBatteryBreakdownService`
- 2 instance variables, 2 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"PLXPCResponderOperatorComposition" _batteryBreakdownResponder;
@"PLXPCResponderOperatorComposition" _modelsResponder;
```

## Properties

```
@property (T@"PLXPCResponderOperatorComposition",&,V_batteryBreakdownResponder) batteryBreakdownResponder;
@property (T@"PLXPCResponderOperatorComposition",&,V_modelsResponder) modelsResponder;
```

## Class methods

```
+[PLBatteryUIService load];
```

## Instance methods

```
-[PLBatteryUIService init];
-[PLBatteryUIService initOperatorDependancies];
-[PLBatteryUIService demoModePath];
-[PLBatteryUIService modelsResponder];
-[PLBatteryUIService writeOutputDemo];
-[PLBatteryUIService adjustScreenOffTimeSecsWithGraphValue:withGraphScreenOnSecs:queryType:andBreakdownEntries:];
-[PLBatteryUIService adjustScreenOnTimeSecsWithGraphValue:queryType:andBreakdownEntries:];
-[PLBatteryUIService batteryBreakdownAndGraphWithPayload:];
-[PLBatteryUIService batteryBreakdownResponder];
-[PLBatteryUIService batteryBreakdownWithPayload:withDayRange:withXDayRange:withDataRange:];
-[PLBatteryUIService batteryLevelsAndChargingIntervalsInRange:withDataRange:];
-[PLBatteryUIService dateAndBatteryLevelPointsInRange:];
-[PLBatteryUIService dateIntervals:containDate:];
-[PLBatteryUIService demoMode];
-[PLBatteryUIService entriesInRange:fromEntries:];
-[PLBatteryUIService floorSeconds:];
-[PLBatteryUIService generateTapBucketsForBucketSize:withNumberOfBuckets:withNowTime:withDrainThreshold:withQueryType:withDataRange:];
-[PLBatteryUIService getDataRangeWithNow:];
-[PLBatteryUIService getLPMIntervalsSpanningRange:];
-[PLBatteryUIService getLastChargeData];
-[PLBatteryUIService getlastDayRangeWithNow:withNowSystem:];
-[PLBatteryUIService getlastXDayRangeWithNow:withNowSystem:];
-[PLBatteryUIService incrementAggdKey];
-[PLBatteryUIService isAppEntryValidForAdjustment:withQueryType:];
-[PLBatteryUIService lastXDaysWithRange:withDataRange:withQueryType:andBatteryBreakdown:];
-[PLBatteryUIService modelsForGraphWithDayRange:withXDayRange:withDataRange:withQueryType:andBatteryBreakdown:];
-[PLBatteryUIService modelsWithPayload:];
-[PLBatteryUIService removeExcessUpgradePlistFiles];
-[PLBatteryUIService screenTimeInRange:withBucketSize:withNumBuckets:withDataRange:withQueryType:andBatteryBreakdown:];
-[PLBatteryUIService setBatteryBreakdownResponder:];
-[PLBatteryUIService setModelsResponder:];
```

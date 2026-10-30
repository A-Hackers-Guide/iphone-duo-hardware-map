# `PLBatteryUIDrainDateInterval`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _startDate;
@"NSDate" _endDate;
@"NSNumber" _accumulatedDrainLevel;
@"NSArray" _sortedAppList;
@"NSDictionary" _appBreakdown;
```

## Properties

```
@property (T@"NSDate",&,V_startDate) startDate;
@property (T@"NSDate",&,V_endDate) endDate;
@property (T@"NSNumber",&,V_accumulatedDrainLevel) accumulatedDrainLevel;
@property (T@"NSArray",&,V_sortedAppList) sortedAppList;
@property (T@"NSDictionary",&,V_appBreakdown) appBreakdown;
```

## Instance methods

```
-[PLBatteryUIDrainDateInterval startDate];
-[PLBatteryUIDrainDateInterval setStartDate:];
-[PLBatteryUIDrainDateInterval endDate];
-[PLBatteryUIDrainDateInterval initWithStartDate:endDate:];
-[PLBatteryUIDrainDateInterval setEndDate:];
-[PLBatteryUIDrainDateInterval description];
-[PLBatteryUIDrainDateInterval accumulatedDrainLevel];
-[PLBatteryUIDrainDateInterval appBreakdown];
-[PLBatteryUIDrainDateInterval initWithStartDate:endDate:accumulatedDrain:];
-[PLBatteryUIDrainDateInterval initWithStartDate:endDate:accumulatedDrain:sortedAppList:appBreakdown:];
-[PLBatteryUIDrainDateInterval setAccumulatedDrainLevel:];
-[PLBatteryUIDrainDateInterval setAppBreakdown:];
-[PLBatteryUIDrainDateInterval setSortedAppList:];
-[PLBatteryUIDrainDateInterval sortedAppList];
```

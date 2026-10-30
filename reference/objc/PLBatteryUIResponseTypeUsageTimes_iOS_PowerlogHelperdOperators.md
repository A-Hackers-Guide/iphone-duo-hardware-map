# `PLBatteryUIResponseTypeUsageTimes_iOS`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 9 instance variables, 13 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
d _range;
d _bucketSize;
@"NSArray" _aggregateEntries;
@"NSDictionary" _resultDictionary;
@"NSMutableArray" _batteryBreakdown_buckets;
@"NSMutableArray" _batteryBreakdown_lastDay;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_range) range;
@property (Td,V_bucketSize) bucketSize;
@property (T@"NSArray",&,V_aggregateEntries) aggregateEntries;
@property (T@"NSDictionary",&,V_resultDictionary) resultDictionary;
@property (T@"NSMutableArray",&,V_batteryBreakdown_buckets) batteryBreakdown_buckets;
@property (T@"NSMutableArray",&,V_batteryBreakdown_lastDay) batteryBreakdown_lastDay;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeUsageTimes_iOS configure:];
-[PLBatteryUIResponseTypeUsageTimes_iOS dependencies];
-[PLBatteryUIResponseTypeUsageTimes_iOS range];
-[PLBatteryUIResponseTypeUsageTimes_iOS start];
-[PLBatteryUIResponseTypeUsageTimes_iOS end];
-[PLBatteryUIResponseTypeUsageTimes_iOS setRange:];
-[PLBatteryUIResponseTypeUsageTimes_iOS coalesce];
-[PLBatteryUIResponseTypeUsageTimes_iOS setEnd:];
-[PLBatteryUIResponseTypeUsageTimes_iOS result];
-[PLBatteryUIResponseTypeUsageTimes_iOS setStart:];
-[PLBatteryUIResponseTypeUsageTimes_iOS run];
-[PLBatteryUIResponseTypeUsageTimes_iOS resultDictionary];
-[PLBatteryUIResponseTypeUsageTimes_iOS bucketSize];
-[PLBatteryUIResponseTypeUsageTimes_iOS adjustScreenOffTimeWithGraphValue:screenOnTime:andEnergyEntries:];
-[PLBatteryUIResponseTypeUsageTimes_iOS adjustScreenOnTimeWithGraphValue:andEnergyEntries:];
-[PLBatteryUIResponseTypeUsageTimes_iOS aggregateEntries];
-[PLBatteryUIResponseTypeUsageTimes_iOS batteryBreakdown_buckets];
-[PLBatteryUIResponseTypeUsageTimes_iOS batteryBreakdown_lastDay];
-[PLBatteryUIResponseTypeUsageTimes_iOS energyEntryValidForAdjustment:];
-[PLBatteryUIResponseTypeUsageTimes_iOS entriesInRange:fromEntries:];
-[PLBatteryUIResponseTypeUsageTimes_iOS gatherDependencies];
-[PLBatteryUIResponseTypeUsageTimes_iOS getDataRange:];
-[PLBatteryUIResponseTypeUsageTimes_iOS responderService];
-[PLBatteryUIResponseTypeUsageTimes_iOS setAggregateEntries:];
-[PLBatteryUIResponseTypeUsageTimes_iOS setBatteryBreakdown_buckets:];
-[PLBatteryUIResponseTypeUsageTimes_iOS setBatteryBreakdown_lastDay:];
-[PLBatteryUIResponseTypeUsageTimes_iOS setBucketSize:];
-[PLBatteryUIResponseTypeUsageTimes_iOS setResponderService:];
-[PLBatteryUIResponseTypeUsageTimes_iOS setResultDictionary:];
```

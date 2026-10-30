# `PLBatteryUIResponseTypeUsageTimes`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 6 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
d _bucketSize;
@"NSArray" _aggregateEntries;
@"NSDictionary" _resultDictionary;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_bucketSize) bucketSize;
@property (T@"NSArray",&,V_aggregateEntries) aggregateEntries;
@property (T@"NSDictionary",&,V_resultDictionary) resultDictionary;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeUsageTimes configure:];
-[PLBatteryUIResponseTypeUsageTimes dependencies];
-[PLBatteryUIResponseTypeUsageTimes start];
-[PLBatteryUIResponseTypeUsageTimes end];
-[PLBatteryUIResponseTypeUsageTimes coalesce];
-[PLBatteryUIResponseTypeUsageTimes setEnd:];
-[PLBatteryUIResponseTypeUsageTimes result];
-[PLBatteryUIResponseTypeUsageTimes setStart:];
-[PLBatteryUIResponseTypeUsageTimes run];
-[PLBatteryUIResponseTypeUsageTimes resultDictionary];
-[PLBatteryUIResponseTypeUsageTimes bucketSize];
-[PLBatteryUIResponseTypeUsageTimes aggregateEntries];
-[PLBatteryUIResponseTypeUsageTimes entriesInRange:fromEntries:];
-[PLBatteryUIResponseTypeUsageTimes responderService];
-[PLBatteryUIResponseTypeUsageTimes setAggregateEntries:];
-[PLBatteryUIResponseTypeUsageTimes setBucketSize:];
-[PLBatteryUIResponseTypeUsageTimes setResponderService:];
-[PLBatteryUIResponseTypeUsageTimes setResultDictionary:];
```

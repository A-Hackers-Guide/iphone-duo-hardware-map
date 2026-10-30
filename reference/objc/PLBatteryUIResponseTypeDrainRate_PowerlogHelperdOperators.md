# `PLBatteryUIResponseTypeDrainRate`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
i _totalDrain;
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
d _bucketSize;
@"NSArray" _uiLevelEntries;
d _totalTimeWhileDraining;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_bucketSize) bucketSize;
@property (T@"NSArray",&,V_uiLevelEntries) uiLevelEntries;
@property (Ti,V_totalDrain) totalDrain;
@property (Td,V_totalTimeWhileDraining) totalTimeWhileDraining;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeDrainRate configure:];
-[PLBatteryUIResponseTypeDrainRate dependencies];
-[PLBatteryUIResponseTypeDrainRate start];
-[PLBatteryUIResponseTypeDrainRate end];
-[PLBatteryUIResponseTypeDrainRate coalesce];
-[PLBatteryUIResponseTypeDrainRate setEnd:];
-[PLBatteryUIResponseTypeDrainRate result];
-[PLBatteryUIResponseTypeDrainRate setStart:];
-[PLBatteryUIResponseTypeDrainRate run];
-[PLBatteryUIResponseTypeDrainRate bucketSize];
-[PLBatteryUIResponseTypeDrainRate responderService];
-[PLBatteryUIResponseTypeDrainRate setBucketSize:];
-[PLBatteryUIResponseTypeDrainRate setResponderService:];
-[PLBatteryUIResponseTypeDrainRate setTotalDrain:];
-[PLBatteryUIResponseTypeDrainRate setTotalTimeWhileDraining:];
-[PLBatteryUIResponseTypeDrainRate setUiLevelEntries:];
-[PLBatteryUIResponseTypeDrainRate totalDrain];
-[PLBatteryUIResponseTypeDrainRate totalTimeWhileDraining];
-[PLBatteryUIResponseTypeDrainRate uiLevelEntries];
```

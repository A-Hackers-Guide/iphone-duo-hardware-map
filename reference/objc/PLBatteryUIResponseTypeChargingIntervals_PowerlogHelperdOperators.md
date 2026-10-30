# `PLBatteryUIResponseTypeChargingIntervals`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 6 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _start;
@"NSDate" _end;
@"NSArray" _battEntries;
@"PLEntry" _lastBattEntry;
@"NSArray" _resultArray;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (T@"NSArray",&,V_battEntries) battEntries;
@property (T@"PLEntry",&,V_lastBattEntry) lastBattEntry;
@property (T@"NSArray",&,V_resultArray) resultArray;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeChargingIntervals configure:];
-[PLBatteryUIResponseTypeChargingIntervals dependencies];
-[PLBatteryUIResponseTypeChargingIntervals start];
-[PLBatteryUIResponseTypeChargingIntervals end];
-[PLBatteryUIResponseTypeChargingIntervals coalesce];
-[PLBatteryUIResponseTypeChargingIntervals setEnd:];
-[PLBatteryUIResponseTypeChargingIntervals result];
-[PLBatteryUIResponseTypeChargingIntervals setStart:];
-[PLBatteryUIResponseTypeChargingIntervals run];
-[PLBatteryUIResponseTypeChargingIntervals resultArray];
-[PLBatteryUIResponseTypeChargingIntervals setBattEntries:];
-[PLBatteryUIResponseTypeChargingIntervals setResultArray:];
-[PLBatteryUIResponseTypeChargingIntervals battEntries];
-[PLBatteryUIResponseTypeChargingIntervals lastBattEntry];
-[PLBatteryUIResponseTypeChargingIntervals responderService];
-[PLBatteryUIResponseTypeChargingIntervals setLastBattEntry:];
-[PLBatteryUIResponseTypeChargingIntervals setResponderService:];
```

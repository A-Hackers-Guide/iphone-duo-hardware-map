# `PLBatteryUIResponseTypeUISOCDrain`

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
@"NSArray" _uiLevelDrainEntries;
@"NSArray" _resultArray;
```

## Properties

```
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_bucketSize) bucketSize;
@property (T@"NSArray",&,V_uiLevelDrainEntries) uiLevelDrainEntries;
@property (T@"NSArray",&,V_resultArray) resultArray;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeUISOCDrain configure:];
-[PLBatteryUIResponseTypeUISOCDrain dependencies];
-[PLBatteryUIResponseTypeUISOCDrain start];
-[PLBatteryUIResponseTypeUISOCDrain end];
-[PLBatteryUIResponseTypeUISOCDrain coalesce];
-[PLBatteryUIResponseTypeUISOCDrain setEnd:];
-[PLBatteryUIResponseTypeUISOCDrain result];
-[PLBatteryUIResponseTypeUISOCDrain setStart:];
-[PLBatteryUIResponseTypeUISOCDrain run];
-[PLBatteryUIResponseTypeUISOCDrain bucketSize];
-[PLBatteryUIResponseTypeUISOCDrain resultArray];
-[PLBatteryUIResponseTypeUISOCDrain setResultArray:];
-[PLBatteryUIResponseTypeUISOCDrain entriesInRange:fromEntries:];
-[PLBatteryUIResponseTypeUISOCDrain responderService];
-[PLBatteryUIResponseTypeUISOCDrain setBucketSize:];
-[PLBatteryUIResponseTypeUISOCDrain setResponderService:];
-[PLBatteryUIResponseTypeUISOCDrain setUiLevelDrainEntries:];
-[PLBatteryUIResponseTypeUISOCDrain uiLevelDrainEntries];
```

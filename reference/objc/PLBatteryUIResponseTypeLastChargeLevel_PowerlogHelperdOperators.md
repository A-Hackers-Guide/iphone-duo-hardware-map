# `PLBatteryUIResponseTypeLastChargeLevel`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"PLBatteryUIResponderService" _responderService;
@"NSNumber" _lastChargeValue;
@"NSNumber" _lastChargeTimestamp;
@"NSDictionary" _resultDictionary;
```

## Properties

```
@property (T@"NSNumber",&,V_lastChargeValue) lastChargeValue;
@property (T@"NSNumber",&,V_lastChargeTimestamp) lastChargeTimestamp;
@property (T@"NSDictionary",&,V_resultDictionary) resultDictionary;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeLastChargeLevel configure:];
-[PLBatteryUIResponseTypeLastChargeLevel dependencies];
-[PLBatteryUIResponseTypeLastChargeLevel coalesce];
-[PLBatteryUIResponseTypeLastChargeLevel result];
-[PLBatteryUIResponseTypeLastChargeLevel run];
-[PLBatteryUIResponseTypeLastChargeLevel resultDictionary];
-[PLBatteryUIResponseTypeLastChargeLevel lastChargeValue];
-[PLBatteryUIResponseTypeLastChargeLevel lastChargeTimestamp];
-[PLBatteryUIResponseTypeLastChargeLevel responderService];
-[PLBatteryUIResponseTypeLastChargeLevel setLastChargeTimestamp:];
-[PLBatteryUIResponseTypeLastChargeLevel setLastChargeValue:];
-[PLBatteryUIResponseTypeLastChargeLevel setResponderService:];
-[PLBatteryUIResponseTypeLastChargeLevel setResultDictionary:];
```

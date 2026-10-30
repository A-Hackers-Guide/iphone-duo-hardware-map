# `PLBatteryUIResponseTypeBackgroundCPUInsight`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _suggest;
@"PLBatteryUIResponderService" _responderService;
@"NSMutableDictionary" _perAppUsage;
@"NSMutableArray" _batteryBreakdown_Last10Days;
```

## Properties

```
@property (TB,V_suggest) suggest;
@property (T@"NSMutableDictionary",&,V_perAppUsage) perAppUsage;
@property (T@"NSMutableArray",&,V_batteryBreakdown_Last10Days) batteryBreakdown_Last10Days;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeBackgroundCPUInsight configure:];
-[PLBatteryUIResponseTypeBackgroundCPUInsight dependencies];
-[PLBatteryUIResponseTypeBackgroundCPUInsight coalesce];
-[PLBatteryUIResponseTypeBackgroundCPUInsight result];
-[PLBatteryUIResponseTypeBackgroundCPUInsight run];
-[PLBatteryUIResponseTypeBackgroundCPUInsight setPerAppUsage:];
-[PLBatteryUIResponseTypeBackgroundCPUInsight setBatteryBreakdown_Last10Days:];
-[PLBatteryUIResponseTypeBackgroundCPUInsight suggest];
-[PLBatteryUIResponseTypeBackgroundCPUInsight batteryBreakdown_Last10Days];
-[PLBatteryUIResponseTypeBackgroundCPUInsight perAppUsage];
-[PLBatteryUIResponseTypeBackgroundCPUInsight responderService];
-[PLBatteryUIResponseTypeBackgroundCPUInsight setResponderService:];
-[PLBatteryUIResponseTypeBackgroundCPUInsight setSuggest:];
```

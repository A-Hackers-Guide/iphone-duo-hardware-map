# `PLBatteryUIResponseTypeOngoingDeviceSetupInsight`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 4 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _suggest;
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _end;
d _lastUpgradeTimestamp;
```

## Properties

```
@property (TB,V_suggest) suggest;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_lastUpgradeTimestamp) lastUpgradeTimestamp;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight configure:];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight dependencies];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight end];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight coalesce];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setEnd:];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight result];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight run];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight suggest];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight didUpgradeInLast:];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight lastUpgradeTimestamp];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight responderService];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setLastUpgradeTimestamp:];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setResponderService:];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight setSuggest:];
-[PLBatteryUIResponseTypeOngoingDeviceSetupInsight shouldShowSuggestionThroughOverrides];
```

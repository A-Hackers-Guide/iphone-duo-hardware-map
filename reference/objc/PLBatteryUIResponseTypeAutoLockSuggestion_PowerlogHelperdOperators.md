# `PLBatteryUIResponseTypeAutoLockSuggestion`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 5 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _suggest;
@"PLBatteryUIResponderService" _responderService;
d _energyPercent;
@"NSNumber" _autoLockTime;
@"NSDictionary" _batteryBreakdown_Last24hrs;
```

## Properties

```
@property (TB,V_suggest) suggest;
@property (Td,V_energyPercent) energyPercent;
@property (T@"NSNumber",&,V_autoLockTime) autoLockTime;
@property (T@"NSDictionary",&,V_batteryBreakdown_Last24hrs) batteryBreakdown_Last24hrs;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeAutoLockSuggestion configure:];
-[PLBatteryUIResponseTypeAutoLockSuggestion dependencies];
-[PLBatteryUIResponseTypeAutoLockSuggestion coalesce];
-[PLBatteryUIResponseTypeAutoLockSuggestion result];
-[PLBatteryUIResponseTypeAutoLockSuggestion run];
-[PLBatteryUIResponseTypeAutoLockSuggestion suggest];
-[PLBatteryUIResponseTypeAutoLockSuggestion autoLockTime];
-[PLBatteryUIResponseTypeAutoLockSuggestion batteryBreakdown_Last24hrs];
-[PLBatteryUIResponseTypeAutoLockSuggestion energyPercent];
-[PLBatteryUIResponseTypeAutoLockSuggestion responderService];
-[PLBatteryUIResponseTypeAutoLockSuggestion setAutoLockTime:];
-[PLBatteryUIResponseTypeAutoLockSuggestion setBatteryBreakdown_Last24hrs:];
-[PLBatteryUIResponseTypeAutoLockSuggestion setEnergyPercent:];
-[PLBatteryUIResponseTypeAutoLockSuggestion setResponderService:];
-[PLBatteryUIResponseTypeAutoLockSuggestion setSuggest:];
-[PLBatteryUIResponseTypeAutoLockSuggestion shouldShowSuggestionThroughOverrides];
```

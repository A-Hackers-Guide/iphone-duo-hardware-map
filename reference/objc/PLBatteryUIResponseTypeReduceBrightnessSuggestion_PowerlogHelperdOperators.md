# `PLBatteryUIResponseTypeReduceBrightnessSuggestion`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 5 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _suggest;
B _isALSCurveHigherThanDefault;
@"PLBatteryUIResponderService" _responderService;
d _energyPercent;
@"NSDictionary" _batteryBreakdown_Last24hrs;
```

## Properties

```
@property (TB,V_suggest) suggest;
@property (Td,V_energyPercent) energyPercent;
@property (TB,V_isALSCurveHigherThanDefault) isALSCurveHigherThanDefault;
@property (T@"NSDictionary",&,V_batteryBreakdown_Last24hrs) batteryBreakdown_Last24hrs;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion configure:];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion dependencies];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion coalesce];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion result];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion run];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion isALSCurveHigherThanDefault];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion setIsALSCurveHigherThanDefault:];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion suggest];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion batteryBreakdown_Last24hrs];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion energyPercent];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion responderService];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion setBatteryBreakdown_Last24hrs:];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion setEnergyPercent:];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion setResponderService:];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion setSuggest:];
-[PLBatteryUIResponseTypeReduceBrightnessSuggestion shouldShowSuggestionThroughOverrides];
```

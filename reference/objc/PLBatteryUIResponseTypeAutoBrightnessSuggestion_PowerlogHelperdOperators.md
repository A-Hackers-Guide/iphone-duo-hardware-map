# `PLBatteryUIResponseTypeAutoBrightnessSuggestion`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 6 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _suggest;
B _isALSEnabled;
B _hasALSPowerSaved;
@"PLBatteryUIResponderService" _responderService;
d _energyPercent;
@"NSArray" _alsPowerSavedEntries;
```

## Properties

```
@property (TB,V_suggest) suggest;
@property (Td,V_energyPercent) energyPercent;
@property (TB,V_isALSEnabled) isALSEnabled;
@property (TB,V_hasALSPowerSaved) hasALSPowerSaved;
@property (T@"NSArray",&,V_alsPowerSavedEntries) alsPowerSavedEntries;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion configure:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion dependencies];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion coalesce];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion result];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion run];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion suggest];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion alsPowerSavedEntries];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion energyPercent];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion hasALSPowerSaved];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion isALSEnabled];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion responderService];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion setAlsPowerSavedEntries:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion setEnergyPercent:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion setHasALSPowerSaved:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion setIsALSEnabled:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion setResponderService:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion setSuggest:];
-[PLBatteryUIResponseTypeAutoBrightnessSuggestion shouldShowSuggestionThroughOverrides];
```

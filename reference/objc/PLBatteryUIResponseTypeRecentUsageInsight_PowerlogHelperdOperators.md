# `PLBatteryUIResponseTypeRecentUsageInsight`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 13 instance variables, 17 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _suggest;
@"PLBatteryUIResponderService" _responderService;
@"NSDate" _end;
d _firstEntryTimestamp;
d _lastUpgradeTimestamp;
d _minTimeValBeforeUpgrade;
d _maxTimeValBeforeUpgrade;
d _minTimeValAfterUpgrade;
d _maxTimeValAfterUpgrade;
d _minDrainPercentBeforeUpgrade;
d _energyThresholdForUpgradeInsight;
d _foregroundTimeThresholdForUpgradeInsight;
@"NSMutableArray" _batteryBreakdown_Last10Days;
```

## Properties

```
@property (TB,V_suggest) suggest;
@property (T@"NSDate",&,V_end) end;
@property (Td,V_firstEntryTimestamp) firstEntryTimestamp;
@property (Td,V_lastUpgradeTimestamp) lastUpgradeTimestamp;
@property (Td,V_minTimeValBeforeUpgrade) minTimeValBeforeUpgrade;
@property (Td,V_maxTimeValBeforeUpgrade) maxTimeValBeforeUpgrade;
@property (Td,V_minTimeValAfterUpgrade) minTimeValAfterUpgrade;
@property (Td,V_maxTimeValAfterUpgrade) maxTimeValAfterUpgrade;
@property (Td,V_minDrainPercentBeforeUpgrade) minDrainPercentBeforeUpgrade;
@property (Td,V_energyThresholdForUpgradeInsight) energyThresholdForUpgradeInsight;
@property (Td,V_foregroundTimeThresholdForUpgradeInsight) foregroundTimeThresholdForUpgradeInsight;
@property (T@"NSMutableArray",&,V_batteryBreakdown_Last10Days) batteryBreakdown_Last10Days;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeRecentUsageInsight configure:];
-[PLBatteryUIResponseTypeRecentUsageInsight dependencies];
-[PLBatteryUIResponseTypeRecentUsageInsight end];
-[PLBatteryUIResponseTypeRecentUsageInsight coalesce];
-[PLBatteryUIResponseTypeRecentUsageInsight setEnd:];
-[PLBatteryUIResponseTypeRecentUsageInsight result];
-[PLBatteryUIResponseTypeRecentUsageInsight run];
-[PLBatteryUIResponseTypeRecentUsageInsight setBatteryBreakdown_Last10Days:];
-[PLBatteryUIResponseTypeRecentUsageInsight suggest];
-[PLBatteryUIResponseTypeRecentUsageInsight batteryBreakdown_Last10Days];
-[PLBatteryUIResponseTypeRecentUsageInsight didUpgrade];
-[PLBatteryUIResponseTypeRecentUsageInsight energyThresholdForUpgradeInsight];
-[PLBatteryUIResponseTypeRecentUsageInsight firstEntryTimestamp];
-[PLBatteryUIResponseTypeRecentUsageInsight foregroundTimeThresholdForUpgradeInsight];
-[PLBatteryUIResponseTypeRecentUsageInsight getfirstEntryTimestampFromDb];
-[PLBatteryUIResponseTypeRecentUsageInsight lastUpgradeTimestamp];
-[PLBatteryUIResponseTypeRecentUsageInsight maxTimeValAfterUpgrade];
-[PLBatteryUIResponseTypeRecentUsageInsight maxTimeValBeforeUpgrade];
-[PLBatteryUIResponseTypeRecentUsageInsight minDrainPercentBeforeUpgrade];
-[PLBatteryUIResponseTypeRecentUsageInsight minTimeValAfterUpgrade];
-[PLBatteryUIResponseTypeRecentUsageInsight minTimeValBeforeUpgrade];
-[PLBatteryUIResponseTypeRecentUsageInsight responderService];
-[PLBatteryUIResponseTypeRecentUsageInsight setEnergyThresholdForUpgradeInsight:];
-[PLBatteryUIResponseTypeRecentUsageInsight setFirstEntryTimestamp:];
-[PLBatteryUIResponseTypeRecentUsageInsight setForegroundTimeThresholdForUpgradeInsight:];
-[PLBatteryUIResponseTypeRecentUsageInsight setLastUpgradeTimestamp:];
-[PLBatteryUIResponseTypeRecentUsageInsight setMaxTimeValAfterUpgrade:];
-[PLBatteryUIResponseTypeRecentUsageInsight setMaxTimeValBeforeUpgrade:];
-[PLBatteryUIResponseTypeRecentUsageInsight setMinDrainPercentBeforeUpgrade:];
-[PLBatteryUIResponseTypeRecentUsageInsight setMinTimeValAfterUpgrade:];
-[PLBatteryUIResponseTypeRecentUsageInsight setMinTimeValBeforeUpgrade:];
-[PLBatteryUIResponseTypeRecentUsageInsight setResponderService:];
-[PLBatteryUIResponseTypeRecentUsageInsight setSuggest:];
-[PLBatteryUIResponseTypeRecentUsageInsight shouldShowSuggestionThroughOverrides];
```

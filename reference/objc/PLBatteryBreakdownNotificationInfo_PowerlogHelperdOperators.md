# `PLBatteryBreakdownNotificationInfo`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 28 instance methods, 1 class methods

## Instance variables

```
B _isFirstParty;
i _notificationType;
@"NSString" _bundleID;
Q _bgWakingCount;
d _bgWakingNSEDuration;
Q _fgWakingCount;
d _fgWakingNSEDuration;
Q _nonWakingCount;
d _nonWakingNSEDuration;
Q _localCount;
```

## Properties

```
@property (T@"NSString",&,V_bundleID) bundleID;
@property (TB,V_isFirstParty) isFirstParty;
@property (Ti,V_notificationType) notificationType;
@property (TQ,V_bgWakingCount) bgWakingCount;
@property (Td,V_bgWakingNSEDuration) bgWakingNSEDuration;
@property (TQ,V_fgWakingCount) fgWakingCount;
@property (Td,V_fgWakingNSEDuration) fgWakingNSEDuration;
@property (TQ,V_nonWakingCount) nonWakingCount;
@property (Td,V_nonWakingNSEDuration) nonWakingNSEDuration;
@property (TQ,V_localCount) localCount;
```

## Class methods

```
+[PLBatteryBreakdownNotificationInfo representativeDisplayPower];
```

## Instance methods

```
-[PLBatteryBreakdownNotificationInfo notificationType];
-[PLBatteryBreakdownNotificationInfo setNotificationType:];
-[PLBatteryBreakdownNotificationInfo setBundleID:];
-[PLBatteryBreakdownNotificationInfo isFirstParty];
-[PLBatteryBreakdownNotificationInfo description];
-[PLBatteryBreakdownNotificationInfo setIsFirstParty:];
-[PLBatteryBreakdownNotificationInfo bundleID];
-[PLBatteryBreakdownNotificationInfo activeEnergy];
-[PLBatteryBreakdownNotificationInfo initWithEntry:];
-[PLBatteryBreakdownNotificationInfo calculateActiveEnergyForNSEDuration:andCount:withNominalEnergy:];
-[PLBatteryBreakdownNotificationInfo baseEnergy];
-[PLBatteryBreakdownNotificationInfo bgWakingCount];
-[PLBatteryBreakdownNotificationInfo bgWakingNSEDuration];
-[PLBatteryBreakdownNotificationInfo combineWith:];
-[PLBatteryBreakdownNotificationInfo displayEnergy];
-[PLBatteryBreakdownNotificationInfo fgWakingCount];
-[PLBatteryBreakdownNotificationInfo fgWakingNSEDuration];
-[PLBatteryBreakdownNotificationInfo localCount];
-[PLBatteryBreakdownNotificationInfo nonWakingCount];
-[PLBatteryBreakdownNotificationInfo nonWakingNSEDuration];
-[PLBatteryBreakdownNotificationInfo notificationEnergy];
-[PLBatteryBreakdownNotificationInfo setBgWakingCount:];
-[PLBatteryBreakdownNotificationInfo setBgWakingNSEDuration:];
-[PLBatteryBreakdownNotificationInfo setFgWakingCount:];
-[PLBatteryBreakdownNotificationInfo setFgWakingNSEDuration:];
-[PLBatteryBreakdownNotificationInfo setLocalCount:];
-[PLBatteryBreakdownNotificationInfo setNonWakingCount:];
-[PLBatteryBreakdownNotificationInfo setNonWakingNSEDuration:];
```

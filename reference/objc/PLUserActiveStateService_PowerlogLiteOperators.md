# `PLUserActiveStateService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 7 instance variables, 8 properties, 22 instance methods, 4 class methods

## Instance variables

```
@"NSDate" _lastUnplugTime;
@"NSDate" _lastPluggedInTime;
d _pluggedInTime;
Q _userActiveNotificationHandle;
@"PLEntryNotificationOperatorComposition" _batteryNotification;
@"NSNumber" _pluggedInState;
@"NSDictionary" _cachedBatteryMetrics;
```

## Properties

```
@property (T@"NSDate",&) lastUserInactiveTime;
@property (T@"NSDate",&,V_lastUnplugTime) lastUnplugTime;
@property (T@"NSDate",&,V_lastPluggedInTime) lastPluggedInTime;
@property (Td,V_pluggedInTime) pluggedInTime;
@property (TQ,V_userActiveNotificationHandle) userActiveNotificationHandle;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryNotification) batteryNotification;
@property (T@"NSNumber",&,V_pluggedInState) pluggedInState;
@property (T@"NSDictionary",&,V_cachedBatteryMetrics) cachedBatteryMetrics;
```

## Class methods

```
+[PLUserActiveStateService entryEventPointDefinitions];
+[PLUserActiveStateService load];
+[PLUserActiveStateService defaults];
+[PLUserActiveStateService entryEventPointDefinitionState];
```

## Instance methods

```
-[PLUserActiveStateService init];
-[PLUserActiveStateService initOperatorDependancies];
-[PLUserActiveStateService lastPluggedInTime];
-[PLUserActiveStateService setLastPluggedInTime:];
-[PLUserActiveStateService batteryNotification];
-[PLUserActiveStateService cachedBatteryMetrics];
-[PLUserActiveStateService getLastSystemSleepDate];
-[PLUserActiveStateService getUserInactiveMinIntervalCA];
-[PLUserActiveStateService handlePluggedInStateUpdate:];
-[PLUserActiveStateService handleUserActiveStateChangeCallback:];
-[PLUserActiveStateService lastUnplugTime];
-[PLUserActiveStateService lastUserInactiveTime];
-[PLUserActiveStateService pluggedInState];
-[PLUserActiveStateService pluggedInTime];
-[PLUserActiveStateService setBatteryNotification:];
-[PLUserActiveStateService setCachedBatteryMetrics:];
-[PLUserActiveStateService setLastUnplugTime:];
-[PLUserActiveStateService setLastUserInactiveTime:];
-[PLUserActiveStateService setPluggedInState:];
-[PLUserActiveStateService setPluggedInTime:];
-[PLUserActiveStateService setUserActiveNotificationHandle:];
-[PLUserActiveStateService userActiveNotificationHandle];
```

# `PLAggregateUsageService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 10 instance variables, 10 properties, 38 instance methods, 2 class methods

## Instance variables

```
@"PLEntryNotificationOperatorComposition" _displayOnNotification;
@"PLEntryNotificationOperatorComposition" _displayOffNotification;
@"PLEntryNotificationOperatorComposition" _wakeEntryNotification;
@"PLEntryNotificationOperatorComposition" _sleepEntryNotification;
@"PLEntryNotificationOperatorComposition" _audioEntryNotification;
@"PLEntryNotificationOperatorComposition" _batteryIsChargingEntryNotification;
@"PLEntryNotificationOperatorComposition" _batteryExternalConnectedEntryNotification;
@"PLEntryNotificationOperatorComposition" _chargingEntryNotification;
@"PLEntryNotificationOperatorComposition" _lockStateEntryNotification;
@"PLIntervalData" _intervalData;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayOnNotification) displayOnNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayOffNotification) displayOffNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeEntryNotification) wakeEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sleepEntryNotification) sleepEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_audioEntryNotification) audioEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryIsChargingEntryNotification) batteryIsChargingEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_batteryExternalConnectedEntryNotification) batteryExternalConnectedEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_chargingEntryNotification) chargingEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_lockStateEntryNotification) lockStateEntryNotification;
@property (T@"PLIntervalData",&,V_intervalData) intervalData;
```

## Class methods

```
+[PLAggregateUsageService load];
+[PLAggregateUsageService defaults];
```

## Instance methods

```
-[PLAggregateUsageService chargingEntryNotification];
-[PLAggregateUsageService scheduleSubmissionAfter:];
-[PLAggregateUsageService handleAudioStateChange:];
-[PLAggregateUsageService initializeMetrics];
-[PLAggregateUsageService displayOnNotification];
-[PLAggregateUsageService setSleepEntryNotification:];
-[PLAggregateUsageService batteryIsChargingEntryNotification];
-[PLAggregateUsageService registerForEntryNotifications];
-[PLAggregateUsageService init];
-[PLAggregateUsageService setChargingEntryNotification:];
-[PLAggregateUsageService numIntervalsToFill];
-[PLAggregateUsageService wakeEntryNotification];
-[PLAggregateUsageService initOperatorDependancies];
-[PLAggregateUsageService instantiateMetrics];
-[PLAggregateUsageService setAudioEntryNotification:];
-[PLAggregateUsageService intervalData];
-[PLAggregateUsageService lockStateEntryNotification];
-[PLAggregateUsageService testService];
-[PLAggregateUsageService handleWakeStateChange:withState:];
-[PLAggregateUsageService setWakeEntryNotification:];
-[PLAggregateUsageService setDisplayOnNotification:];
-[PLAggregateUsageService handleChargingChange:];
-[PLAggregateUsageService submitMetricsToAggd];
-[PLAggregateUsageService handleScreenStateChange:withState:];
-[PLAggregateUsageService setBatteryExternalConnectedEntryNotification:];
-[PLAggregateUsageService handleConnectedChange:];
-[PLAggregateUsageService displayOffNotification];
-[PLAggregateUsageService setBatteryIsChargingEntryNotification:];
-[PLAggregateUsageService setIntervalData:];
-[PLAggregateUsageService handleLargeTimeGap];
-[PLAggregateUsageService batteryExternalConnectedEntryNotification];
-[PLAggregateUsageService setLockStateEntryNotification:];
-[PLAggregateUsageService updateSampledMetrics];
-[PLAggregateUsageService sleepEntryNotification];
-[PLAggregateUsageService handleExternalConnectedChange:];
-[PLAggregateUsageService audioEntryNotification];
-[PLAggregateUsageService handleLockStateChange:];
-[PLAggregateUsageService setDisplayOffNotification:];
```

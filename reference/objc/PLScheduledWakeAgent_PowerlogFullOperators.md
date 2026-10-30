# `PLScheduledWakeAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogFullOperators.framework/PowerlogFullOperators`](../userland/System__Library__PrivateFrameworks__PowerlogFullOperators.framework__PowerlogFullOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 3 instance variables, 3 properties, 11 instance methods, 9 class methods

## Instance variables

```
@"PLEntryNotificationOperatorComposition" _canSleepNotification;
@"PLSemaphore" _canSleepSemaphore;
@"NSMutableDictionary" _previousScheduleWakeEvents;
```

## Properties

```
@property (T@"PLEntryNotificationOperatorComposition",&,V_canSleepNotification) canSleepNotification;
@property (T@"PLSemaphore",&,V_canSleepSemaphore) canSleepSemaphore;
@property (T@"NSMutableDictionary",&,V_previousScheduleWakeEvents) previousScheduleWakeEvents;
```

## Class methods

```
+[PLScheduledWakeAgent entryEventIntervalDefinitions];
+[PLScheduledWakeAgent entryEventPointDefinitions];
+[PLScheduledWakeAgent entryEventForwardDefinitions];
+[PLScheduledWakeAgent entryEventBackwardDefinitions];
+[PLScheduledWakeAgent entryEventNoneDefinitions];
+[PLScheduledWakeAgent load];
+[PLScheduledWakeAgent defaults];
+[PLScheduledWakeAgent accountingGroupDefinitions];
+[PLScheduledWakeAgent railDefinitions];
```

## Instance methods

```
-[PLScheduledWakeAgent init];
-[PLScheduledWakeAgent canSleepNotification];
-[PLScheduledWakeAgent initOperatorDependancies];
-[PLScheduledWakeAgent setCanSleepSemaphore:];
-[PLScheduledWakeAgent canSleepSemaphore];
-[PLScheduledWakeAgent setCanSleepNotification:];
-[PLScheduledWakeAgent log];
-[PLScheduledWakeAgent humanReadableScheduledWakeString:];
-[PLScheduledWakeAgent logEventForwardScheduledEvent];
-[PLScheduledWakeAgent previousScheduleWakeEvents];
-[PLScheduledWakeAgent setPreviousScheduleWakeEvents:];
```

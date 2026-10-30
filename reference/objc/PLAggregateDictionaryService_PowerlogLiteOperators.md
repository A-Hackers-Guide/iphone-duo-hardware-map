# `PLAggregateDictionaryService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 12 instance variables, 10 properties, 44 instance methods, 4 class methods

## Instance variables

```
d remainderUnpluggedEnergy;
d remainderUnpluggedTime;
B _firstScreenOnAfterWake;
@"NSMutableArray" _registeredNotifications;
@"PLMonotonicTimer" _dailyTaskTimer;
@"PLCFNotificationOperatorComposition" _blmAggregateCFNotification;
@"NSNumber" _currentMachWakeTime;
@"NSString" _wakeReasons;
@"NSString" _wakeReasonString;
@"NSMutableDictionary" _validReasonsDictionary;
@"NSMutableDictionary" _localCache;
{AggState="state"i"level"d"timestamp"d} _last_state;
```

## Properties

```
@property (T@"NSMutableArray",&,V_registeredNotifications) registeredNotifications;
@property (T@"PLMonotonicTimer",&,V_dailyTaskTimer) dailyTaskTimer;
@property (T@"PLCFNotificationOperatorComposition",&,V_blmAggregateCFNotification) blmAggregateCFNotification;
@property (T{AggState=idd},V_last_state) last_state;
@property (TB,V_firstScreenOnAfterWake) firstScreenOnAfterWake;
@property (T@"NSNumber",&,V_currentMachWakeTime) currentMachWakeTime;
@property (T@"NSString",&,V_wakeReasons) wakeReasons;
@property (T@"NSString",&,V_wakeReasonString) wakeReasonString;
@property (T@"NSMutableDictionary",&,V_validReasonsDictionary) validReasonsDictionary;
@property (T@"NSMutableDictionary",&,V_localCache) localCache;
```

## Class methods

```
+[PLAggregateDictionaryService entryEventNoneDefinitions];
+[PLAggregateDictionaryService load];
+[PLAggregateDictionaryService defaults];
+[PLAggregateDictionaryService entryEventNoneDefinitionSessionsFile];
```

## Instance methods

```
-[PLAggregateDictionaryService dailyTaskTimer];
-[PLAggregateDictionaryService logAggregateUIKitActivityKey:withInfo:AggDKey:];
-[PLAggregateDictionaryService registerForCameraNotifications];
-[PLAggregateDictionaryService logAggregateUIKitKeyboardActivityKey:withInfo:AggDKey:];
-[PLAggregateDictionaryService last_state];
-[PLAggregateDictionaryService currentMachWakeTime];
-[PLAggregateDictionaryService registerForBacklightLatencyNotifications];
-[PLAggregateDictionaryService setLocalCache:];
-[PLAggregateDictionaryService init];
-[PLAggregateDictionaryService registerForSCDynamicStoreNotifications];
-[PLAggregateDictionaryService registerForBluetoothNotifications];
-[PLAggregateDictionaryService registerForLocationNotifications];
-[PLAggregateDictionaryService initValidReasonsDictionary];
-[PLAggregateDictionaryService initOperatorDependancies];
-[PLAggregateDictionaryService registerForUIKitNotifications];
-[PLAggregateDictionaryService registerForSafariNotifications];
-[PLAggregateDictionaryService registerForApplicationNotifications];
-[PLAggregateDictionaryService setLast_state:];
-[PLAggregateDictionaryService setCurrentMachWakeTime:];
-[PLAggregateDictionaryService registerForBatteryNotifications];
-[PLAggregateDictionaryService setWakeReasons:];
-[PLAggregateDictionaryService logDuration:asDistribution:];
-[PLAggregateDictionaryService registerForCalendarNotifications];
-[PLAggregateDictionaryService bucketWakeTime:];
-[PLAggregateDictionaryService registeredNotifications];
-[PLAggregateDictionaryService setBlmAggregateCFNotification:];
-[PLAggregateDictionaryService setDailyTaskTimer:];
-[PLAggregateDictionaryService wakeReasonString];
-[PLAggregateDictionaryService blmAggregateCFNotification];
-[PLAggregateDictionaryService setValidReasonsDictionary:];
-[PLAggregateDictionaryService firstScreenOnAfterWake];
-[PLAggregateDictionaryService updateAggregateStateWithEntry:];
-[PLAggregateDictionaryService setFirstScreenOnAfterWake:];
-[PLAggregateDictionaryService localCache];
-[PLAggregateDictionaryService abstimeToNanosec:];
-[PLAggregateDictionaryService addToDurationScalarKey:withDuration:];
-[PLAggregateDictionaryService wakeReasons];
-[PLAggregateDictionaryService setWakeReasonString:];
-[PLAggregateDictionaryService registerForMailNotifications];
-[PLAggregateDictionaryService registerForAudioNotifications];
-[PLAggregateDictionaryService registerForSpringboardNotifications];
-[PLAggregateDictionaryService registerForVideoNotifications];
-[PLAggregateDictionaryService validReasonsDictionary];
-[PLAggregateDictionaryService setRegisteredNotifications:];
```

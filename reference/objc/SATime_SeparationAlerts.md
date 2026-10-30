# `SATime`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SATimeServiceProtocol`
- 5 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _isReplay;
@"NSDate" _now;
@"NSMutableSet" _ongoingAlarms;
^v _alarmQueue;
@"<SATimeEventRequestProtocol>" _externalTimer;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_ongoingAlarms) ongoingAlarms;
@property (T^v,N,V_alarmQueue) alarmQueue;
@property (T@"<SATimeEventRequestProtocol>",W,N,V_externalTimer) externalTimer;
@property (TB,N,V_isReplay) isReplay;
@property (T@"NSDate",R,N,V_now) now;
```

## Instance methods

```
-[SATime alarmQueue];
-[SATime ingestTAEvent:];
-[SATime now];
-[SATime addAlarm:];
-[SATime alarmCount];
-[SATime dealloc];
-[SATime alarmFired:];
-[SATime initWithExternalTimer:isReplay:];
-[SATime advanceTimeWithEvent:];
-[SATime cancelAlarmWithUUID:];
-[SATime earliestAlarm];
-[SATime externalTimer];
-[SATime fireAlarmsIfReady];
-[SATime getCurrentTime];
-[SATime getEarliestAlarmDate];
-[SATime isReplay];
-[SATime ongoingAlarms];
-[SATime popAlarm];
-[SATime setAlarmQueue:];
-[SATime setExternalTimer:];
-[SATime setIsReplay:];
-[SATime setOngoingAlarms:];
-[SATime setupAlarmFireAt:forClient:];
```

# `SBAmbientScheduledAlarmObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _observationEnabled;
@"<SBAmbientScheduledAlarmObserverDelegate>" _delegate;
@"MTAlarmManager" _alarmManager;
@"NSObject<OS_dispatch_queue>" _scheduledTimerQueue;
@"NSMutableDictionary" _scheduledTimers;
```

## Properties

```
@property (T@"MTAlarmManager",&,N,V_alarmManager) alarmManager;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_scheduledTimerQueue) scheduledTimerQueue;
@property (T@"NSMutableDictionary",&,N,V_scheduledTimers) scheduledTimers;
@property (T@"<SBAmbientScheduledAlarmObserverDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_observationEnabled) observationEnabled;
```

## Instance methods

```
-[SBAmbientScheduledAlarmObserver alarmManager];
-[SBAmbientScheduledAlarmObserver setAlarmManager:];
-[SBAmbientScheduledAlarmObserver init];
-[SBAmbientScheduledAlarmObserver dealloc];
-[SBAmbientScheduledAlarmObserver setDelegate:];
-[SBAmbientScheduledAlarmObserver delegate];
-[SBAmbientScheduledAlarmObserver scheduledTimers];
-[SBAmbientScheduledAlarmObserver setObservationEnabled:];
-[SBAmbientScheduledAlarmObserver _timerFired:];
-[SBAmbientScheduledAlarmObserver _registerForAlarmNotifications];
-[SBAmbientScheduledAlarmObserver setScheduledTimers:];
-[SBAmbientScheduledAlarmObserver _firingAlarmUpdated:];
-[SBAmbientScheduledAlarmObserver _invalidateAllScheduledTimers];
-[SBAmbientScheduledAlarmObserver _newScheduledTimerForFireDate:];
-[SBAmbientScheduledAlarmObserver _nextAlarmChanged:];
-[SBAmbientScheduledAlarmObserver _publishTimerFired:];
-[SBAmbientScheduledAlarmObserver _scheduleTimersForAlarm:];
-[SBAmbientScheduledAlarmObserver _timeIntervalsWithReasons];
-[SBAmbientScheduledAlarmObserver _unregisterForAlarmNotifications];
-[SBAmbientScheduledAlarmObserver _updateAlarmObservation];
-[SBAmbientScheduledAlarmObserver _updateScheduledTimersForNextAlarm];
-[SBAmbientScheduledAlarmObserver observationEnabled];
-[SBAmbientScheduledAlarmObserver scheduledTimerQueue];
-[SBAmbientScheduledAlarmObserver setScheduledTimerQueue:];
```

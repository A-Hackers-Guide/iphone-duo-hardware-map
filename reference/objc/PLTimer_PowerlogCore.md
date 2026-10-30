# `PLTimer`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 12 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _repeats;
@"NSDate" _fireDate;
@"NSObject<OS_dispatch_queue>" _queue;
@? _block;
@"NSObject<OS_dispatch_source>" _timer;
d _interval;
d _tolerance;
@ _userInfo;
@"PLEntryNotificationOperatorComposition" _sleepEntryNotification;
@"PLEntryNotificationOperatorComposition" _wakeEntryNotification;
@"NSDate" _lastSleepTime;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@?,C,V_block) block;
@property (T@"NSObject<OS_dispatch_source>",&,V_timer) timer;
@property (Td,V_interval) interval;
@property (Td,V_tolerance) tolerance;
@property (TB,V_repeats) repeats;
@property (T@,&,V_userInfo) userInfo;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sleepEntryNotification) sleepEntryNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_wakeEntryNotification) wakeEntryNotification;
@property (T@"NSDate",&,V_lastSleepTime) lastSleepTime;
@property (TB,N) timerActive;
@property (T@"NSDate",&,N,V_fireDate) fireDate;
```

## Instance methods

```
-[PLTimer setRepeats:];
-[PLTimer repeats];
-[PLTimer fire];
-[PLTimer block];
-[PLTimer setTimer:];
-[PLTimer setSleepEntryNotification:];
-[PLTimer setInterval:];
-[PLTimer interval];
-[PLTimer setBlock:];
-[PLTimer timer];
-[PLTimer tolerance];
-[PLTimer userInfo];
-[PLTimer dealloc];
-[PLTimer wakeEntryNotification];
-[PLTimer fireDate];
-[PLTimer setUserInfo:];
-[PLTimer queue];
-[PLTimer setWakeEntryNotification:];
-[PLTimer setFireDate:];
-[PLTimer invalidate];
-[PLTimer sleepEntryNotification];
-[PLTimer setTolerance:];
-[PLTimer setQueue:];
-[PLTimer arm];
-[PLTimer handleTimerFire];
-[PLTimer setTimerActive:];
-[PLTimer initWithFireDate:withInterval:withTolerance:repeats:withUserInfo:withQueue:withBlock:];
-[PLTimer lastSleepTime];
-[PLTimer setLastSleepTime:];
-[PLTimer timerActive];
```

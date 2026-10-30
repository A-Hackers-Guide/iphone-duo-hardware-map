# `SBApplicationWakeScheduler`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<SBApplicationWakeLifecycleHandling>" _lifecycleTracker;
@"SBApplication" _application;
B _invalidated;
@"<BSTimerScheduleQuerying><BSInvalidatable>" _wakeTimer;
```

## Properties

```
@property (T@"<BSTimerScheduleQuerying><BSInvalidatable>",&,N,V_wakeTimer) wakeTimer;
@property (T@"NSDate",R,N) scheduledDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationWakeScheduler init];
-[SBApplicationWakeScheduler dealloc];
-[SBApplicationWakeScheduler unschedule];
-[SBApplicationWakeScheduler invalidate];
-[SBApplicationWakeScheduler scheduledDate];
-[SBApplicationWakeScheduler wakeImmediately];
-[SBApplicationWakeScheduler _applicationProcessStateDidChange:];
-[SBApplicationWakeScheduler _expectedFireDateForTimer:];
-[SBApplicationWakeScheduler _forceInvalidate];
-[SBApplicationWakeScheduler _initWithLifecycleTracker:forApplication:];
-[SBApplicationWakeScheduler endResumeIfAwoken];
-[SBApplicationWakeScheduler scheduleWakeForDate:];
-[SBApplicationWakeScheduler setWakeTimer:];
-[SBApplicationWakeScheduler wakeTimer];
```

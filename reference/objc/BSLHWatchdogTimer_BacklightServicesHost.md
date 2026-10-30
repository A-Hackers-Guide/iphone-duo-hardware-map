# `BSLHWatchdogTimer`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SWSystemSleepObserver`, `BLSHWatchdogTiming`
- 11 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _timer;
@"NSString" _explanation;
@"<BLSHWatchdogDelegate>" _delegate;
@"BLSHWatchdogProvider" _provider;
d _lock_timeout;
d _lock_watchdogStart;
B _lock_sleepImminentSinceScheduled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
Q _lock_invalidationReason;
B _sleepImminentWhenScheduled;
```

## Properties

```
@property (TB,N,GhasSleepBeenImminentSinceScheduled) sleepImminentSinceScheduled;
@property (TB,R,N,GwasSleepImminentWhenScheduled,V_sleepImminentWhenScheduled) sleepImminentWhenScheduled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisInvalidated) invalidated;
@property (TQ,R,N) invalidationReason;
@property (T@"NSString",R,C,N) explanation;
```

## Instance methods

```
-[BSLHWatchdogTimer invalidate:];
-[BSLHWatchdogTimer systemSleepMonitorDidWakeFromSleep:];
-[BSLHWatchdogTimer explanation];
-[BSLHWatchdogTimer dealloc];
-[BSLHWatchdogTimer systemSleepMonitorWillWakeFromSleep:];
-[BSLHWatchdogTimer isInvalidated];
-[BSLHWatchdogTimer invalidationReason];
-[BSLHWatchdogTimer description];
-[BSLHWatchdogTimer timerFired];
-[BSLHWatchdogTimer systemSleepMonitorSleepRequestAborted:];
-[BSLHWatchdogTimer setSleepImminentSinceScheduled:];
-[BSLHWatchdogTimer hasSleepBeenImminentSinceScheduled];
-[BSLHWatchdogTimer initWithExplanation:delegate:provider:];
-[BSLHWatchdogTimer scheduleWithTimeout:];
-[BSLHWatchdogTimer wasSleepImminentWhenScheduled];
```

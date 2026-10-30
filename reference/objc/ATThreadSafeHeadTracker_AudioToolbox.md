# `ATThreadSafeHeadTracker`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SWSystemSleepObserver`
- 2 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<ThreadSafeHeadTracker>="__ptr_"^{ThreadSafeHeadTracker}"__cntrl_"^{__shared_weak_count}} _impl;
@"SWSystemSleepMonitor" _sleepMonitor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ATThreadSafeHeadTracker systemSleepMonitorDidWakeFromSleep:];
-[ATThreadSafeHeadTracker dealloc];
-[ATThreadSafeHeadTracker handleSystemSleepMonitorDidWakeFromSleep];
-[ATThreadSafeHeadTracker initWithRateLimit:detectPredictionAnchor:userContext:factory:execution:finalizer:useSleepWakeDetector:];
```

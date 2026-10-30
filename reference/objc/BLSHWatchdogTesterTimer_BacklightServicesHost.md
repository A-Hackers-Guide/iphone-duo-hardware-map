# `BLSHWatchdogTesterTimer`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHWatchdogTiming`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
Q _invalidationReason;
@"NSString" _explanation;
B _sleepImminentSinceScheduled;
```

## Properties

```
@property (TB,N,GhasSleepBeenImminentSinceScheduled,V_sleepImminentSinceScheduled) sleepImminentSinceScheduled;
@property (TB,R,N,GisInvalidated) invalidated;
@property (TQ,R,N) invalidationReason;
@property (T@"NSString",R,C,N) explanation;
```

## Instance methods

```
-[BLSHWatchdogTesterTimer invalidate:];
-[BLSHWatchdogTesterTimer explanation];
-[BLSHWatchdogTesterTimer isInvalidated];
-[BLSHWatchdogTesterTimer invalidationReason];
-[BLSHWatchdogTesterTimer initWithExplanation:];
-[BLSHWatchdogTesterTimer setSleepImminentSinceScheduled:];
-[BLSHWatchdogTesterTimer hasSleepBeenImminentSinceScheduled];
```

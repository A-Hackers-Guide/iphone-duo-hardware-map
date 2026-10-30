# `BLSHWatchdogTiming` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSHWatchdogInvalidatable`
- 0 instance variables, 3 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisInvalidated) invalidated;
@property (TQ,R,N) invalidationReason;
@property (TB,R,N,GhasSleepBeenImminentSinceScheduled) sleepImminentSinceScheduled;
```

## Instance methods

```
-[BLSHWatchdogTiming isInvalidated];
-[BLSHWatchdogTiming invalidationReason];
-[BLSHWatchdogTiming hasSleepBeenImminentSinceScheduled];
```

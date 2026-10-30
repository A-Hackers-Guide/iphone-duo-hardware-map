# `BLSHBacklightOSTimerProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHOSTimerProviding`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) mach_continuous_time;
@property (Td,R,N) bsContinuousMachTimeNow;
@property (T@"NSDate",R,N) now;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBacklightOSTimerProvider now];
-[BLSHBacklightOSTimerProvider dispatchToMainQueueAfterSecondsDelay:identifier:block:];
-[BLSHBacklightOSTimerProvider dateWithTimeIntervalSinceNow:];
-[BLSHBacklightOSTimerProvider bsContinuousMachTimeNow];
-[BLSHBacklightOSTimerProvider dateWithBSContinuousMachTime:];
-[BLSHBacklightOSTimerProvider mach_continuous_time];
-[BLSHBacklightOSTimerProvider scheduledTimerWithIdentifier:interval:leewayInterval:handler:];
-[BLSHBacklightOSTimerProvider scheduledWakingTimerWithIdentifier:interval:leewayInterval:handler:];
```

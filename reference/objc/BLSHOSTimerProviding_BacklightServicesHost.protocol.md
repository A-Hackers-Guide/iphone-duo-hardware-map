# `BLSHOSTimerProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) mach_continuous_time;
@property (Td,R,N) bsContinuousMachTimeNow;
@property (T@"NSDate",R,N) now;
```

## Instance methods

```
-[BLSHOSTimerProviding now];
-[BLSHOSTimerProviding dispatchToMainQueueAfterSecondsDelay:identifier:block:];
-[BLSHOSTimerProviding dateWithTimeIntervalSinceNow:];
-[BLSHOSTimerProviding bsContinuousMachTimeNow];
-[BLSHOSTimerProviding dateWithBSContinuousMachTime:];
-[BLSHOSTimerProviding mach_continuous_time];
-[BLSHOSTimerProviding scheduledTimerWithIdentifier:interval:leewayInterval:handler:];
-[BLSHOSTimerProviding scheduledWakingTimerWithIdentifier:interval:leewayInterval:handler:];
```

# `BLSHMeasureCommitOnWakeOperation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 7 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSHCATransactionTelemetryContext" _lock_caTransaction;
@"BSContinuousMachTimer" _lock_timeoutTimer;
B _lock_didBegin;
B _lock_didComplete;
B _lock_didTimeout;
B _lock_invalidated;
```

## Properties

```
@property (TB,R,N,GisCommitPending) commitPending;
@property (TB,R,N) didTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHMeasureCommitOnWakeOperation init];
-[BLSHMeasureCommitOnWakeOperation dealloc];
-[BLSHMeasureCommitOnWakeOperation invalidate];
-[BLSHMeasureCommitOnWakeOperation didTimeout];
-[BLSHMeasureCommitOnWakeOperation isCommitPending];
-[BLSHMeasureCommitOnWakeOperation beginMeasurementForTransactionID:withCompletion:];
-[BLSHMeasureCommitOnWakeOperation performCommitToMeasure];
```

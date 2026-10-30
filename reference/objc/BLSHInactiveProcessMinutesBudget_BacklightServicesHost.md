# `BLSHInactiveProcessMinutesBudget`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHInactiveProcessBudgeting`
- 6 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"<BLSHOSTimerProviding>" _osTimerProvider;
@"NSMutableArray" _lock_buckets;
@"<BSTimerScheduleQuerying><BSInvalidatable>" _lock_invalidationTimer;
Q _lock_lastInvalidationTimestamp;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TQ,R,N) bucketCount;
@property (TQ,R,N) secondsBucketCount;
@property (T@"NSArray",R,C,N) buckets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHInactiveProcessMinutesBudget debugDescription];
-[BLSHInactiveProcessMinutesBudget buckets];
-[BLSHInactiveProcessMinutesBudget dealloc];
-[BLSHInactiveProcessMinutesBudget description];
-[BLSHInactiveProcessMinutesBudget bucketCount];
-[BLSHInactiveProcessMinutesBudget allowedFidelityAtDate:expectedFidelity:];
-[BLSHInactiveProcessMinutesBudget chargeRenderedSpecifier:expectedFidelity:];
-[BLSHInactiveProcessMinutesBudget hasSecondsBudgetAtDate:];
-[BLSHInactiveProcessMinutesBudget initWithIdentifier:osTimerProvider:];
-[BLSHInactiveProcessMinutesBudget invalidateAtRequestDate:expectedFidelity:invalidationBlock:];
-[BLSHInactiveProcessMinutesBudget performInvalidation];
-[BLSHInactiveProcessMinutesBudget resetFutureSpecifiers];
-[BLSHInactiveProcessMinutesBudget secondsBucketCount];
-[BLSHInactiveProcessMinutesBudget stillTrackingAfterPurgingStaleDataForNowDate:];
-[BLSHInactiveProcessMinutesBudget validateAndChargeFutureSpecifier:nextSpecifier:expectedFidelity:];
```

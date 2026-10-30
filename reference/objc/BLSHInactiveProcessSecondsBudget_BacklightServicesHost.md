# `BLSHInactiveProcessSecondsBudget`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHInactiveProcessBudgeting`
- 8 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<BLSHOSTimerProviding>" _osTimerProvider;
@"NSString" _identifier;
@"BLSAlwaysOnDateSpecifier" _lock_previousSecondsFutureSpecifier;
@"BLSAlwaysOnDateSpecifier" _lock_exemptedSecondsFutureSpecifier;
@"BLSAlwaysOnDateSpecifier" _lock_previousSecondsRenderedSpecifier;
@"NSDate" _lock_lastInvalidation;
@"<BSTimerScheduleQuerying><BSInvalidatable>" _lock_invalidationTimer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
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
-[BLSHInactiveProcessSecondsBudget dealloc];
-[BLSHInactiveProcessSecondsBudget description];
-[BLSHInactiveProcessSecondsBudget allowedFidelityAtDate:expectedFidelity:];
-[BLSHInactiveProcessSecondsBudget chargeRenderedSpecifier:expectedFidelity:];
-[BLSHInactiveProcessSecondsBudget initWithIdentifier:osTimerProvider:];
-[BLSHInactiveProcessSecondsBudget invalidateAtRequestDate:expectedFidelity:invalidationBlock:];
-[BLSHInactiveProcessSecondsBudget performInvalidation];
-[BLSHInactiveProcessSecondsBudget resetFutureSpecifiers];
-[BLSHInactiveProcessSecondsBudget stillTrackingAfterPurgingStaleDataForNowDate:];
-[BLSHInactiveProcessSecondsBudget validateAndChargeFutureSpecifier:nextSpecifier:expectedFidelity:];
```

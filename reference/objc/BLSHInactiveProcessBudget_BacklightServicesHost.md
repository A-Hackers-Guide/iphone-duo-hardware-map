# `BLSHInactiveProcessBudget`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHInactiveProcessBudgeting`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"BLSHInactiveProcessSecondsBudget" _secondsBudget;
@"BLSHInactiveProcessMinutesBudget" _minutesBudget;
Q _stateHandler;
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
-[BLSHInactiveProcessBudget debugDescription];
-[BLSHInactiveProcessBudget dealloc];
-[BLSHInactiveProcessBudget description];
-[BLSHInactiveProcessBudget allowedFidelityAtDate:expectedFidelity:];
-[BLSHInactiveProcessBudget chargeRenderedSpecifier:expectedFidelity:];
-[BLSHInactiveProcessBudget initWithIdentifier:osTimerProvider:];
-[BLSHInactiveProcessBudget invalidateAtRequestDate:expectedFidelity:invalidationBlock:];
-[BLSHInactiveProcessBudget performInvalidation];
-[BLSHInactiveProcessBudget resetFutureSpecifiers];
-[BLSHInactiveProcessBudget stillTrackingAfterPurgingStaleDataForNowDate:];
-[BLSHInactiveProcessBudget validateAndChargeFutureSpecifier:nextSpecifier:expectedFidelity:];
```

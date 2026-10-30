# `BLSHInactiveBudgetPolicy`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHInactiveBudgetPolicing_Private`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _budgets;
@? _budgetFactory;
@"BLSHNullInactiveProcessBudget" _nullBudget;
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
-[BLSHInactiveBudgetPolicy description];
-[BLSHInactiveBudgetPolicy allowedFidelityAtDate:forEnvironment:expectedFidelity:];
-[BLSHInactiveBudgetPolicy chargeRenderedSpecifier:];
-[BLSHInactiveBudgetPolicy initWithBudgetFactory:];
-[BLSHInactiveBudgetPolicy initWithOSTimerProvider:];
-[BLSHInactiveBudgetPolicy invalidateAtRequestDate:forEnvironment:invalidationBlock:];
-[BLSHInactiveBudgetPolicy performInvalidation];
-[BLSHInactiveBudgetPolicy purgeStaleDataForNowDate:];
-[BLSHInactiveBudgetPolicy resetAllBudgetsForReason:];
-[BLSHInactiveBudgetPolicy resetBudgetForProcess:reason:];
-[BLSHInactiveBudgetPolicy resetFutureSpecifiers];
-[BLSHInactiveBudgetPolicy validateAndChargeFutureSpecifier:nextSpecifier:forEnvironment:];
```

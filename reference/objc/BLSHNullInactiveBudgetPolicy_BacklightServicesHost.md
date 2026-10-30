# `BLSHNullInactiveBudgetPolicy`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHInactiveBudgetPolicing_Private`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHNullInactiveBudgetPolicy allowedFidelityAtDate:forEnvironment:expectedFidelity:];
-[BLSHNullInactiveBudgetPolicy chargeRenderedSpecifier:];
-[BLSHNullInactiveBudgetPolicy invalidateAtRequestDate:forEnvironment:invalidationBlock:];
-[BLSHNullInactiveBudgetPolicy performInvalidation];
-[BLSHNullInactiveBudgetPolicy purgeStaleDataForNowDate:];
-[BLSHNullInactiveBudgetPolicy resetAllBudgetsForReason:];
-[BLSHNullInactiveBudgetPolicy resetBudgetForProcess:reason:];
-[BLSHNullInactiveBudgetPolicy resetFutureSpecifiers];
-[BLSHNullInactiveBudgetPolicy validateAndChargeFutureSpecifier:nextSpecifier:forEnvironment:];
```

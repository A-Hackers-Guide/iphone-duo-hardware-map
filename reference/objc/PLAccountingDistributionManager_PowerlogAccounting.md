# `PLAccountingDistributionManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingOwnerDependencyManager`
- Protocols: `PLAccountingDistributionOwnerManager`
- 1 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<PLAccountingDistributionManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<PLAccountingDistributionManagerDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLAccountingDistributionManager freeTimerInterval];
```

## Instance methods

```
-[PLAccountingDistributionManager didDistributeEnergyEstimate:];
-[PLAccountingDistributionManager init];
-[PLAccountingDistributionManager setDelegate:];
-[PLAccountingDistributionManager reloadDependenciesNewerThanDate:];
-[PLAccountingDistributionManager ownerIDsForDependency:];
-[PLAccountingDistributionManager delegate];
-[PLAccountingDistributionManager dependencyIDsForOwner:];
-[PLAccountingDistributionManager addDistributionEvent:];
-[PLAccountingDistributionManager didDistributeToChildEnergyEstimate:fromParentEnergyEstimate:];
-[PLAccountingDistributionManager closeLastDistributionEventForwardWithDistributionID:withEndDate:];
-[PLAccountingDistributionManager addEnergyEstimate:withNow:];
```

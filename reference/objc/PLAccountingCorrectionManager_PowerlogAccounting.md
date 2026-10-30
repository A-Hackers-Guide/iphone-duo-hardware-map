# `PLAccountingCorrectionManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingOwnerDependencyManager`
- Protocols: `PLAccountingCorrectionOwnerManager`
- 2 instance variables, 6 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"<PLAccountingCorrectionManagerDelegate>" _delegate;
@"NSMutableDictionary" _parentEntryIDToChildEnergyEstimates;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_parentEntryIDToChildEnergyEstimates) parentEntryIDToChildEnergyEstimates;
@property (T@"<PLAccountingCorrectionManagerDelegate>",W,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLAccountingCorrectionManager disableCorrection];
+[PLAccountingCorrectionManager freeTimerInterval];
```

## Instance methods

```
-[PLAccountingCorrectionManager parentEntryIDToChildEnergyEstimates];
-[PLAccountingCorrectionManager correctChildEnergyEstimate:withParentEnergyEstimate:withNow:];
-[PLAccountingCorrectionManager setDelegate:];
-[PLAccountingCorrectionManager reloadDependenciesNewerThanDate:];
-[PLAccountingCorrectionManager addRootEnergyEstimate:withNow:];
-[PLAccountingCorrectionManager ownerIDsForDependency:];
-[PLAccountingCorrectionManager delegate];
-[PLAccountingCorrectionManager dependencyIDsForOwner:];
-[PLAccountingCorrectionManager didCorrectEnergyEstimate:];
-[PLAccountingCorrectionManager childEnergyEstimatesForParentEntryID:];
-[PLAccountingCorrectionManager addEnergyMeasurement:];
-[PLAccountingCorrectionManager setParentEntryIDToChildEnergyEstimates:];
```

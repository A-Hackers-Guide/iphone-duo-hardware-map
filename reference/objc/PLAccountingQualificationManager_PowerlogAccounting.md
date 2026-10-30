# `PLAccountingQualificationManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingOwnerDependencyManager`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<PLAccountingQualificationManagerDelegate>" _delegate;
@"NSDate" _lastQualifiedEnergyEventDate;
```

## Properties

```
@property (T@"<PLAccountingQualificationManagerDelegate>",W,V_delegate) delegate;
@property (T@"NSDate",&,V_lastQualifiedEnergyEventDate) lastQualifiedEnergyEventDate;
```

## Class methods

```
+[PLAccountingQualificationManager freeTimerInterval];
```

## Instance methods

```
-[PLAccountingQualificationManager didQualifyEnergyEvent:withRootNodeID:withQualificationID:];
-[PLAccountingQualificationManager addQualificationEvent:];
-[PLAccountingQualificationManager closeLastQualificationEventForwardWithQualificationID:withEndDate:];
-[PLAccountingQualificationManager setDelegate:];
-[PLAccountingQualificationManager reloadDependenciesNewerThanDate:];
-[PLAccountingQualificationManager ownerIDsForDependency:];
-[PLAccountingQualificationManager delegate];
-[PLAccountingQualificationManager dependencyIDsForOwner:];
-[PLAccountingQualificationManager lastQualifiedEnergyEventDate];
-[PLAccountingQualificationManager setLastQualifiedEnergyEventDate:];
-[PLAccountingQualificationManager addEnergyEstimate:withNow:];
```

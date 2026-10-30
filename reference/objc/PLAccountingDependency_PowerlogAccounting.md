# `PLAccountingDependency`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _skipLastAllRunDateCheck;
@"<PLAccountingDependencyManager>" _manager;
@"NSNumber" _ID;
@"NSDate" _activationDate;
@"NSMutableSet" _observingOwnerIDs;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_observingOwnerIDs) observingOwnerIDs;
@property (T@"<PLAccountingDependencyManager>",W,V_manager) manager;
@property (TB,N,V_skipLastAllRunDateCheck) skipLastAllRunDateCheck;
@property (T@"NSNumber",&,N,V_ID) ID;
@property (T@"PLAccountingRange",&,N) range;
@property (T@"NSDate",&,N,V_activationDate) activationDate;
```

## Instance methods

```
-[PLAccountingDependency setID:];
-[PLAccountingDependency ID];
-[PLAccountingDependency deactivate];
-[PLAccountingDependency range];
-[PLAccountingDependency setManager:];
-[PLAccountingDependency activationDate];
-[PLAccountingDependency manager];
-[PLAccountingDependency setRange:];
-[PLAccountingDependency activate];
-[PLAccountingDependency description];
-[PLAccountingDependency setActivationDate:];
-[PLAccountingDependency didReceiveOwner:];
-[PLAccountingDependency observingOwnerIDs];
-[PLAccountingDependency setObservingOwnerIDs:];
-[PLAccountingDependency setSkipLastAllRunDateCheck:];
-[PLAccountingDependency skipLastAllRunDateCheck];
-[PLAccountingDependency updateWithEndDate:];
```

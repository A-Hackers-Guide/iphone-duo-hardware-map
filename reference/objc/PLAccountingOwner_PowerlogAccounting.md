# `PLAccountingOwner`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLAccountingDependencyOwner`
- 7 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"<PLAccountingOwnerManager>" _manager;
@"NSNumber" _ID;
@"PLAccountingRange" _range;
@"NSDate" _activationDate;
@"NSDate" _runDate;
@"NSMutableSet" _observingDependencyIDs;
@"NSMutableDictionary" _dependencyIDToDependenciesInRange;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_observingDependencyIDs) observingDependencyIDs;
@property (T@"NSMutableDictionary",&,N,V_dependencyIDToDependenciesInRange) dependencyIDToDependenciesInRange;
@property (T@"<PLAccountingOwnerManager>",W,V_manager) manager;
@property (T@"NSNumber",&,N,V_ID) ID;
@property (T@"PLAccountingRange",&,N,V_range) range;
@property (T@"NSDate",&,N,V_activationDate) activationDate;
@property (T@"NSDate",&,N,V_runDate) runDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLAccountingOwner setRunDate:];
-[PLAccountingOwner setID:];
-[PLAccountingOwner ID];
-[PLAccountingOwner deactivate];
-[PLAccountingOwner range];
-[PLAccountingOwner setManager:];
-[PLAccountingOwner activationDate];
-[PLAccountingOwner manager];
-[PLAccountingOwner setRange:];
-[PLAccountingOwner addDependency:];
-[PLAccountingOwner activate];
-[PLAccountingOwner description];
-[PLAccountingOwner runDate];
-[PLAccountingOwner run];
-[PLAccountingOwner setActivationDate:];
-[PLAccountingOwner hasRun];
-[PLAccountingOwner allRun];
-[PLAccountingOwner dependencyIDToDependenciesInRange];
-[PLAccountingOwner didReceiveDependency:];
-[PLAccountingOwner observingDependencyIDs];
-[PLAccountingOwner setDependencyIDToDependenciesInRange:];
-[PLAccountingOwner setObservingDependencyIDs:];
```

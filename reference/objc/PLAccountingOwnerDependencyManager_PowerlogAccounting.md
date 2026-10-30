# `PLAccountingOwnerDependencyManager`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLAccountingOwnerManager`, `PLAccountingDependencyManager`
- 9 instance variables, 13 properties, 39 instance methods, 3 class methods

## Instance variables

```
i _numDependencies;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSMutableDictionary" _dependencyIDToObservingOwners;
@"NSMutableDictionary" _dependencyIDToDependencies;
@"NSMutableDictionary" _ownerIDToObservingDependencies;
@"NSMutableDictionary" _ownerIDToLastOwner;
@"NSMutableDictionary" _ownerIDToLastAllRunDate;
@"NSMutableSet" _ownersRepository;
@"PLTimer" _freeTimer;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_dependencyIDToObservingOwners) dependencyIDToObservingOwners;
@property (T@"NSMutableDictionary",&,V_dependencyIDToDependencies) dependencyIDToDependencies;
@property (Ti,V_numDependencies) numDependencies;
@property (T@"NSMutableDictionary",&,V_ownerIDToObservingDependencies) ownerIDToObservingDependencies;
@property (T@"NSMutableDictionary",&,V_ownerIDToLastOwner) ownerIDToLastOwner;
@property (T@"NSMutableDictionary",&,V_ownerIDToLastAllRunDate) ownerIDToLastAllRunDate;
@property (T@"NSMutableSet",&,V_ownersRepository) ownersRepository;
@property (T@"PLTimer",&,V_freeTimer) freeTimer;
@property (T@"NSObject<OS_dispatch_queue>",R,V_workQueue) workQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLAccountingOwnerDependencyManager maxDependencies];
+[PLAccountingOwnerDependencyManager freeTimerInterval];
+[PLAccountingOwnerDependencyManager maxOwners];
```

## Instance methods

```
-[PLAccountingOwnerDependencyManager init];
-[PLAccountingOwnerDependencyManager workQueue];
-[PLAccountingOwnerDependencyManager reloadDependenciesNewerThanDate:];
-[PLAccountingOwnerDependencyManager addDependency:];
-[PLAccountingOwnerDependencyManager ownerIDsForDependency:];
-[PLAccountingOwnerDependencyManager dependencyIDsForOwner:];
-[PLAccountingOwnerDependencyManager numDependencies];
-[PLAccountingOwnerDependencyManager _lastDependencyForDependencyID:];
-[PLAccountingOwnerDependencyManager addOwner:];
-[PLAccountingOwnerDependencyManager canFreeDependency:];
-[PLAccountingOwnerDependencyManager canFreeOwner:];
-[PLAccountingOwnerDependencyManager dependenciesWithDependencyID:withRange:];
-[PLAccountingOwnerDependencyManager dependencyIDToDependencies];
-[PLAccountingOwnerDependencyManager dependencyIDToObservingOwners];
-[PLAccountingOwnerDependencyManager freeExpiredDependenciesAtNow:];
-[PLAccountingOwnerDependencyManager freeExpiredOwnersAtNow:];
-[PLAccountingOwnerDependencyManager freeTimer];
-[PLAccountingOwnerDependencyManager lastAllRunDateForOwnerID:];
-[PLAccountingOwnerDependencyManager lastDependencyForDependencyID:];
-[PLAccountingOwnerDependencyManager lastOwnerForOwnerID:];
-[PLAccountingOwnerDependencyManager notifyDependenciesWithOwner:];
-[PLAccountingOwnerDependencyManager notifyOwnersWithDependency:];
-[PLAccountingOwnerDependencyManager ownerIDToLastAllRunDate];
-[PLAccountingOwnerDependencyManager ownerIDToLastOwner];
-[PLAccountingOwnerDependencyManager ownerIDToObservingDependencies];
-[PLAccountingOwnerDependencyManager ownersRepository];
-[PLAccountingOwnerDependencyManager setDependencyIDToDependencies:];
-[PLAccountingOwnerDependencyManager setDependencyIDToObservingOwners:];
-[PLAccountingOwnerDependencyManager setFreeTimer:];
-[PLAccountingOwnerDependencyManager setNumDependencies:];
-[PLAccountingOwnerDependencyManager setOwnerIDToLastAllRunDate:];
-[PLAccountingOwnerDependencyManager setOwnerIDToLastOwner:];
-[PLAccountingOwnerDependencyManager setOwnerIDToObservingDependencies:];
-[PLAccountingOwnerDependencyManager setOwnersRepository:];
-[PLAccountingOwnerDependencyManager startObservingDependencyID:forOwner:];
-[PLAccountingOwnerDependencyManager startObservingOwnerID:forDependency:];
-[PLAccountingOwnerDependencyManager stopObservingDependencyID:forOwner:];
-[PLAccountingOwnerDependencyManager stopObservingOwnerID:forDependency:];
-[PLAccountingOwnerDependencyManager updateLastDependencyID:withEndDate:];
```

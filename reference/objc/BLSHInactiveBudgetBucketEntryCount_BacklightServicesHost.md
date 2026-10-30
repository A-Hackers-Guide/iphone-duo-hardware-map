# `BLSHInactiveBudgetBucketEntryCount`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _secondsFidelity;
i _count;
@"NSDate" _lastEntryInitialDate;
@"NSDate" _lastEntryFinalDate;
```

## Properties

```
@property (Ti,R,N,V_count) count;
@property (TB,R,N,GisSecondsFidelity,V_secondsFidelity) secondsFidelity;
@property (T@"NSDate",R,N,V_lastEntryInitialDate) lastEntryInitialDate;
@property (T@"NSDate",R,N,V_lastEntryFinalDate) lastEntryFinalDate;
```

## Instance methods

```
-[BLSHInactiveBudgetBucketEntryCount init];
-[BLSHInactiveBudgetBucketEntryCount count];
-[BLSHInactiveBudgetBucketEntryCount description];
-[BLSHInactiveBudgetBucketEntryCount copyWithZone:];
-[BLSHInactiveBudgetBucketEntryCount countSpecifier:hasSecondsBudget:isCoalesceAllowed:];
-[BLSHInactiveBudgetBucketEntryCount isSecondsFidelity];
-[BLSHInactiveBudgetBucketEntryCount lastEntryFinalDate];
-[BLSHInactiveBudgetBucketEntryCount lastEntryInitialDate];
-[BLSHInactiveBudgetBucketEntryCount timeIntervalFromLastEntryToDate:];
```

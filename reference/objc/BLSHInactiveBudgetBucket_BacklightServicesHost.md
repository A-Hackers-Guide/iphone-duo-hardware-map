# `BLSHInactiveBudgetBucket`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _rendered;
B _containsInvalidation;
@"NSDate" _startDate;
@"NSDate" _minuteBoundaryDate;
@"BLSHInactiveBudgetBucketEntryCount" _entryCount;
@"BLSHInactiveBudgetBucketEntryCount" _renderedEntryCount;
@"BLSHInactiveBudgetBucketEntryCount" _invalidatedEntryCount;
```

## Properties

```
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_minuteBoundaryDate) minuteBoundaryDate;
@property (T@"BLSHInactiveBudgetBucketEntryCount",R,N,V_entryCount) entryCount;
@property (T@"BLSHInactiveBudgetBucketEntryCount",R,N,V_renderedEntryCount) renderedEntryCount;
@property (T@"BLSHInactiveBudgetBucketEntryCount",R,N,V_invalidatedEntryCount) invalidatedEntryCount;
@property (TB,R,N,GisSecondsFidelity) secondsFidelity;
@property (TB,R,N,GhasBeenRendered,V_rendered) rendered;
@property (TB,R,N,V_containsInvalidation) containsInvalidation;
```

## Instance methods

```
-[BLSHInactiveBudgetBucket startDate];
-[BLSHInactiveBudgetBucket debugDescription];
-[BLSHInactiveBudgetBucket compare:];
-[BLSHInactiveBudgetBucket description];
-[BLSHInactiveBudgetBucket entryCount];
-[BLSHInactiveBudgetBucket hasBeenRendered];
-[BLSHInactiveBudgetBucket addFutureSpecifier:hasSecondsBudget:allowBeforeStart:];
-[BLSHInactiveBudgetBucket addInvalidation:hasSecondsBudget:allowBeforeStart:];
-[BLSHInactiveBudgetBucket applyRenderedSpecifier:allowBeforeStart:];
-[BLSHInactiveBudgetBucket containsInvalidation];
-[BLSHInactiveBudgetBucket initWithFutureSpecifier:];
-[BLSHInactiveBudgetBucket initWithInvalidation:];
-[BLSHInactiveBudgetBucket invalidatedEntryCount];
-[BLSHInactiveBudgetBucket isSecondsFidelity];
-[BLSHInactiveBudgetBucket minuteBoundaryDate];
-[BLSHInactiveBudgetBucket renderedEntryCount];
-[BLSHInactiveBudgetBucket resetFutureAndRenderedSpecifiers];
-[BLSHInactiveBudgetBucket resetFutureSpecifiers];
-[BLSHInactiveBudgetBucket shortLoggingString];
-[BLSHInactiveBudgetBucket validAtDate:];
```

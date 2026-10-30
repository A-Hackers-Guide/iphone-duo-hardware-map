# `PLAccountingDistributionEventEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingEventEntry`
- 2 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
B __distributeRangeWeightedTotal;
@"NSDictionary" _childNodeIDToWeight;
```

## Properties

```
@property (TB,V__distributeRangeWeightedTotal) _distributeRangeWeightedTotal;
@property (T@"NSNumber",R,N) distributionID;
@property (T@"NSDictionary",R,N,V_childNodeIDToWeight) childNodeIDToWeight;
@property (T@"NSDictionary",R,N) childNodeNameToWeight;
@property (TB,R,N) distributeRangeWeightedTotal;
```

## Class methods

```
+[PLAccountingDistributionEventEntry load];
+[PLAccountingDistributionEventEntry mergingDenyList];
```

## Instance methods

```
-[PLAccountingDistributionEventEntry distributionID];
-[PLAccountingDistributionEventEntry canMergeWithEvent:];
-[PLAccountingDistributionEventEntry subEntryKey];
-[PLAccountingDistributionEventEntry _distributeRangeWeightedTotal];
-[PLAccountingDistributionEventEntry childNodeIDToWeight];
-[PLAccountingDistributionEventEntry childNodeNameToWeight];
-[PLAccountingDistributionEventEntry distributeRangeWeightedTotal];
-[PLAccountingDistributionEventEntry initWithDistributionID:withChildNodeIDToWeight:withRange:];
-[PLAccountingDistributionEventEntry initWithDistributionID:withChildNodeNameToWeight:withRange:];
-[PLAccountingDistributionEventEntry instanceDirectionality];
-[PLAccountingDistributionEventEntry isEmptyEvent];
-[PLAccountingDistributionEventEntry isEqualContentsWithEvent:];
-[PLAccountingDistributionEventEntry set_distributeRangeWeightedTotal:];
```

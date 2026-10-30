# `PLAccountingEnergyEstimateEventEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogAccounting.framework/PowerlogAccounting`](../userland/System__Library__PrivateFrameworks__PowerlogAccounting.framework__PowerlogAccounting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAccountingEnergyEventEntry`
- 1 instance variables, 11 properties, 19 instance methods, 2 class methods

## Instance variables

```
B _isRootNodeEnergyAggregated;
```

## Properties

```
@property (T@"NSNumber",R,N) rootNodeID;
@property (Ti,R,N) parentEntryID;
@property (Ti,R,N) numAncestors;
@property (T@"NSNumber",R,N) distributionRuleID;
@property (T@"NSNumber",R,N) qualificationRuleIDSum;
@property (Td,N) correctionEnergy;
@property (Td,N) terminationRatio;
@property (T@"NSDate",&,N) distributionDate;
@property (T@"NSDate",&,N) correctionDate;
@property (T@"NSDate",&,N) qualificationDate;
@property (TB,V_isRootNodeEnergyAggregated) isRootNodeEnergyAggregated;
```

## Class methods

```
+[PLAccountingEnergyEstimateEventEntry load];
+[PLAccountingEnergyEstimateEventEntry entryKey];
```

## Instance methods

```
-[PLAccountingEnergyEstimateEventEntry setDistributionDate:];
-[PLAccountingEnergyEstimateEventEntry setQualificationDate:];
-[PLAccountingEnergyEstimateEventEntry terminationRatio];
-[PLAccountingEnergyEstimateEventEntry isRootNodeEnergyAggregated];
-[PLAccountingEnergyEstimateEventEntry correctionDate];
-[PLAccountingEnergyEstimateEventEntry dealloc];
-[PLAccountingEnergyEstimateEventEntry qualificationDate];
-[PLAccountingEnergyEstimateEventEntry qualificationRuleIDSum];
-[PLAccountingEnergyEstimateEventEntry initWithNodeID:withRootNodeID:withParentEntryID:withNumAncestors:withEnergy:withRange:withEntryDate:];
-[PLAccountingEnergyEstimateEventEntry rootNodeID];
-[PLAccountingEnergyEstimateEventEntry distributionRuleID];
-[PLAccountingEnergyEstimateEventEntry correctionEnergy];
-[PLAccountingEnergyEstimateEventEntry setTerminationRatio:];
-[PLAccountingEnergyEstimateEventEntry parentEntryID];
-[PLAccountingEnergyEstimateEventEntry numAncestors];
-[PLAccountingEnergyEstimateEventEntry setCorrectionDate:];
-[PLAccountingEnergyEstimateEventEntry setCorrectionEnergy:];
-[PLAccountingEnergyEstimateEventEntry distributionDate];
-[PLAccountingEnergyEstimateEventEntry setIsRootNodeEnergyAggregated:];
```
